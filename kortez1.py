def tpl_sort(a):

    for z in a:
        if not isinstance(z, int):
            return ()
    return tuple(sorted(a))
       
print(tpl_sort((7, 13, 4, 1, 8)))
print(tpl_sort((7, 2, 4.3, 5, 1)))