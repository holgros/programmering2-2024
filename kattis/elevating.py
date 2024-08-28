# https://open.kattis.com/problems/elevatingtheprank (Elevating the Prank)
a, b = input().split(" ")
a = int(a)
b = int(b)
transport_time = 4*abs(a-b)
if a < b:
    floors_between = range(a+1, b)
else:
    floors_between = range(b+1, a)
n = int(input())
floors = set()
for i in range(n):
    floor = int(input())
    if floor in floors_between:
        floors.add(floor)
doors_time = 10*len(floors)
total_time = transport_time + doors_time
print(total_time)