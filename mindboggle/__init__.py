# emacs: -*- mode: python-mode; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:

import os

from .dist_info import __version__, long_description as __doc__
__doc__ += """
Quickstart
==========

::

   import mindboggle as mb

   mindboggle('my_file.nii.gz')

For more detailed information see the :ref:`manual`.
"""
# module imports
#from . import blah as blah
# object imports
#from .blah import blah, blah

# be friendly on systems with ancient numpy -- no tests, but at least importable
try:
    from numpy.testing import Tester
    test = Tester().test
    bench = Tester().bench
    del Tester
except ImportError:
    def test(*args, **kwargs): raise RuntimeError('Need numpy >= 1.2 for tests')

from .dist_pkg_info import get_pkg_info as _get_pkg_info
get_info = lambda : _get_pkg_info(os.path.dirname(__file__))
