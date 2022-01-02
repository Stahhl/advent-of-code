# https://adventofcode.com/2020/day/1

def part1(data):
    for a in data:
        for b in data:
            if a + b == 2020:
                return a * b

def part2(data):
    for a in data:
        for b in data:
            for c in data:
                if a + b + c == 2020:
                    return a * b * c

input = open('01/input.txt', 'r', encoding='utf-8').read().splitlines()
dataInt = [int(x) for x in input]

print(part1(dataInt))
print(part2(dataInt))