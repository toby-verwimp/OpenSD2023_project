
import opensd_project
import numpy as np

# Pytest will discover and run all test functions named `test_*` or `*_test`.

def test_version():
    """ check opensd_project exposes a version attribute """
    assert hasattr(opensd_project, "__version__")
    assert isinstance(opensd_project.__version__, str)


class TestCore:
    """ Testing core functions """

    def test_roi_xy(self):
        """ Test the `roi_xy` function """
        xy = np.arange(-4, 5)
        roi_xy = opensd_project.roi_xy([0, 0], [8, 8])
        assert  np.all(np.equal(roi_xy, [xy, xy]))

    def test_get_displacements_zero_images(self):
        """ Test the `get_displacements` function. """
        images = np.zeros([2, 5, 5])
        d = opensd_project.get_displacements(images, [2, 2], [3, 3])
        assert np.all(np.equal(d, np.zeros((2, 2))))