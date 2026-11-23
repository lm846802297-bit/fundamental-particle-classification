"""Exact q=3 ordered Potts checks in Q(i*sqrt(3)); no external packages."""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
import unittest


@dataclass(frozen=True)
class Q:
    a: F
    b: F = F(0)  # i*sqrt(3) coefficient

    def __add__(self, other):
        return Q(self.a + other.a, self.b + other.b)

    def __neg__(self):
        return Q(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Q(self.a*other.a - 3*self.b*other.b,
                 self.a*other.b + self.b*other.a)

    def __truediv__(self, other):
        norm = other.a**2 + 3*other.b**2
        num = self*Q(other.a, -other.b)
        return Q(num.a/norm, num.b/norm)


ONE = Q(F(1))
Z = Q(F(1, 2), F(1, 2))
G = Q(F(0), F(1))


def block(x, v):
    x = x if isinstance(x, Q) else Q(x)
    return (x*v - ONE)/(x - v)


def scattering(x, equal_charges):
    return block(x, Z*Z) if equal_charges else -block(x, Z)


def sign_rep(value):
    return {1: 1, 2: -1}[value % 3]


def path_from_increments(start, charges):
    path = [start]
    for charge in charges:
        path.append((path[-1] + charge) % 3)
    return tuple(path)


def zf_step(legs, at):
    c, x = legs[at]
    d, y = legs[at+1]
    return (legs[:at] + (legs[at+1], legs[at]) + legs[at+2:],
            scattering(x/y, c == d))


def reorder(legs, word):
    factor = ONE
    for i in word:
        legs, step = zf_step(legs, i)
        factor = factor*step
    return legs, factor


class OrderedPottsAudit(unittest.TestCase):
    def test_path_bijection_and_middle_vacuum_switch(self):
        for n in range(1, 6):
            for start in range(3):
                generated = {}
                for signs in product((-1, 1), repeat=n):
                    path = path_from_increments(start, signs)
                    reconstructed = tuple(sign_rep(b-a) for a, b in zip(path, path[1:]))
                    self.assertEqual(reconstructed, signs)
                    generated[path] = signs
                independently = {
                    (start,) + tail for tail in product(range(3), repeat=n)
                    if all(a != b for a, b in zip((start,) + tail, tail))}
                self.assertEqual(generated.keys(), independently)
        for a in range(3):
            inputs = path_from_increments(a, (1, -1))
            outputs = path_from_increments(a, (-1, 1))
            self.assertEqual(inputs[0], inputs[-1])
            self.assertEqual(outputs[0], outputs[-1])
            self.assertNotEqual(inputs[1], outputs[1])

    def test_crossing_and_elastic_inverse(self):
        for x in map(F, (1, 2, 3, 5)):
            self.assertEqual(scattering(x, True), scattering(-1/x, False))
            for equal in (False, True):
                self.assertEqual(scattering(x, equal)*scattering(1/x, equal), ONE)
                self.assertEqual(scattering(x, equal)*Q(scattering(x, equal).a,
                                                       -scattering(x, equal).b), ONE)

    def test_swap_uses_reversed_rapidity_and_three_leg_consistency(self):
        for signs in product((-1, 1), repeat=3):
            legs = tuple(zip(signs, map(F, (2, 3, 5))))
            self.assertEqual(reorder(legs, (0, 0)), (legs, ONE))
            self.assertEqual(reorder(legs, (0, 1, 0)), reorder(legs, (1, 0, 1)))
        s = scattering(F(2), False)
        self.assertNotEqual(s*s, ONE)

    def test_phase_slope_from_rational_expression(self):
        x = F(2)
        slopes = []
        for v in (Z*Z, Z):
            rational_log_derivative = Q(x)*(
                v/(Q(x)*v - ONE) - ONE/(Q(x) - v))
            slopes.append(rational_log_derivative)
        self.assertEqual(slopes, [Q(F(0), F(-2, 7)), Q(F(0), F(-2, 3))])

    def test_residues_in_rapidity_and_fusion_mass(self):
        for v, sign, expected in ((Z*Z, ONE, G), (Z, -ONE, -G)):
            # Numerator at x=v divided by dx/dθ=v.
            self.assertEqual(sign*(v*v - ONE)/v, expected)
        cos_half_pole_angle = Z.a
        self.assertEqual(2*cos_half_pole_angle, 1)


    def test_fusion_bootstrap_against_same_charge_spectator(self):
        v = Z*Z
        for x in map(F, (1, 2, 3, 5)):
            first = block(Q(x)*Z, v)
            second = block(Q(x)/Z, v)
            self.assertEqual(first*second, scattering(x, False))


if __name__ == "__main__":
    unittest.main(verbosity=2)
