def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
            for sub in flatten(el):
                yield sub
        else:
            yield el


a_list = [1, 2, 3]
b_list = [1, 2, 3]

lofl = [[180.0], [173.8], [164.2], [156.5], [147.2], [138.2]]
print lofl
print flatten(lofl)