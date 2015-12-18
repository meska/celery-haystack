__version__ = '0.91'


def version_hook(config):
    config['metadata']['version'] = __version__
