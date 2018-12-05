
def get_polymer(file):
    with open(file) as f:
        pol = f.read().strip()
    return pol

def units(pol):
    idx = 0
    while idx < len(pol) - 1:
        if pol[idx] == pol[idx + 1]:
            idx += 1
        elif pol[idx].upper() == pol[idx + 1].upper():
            pol = pol[:idx] + pol[idx + 2:]
            idx -= 1
        else:
            idx += 1
    return len(pol)


def remove(pol):
    min = None
    for l in set(pol):
        sz = units(pol.replace(l, '').replace(l.upper(), ''))
        if min == None or min > sz:
            min = sz
    return min


polymer = get_polymer('inp1')

print(units(polymer))
print(remove(polymer))
