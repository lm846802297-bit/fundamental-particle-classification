"""Independent exact-arithmetic checks for docs/existence-audit-01.md."""
from fractions import Fraction as F
import unittest


def exchange_phase(spin, winding):
    """Exponent mod 1 in exp(2*pi*i*x), from Plaschke (3.31), (3.49)."""
    return (spin * (2 * winding + 1)) % 1


def minkowski_square(vector):
    return vector[0] ** 2 - sum(x ** 2 for x in vector[1:])


def pair_sum(pair):
    return tuple(sum(components) for components in zip(*pair))


class ExistenceAudit(unittest.TestCase):
    def test_quarter_spin_same_ordering_winding(self):
        spin = F(1, 4)
        self.assertEqual(exchange_phase(spin, 0), F(1, 4))
        self.assertEqual(exchange_phase(spin, 1), F(3, 4))
        for winding in range(-4, 5):
            one = exchange_phase(spin, winding)
            self.assertEqual((2 * one) % 1, F(1, 2))
            self.assertEqual((exchange_phase(spin, winding + 1) - one) % 1,
                             F(1, 2))

    def test_inverse_orientation_is_not_double_exchange(self):
        for winding in range(-4, 5):
            one = exchange_phase(F(1, 4), winding)
            inverse = exchange_phase(F(1, 4), -winding - 1)
            self.assertEqual((one + inverse) % 1, 0)

    def test_bose_and_fermi_controls(self):
        for winding in range(-4, 5):
            for spin, expected in ((F(2), F(0)), (F(-3, 2), F(1, 2))):
                self.assertEqual(exchange_phase(spin, winding), expected)
                self.assertEqual((2 * expected) % 1, 0)

    def test_charge_one_block_parity(self):
        for charge in (-1, 1):
            counts = sorted(p + a for p in range(5) for a in range(5)
                            if p - a == charge)
            self.assertEqual(counts[:2], [1, 3])
            self.assertTrue(all(count % 2 == 1 for count in counts))

    def test_off_forward_wedge_ordered_open_patch_centers(self):
        # p=4, m=3, E=5, and (cos alpha,sin alpha)=(3/5,4/5).
        incoming = ((5, 4, 0), (5, -4, 0))
        outgoing = ((5, F(12, 5), F(16, 5)), (5, F(-12, 5), F(-16, 5)))
        self.assertEqual(len(set(incoming + outgoing)), 4)
        self.assertEqual(pair_sum(incoming), (10, 0, 0))
        self.assertEqual(pair_sum(outgoing), (10, 0, 0))
        for pair in (incoming, outgoing):
            self.assertTrue(all(v[0] > 0 and minkowski_square(v) == 9
                                for v in pair))
            speed_diff = tuple(F(a, pair[0][0]) - F(b, pair[1][0])
                               for a, b in zip(pair[0][1:], pair[1][1:]))
            self.assertGreater(speed_diff[0], 0)

    def test_ising_channel_monodromies(self):
        h_sigma, h_1, h_psi = F(1, 16), F(0), F(1, 2)
        exponents = tuple((h - 2 * h_sigma) % 1 for h in (h_1, h_psi))
        self.assertEqual(exponents, (F(7, 8), F(3, 8)))
        self.assertEqual((exponents[1] - exponents[0]) % 1, F(1, 2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
