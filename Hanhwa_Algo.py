# 한화시스템 23년 상반기 코테

import sys
si = sys.stdin.readline
n = int(si())
a = list(map(int, si().split()))

def get_additional_score(selected):
    ret = 0
    a, b, c, d = selected
    if a + 1 == b and b + 1 == c and c + 1 == d:  # 4 문제 연속 해결
        return 5
    if a + 1 == b and b + 1 == c: # 세 문제 연속 해결
        return 3
    if b + 1 == c and c + 1 == d:
        return 3
    if a + 1 == b:  # a, b 연속
        ret += 2
    if b + 1 == c:  # b, c 연속
        ret += 2
    if c + 1 == d:  # c, d 연속
        ret += 2
    return ret

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                # i, j, k, l 번 문제를 풀 것이다.
                score = a[i] + a[j] + a[k] + a[l]
                score += get_additional_score((i, j, k, l))
                ans = max(ans, score)
print(ans)
'''
5
4 1 4 5 5
=>
21
'''