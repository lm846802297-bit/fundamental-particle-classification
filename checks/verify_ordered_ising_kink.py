"""Exact checks for dimensions/1+1d/ordered-ising-kink-audit.md."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import prod
import unittest


def vacuum_chains(a, b, n):
    candidates = ((a,) + middle + (b,) for middle in product((-1, 1), repeat=n - 1))
    return [chain for chain in candidates
            if all(x != y for x, y in zip(chain, chain[1:]))]


def append_by_car(state, mode):
    coefficient, ordered = state
    if mode in ordered:
        return 0, ()
    crossings = sum(x > mode for x in ordered)
    return coefficient * (-1)**crossings, tuple(sorted(ordered + (mode,)))


def relative_tanh(x, y):
    return F(x - y, x + y)


def stripped_form_factor(xs):
    return prod(relative_tanh(x, y) for x, y in combinations(xs, 2))


def swapped(xs, i):
    values = list(xs)
    values[i], values[i + 1] = values[i + 1], values[i]
    return tuple(values)


class OrderedIsingAudit(unittest.TestCase):
    def test_exact_boundary_parity_and_unique_chain(self):
        for a, b, n in product((-1, 1), (-1, 1), range(1, 8)):
            expected = [tuple(a * (-1)**i for i in range(n + 1))] \
                if b == (-1)**n * a else []
            self.assertEqual(vacuum_chains(a, b, n), expected)
        self.assertEqual([n for n in range(1, 5) if vacuum_chains(1, -1, n)],
                         [1, 3])

    def test_car_matches_adjacent_zf_exchange_and_its_square(self):
        for n in range(2, 6):
            def ordered_state(xs):
                state = (1, ())
                for x in xs:
                    state = append_by_car(state, x)
                return state
            for xs in permutations(range(n)):
                sign, modes = ordered_state(xs)
                for i in range(n - 1):
                    ys = swapped(xs, i)
                    self.assertEqual(ordered_state(ys), (-sign, modes))
                    self.assertEqual(swapped(ys, i), xs)

    def test_local_form_factor_watson_sign(self):
        for n in (2, 4, 6):
            for xs in permutations((2, 3, 5, 7, 11, 13)[:n]):
                initial = stripped_form_factor(xs)
                self.assertNotEqual(initial, 0)
                for i in range(n - 1):
                    self.assertEqual(stripped_form_factor(swapped(xs, i)), -initial)

    def test_crossing_at_distinct_real_rapidities(self):
        for x, y in permutations((2, 3, 5, 7), 2):
            unshifted = relative_tanh(x, y)
            crossed = relative_tanh(-x, y)
            self.assertEqual(crossed, 1 / unshifted)
        self.assertEqual(relative_tanh(3, 5), F(-1, 4))
        self.assertEqual(relative_tanh(-3, 5), -4)

    def test_two_body_delta_weight_in_two_ways(self):
        mass = F(1)
        for x, expected in ((F(2), F(12, 125)), (F(3), F(9, 125))):
            # Opposite rapidities exp(θ)=x and exp(-θ)=1/x.
            s = mass**2 * (x + 1/x)**2
            t = relative_tanh(x, 1/x)
            jacobian = mass**2 * (x**2 - 1/x**2)
            direct = t**2 / jacobian  # two roots cancel 2!
            self.assertEqual(jacobian**2, s * (s - 4*mass**2))
            self.assertEqual(direct**2, (s - 4*mass**2) / s**3)
            self.assertEqual(direct, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
