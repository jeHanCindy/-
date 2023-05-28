# 국민은행 23년 상반기 코테 1번 문제

import sys
si = sys.stdin.readline
n, p = map(int, si().split())
link = dict()  # link[a] = b -> b가 a 를 추천한 사람
score = dict()  # score[a] = b -> a의 점수가 b 점
timestamp = dict()

def update(name, point):
    if point == 0:
        return
    score[name] += point
    if name in link:
        update(link[name], point // 10)

for ts in range(n):
    a, b = si().split()
    timestamp[a] = ts
    score[a] = 0
    if b == "-":
        continue
    link[a] = b
    update(b, p)

members = list(score.items())
members.sort(key=lambda x: (-x[1], timestamp[x[0]]))

for name, score in members:
    print(name, score)

# 6 500
# a -
# b a
# c b
# d c
# e d
# f d
# =>
# d 1000
# c 600