from collections import defaultdict, deque

def solution(file):
    graph_bw = defaultdict(set)
    graph = defaultdict(set)
    with open(file) as f:
        for line in f:
            sline = line.split(" ")
            graph[sline[1]].add(sline[7])
            graph_bw[sline[7]].add(sline[1])

    fst_elms = set(graph.keys()) - set(graph_bw.keys())
    fst_el = fst_elms.pop()

    order = ""

    available = list(sorted(set(graph.keys()) - set(graph_bw.keys()))[::-1])
    while available:
        nxt = available.pop()

        if all(e_fw in order for e_fw in graph_bw[nxt]):
            order += nxt

        for e in graph[nxt]:
            if e not in available:
                available.append(e)
        available = sorted(available)[::-1]

    print(order)


import sys

def part2(file, nworkers = 5):

    def time(c):
        return 60 + ord(c) - ord('A')

    def next_step(steps, l):
        return [s for s in steps if all(b != s for (_, b) in l)]

    def read_input(file):
        with open(file) as f:
            lines = map(lambda l: l.split(), f.readlines())
        return [(l[1], l[7]) for l in lines]

    lines = read_input(file)
    steps = set([s[0] for s in lines] + [s[1] for s in lines])

    tick = 0
    workers = [0 for _ in range(nworkers)]
    work = [None for _ in range(nworkers)]
    while steps or any(w > 0 for w in workers):
        cand = list(next_step(steps, lines))
        cand.sort()
        cand = cand[::-1]

        for i in range(5):
            workers[i] = max(workers[i] - 1, 0)
            if workers[i] == 0:
                if work[i] is not None:
                    lines = [(a, b) for (a, b) in lines if a != work[i]]
                if cand:
                    n = cand.pop()
                    workers[i] = time(n)
                    work[i] = n
                    steps.remove(n)

        tick += 1

    print(tick)


solution('inp1')
part2('inp1')
