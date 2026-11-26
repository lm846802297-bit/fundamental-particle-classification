"""Exact finite checks of the ray pushforward and spectral-transfer logic.

The finite probes are not representations of the current net.
"""
from fractions import Fraction as Q
import unittest


def pushforward(u, t):
    return 1 - u / t


def energies_after(energies, drop):
    return tuple(e - drop for e in energies if e >= drop)


class ChiralDetectorAudit(unittest.TestCase):
    def test_velocity_response_for_a_compact_profile(self):
        # The uniform density on [-1,1] has mass 2, zero mean, and second
        # moment 2/3. Test g(z)=z² on this compact velocity image.
        for time in (Q(2), Q(5), Q(20)):
            x_lo, x_hi = 1 - 1 / time, 1 + 1 / time
            result = time * (x_hi**3 - x_lo**3) / 3
            self.assertEqual(result, 2 + Q(2, 3) / time**2)

    def test_separated_acceptances_exclude_compact_double_density(self):
        # u1,u2 in [-1,1] implies only velocities in [1-1/t,1+1/t].
        t = Q(10)
        ray_image = (pushforward(Q(1), t), pushforward(Q(-1), t))
        accept_r = (Q(3, 4), Q(5, 4))
        accept_l = (Q(-5, 4), Q(-3, 4))
        self.assertLess(accept_r[0], ray_image[0])
        self.assertLess(ray_image[0], ray_image[1])
        self.assertLess(ray_image[1], accept_r[1])
        self.assertLess(accept_l[1], ray_image[0])

    def test_sequential_negative_energy_transfers(self):
        # Either drop can act on an energy-3 input, but both cannot.
        e = (Q(3),)
        self.assertEqual(energies_after(e, Q(2)), (Q(1),))
        self.assertEqual(energies_after(energies_after(e, Q(2)), Q(2)), ())
        self.assertEqual(energies_after(energies_after((Q(5),), Q(2)), Q(2)), (Q(1),))

    def test_detector_matrix_element_does_not_read_overall_phase(self):
        # A detector that is neither diagonal nor the identity.
        vector = (2+3j, 1-2j)
        def response(v):
            z = v[0] - 2j * v[1]
            return int(z.real)**2 + int(z.imag)**2

        self.assertEqual(response(vector), 5)
        self.assertEqual(response(vector), response(tuple(-1j * x for x in vector)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
