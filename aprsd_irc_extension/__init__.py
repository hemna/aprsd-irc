from importlib.metadata import PackageNotFoundError, version


try:
    __version__ = version("aprsd-irc-extension")
except PackageNotFoundError:
    pass
