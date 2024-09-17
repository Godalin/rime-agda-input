# Rime-Agda-Input

Typing symbols with agda-style shortcuts in RIME.

If you once played with agda, you will like it.

Agda 輸入法, 碼錶取材於 `agda-input.el`,
提供了大量 (數學) 符號的簡便輸入方式, 比較適用於日常記錄筆記.

## Use with other schemas

參考 `rime-latex` 以實現如何將 `rime-agda-input` 結合其他輸入方案使用.

下面是一個結合 `rime-latex` 以及 `rime-agda-input` 使用的例子 `default.custom.yaml` (我自己使用的):

```yaml
# 一個優秀的雙拼輸入法: 西文 + 中文默認西文標點

# 支持 LaTeX + Agda 符號快捷輸入, etc.
# 用輸入的鍵碼而非對應的全拼: 這個需要修改.

patch:
  # 默認英文標點符號
  switches/@0/reset: 0
  switches/@3/reset: 1

  # 設置 LaTeX 輸入結合雙拼輸入 (應當製作一個新的輸入法)
  # 把反斜槓 `\` 加入字母表
  speller/alphabet: zyxwvutsrqponmlkjihgfedcba\
  speller/delimiter: "'"
  speller/auto_select: true

  # 並且在標點階段處理, 這樣的話就可以處理全角和半角, 不用忍受奇怪的候選了
  punctuator/half_shape:
    "\\": ["\\"]
  punctuator/full_shape:
    "\\": ["、", "＼"]

  engine/+:
    # 添加碼錶
    translators/+:
      - table_translator@latex_input
      - table_translator@agda_input

  # translator's prefix will consume one '\\'. so user only type once '\' key, only recognize uppercase and lowercase letters, so you can use the number keys to select words.
  schema/dependencies/+:
    - latex
    - agda_input

  recognizer/patterns/latex_input: '^\\[a-zA-Z]+$'
  latex_input:
    tag: latex_input
    dictionary: latex
    prefix: '\'
    enable_sentence: false
    enable_completion: true # enable autocomplete
    enable_user_dict: true # enable word frequency, use with user_dict
    user_dict: custom_latex_user # generate a file name custom_latex_user.txt
    db_class: tabledb
    tips: "[LaTeX]"

  recognizer/patterns/agda_input: "^\\\\[\\D]$" # TODO: 如何得到一個支持數字變體的方案
  agda_input:
    tag: agda_input
    dictionary: agda_input
    prefix: '\_^'
    enable_sentence: false
    enable_completion: true # enable autocomplete
    enable_user_dict: true # enable word frequency,  use with user_dict
    user_dict: custom_agda_user # generate a file name custom_agda_user.txt
    db_class: tabledb
    tips: "[Agda]"

```

## Installation

可以使用 `/plum/` 進行安裝:

```bash
rime-install godalin/rime-agda-input
```

## References

本輸入法參考了 rime-latex 以及 agda 的倉庫:

- [rime-latex](https://github.com/shenlebantongying/rime_latex)
- [agda-input.el](https://github.com/agda/agda/blob/master/src/data/emacs-mode/agda-input.el)