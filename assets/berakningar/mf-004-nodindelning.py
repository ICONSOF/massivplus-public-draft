from copy import deepcopy
from fractions import Fraction as F
import json

# Påhittade mängder. Alla utsläpp anges i ton CO2e, material i ton.
BASE = [
    dict(supplier='Stålverk A', supplier_node='A-G', group='grön', mass=F(50), ef=F('0.4'), buyers=[F(40), F(10)]),
    dict(supplier='Stålverk B', supplier_node='B-G', group='grön', mass=F(50), ef=F('0.8'), buyers=[F(40), F(10)]),
    dict(supplier='Stålverk A', supplier_node='A-B', group='brun', mass=F(50), ef=F(2), buyers=[F(10), F(40)]),
    dict(supplier='Stålverk B', supplier_node='B-B', group='brun', mass=F(50), ef=F('2.4'), buyers=[F(10), F(40)]),
]
PARTITIONS = {
    'En nod': (),
    'Leverantörsbolag': ('supplier',),
    'Inkommande leverantörsnod': ('supplier_node',),
    'Artikelgrupp': ('group',),
    'Leverantörsbolag och grupp': ('supplier', 'group'),
    'Kund, med exakt inflödesfördelning': None,
}


def calculate(flows, partition, unknown=()):
    total_mass = sum(x['mass'] for x in flows)
    own = F(10)
    assert total_mass == 200
    assert all(sum(x['buyers']) == x['mass'] for x in flows)
    buckets = {}
    for f in flows:
        pieces = [(tuple(f[k] for k in partition), f['mass'], f['buyers'])] if partition is not None else [
            ((str(j),), mass, [mass if i == j else F(0) for i in range(2)])
            for j, mass in enumerate(f['buyers']) if mass
        ]
        for key, mass, buyers in pieces:
            b = buckets.setdefault(key, dict(actual=F(0), unknown=F(0), buyers=[F(0), F(0)]))
            kind = 'unknown' if f['supplier'] in unknown else 'actual'
            b[kind] += mass * f['ef']
            b['actual'] += own * mass / total_mass
            for i in range(2):
                b['buyers'][i] += buyers[i]
    out = [dict(actual=F(0), unknown=F(0)) for _ in range(2)]
    for b in buckets.values():
        denominator = sum(b['buyers'])
        assert denominator > 0
        for kind in ('actual', 'unknown'):
            node_out = F(0)
            for i in range(2):
                amount = b[kind] * b['buyers'][i] / denominator
                out[i][kind] += amount
                node_out += amount
            assert node_out == b[kind]
    expected = own + sum(x['mass'] * x['ef'] for x in flows)
    assert sum(sum(x.values()) for x in out) == expected
    assert sum(x['unknown'] for x in out) == sum(x['mass'] * x['ef'] for x in flows if x['supplier'] in unknown)
    return [sum(x.values()) for x in out], [x['actual'] / sum(x.values()) for x in out]


scenarios = {'Bas': deepcopy(BASE)}
greener = deepcopy(BASE)
for flow, mass, buyers in zip(greener, [60, 60, 40, 40], [[50, 10], [50, 10], [0, 40], [0, 40]]):
    flow.update(mass=F(mass), buyers=list(map(F, buyers)))
scenarios['Verkstaden byter sina 20 bruna ton mot gröna'] = greener
efficiency = deepcopy(BASE)
efficiency[0]['ef'] = F('0.2')
scenarios['Stålverk A halverar utsläppen i grön produktion'] = efficiency
origin = deepcopy(BASE)
origin[0]['buyers'] = [F(50), F(0)]
origin[1]['buyers'] = [F(30), F(20)]
scenarios['Verkstaden köper sitt gröna från Stålverk A'] = origin
coarse = deepcopy(BASE)
for f in coarse:
    f['ef'] = F('1.2') if f['supplier'] == 'Stålverk A' else F('1.6')
    f['supplier_node'] = f['supplier']
scenarios['Bara bolagstotaler från leverantörerna, massfördelning'] = coarse

for label, flows in scenarios.items():
    result = {}
    for name, partition in PARTITIONS.items():
        values, coverage = calculate(flows, partition)
        result[name] = [round(float(x), 6) for x in values]
    print(json.dumps(dict(scenario=label, allocations=result), ensure_ascii=False))

for name in ('En nod', 'Artikelgrupp'):
    values, coverage = calculate(BASE, PARTITIONS[name], unknown=('Stålverk B',))
    print(json.dumps(dict(scenario='Stålverk B okänd, ' + name, totals=list(map(float, values)), coverage=[round(float(x), 6) for x in coverage]), ensure_ascii=False))

# Kontrollera centrala resultat med oberoende, direkt utskrivna formler.
assert calculate(BASE, ())[0] == [F(145), F(145)]
assert calculate(BASE, ('supplier',))[0] == calculate(BASE, ())[0]
assert calculate(BASE, ('group',))[0] == [F(65)*F(4,5)+F(225)*F(1,5), F(65)*F(1,5)+F(225)*F(4,5)]
assert calculate(BASE, ('supplier_node',))[0] == calculate(BASE, ('group',))[0]
assert calculate(greener, ('group',))[0] == [F(78)*F(5,6), F(78)*F(1,6)+F(180)]
assert calculate(greener, ('group',))[0][1] == calculate(BASE, ('group',))[0][1]
assert calculate(origin, ('group',))[0] == calculate(BASE, ('group',))[0]
assert calculate(coarse, ('group',))[0] == calculate(BASE, ())[0]
values, coverage = calculate(BASE, ('group',), unknown=('Stålverk B',))
assert values == [F(97), F(193)]
assert sum(v * c for v, c in zip(values, coverage)) / sum(values) == F(130, 290)
print('Kontroller godkända: inflöden, utflöden, totalbalans, U-balans och centrala jämförelser.')
