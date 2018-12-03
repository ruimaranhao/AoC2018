import re

def square_inches(file):
    matches = []
    with open('inp0') as f:
        for line in f:
            match = re.match(r'#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)', line).groupdict()
            matches.append({k: int(v) for k, v in match.items()})

    fabric = []
    for y in range(1000):
        fabric.append([])
        for x in range(1000):
            fabric[y].append([0, set()])

    for k in matches:
        for y in range(k['y'], k['y'] + k['h']):
            for x in range(k['x'], k['x'] + k['w']):
                fabric[y][x][0] += 1
                fabric[y][x][1].add(k['id'])

        overlap = 0
        for y in fabric:
            for x in y:
                if x[0] > 1:
                    overlap += 1
        print(overlap)

    for k in matches:
        intact = True
        for y in range(k['y'], k['y'] + k['h']):
            for x in range(k['x'], k['x'] + k['w']):
                if any(i != k['id'] for i in fabric[y][x][1]):
                    intact = False
                    break
        if intact:
            print(k['id'])



def square_inches_v2(file):
    matches = []
    with open(file) as f:
        for line in f:
            match = re.match(r'#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)', line).groupdict()
            matches.append({k: int(v) for k, v in match.items()})

    sum_fabric = 0
    for idx_m in range(len(matches)):
        for idx_m_ in range(idx_m + 1, len(matches)):
            m = matches[idx_m]
            m_ = matches[idx_m_]

            inter_x = set(range(m['x'], m['x'] + m['w'])).intersection(range(m_['x'], m_['x'] + m_['w']))
            if inter_x != set():
                inter_y = set(range(m['y'], m['y'] + m['h'])).intersection(range(m_['y'], m_['y'] + m_['h']))
                if inter_y != set():
                    print(m, m_)
                    print(inter_x, inter_y, len(inter_x) * len(inter_y))
                    sum_fabric += len(inter_x) * len(inter_y)

    return sum_fabric


print(square_inches_v2('inp0'))
