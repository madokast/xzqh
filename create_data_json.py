'''
读取 data 中各个年份，生成 JSON 文件
'''
import os
import json

data = dict() # code -> year -> (area)

for root, _, files in os.walk("./data"):
    for file in files:
        if file.endswith("txt"):
            year = file[:4]
            print("process", year)
            with open(os.path.join(root, file), mode='r', encoding='utf-8') as open_file:
                for line in open_file.readlines():
                    line = line.rstrip()
                    if len(line) > 8 and line[:6].isdigit():
                        code = int(line[:6])
                        area = ''.join((c for c in line[6:] if c.isprintable() and not c.isspace()))
                        if str(code) not in data:
                            data[str(code)] = dict()
                        if code % 10000 == 0:
                            data[str(code)][year] = (area, "", "")
                        elif code % 100 == 0:
                            father = data[str(code // 10000 * 10000)][year]
                            data[str(code)][year] = (father[0], area, "")
                        else:
                            if str(code // 100 * 100) in data and year in data[str(code // 100 * 100)]:
                                father = data[str(code // 100 * 100)][year]
                                data[str(code)][year] = (father[0], father[1], area)
                            else:
                                father = data[str(code // 10000 * 10000)][year]
                                data[str(code)][year] = (father[0], "", area)

with open("data.json", mode="w+", encoding='utf-8') as f:
    print("dumps", "data.json")
    json.dump(data, f, ensure_ascii=False)

with open("data_pretty.json", mode="w+", encoding='utf-8') as f:
    print("dumps", "data_pretty.json")
    json.dump(data, f, ensure_ascii=False, indent=2)


print(data["110000"])
print(data["110101"])
print(data["130100"])
print(data["430102"])
print(data["520326"])

print(data["330114"])
print(data["610322"])
    