"""Finite checks for dimensions/1+1d/kink-quasistatistics-audit.md."""
from itertools import combinations, product
from math import comb
import unittest


def cut_lengths(length, cuts):
    endpoints = (0,) + cuts + (length,)
    return tuple(b - a for a, b in zip(endpoints, endpoints[1:]))


def from_partitions(n, m):
    if not (n and m):
        return {"+" * n + "-" * m}
    return {
        "".join("+" * p + "-" * q for p, q in
                zip(cut_lengths(n, pc), cut_lengths(m, mc)))
        for count in range(min(n, m))
        for pc in combinations(range(1, n), count)
        for mc in combinations(range(1, m), count)
    }


def from_positions(n, m):
    if not (n and m):
        return {"+" * n + "-" * m}
    return {
        "+" + "".join("+" if i in slots else "-" for i in range(n + m - 2)) + "-"
        for slots in combinations(range(n + m - 2), n - 1)
    }


def compose(*permutations):
    result = permutations[-1]
    for left in reversed(permutations[:-1]):
        result = tuple(left[i] for i in result)
    return result


def inverse(p):
    return tuple(p.index(i) for i in range(len(p)))


def arrows(u):
    return {(a, b): compose(ua, inverse(ub))
            for a, ua in u.items() for b, ub in u.items()}


class KinkAudit(unittest.TestCase):
    def setUp(self):
        self.identity = (0, 1, 2, 3)
        self.u = {"a": (1, 0, 2, 3), "b": (0, 2, 1, 3), "c": (2, 3, 1, 0)}
        self.v = {"a": (0, 2, 1, 3), "b": (1, 2, 3, 0), "c": (0, 1, 3, 2)}
        self.e = arrows(self.u)

    def test_independent_arrangement_enumerators(self):
        for n, m in product(range(9), repeat=2):
            expected = comb(n + m - 2, n - 1) if n and m else 1
            a, b = from_partitions(n, m), from_positions(n, m)
            self.assertEqual(a, b)
            self.assertEqual(len(a), expected)
        self.assertEqual(from_partitions(2, 2), {"++--", "+-+-"})

    def test_transitivity_and_closed_loops(self):
        self.assertNotEqual(compose(self.u["a"], self.u["b"]),
                            compose(self.u["b"], self.u["a"]))
        for a, b, c in product(self.u, repeat=3):
            self.assertEqual(compose(self.e[a, b], self.e[b, c]), self.e[a, c])
            self.assertEqual(compose(self.e[a, b], self.e[b, c], self.e[c, a]),
                             self.identity)

    def test_representative_covariance(self):
        e_new = arrows({a: compose(self.v[a], self.u[a]) for a in self.u})
        for a, b in product(self.u, repeat=2):
            self.assertEqual(e_new[a, b],
                             compose(self.v[a], self.e[a, b], inverse(self.v[b])))

    def test_in_out_overlap_conjugates_and_can_be_nontrivial(self):
        t_in, t_out = (1, 0, 2, 3), (0, 2, 3, 1)
        s = compose(t_out, inverse(t_in))
        self.assertNotEqual(s, self.identity)
        tensor_arrows = arrows(self.v)
        for a, b in product(self.u, repeat=2):
            u_ab, e_ab = tensor_arrows[a, b], self.e[a, b]
            t_in_a = compose(u_ab, t_in, inverse(e_ab))
            t_out_a = compose(u_ab, t_out, inverse(e_ab))
            for map_a, map_b in ((t_in_a, t_in), (t_out_a, t_out)):
                self.assertEqual(compose(map_a, e_ab), compose(u_ab, map_b))
            self.assertEqual(compose(t_out_a, inverse(t_in_a)),
                             compose(u_ab, s, inverse(u_ab)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
