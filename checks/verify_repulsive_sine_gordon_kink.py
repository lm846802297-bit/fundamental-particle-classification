"""Exact finite checks for the ξ=2 continuum sine-Gordon kink control."""
from fractions import Fraction as F
from dataclasses import dataclass
import unittest


@dataclass(frozen=True)
class C:
    a: F = F(0)
    b: F = F(0)

    def __add__(self, other):
        return C(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return C(self.a*other.a - self.b*other.b,
                 self.a*other.b + self.b*other.a)

    def conjugate(self):
        return C(self.a, -self.b)


ZERO, ONE, I = C(), C(F(1)), C(F(0), F(1))
ID = ((ONE, ZERO), (ZERO, ONE))
PLUS, MINUS = ((ONE, ZERO), (ZERO, ZERO)), ((ZERO, ZERO), (ZERO, ONE))


def multiply(a, b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(2)), ZERO)
                       for j in range(2)) for i in range(2))


def dagger(a):
    return tuple(tuple(a[j][i].conjugate() for j in range(2)) for i in range(2))


def transform(operator, u, v):
    return multiply(multiply(u, operator), dagger(v))


def probability(s, pout, pin):
    matrix = multiply(multiply(multiply(pout, s), pin), dagger(s))
    return matrix[0][0] + matrix[1][1]


def block(x):
    # x=exp(relative rapidity/2); both the hyperbolic functions are rational.
    t = C(F(0), -(x - 1/x)/(x + 1/x))
    r = C(2/(x + 1/x))
    return ((t, r), (r, t))


class SineGordonAudit(unittest.TestCase):
    def test_amplitudes_and_probability(self):
        s = block(F(2))
        self.assertEqual(s[0], (C(F(0), F(-3, 5)), C(F(4, 5))))
        self.assertEqual(probability(s, MINUS, PLUS), C(F(16, 25)))
        self.assertEqual(probability(s, PLUS, PLUS), C(F(9, 25)))

    def test_mandelstam_s_from_mass_shell_and_rapidity(self):
        mass = F(5, 2)
        for x in map(F, (2, 3, 5)):
            energy = mass*(x + 1/x)/2
            p = mass*(x - 1/x)/2
            self.assertEqual(energy**2 - p**2, mass**2)
            com_s = (2*energy)**2  # p_fast+p_slow=0
            s_from_dot_product = 2*mass**2 + 2*(energy**2 + p**2)
            self.assertEqual(com_s, s_from_dot_product)
            self.assertEqual(probability(block(x), MINUS, PLUS),
                             C(4*mass**2/com_s))

    def test_unitarity_and_inverse_scattering(self):
        for x in map(F, (2, 3, 5)):
            s = block(x)
            self.assertEqual(multiply(s, dagger(s)), ID)
            self.assertEqual(multiply(s, block(1/x)), ID)
            self.assertNotEqual(multiply(s, s), ID)

    def test_probability_is_invariant_under_independent_basis_changes(self):
        s = block(F(2))
        u = ((C(F(3, 5)), C(F(4, 5))), (C(F(-4, 5)), C(F(3, 5))))
        v = ((ZERO, I), (ONE, ZERO))
        self.assertEqual(multiply(u, dagger(u)), ID)
        self.assertEqual(multiply(v, dagger(v)), ID)
        changed = probability(transform(s, u, v), transform(MINUS, u, u),
                              transform(PLUS, v, v))
        self.assertEqual(changed, C(F(16, 25)))

    def test_equal_time_canonical_phase_for_both_orders(self):
        for beta in map(F, (2, 3, 5)):  # symbolic product of a beta and an inverse beta
            for component, sign_x_minus_y in ((c, o) for c in (-1, 1) for o in (-1, 1)):
                # α γ / π = (±β/2)(2/β). Step functions give −sgn(x−y).
                alpha, gamma_over_pi = component*beta/2, 2/beta
                step_difference = (sign_x_minus_y < 0) - (sign_x_minus_y > 0)
                exponent_in_pi = -alpha*gamma_over_pi*step_difference
                self.assertEqual(exponent_in_pi % 2, 1)  # exp(iπ times an odd integer)


if __name__ == "__main__":
    unittest.main(verbosity=2)
