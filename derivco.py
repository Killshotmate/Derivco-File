matching = input()
line = matching.replace(" ", "")
values = dict()

for letter in line:
    if (letter in values):
        values[letter] += 1
    else:
        values[letter] = 1


visited = dict()
occurStr = "" # Used to store occurences

for letter in line:
    if (letter in visited): # Don't re-add freqencies if already visited
        continue

    visited[letter] = True
    occurStr += str(values[letter])

line = occurStr
n = len(line)

while (n > 2):
    prevStr = ""

    for i in range(n // 2):
        left = line[i]
        right = line[n - i - 1]
        letterSum = int(left) + int(right)
        prevStr += str(letterSum)

    if (n % 2 == 1):
        prevStr += line[n // 2]

    line = prevStr
    n = len(prevStr)

output = matching + " {}%".format(prevStr)

if (int(prevStr) >= 80):
    output += ", good match"

print(output)

