lines = open("words.txt").readlines()

# lines.sort(key=len)
# maximum = lines[-1]
# print(maximum)
# print(len(maximum))

maximum = max(lines, key=len)
# print(maximum)
# print(len(maximum))

for i in lines:
    if len(i) == len(maximum):
        print(i)
