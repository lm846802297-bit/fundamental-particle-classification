"""Exact checks accompanying the 1+1D massive DHR/duality audit."""
from fractions import Fraction as F
from itertools import product
import unittest


def multiply(a, b):
    rows, columns = len(a), len(b[0])
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                       for j in range(columns)) for i in range(rows))


def tensor(a, b):
    return tuple(tuple(a[i][j]*b[k][l]
                       for j, l in product(range(len(a[0])), range(len(b[0]))))
                 for i, k in product(range(len(a)), range(len(b))))


def parity_average(a, parity):
    signed = multiply(multiply(parity, a), parity)
    return tuple(tuple(F(x + y, 2) for x, y in zip(r, s))
                 for r, s in zip(a, signed))


X = ((0, 1), (1, 0))
Z = ((1, 0), (0, -1))
I = ((1, 0), (0, 1))
LEFT, RIGHT = tensor(Z, I), tensor(I, Z)
GLOBAL = tensor(Z, Z)
BILOCAL = tensor(X, X)


def even_block(a):
    return tuple(tuple(a[i][j] for j in (0, 3)) for i in (0, 3))


def mass_square(xs, mass=F(1)):
    ep = sum(mass*x for x in xs)      # P^0+P^1
    em = sum(mass/x for x in xs)      # P^0-P^1
    return ep*em


class DualityAudit(unittest.TestCase):
    def test_global_parity_fixes_bilocal_not_independent_parities(self):
        self.assertEqual(parity_average(BILOCAL, GLOBAL), BILOCAL)
        zero = tuple((0,)*4 for _ in range(4))
        self.assertEqual(parity_average(BILOCAL, LEFT), zero)
        self.assertEqual(parity_average(BILOCAL, RIGHT), zero)

    def test_even_compression_keeps_bilocal_off_diagonal(self):
        self.assertEqual(even_block(BILOCAL), X)
        # Independently even matrices restrict to a diagonal algebra in this
        # finite grading model. This is a check, not the continuum proof.
        for i, j in product(range(4), repeat=2):
            matrix_unit = tuple(tuple(int(k == i and l == j) for l in range(4))
                                for k in range(4))
            restricted = even_block(parity_average(
                parity_average(matrix_unit, LEFT), RIGHT))
            self.assertEqual((restricted[0][1], restricted[1][0]), (0, 0))

    def test_local_odd_operator_switches_parity_and_commutes_with_other_side(self):
        left_odd, right_odd = tensor(X, I), tensor(I, X)
        self.assertEqual(multiply(left_odd, left_odd), tensor(I, I))
        self.assertEqual(multiply(left_odd, right_odd),
                         multiply(right_odd, left_odd))
        self.assertNotEqual(multiply(left_odd, GLOBAL), multiply(GLOBAL, left_odd))
        self.assertEqual(parity_average(left_odd, GLOBAL),
                         tuple((0,)*4 for _ in range(4)))

    def test_mass_shell_and_odd_multiparticle_threshold(self):
        m = F(5, 3)
        for n in (1, 3, 5):
            for xs in product(map(F, (1, 2, 3)), repeat=n):
                bound = (n*m)**2
                s = mass_square(xs, m)
                self.assertGreaterEqual(s, bound)
                self.assertEqual(s == bound, len(set(xs)) == 1)
                self.assertEqual(s, mass_square(tuple(F(5, 2)*x for x in xs), m))
        self.assertEqual(mass_square((F(1),)*3, m), 9*m*m)
        s1 = mass_square((F(1), F(101, 100), F(99, 100)), m)
        s2 = mass_square((F(1), F(1001, 1000), F(999, 1000)), m)
        self.assertLess(9*m*m, s2)
        self.assertLess(s2, s1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
