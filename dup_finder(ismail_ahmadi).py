name_list = [ 'Mir', 'Azim', 'Sami', 'Masih', 'Sami', 'Ahmad', 'Mir', 'Mir', 'Ahmad']
duplicates = []
for x in name_list:
    if name_list.count(x) > 1 and x not in duplicates:
        duplicates.append(x)
        print( str(x) + ' is repeated (' + str(name_list.count(x)) + ') Times')