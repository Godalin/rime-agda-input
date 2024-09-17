import re
import string

# 打开文件，确保使用'utf-8'编码
with open('./agda-input.el', 'r', encoding='utf-8') as file:
    content = file.read()


# 定义要匹配的正则表达式
pattern = re.compile(
    r'''\(\"(?P<key>.*?)\"\s*\.\s*(?P<sym>
      \,\(agda-input-to-string-list\s*\"(?P<symlist>.*?)\"\)|
      \(\"(?P<symsing>.*?)\"\))\)''',
    re.X)

# 使用re.search来查找匹配的字符串
matches = pattern.finditer(content)


def add_single_symbol(key: str, symbol, file):
    """ if key.startswith(("^", "_")):
        pass
    else: """
    key = "\\" + key
    print(symbol, key, sep="\t", file=file)

def add_symbol_list(key, symbols, file):
    for sym in symbols:
        if sym in string.whitespace:
            continue
        add_single_symbol(key, sym, file)



if matches:
    print("找到匹配的字符串, 開始生成碼錶")
    with open("agda_input.dict.yaml", 'w', encoding='utf-8') as dict_yaml:
        print("""\
# Rime dictionary
# encoding: utf-8

---
name: agda_input
version: "0.1"
sort: original
columns:
  - text
  - code
...

""", file=dict_yaml, end="")
        
        for match_dict in matches:
            match_dict = match_dict.groupdict()
            if match_dict["symsing"] != None:
                add_single_symbol(
                    match_dict["key"],
                    match_dict["symsing"],
                    dict_yaml)
            elif match_dict["symlist"] != None:
                add_symbol_list(
                    match_dict["key"],
                    match_dict["symlist"],
                    dict_yaml)
else:
    print("冇匹配的字符串")