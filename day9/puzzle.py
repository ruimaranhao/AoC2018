
from collections import deque, defaultdict

def play_game(nplayers, marbles):
    def rotateR(circle, rotations = 1):
        for _ in range(rotations):
            el = circle.pop()
            circle.appendleft(el)

    def rotateL(circle):
        el = circle.popleft()
        circle.append(el)

    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, marbles + 1):
        if marble % 23 == 0:
            rotateR(circle, 7)
            scores[marble % nplayers] += marble + circle.pop()
            rotateR(circle, 1)
        else:
            rotateL(circle)
            circle.append(marble)

    return max(scores.values())

#print(play_game(9, 25))
print(play_game(405,70953))
#print(play_game(405,70953 * 100))
