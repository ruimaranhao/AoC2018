

def compute_frequency():
    frequency = 0
    with open("input") as f:
        for line in f:
            frequency += int(line)
    return frequency

def part2():
    seen = set()
    with open("input") as f:
        changes = list(map(int, f.readlines()))

    i = 0
    frequency = 0
    while True:
        if frequency in seen:
            break

        seen.add(frequency)
        frequency = frequency + changes[i]
        i = (i + 1) % len(changes)

    return frequency

def combined():
    changes = list(map(int, open("input").readlines()))

    seen = set()
    i, frequency, n_yields = 0, 0, 0
    while n_yields != 2:
        if frequency in seen:
            n_yields += 1
            yield ('seen', frequency)

        seen.add(frequency)
        frequency = frequency + changes[i % len(changes)]

        i += 1
        if i == len(changes):
            n_yields += 1
            yield ('freq', frequency)


#print(compute_frequency())
#print(part2())
print(list(combined()))
