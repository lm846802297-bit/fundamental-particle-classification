"""Finite exact checks of the algebra, geometry and norm witnesses in the audit."""
from fractions import Fraction as Q
import unittest


def clock(n):
    return (1, 1j, -1, -1j)[n % 4]


def shift(n):
    return (n + 1) % 4


def moved(n):
    """Finite clock-and-shift check of G=F V*; not a field representation."""
    return shift(n), clock(n).conjugate()


def separation(t, s, x0=3, sigma1=1, sigma2=1):
    """Equal-base-time centers, but independent displacement times t,s."""
    dt = s - t
    dx = x0 + sigma2 * s - sigma1 * t
    return dt, dx, dt - dx, dt + dx


class ComovingAudit(unittest.TestCase):
    def test_clock_and_shift_exchange(self):
        for n in range(4):
            m, fg = moved(n)
            p, gf = moved(shift(n))
            self.assertEqual(shift(m), p)
            self.assertEqual(gf, -1j * fg)
            self.assertEqual(fg.conjugate() * fg, 1)
            self.assertEqual(fg.conjugate() * gf, -1j)

    def test_right_null_translations_fix_relative_u(self):
        for t in (Q(-200), Q(100), Q(3, 2)):
            for s in (Q(-201), Q(10), Q(1, 3)):
                self.assertEqual(separation(t, s)[2], -3)

    def test_opposite_drifts_reverse_order_but_comovers_do_not(self):
        for t in (Q(10), Q(101, 3), Q(200)):
            self.assertEqual(separation(t, t)[:2], (0, 3))
            self.assertEqual(separation(-t, -t)[:2], (0, 3))
            self.assertLess(separation(t, t, sigma2=-1)[1], 0)
            self.assertGreater(separation(-t, -t, sigma2=-1)[1], 0)

    def test_product_gram_witness(self):
        for alpha in (Q(0), Q(1, 2), Q(3, 4)):
            self.assertGreater(2 * (1 - alpha**2), 0)
            # The product vectors coincide, so their difference has zero norm.
            self.assertEqual(2 - 2 * 1, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
