from copy import deepcopy
from fractions import Fraction as F
import json

# Påhittade mängder. Alla utsläpp anges i ton CO2e, material i ton.
BASE = [
    dict(supplier='Ovako', supplier_node='O-G', group='grön', mass=F(40), ef=F('0.4'), buyers=[F(32), F(8)]),
    dict(supplier='SSAB', supplier_node='S-G', group='grön', mass=F(60), ef=F('0.8'), buyers=[F(48), F(12)]),
    dict(supplier='Ovako', supplier_node='O-B', group='brun', mass=F(60), ef=F(2), buyers=[F(12), F(48)]),
    dict(supplier='SSAB', supplier_node='S-B', group='brun', mass=F(40), ef=F('2.4'), buyers=[F(8), F(32)]),
]
PARTITIONS = {
    'En nod': (),
    'Leverantörsbolag': ('supplier',),
    'Inkommande leverantörsnod': ('supplier_node',),
    'Artikelgrupp': ('group',),
    'Leverantörsbolag och grupp': ('supplier', 'group'),
    'Kund, med exakt inflödesfördelning': None,
}


def calculate(flows, partition, unknown=(), revenue=False):
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
            price = F(2) if revenue and f['group'] == 'grön' else F(1)
            for i in range(2):
                b['buyers'][i] += buyers[i] * price
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
efficiency = deepcopy(BASE)
efficiency[0]['ef'] = F('0.2')
scenarios['Ovako effektiviserar grön produktion'] = efficiency
switch = deepcopy(BASE)
switch[0].update(mass=F(60), buyers=[F(48), F(12)])
switch[1].update(mass=F(40), buyers=[F(32), F(8)])
scenarios['20 ton grönt från SSAB till Ovako'] = switch
greener = deepcopy(BASE)
for flow, mass, buyers in zip(greener, [52, 68, 48, 32], [[44, 8], [56, 12], [0, 48], [0, 32]]):
    flow.update(mass=F(mass), buyers=list(map(F, buyers)))
scenarios['Sandvik byter sina 20 bruna ton mot gröna'] = greener
origin = deepcopy(BASE)
origin[0]['buyers'] = [F(40), F(0)]
origin[1]['buyers'] = [F(40), F(20)]
scenarios['Samma kundmängder, olika grönt ursprung'] = origin
coarse = deepcopy(BASE)
for f in coarse:
    f['ef'] = F('1.36') if f['supplier'] == 'Ovako' else F('1.44')
    f['supplier_node'] = f['supplier']
scenarios['Grova leverantörsdeklarationer, massfördelning'] = coarse

for label, flows in scenarios.items():
    result = {}
    for name, partition in PARTITIONS.items():
        values, coverage = calculate(flows, partition)
        result[name] = [round(float(x), 6) for x in values]
    print(json.dumps(dict(scenario=label, allocations=result), ensure_ascii=False))

mixed, mixed_coverage = calculate(BASE, PARTITIONS['Artikelgrupp'], unknown=('SSAB',))
assert mixed == [F('99.4'), F('190.6')]
print(json.dumps(dict(scenario='SSAB okänd, artikelgrupper', totals=list(map(float, mixed)), coverage=list(map(float, mixed_coverage))), ensure_ascii=False))
values, _ = calculate(BASE, (), revenue=True)
assert values == [F(174), F(116)]
print(json.dumps(dict(scenario='En nod, grön prispremie 100 procent, intäktsnyckel', allocations=list(map(float, values))), ensure_ascii=False))

# Kontrollera centrala resultat med oberoende, direkt utskrivna formler.
assert calculate(BASE, ())[0] == [F(290)/2, F(290)/2]
assert calculate(BASE, ('group',))[0] == [F(69)*F(4,5)+F(221)*F(1,5), F(69)*F(1,5)+F(221)*F(4,5)]
assert calculate(BASE, ('supplier_node',))[0] == calculate(BASE, ('supplier', 'group'))[0]
assert calculate(greener, ('group',))[0] == [F('81.2')*F(5,6), F('81.2')*F(1,6)+F('176.8')]
assert calculate(greener, ('supplier', 'group'))[0][1] == calculate(BASE, ('supplier', 'group'))[0][1]
assert calculate(coarse, ('group',))[0] == calculate(BASE, ('supplier',))[0]
print('Kontroller godkända: inflöden, utflöden, totalbalans, U-balans och centrala jämförelser.')
