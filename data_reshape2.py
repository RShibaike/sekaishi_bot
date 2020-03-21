import csv
import pprint


converter_matrix = {"ア": 1, "イ": 2, "ウ": 3, "エ": 4, "オ": 5,
                    "カ": 6, "キ": 7, "ク": 8, "ケ": 9, "コ": 10,
                    "サ": 11, "シ": 12, "ス": 13, "セ": 14, "ソ": 15,
                    "タ": 16, "チ": 17, "ツ": 18, "テ": 19, "ト": 20,
                    "ナ": 21, "ニ": 22, "ヌ": 23, "ネ": 24, "ノ": 25,
                    "ハ": 26, "ヒ": 27, "フ": 28, "ヘ": 29, "ホ": 30,
                    "マ": 31, "ミ": 32, "ム": 33, "メ": 34, "モ": 35,
                    "ヤ": 36, "ユ": 37, "ヨ": 38,
                    "ラ": 39, "リ": 40, "ル": 41, "レ": 42, "ロ": 43,
                    "ワ": 44, "ヲ": 45, "ン": 46,
                    "ガ": 47, "ギ": 48, "グ": 49, "ゲ": 50, "ゴ": 51,
                    "ザ": 52, "ジ": 53, "ズ": 54, "ゼ": 55, "ゾ": 56,
                    "ダ": 57, "ヂ": 58, "ヅ": 59, "デ": 60, "ド": 61,
                    "バ": 62, "ビ": 63, "ブ": 64, "ベ": 65, "ボ": 66,
                    "パ": 67, "ピ": 68, "プ": 69, "ペ": 70, "ポ": 71,
                    "ャ": 72, "ュ": 73, "ョ": 74,
                    "ァ": 75, "ィ": 76, "ゥ": 77, "ェ": 78, "ォ": 79,
                    "0": 80, "1": 81, "2": 82, "3": 83, "4": 84, "5": 85, "6": 86, "7": 87, "8": 80, "9": 90,
                    "世": 91, "・": 92, "＝": 93,
                    "ッ": 94, "ー": 95, "ヴ": 96, "伯": 97, "王": 98,
                    "公": 99, "侯": 100, "大": 101


                    }


def Isconverter(x):
    if not x in converter_matrix.keys():
        return True
    else:
        return False


def converter(x):
    return converter_matrix[x]


with open('names_fixed_fixed3.csv') as f:
    reader = csv.reader(f)
    l2 = [row for row in reader]

l = []
for i in range(len(l2)):
    l.append(list(l2[i][0]))


return_list = []
return_list2 = []
for i in range(len(l)):
    pre_return_list = []
    pre_return_list2 = []
    for j in range(len(l[i])):
        if Isconverter(l[i][j]):
            pre_return_list2.append(i)
            pre_return_list2.append(l[i][j])
        else:
            pre_return_list.append(converter(l[i][j]))
    return_list.append(pre_return_list)
    if len(pre_return_list2) != 0:
        return_list2.append(pre_return_list2)


with open("names_fixed_fixed_fixed.csv", 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(return_list)

# print(return_list)
print(return_list2)
print(len(return_list2))
