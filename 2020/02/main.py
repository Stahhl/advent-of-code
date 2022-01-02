# https://adventofcode.com/2020/day/2

input = open('02/input.txt', 'r', encoding='utf-8').read().splitlines()

def part1():
    answer = 0
    for row in input:
        lower = int(row[0:row.index("-")])
        upper = int(row[row.index("-")+1:row.index(" ")])
        letter = row[row.index(" ")+1:row.index(":")].strip()
        password = row[row.index(":")+1:].strip()
        numberOfLettersInPassword = sum(i==letter for i in password)
        if lower <= numberOfLettersInPassword <= upper:
            answer += 1
    return answer

def part2():
    answer = 0
    for row in input:
        lower = int(row[0:row.index("-")])
        upper = int(row[row.index("-")+1:row.index(" ")])
        letter = row[row.index(" ")+1:row.index(":")].strip()
        password = row[row.index(":")+1:].strip()
        if (password[lower-1] == letter) ^ (password[upper-1] == letter):
            answer += 1
    return answer

print(part1())
print(part2())