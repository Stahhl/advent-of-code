# https://adventofcode.com/2020/day/3

input = open('03/input.txt', 'r', encoding='utf-8').read().splitlines()

def downhill(input, xMove, yMove):
    answer, x, y = 0, 0, 0
    xMax = len(input[0])
    yMax = len(input)
    while y < yMax:
        if input[y][x % xMax] == '#':
            answer += 1
        x += xMove
        y += yMove
    return answer

def part1():
    return downhill(input, 3, 1)

def part2():
    answer = 1
    slopes = [(1, 1),(3, 1),(5, 1),(7, 1),(1, 2)]
    for slope in slopes:
        answer *= downhill(input, slope[0], slope[1])
    return answer

print(part1())
print(part2())
