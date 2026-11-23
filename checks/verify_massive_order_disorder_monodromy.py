"""Exact algebraic checks for the 1+1D order–disorder/monodromy audit."""
import unittest
from itertools import product
from collections import Counter
from fractions import Fraction as F


LABELS = tuple(product(range(3), repeat=2))
E, D, X = (0, 1), (1, 0), (1, 1)


def fuse(x, y):
    return tuple((a+b) % 3 for a, b in zip(x, y))


def exchange(x, y):
    # Phase exponent in zeta=e^(2*pi*i/3), R=sum V_g tensor U(g).
    return (x[0]*y[1]) % 3


def monodromy(x, y):
    return (exchange(x, y) + exchange(y, x)) % 3


def cyclotomic_sum(exponents):
    # Reduce a+b*zeta+c*zeta**2 in Z[zeta], using zeta**2=-1-zeta.
    c = Counter(e % 3 for e in exponents)
    return c[0]-c[2], c[1]-c[2]


def charge_sectors(number):
    return Counter(sum(word) % 3 for word in product((1, -1), repeat=number))


class MonodromyAudit(unittest.TestCase):
    def test_mixed_and_dyon_monodromies(self):
        self.assertEqual((exchange(E, D), exchange(D, E)), (0, 1))
        self.assertEqual(monodromy(E, D), 1)
        self.assertEqual(monodromy(X, X), 2)
        for e, f in product(range(3), repeat=2):
            self.assertEqual(monodromy((0, e), (0, f)), 0)

    def test_exchange_and_monodromy_respect_fusion(self):
        for x, y, z in product(LABELS, repeat=3):
            self.assertEqual(exchange(x, fuse(y, z)),
                             (exchange(x, y) + exchange(x, z)) % 3)
            self.assertEqual(monodromy(fuse(x, y), z),
                             (monodromy(x, z) + monodromy(y, z)) % 3)

    def test_full_character_table_orthogonality(self):
        for x, y in product(LABELS, repeat=2):
            row_dot = cyclotomic_sum(monodromy(x, z)-monodromy(y, z) for z in LABELS)
            self.assertEqual(row_dot, (9, 0) if x == y else (0, 0))

    def test_disorder_extensions_agree_only_on_neutral_states_for_generator(self):
        # If U_L(g) U_R(g)=U(g), U_L(g)/U_R(g^-1) has exponent e*g.
        for e, g, right in product(range(3), repeat=3):
            left = (e*g-right) % 3
            self.assertEqual((left+right) % 3, (e*g) % 3)
            self.assertEqual(left == (-right) % 3, e == 0 or g == 0)

    def test_mass_m_multiplicity_and_charged_threshold(self):
        self.assertEqual(charge_sectors(0), {0: 1})
        self.assertEqual(charge_sectors(1), {1: 1, 2: 1})
        self.assertEqual(charge_sectors(2), {0: 2, 1: 1, 2: 1})
        self.assertEqual(sum((-1, -1)) % 3, 1)
        self.assertEqual(sum((1, 1)) % 3, 2)
        # Rational light-cone factors exp(theta) at several boosts.
        for x, y in product(map(F, (1, 2, 5)), repeat=2):
            squared_mass_in_m_units = (x+y)*(1/x+1/y)
            self.assertGreaterEqual(squared_mass_in_m_units, 4)
            self.assertEqual(squared_mass_in_m_units == 4, x == y)


if __name__ == "__main__":
    unittest.main(verbosity=2)
