import unittest
import atmosfera_estandar
class TestAtmosferaEstandar(unittest.TestCase):

    def setUp(self):
        self.rho0 = 1.225   #[kg/m**3]
        self.tol_p = 10
        self.tol_t = 1e-1
        self.tol_rho = 1e-2
        self.tol_mu = 1e-6
        self.tol_vson = 1

        self.values = [  [   0,	288.15,	1.01325, 1.0000,	1.461,	2.534,	340.3 ],
                    [ 500,  284.9,	0.9546,	0.9529,	1.520,	2.509,	338.4 ],
                    [1000,	281.7,	0.8988,	0.9075,	1.581,	2.483,	336.4 ],
                    [1500,	278.4,	0.8456,	0.8638,	1.646,	2.457,	334.5 ],
                    [2000,	275.2,	0.7950,	0.8217,	1.715,	2.431,	332.5 ],
                    [2500,	271.9,	0.7469,	0.7812,	1.787,	2.405,	330.6 ],
                    [3000,	268.7,	0.7012,	0.7423,	1.863,	2.379,	328.6 ],
                    [3500,	265.4,	0.6578,	0.7048,	1.943,	2.353,	326.6 ],
                    [4000,	262.2,	0.6166,	0.6689,	2.028,	2.327,	324.6 ],
                    [4500,	258.9,	0.5775,	0.6343,	2.117,	2.301,	322.6 ],
                    [5000,	255.7,	0.5405,	0.6012,	2.211,	2.275,	320.5 ],
                    [5500,	252.4,	0.5054,	0.5694,	2.311,	2.248,	318.5 ],
                    [6000,	249.2,	0.4722,	0.5389,	2.416,	2.222,	316.5 ],
                    [6500,	245.9,	0.4408,	0.5096,	2.528,	2.195,	314.4 ],
                    [7000,	242.7,	0.4111,	0.4817,	2.646,	2.169,	312.3 ],
                    [7500,	239.5,	0.3830,	0.4549,	2.771,	2.142,	310.2 ],
                    [8000,	236.2,	0.3565,	0.4292,	2.904,	2.115,	308.1 ],
                    [8500,	233.0,	0.3315,	0.4047,	3.046,	2.088,	306.0 ],
                    [9000,	229.7,	0.3080,	0.3813,	3.196,	2.061,	303.8 ],
                    [9500,	226.5,	0.2858,	0.3589,	3.355,	2.034,	301.7 ],
                    [10000,	223.3,	0.2650,	0.3376,	3.525,	2.007,	299.8 ],
                    [10500,	220.0,	0.2454,	0.3172,	3.706,	1.980,	297.4 ],
                    [11000,	216.8,	0.2270,	0.2978,	3.899,	1.953,	295.2 ],
                    [11500,	216.7,	0.2098,	0.2755,	4.213,	1.952,	295.1 ],
                    [12000,	216.7,	0.1940,	0.2546,	4.557,	1.952,	295.1 ],
                    [12500,	216.7,	0.1793,	0.2354,	4.930,	1.952,	295.1 ],
                    [13000,	216.7,	0.1658,	0.2176,	5.333,	1.952,	295.1 ],
                    [13500,	216.7,	0.1533,	0.2012,	5.768,	1.952,	295.1 ],
                    [14000,	216.7,	0.1417,	0.1860,	6.239,	1.952,	295.1 ],
                    [14500,	216.7,	0.1310,	0.1720,	6.749,	1.952,	295.1 ],
                    [15000,	216.7,	0.1211,	0.1590,	7.300,	1.952,	295.1 ],
                    [15500,	216.7,	0.1120,	0.1470,	7.895,	1.952,	295.1 ],
                    [16000,	216.7,	0.1035,	0.1359,	8.540,	1.952,	295.1 ],
                    [16500,	216.7,	0.09572, 0.1256,	9.237,	1.952,	295.1 ],
                    [17000,	216.7,	0.08850, 0.1162,	9.990,	1.952,	295.1 ],
                    [17500,	216.7,	0.08182,	0.1074,	10.805,	1.952,	295.1 ],
                    [18000,	216.7,	0.07565,	0.09930,	11.686,	1.952,	295.1 ],
                    [18500,	216.7,	0.06995,	0.09182,	12.639,	1.952,	295.1 ],
                    [19000,	216.7,	0.06467,	0.08489,	13.670,	1.952,	295.1 ],
                    [19500,	216.7,	0.05980,	0.07850,	14.784,	1.952,	295.1 ],
                    [20000,	216.7,	0.05529,	0.07258,	15.989,	1.952,	295.1 ],
                    [22000,	218.6,	0.04047,	0.05266,	22.201,	1.968,	296.4 ],
                    [24000,	220.6,	0.02972,	0.03832,	30.743,	1.985,	297.7 ],
                    [26000,	222.5,	0.02188,	0.02797,	42.439,	2.001,	299.1 ],
                    [28000,	224.5,	0.01616,	0.02047,	58.405,	2.018,	300.4 ],
                    [30000,	226.5,	0.01197,	0.01503,	80.134,	2.034,	301.7 ] ]
        # Values from:http://www.engineeringtoolbox.com/international-standard-atmosphere-d_985.html
        # headers: Elevation [m], Temperature [K], Pressure[Pa*1e-5], Relative density, Kinematic Viscosity[m/s2*1e-5], Thermal conductivity [W/m K*1e-2], Speed of sound [m/s]

    def test_up_to_70000_ft_pressure(self):
        for line in self.values:
            h, _, p, t, rho, mu, vson = atmosfera_estandar.atmosfera_estandar('altura', line[0], deltaT=0)
            self.assertAlmostEquals(p, line[2] * 1e5, delta=self.tol_p, msg="Expected {}+-{}, got {}. Fail with h = {}m".format(line[2]*1e5, self.tol_p, p, h))

    def test_up_to_70000_ft_temperature(self):
        for line in self.values:
            h, _, p, t, rho, mu, vson = atmosfera_estandar.atmosfera_estandar('altura', line[0], deltaT=0)
            self.assertAlmostEquals(t, line[1], delta=self.tol_t, msg="Expected {}+-{}, got {}. Fail with h = {}m".format(line[1], self.tol_t, t, h))

    def test_up_to_70000_ft_densidad(self):
        for line in self.values:
            h, _, p, t, rho, mu, vson = atmosfera_estandar.atmosfera_estandar('altura', line[0], deltaT=0)
            self.assertAlmostEquals(rho, line[3]*self.rho0, delta=self.tol_rho, msg="Expected {}+-{}, got {}. Fail with h = {}m".format(line[3], self.tol_rho, rho, h))

    def test_up_to_70000_ft_viscosidad(self):
        for line in self.values:
            h, _, p, t, rho, mu, vson = atmosfera_estandar.atmosfera_estandar('altura', line[0], deltaT=0)
            self.assertAlmostEquals(mu, line[4]*1e-5, delta=self.tol_mu, msg="Expected {}+-{}, got {}. Fail with h = {}m".format(line[4]*1e-5, self.tol_mu, mu, h))

    def test_up_to_70000_ft_vson(self):
        for line in self.values:
            h, _, p, t, rho, mu, vson = atmosfera_estandar.atmosfera_estandar('altura', line[0], deltaT=0)
            self.assertAlmostEquals(vson, line[6], delta=self.tol_vson, msg="Expected {}+-{}, got {}. Fail with h = {}m".format(line[6], self.tol_vson, vson, h))

if __name__ == "__main__":
    unittest.main()