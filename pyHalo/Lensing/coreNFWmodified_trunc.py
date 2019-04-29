from pyHalo.Halos.Profiles.coreTNFW import coreTNFW
from pyHalo.Lensing.numerical_alphas.coreNFWmodifiedtrunc import InterpCNFWmodtrunc
import numpy as np

class coreNFWmodifiedtruncLensing(object):

    hybrid = False

    lenstronomy_ID = 'NumericalAlpha'

    def __init__(self, lens_cosmo = None, zlens = None, z_source = None):

        if lens_cosmo is None:
            from pyHalo.Cosmology.lens_cosmo import LensCosmo
            lens_cosmo = LensCosmo(zlens, z_source)

        self.lens_cosmo = coreTNFW(lens_cosmo)
        self.numerical_class = InterpCNFWmodtrunc()

    def params(self, x, y, mass, redshift, concentration, r_trunc, b):

        Rs_angle, theta_Rs_nfw = self.lens_cosmo.tnfw_physical2angle(mass,
                       concentration, r_trunc, redshift)

        normalization = self._normalize(Rs_angle, theta_Rs_nfw)

        x, y = np.round(x, 4), np.round(y, 4)

        Rs_angle = np.round(Rs_angle, 6)

        r_core = np.round(b*Rs_angle, 6)

        kwargs = {'center_x': x, 'center_y': y,'Rs': Rs_angle,
                  'r_core': r_core, 'norm': normalization, 'r_trunc': r_trunc}

        return kwargs, self.numerical_class

    def _normalize(self, Rs, theta_Rs_nfw):

        bmin = self.numerical_class._betamin
        taumax = self.numerical_class._tau_max

        trs_corenfw = self.numerical_class(Rs, 0, Rs, bmin, taumax, 1)

        norm = theta_Rs_nfw * trs_corenfw ** -1
        return norm

