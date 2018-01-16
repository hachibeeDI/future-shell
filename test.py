if __name__ == '__main__':
    import doctest
    doctest.ELLIPSIS = True
    doctest.NORMALIZE_WHITESPACE = True
    doctest.testfile('README.md', optionflags=doctest.ELLIPSIS)
