"""Exact finite checks of the formulas in the chiral current audit.

These tests verify rational phase exponents and a matrix identity; the audit
gives the infinite-dimensional spectral and charge-transport arguments.
"""
from fractions import Fraction as Q
import unittest


def matmul(a, b):
    return tuple(
        tuple(sum(x * y for x, y in zip(row, col)) for col in zip(*b))
        for row in a
    )


def braid_exponent(x, y):
    """Exponent in units of pi*i, with each charge an integer multiple of q."""
    return Q(x[0] * y[0] - x[1] * y[1], 2) % 2


def monodromy_exponent(x, y):
    return (braid_exponent(x, y) + braid_exponent(y, x)) % 2


def wave_presence(x):
    """Null spectral projections are nonzero precisely with spectator vacuum."""
    return (x[1] == 0, x[0] == 0)


class ChiralCurrentAudit(unittest.TestCase):
    def test_orientation_reversal(self):
        x, y = (1, 0), (2, 3)
        self.assertEqual(braid_exponent(x[::-1], y[::-1]), -braid_exponent(x, y) % 2)
        self.assertEqual(braid_exponent((1, 0), (1, 0)), Q(1, 2))
        self.assertEqual(braid_exponent((0, 1), (0, 1)), Q(3, 2))

    def test_same_orientation_monodromy(self):
        for charge in ((1, 0), (0, 1)):
            self.assertEqual(monodromy_exponent(charge, charge), 1)
        for charge in ((0, 0), (1, 1)):
            self.assertEqual(monodromy_exponent(charge, charge), 0)

    def test_additivity_under_fusion(self):
        x, y, z = (1, 0), (0, 1), (1, 3)
        xy = tuple(a + b for a, b in zip(x, y))
        self.assertEqual(
            monodromy_exponent(xy, z),
            (monodromy_exponent(x, z) + monodromy_exponent(y, z)) % 2,
        )
        # A diagonal sector's self-braid can cancel without transparency.
        self.assertEqual(monodromy_exponent(xy, x), 1)

    def test_null_projection_presence_and_mass_formula(self):
        self.assertEqual(wave_presence((0, 0)), (True, True))
        self.assertEqual(wave_presence((1, 0)), (True, False))
        self.assertEqual(wave_presence((0, 1)), (False, True))
        self.assertEqual(wave_presence((1, 1)), (False, False))
        for a in (Q(0), Q(1, 7), Q(2)):
            for b in (Q(0), Q(3, 13), Q(5)):
                self.assertEqual((a + b) ** 2 - (a - b) ** 2, 4 * a * b)

    def test_mobius_group_identity(self):
        for r in (Q(1, 2), Q(1), Q(7, 4)):
            for y in (Q(-3, 5), Q(1, 10), Q(2)):
                n = lambda u: ((1, u), (0, 1))
                lower = ((1, 0), (y, 1))
                lhs = matmul(matmul(n((r - 1) / y), lower), n((1/r - 1) / y))
                self.assertEqual(lhs, ((r, 0), (y, 1/r)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
