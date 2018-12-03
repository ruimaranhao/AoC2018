
def checksum(file):
    def check(id):
        mem = {}
        for letter in id:
            mem[letter] = mem.get(letter, 0) + 1

        two = 0
        three = 0
        for k, v in mem.items():
            if v == 2:
                two = 1
            elif v == 3:
                three = 1
        return two, three

    twos = 0
    threes = 0
    with open(file) as f:
        ids = f.readlines()

    for id in ids:
        tw, th = check(id)
        twos += tw
        threes += th

    return twos * threes


def boxes(file):
    with open(file) as f:
        ids = f.readlines()

    for id1 in range(len(ids)):
        for id2 in range(id1 + 1, len(ids)):
            noteq = 0
            common = ''
            for f, s in zip(ids[id1].strip(), ids[id2].strip()):
                if f == s:
                    common += f
                elif f != s:
                    noteq += 1
                if noteq == 2:
                    break
            if noteq == 1:
                print(ids[id1].strip(), ids[id2].strip())
                return common



#print(checksum("inp1"))
print(boxes("inp1"))
