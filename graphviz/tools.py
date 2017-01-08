# tools.py

import os

from . import _compat

__all__ = ['attach', 'mkdirs', 'mapping_items']


def attach(object, name):
    """Return a decorator doing setattr(object, name) with its argument.

    >>> spam = type('Spam', (object,), {})()
    >>> @attach(spam, 'eggs')
    ... def func():
    ...     pass
    >>> spam.eggs  # doctest: +ELLIPSIS
    <function func at 0x...>
    """
    def decorator(func):
        setattr(object, name, func)
        return func
    return decorator


def mkdirs(filename, mode=0o777):
    """Recursively create directories up to the path of filename as needed."""
    dirname = os.path.dirname(filename)
    if not dirname:
        return
    _compat.makedirs(dirname, mode=mode, exist_ok=True)


def mapping_items(mapping, _iteritems=_compat.iteritems):
    """Return an iterator over the mapping items, sort if it's a plain dict.

    >>> list(mapping_items({'spam': 0, 'ham': 1, 'eggs': 2}))
    [('eggs', 2), ('ham', 1), ('spam', 0)]

    >>> from collections import OrderedDict  # doctest: +SKIP
    >>> list(mapping_items(OrderedDict(enumerate(['spam', 'ham', 'eggs']))))  # doctest:+SKIP
    [(0, 'spam'), (1, 'ham'), (2, 'eggs')]
    """
    if type(mapping) is dict:
        return iter(sorted(_iteritems(mapping)))
    return _iteritems(mapping)
