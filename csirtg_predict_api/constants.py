from ._version import get_versions
__version__ = get_versions()['version']
VERSION = __version__
del get_versions

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s[%(lineno)s] - %(message)s'