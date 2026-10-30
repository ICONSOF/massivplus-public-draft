"""Pröva D för ett fast område och för mottagaren av dess allokering.

Alla tal är påhittade. Actual här avser externt mottagen faktisk börda;
områdets egna utsläpp hålls separat även när de passerar interna noder.
"""

from dataclasses import dataclass
from fractions import Fraction as F
import json
from random import Random


@dataclass(frozen=True)
class Amount:
    actual: F = F(0)
    unknown: F = F(0)
    own: F = F(0)

    def __post_init__(self):
        if min(self.actual, self.unknown, self.own) < 0:
            raise ValueError('Prövningen förutsätter icke-negativa mängder.')

    def __add__(self, other):
        return Amount(self.actual + other.actual,
                      self.unknown + other.unknown, self.own + other.own)

    @property
    def upstream(self):
        return self.actual + self.unknown

    @property
    def total(self):
        return self.upstream + self.own

    def scaled(self, share):
        return Amount(self.actual * share, self.unknown * share, self.own * share)


def boundary(nodes, recipients):
    """Summera externa tilldelningar över samma mottagare, oavsett nodnamn."""
    result = {r: Amount() for r in recipients}
    for node in nodes.values():
        for recipient, amount in node.items():
            if recipient not in result:
                raise ValueError('Mottagaruppsättningen måste hållas fast.')
            result[recipient] = result[recipient] + amount
    return result


def distance(value, reference, separate_components=True):
    if separate_components:
        return (abs(value.actual - reference.actual)
                + abs(value.unknown - reference.unknown))
    return abs(value.upstream - reference.upstream)


def evaluate(outgoing, reference, separate_components=True):
    if reference is None:
        return dict(D=None, reason='Referens saknas')
    if set(outgoing) != set(reference):
        raise ValueError('Samma mottagaruppsättning krävs.')
    for component in ('actual', 'unknown'):
        if (sum(getattr(a, component) for a in outgoing.values())
                != sum(getattr(a, component) for a in reference.values())):
            raise ValueError('Extern Actual och Unknown ska balansera var för sig.')
    upstream = sum(a.upstream for a in reference.values())
    if upstream == 0:
        return dict(D=None, reason='Ingen extern uppströmsbörda')

    details = {}
    for r, value in outgoing.items():
        ref = reference[r]
        diff = distance(value, ref, separate_components)
        denominator = value.upstream + ref.upstream
        details[r] = dict(
            upstream=value.upstream,
            total=value.total,
            reference=ref.upstream,
            delta=value.upstream - ref.upstream,
            delta_actual=value.actual - ref.actual,
            delta_unknown=value.unknown - ref.unknown,
            D_relation=diff / denominator if denominator else None,
            weight=denominator / (2 * upstream),
        )
    combined = sum(distance(outgoing[r], reference[r], separate_components)
                   for r in outgoing) / (2 * upstream)
    weighted = sum(d['weight'] * d['D_relation'] for d in details.values()
                   if d['D_relation'] is not None)
    assert combined == weighted
    return dict(D=combined, relations=details)


def json_value(value):
    if isinstance(value, F):
        return round(float(value), 8)
    raise TypeError(type(value))


def show(name, nodes, reference, recipients=('X', 'Y')):
    outgoing = boundary(nodes, recipients)
    result = evaluate(outgoing, reference)
    result['D_summa'] = evaluate(outgoing, reference, False)['D']
    print(json.dumps(dict(case=name, **result), default=json_value, ensure_ascii=False))
    return result


def main():
    ref = {'X': Amount(F(40), own=F('2.5')),
           'Y': Amount(F(200), own=F('2.5'))}
    pooled = Amount(F(120), own=F('2.5'))
    one = {'H': {'X': pooled, 'Y': pooled}}
    customer_average = {'H-X': {'X': pooled}, 'H-Y': {'Y': pooled}}
    separated = {'H-low': {'X': ref['X']}, 'H-high': {'Y': ref['Y']}}
    a = show('En nod, massnyckel', one, ref)
    b = show('Två kundnoder, oförändrat genomsnitt', customer_average, ref)
    c = show('Åtskilda inflöden', separated, ref)
    assert a == b
    assert a['D'] == F(1, 3) and c['D'] == 0
    assert a['relations']['X']['D_relation'] == F(1, 2)
    assert a['relations']['Y']['D_relation'] == F(1, 4)

    revenue = {'H': {'X': Amount(F(144), own=F(3)),
                     'Y': Amount(F(96), own=F(2))}}
    revenue_result = show('Intäktsnyckel 60/40, fysisk referens', revenue, ref)
    assert revenue_result['D'] == F(13, 30)
    contract_ref = boundary(revenue, ('X', 'Y'))
    assert show('Samma intäktsnyckel, avtalad referens 60/40', revenue, contract_ref)['D'] == 0

    mixed_ref = {'X': Amount(F(100)), 'Y': Amount(unknown=F(100))}
    mixed = {'H': {'X': Amount(F(50), F(50)), 'Y': Amount(F(50), F(50))}}
    m = show('Lika totaler, A och U jämnas ut', mixed, mixed_ref)
    assert m['D_summa'] == 0 and m['D'] == F(1, 2)

    small_ref = {'X': Amount(F(8)), 'Y': Amount(F(360))}
    small = {'H': {'X': Amount(F('36.8')), 'Y': Amount(F('331.2'))}}
    s = show('Liten kund, massnyckel 10/90', small, small_ref)
    assert s['D'] == F(9, 115)
    assert s['relations']['X']['D_relation'] == F(9, 14)
    assert s['relations']['Y']['D_relation'] == F(1, 24)

    fine_ref = {'X-grön': Amount(F(100)), 'X-brun': Amount(unknown=F(100))}
    fine = {'H': {r: Amount(F(50), F(50)) for r in fine_ref}}
    fine_result = show('En kund, två leveransgrupper', fine, fine_ref, tuple(fine_ref))
    coarse_ref = {'X': sum(fine_ref.values(), Amount())}
    coarse = {'H': {'X': sum(boundary(fine, tuple(fine_ref)).values(), Amount())}}
    coarse_result = show('Samma flöden, en kundtotal', coarse, coarse_ref, ('X',))
    assert fine_result['D'] == F(1, 2) and coarse_result['D'] == 0

    assert show('Referens saknas', one, None)['D'] is None
    zero = {'X': Amount(), 'Y': Amount()}
    assert evaluate(zero, zero)['D'] is None
    opposite = {'X': Amount(F(100)), 'Y': Amount()}
    opposite_ref = {'X': Amount(), 'Y': Amount(F(100))}
    assert evaluate(opposite, opposite_ref)['D'] == 1
    assert all(d['D_relation'] == 1
               for d in evaluate(opposite, opposite_ref)['relations'].values())
    try:
        evaluate({'X': Amount(F(10))}, {'X': Amount(F(9))})
    except ValueError:
        pass
    else:
        raise AssertionError('Obalans får inte normaliseras bort.')

    # Egenskapskontroller på varierande fördelningar, med exakta bråk.
    rng = Random(20261030)
    for _ in range(100):
        actual = F(rng.randint(1, 200))
        unknown = F(rng.randint(1, 200))
        p, q, r, t = [F(rng.randint(0, 20), 20) for _ in range(4)]
        out = {'X': Amount(actual*p, unknown*q),
               'Y': Amount(actual*(1-p), unknown*(1-q))}
        reference = {'X': Amount(actual*r, unknown*t),
                     'Y': Amount(actual*(1-r), unknown*(1-t))}
        result = evaluate(out, reference)
        assert 0 <= result['D'] <= 1
        assert result['D'] >= evaluate(out, reference, False)['D']
        assert all(d['D_relation'] is None or 0 <= d['D_relation'] <= 1
                   for d in result['relations'].values())
        assert evaluate(reference, reference)['D'] == 0
        reversed_out = dict(reversed(list(out.items())))
        assert result == evaluate(reversed_out, reference)
        split = {f'node-{i}': {k: v.scaled(F(1, 3)) for k, v in out.items()}
                 for i in range(3)}
        assert boundary(split, ('X', 'Y')) == out
        assert evaluate(boundary(split, ('X', 'Y')), reference) == result
        with_own = {k: Amount(v.actual, v.unknown, F(rng.randint(0, 1000)))
                    for k, v in out.items()}
        assert evaluate(with_own, reference)['D'] == result['D']
    print('Kontroller godkända: omindelning, A/U-balans, kundperspektiv, gränsfall och 100 varierade fördelningar.')


if __name__ == '__main__':
    main()
