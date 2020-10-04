__title__ = "zuraaa-vote-checker"
__author__ = "uKaigo"
__license__ = "MIT"
__version__ = "0.1.2"

from collections import namedtuple

from .cog import *

ver_tuple = namedtuple('VersionInfo', 'major minor micro releaselevel serial')
version_info = ver_tuple(0, 1, 2, 'final', 0)

del(namedtuple)
del(ver_tuple)
