import csv
import pprint

with open('names.csv') as f:
    reader = csv.reader(f)
    l2 = [row for row in reader]

l = []
for i in range(len(l2)):
    l.append(list(l2[i][0]))


for i in l:
    for j in range(len(i)):
        if i[0].isdecimal():
            del i[0]
        else:
            break

    if "." in i:
        i.remove(".")

    if "?" in i:
        i.remove("?")

    if i[0] == " ":
        del i[0]

    for j in range(len(i)):
        if i[j] == "（":
            del i[j:]
            break
        if i[j] == "(":
            del i[j:]
            break
        if i[j] == "[":
            del i[j:]
            break


l = [s for s in l if s != []]


rl = []
for i in l:
    i = "".join(i)
    rl.append(i)


rl2 = [[x] for x in rl]
# pprint.pprint(rl2)
with open("names_fixed.csv", 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rl2)


# with open('names_fixed.csv') as f:
#     reader = csv.reader(f)
#     l2 = [row for row in reader]

# l = []
# for i in range(len(l2)):
#     l.append(list(l2[i]))


# pprint.pprint(l)
