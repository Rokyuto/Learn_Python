def comp(o):
    return int(o.split()[0])

l = ['4 dollars', '8 dollars', '12 dollars', '23 dollars', '4 dollars']
l.sort(key=comp)
print(l)