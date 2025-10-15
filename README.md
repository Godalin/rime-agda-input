# Rime-Agda-Input

Typing symbols with agda-style shortcuts in RIME.

If you once played with agda, you will like it.

![examples](/image/examples.png)


Agda 輸入法, 碼錶取材於 `agda-input.el`,
提供了大量 (數學) 符號的簡便輸入方式, 比較適用於日常記錄筆記.

## Use with other schemas

參考 `rime-latex` 以實現如何將 `rime-agda-input` 結合其他輸入方案使用.

下面是一個結合 `rime-latex` 以及 `rime-agda-input` 使用的例子.

`default.custom.yaml` (我自己使用的) [可以參考這裏](https://github.com/Godalin/RimeConfig)來詳細瞭解如何結合符號輸入法到已有輸入法, 或者基於符號輸入法構造新的輸入法:

```yaml
# 一個優秀的雙拼輸入法: 西文 + 中文默認西文標點

# 支持 LaTeX 公式快捷輸入, etc.
# 支持 agda-input 公式輸入, 因爲這套方案很優雅.
# 從此需要習慣使用 enter 鍵入當前的英文內容. 把它設置成 tab 就更好了.
# 用輸入的鍵碼而非對應的全拼: 這個需要修改.

patch:
  schema/name: 自然碼雙拼⟨魔改⟩
  # 依赖于 rime-latex 以及 rime-agda
  schema/dependencies/+:
    - latex
    - agda_input

  # 默認英文標點符號
  switches/@0/reset: 0
  switches/@3/reset: 1

  # 設置 LaTeX 輸入結合雙拼輸入 (應當製作一個新的輸入法)
  # 把反斜槓 `\` 加入字母表
  speller/alphabet: zyxwvutsrqponmlkjihgfedcba\
  speller/delimiter: "'"
  speller/auto_select: true

  # 並且在標點階段處理, 這樣的話就可以處理全角和半角, 不用忍受奇怪的候選了
  # punctuator/half_shape:
  #   "\\": ["\\"]
  # punctuator/full_shape:
  #   "\\": ["、", "＼"]

  engine/+:
    # 加入 latex 的碼錶, 如果我想加入自己的碼錶, 我就應該在這裏加上
    # 以及 Agda 輸入法 (現已加入全家桶)
    translators/+:
      - table_translator@latex
      - table_translator@agda_input

  recognizer/patterns/+:
    # 將下面的模式都映射到 symbol tag, 並且啓用下面的兩張表去查對應的符號
    symbol: "^\\\\(\\D|(\\\\\\d))+$"

  latex:
    tag: symbol
    dictionary: latex
    prefix: '\'
    enable_sentence: false
    enable_completion: true
    enable_user_dict: true
    user_dict: custom_latex_user
    db_class: tabledb
    tips: "[LaTeX]"

  agda_input:
    tag: symbol
    dictionary: agda_input
    prefix: '\'
    enable_sentence: false
    enable_completion: true
    enable_user_dict: true
    user_dict: custom_agda_user
    db_class: tabledb
    tips: "[Agda]"
```

爲了保留所有需要用到數字的符號, 把 `\d` 都轉換成了 `\\d`.
然後, 需要配置一下 `agda_input` 的拼寫運算以啓用上述轉化:

`agda_input.custom.yaml`:

```yaml
patch:
  speller/algebra/+:
    - derive/(\d)/\\$1
```

這樣就可以用到數字鍵位了. 舉例:

```
爲了打 𝟝, 可以輸入 \b\5, 會轉化成 \b5, 此時只有一個候選, 按 1 不會增加鍵入碼的長度, 而是會選擇 𝟝.
```

非常地好用.

## Installation

可以使用 `/plum/` 進行安裝:

```bash
rime-install godalin/rime-agda-input
```

## TODOs:

- ~~現在同時啓用 rime-agda-input 和 rime-latex, 後者會不起作用. 後續會進行修改.~~
- 暫無

## References

本輸入法參考了 rime-latex 以及 agda 的倉庫,
感謝各位大佬對開源社區的貢獻, 同時我也想把這份精神傳承下去:

- [rime-latex](https://github.com/shenlebantongying/rime_latex)
- [agda-input.el](https://github.com/agda/agda/blob/master/src/data/emacs-mode/agda-input.el)
