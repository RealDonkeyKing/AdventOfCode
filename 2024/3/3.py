import re
sum = 0

txt = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
with open('input.txt') as file:
    line = file.read().strip()
#data = [[int(y) for y in x.split(' ')] for x in open('input.txt').read().split('\n')]
correctmuls =  re.findall(r"mul\((\d+),(\d+)\)", line)
for correctmul in correctmuls:
    num1, num2 = map(int, correctmul)
    sum += num1 * num2
print(sum)
# Solution 1 -> 157621318
sum=0
#correctmuls = re.findall(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", line)
correctmuls = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", line)
doit=1
for correctmul in correctmuls:
    if correctmul == "do()":
        doit=1
    elif correctmul == "don't()":
        doit=0
    else:
        if doit and correctmul.startswith("mul"):
            num1, num2 = map(int, re.findall(r"\d+", correctmul))
            sum += num1 * num2
print(sum)
#Solutions 2 -> 79845780