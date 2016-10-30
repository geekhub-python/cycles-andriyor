#!/usr/bin/env python3

day_seven = 0
day_n = 0
m = 10
n = int(input())
for i in range(1, 9999):
    if i <= 10:
        print('За', i, 'дней', 'лыжник пробежал', round(m, 2), 'километров')
    if i <= 7:
        day_seven += m
    if i <= n:
        day_n += m
    if m >= 80:
        stop = i
        break
    m *= 1.1
print('За первые 7 дней тренировок пробежал', round(day_seven, 2), 'км')
print('суммарный путь за', n, 'дней тренировок:', round(day_n, 2), 'км')
print("В", stop, 'день следует прекратить увеличивать пробег')
