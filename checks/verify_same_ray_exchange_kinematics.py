"""Exact finite checks for the same-ray kinematic comparison.

The tests do not construct a field net or a scattering representation.
"""
from fractions import Fraction as Q
from itertools import product
import unittest


def energy_fraction(p1, p2):
    return p1 + p2, p1 / (p1 + p2)


def braid_applied(state, word, phase):
    amp = 1
    values = list(state)
    for j in word:
        values[j], values[j + 1] = values[j + 1], values[j]
        amp *= phase
    return amp, tuple(values)


class SameRayKinematicAudit(unittest.TestCase):
    def test_fraction_measure_from_jacobian(self):
        for p1, p2 in product((Q(2, 3), Q(7, 4), Q(11)), repeat=2):
            total, fraction = energy_fraction(p1, p2)
            dp1_dtotal, dp1_dfraction = fraction, total
            dp2_dtotal, dp2_dfraction = 1 - fraction, -total
            jac = abs(dp1_dtotal * dp2_dfraction - dp1_dfraction * dp2_dtotal)
            self.assertEqual(jac, total)
            self.assertEqual(jac / (p1 * p2), 1 / (total * fraction * (1 - fraction)))

    def test_boost_and_flip_actions(self):
        for p1, p2, boost in product((Q(2, 3), Q(7, 4), Q(11)), repeat=3):
            total, fraction = energy_fraction(p1, p2)
            self.assertEqual(energy_fraction(boost * p1, boost * p2), (boost * total, fraction))
            self.assertEqual(energy_fraction(p2, p1), (total, 1 - fraction))

    def test_braid_relations_allow_both_squares(self):
        state = (2, 3, 5, 7)
        for phase, square in ((1, 1), (-1, 1), (1j, -1), (-1j, -1)):
            self.assertEqual(braid_applied(state, (0, 0), phase), (square, state))
            self.assertEqual(braid_applied(state, (0, 1, 0), phase),
                             braid_applied(state, (1, 0, 1), phase))
            self.assertEqual(braid_applied(state, (0, 2), phase),
                             braid_applied(state, (2, 0), phase))


    def test_coherent_reference_distinguishes_relative_phase(self):
        # Unnormalized |0> + phase |1>, with norm squared exactly 2.
        for phase, expected in ((1, (1, 0)), (-1, (-1, 0)),
                                (1j, (0, 1)), (-1j, (0, -1))):
            e_x = (phase + phase.conjugate()).real / 2
            e_y = (-1j * phase + 1j * phase.conjugate()).real / 2
            self.assertEqual((e_x, e_y), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
