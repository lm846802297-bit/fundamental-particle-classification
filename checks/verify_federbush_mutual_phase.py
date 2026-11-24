"""Exact finite checks derived from the Federbush audit.

They check charge counting, exchange and diagonal LSZ phase algebra, not
analytic field construction or scattering completeness.
"""
from itertools import product
import unittest

ROOTS4 = (1, 1j, -1, -1j)


def phase(power):
    return ROOTS4[power % 4]


def local_reorder(a, b):
    # Castro-Alvaredo--Fring (59), lambda=1/4, a,b in {1,2}.
    return -phase(-(-1)**b * int(a != b)), (b, a)


def scattering(s1, d1, s2, d2, order=1):
    # Ruijsenaars (5.27), lambda=1/4. A phase exponent in units of pi/2.
    return phase(-(s1 - s2) // 2 * d1 * d2 * order)


class FederbushAudit(unittest.TestCase):
    def test_charge_threshold_both_species_both_signs(self):
        for masses in ((1, 4), (7, 2), (3, 3)):
            for species, sign in product((0, 1), (-1, 1)):
                wanted = tuple(sign * int(j == species) for j in (0, 1))
                weights = []
                for n0, b0, n1, b1 in product(range(4), repeat=4):
                    if (n0 - b0, n1 - b1) == wanted and n0 + b0 + n1 + b1 > 1:
                        weights.append(masses[0] * (n0 + b0) + masses[1] * (n1 + b1))
                self.assertEqual(min(weights), masses[species] + 2 * min(masses))

    def test_field_reordering_is_involutive(self):
        for a, b in product((1, 2), repeat=2):
            first, swapped = local_reorder(a, b)
            second, back = local_reorder(*swapped)
            self.assertEqual(back, (a, b))
            self.assertEqual(first * second, 1)
            if a == b:
                self.assertEqual(first, -1)
            else:
                self.assertIn(first, (1j, -1j))

    def test_mixed_lsz_eigenvalues_and_common_ordering(self):
        pair = (scattering(1, 1, -1, 1), scattering(-1, 1, 1, 1))
        self.assertEqual(pair, (-1j, 1j))
        for label_order in (pair, pair[::-1]):
            self.assertEqual((sum(label_order), label_order[0] * label_order[1]), (0, 1))
        self.assertNotEqual(sum(pair), sum((1, 1)))

    def test_scatters_on_antisymmetric_space(self):
        for s1, d1, s2, d2 in product((-1, 1), repeat=4):
            forward = scattering(s1, d1, s2, d2)
            self.assertEqual(forward, scattering(s2, d2, s1, d1, order=-1))
            if s1 == s2:
                self.assertEqual(forward, 1)
            else:
                self.assertEqual(forward, scattering(s1, -d1, s2, d2).conjugate())


if __name__ == "__main__":
    unittest.main(verbosity=2)
