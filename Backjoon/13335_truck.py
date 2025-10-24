"""
Backjoon_13335 - 트럭 - S1

문제
- 
"""

from collections import deque

n, w, L = map(int, input())
truck = list(map(int, input().split()))

my_t = deque()
arrived = 0
time = 0
length = 0
weight = 0
index = 0

while arrived < n:
    