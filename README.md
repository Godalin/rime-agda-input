# Rime-Agda-Input

Typing symbols with agda-style shortcuts in RIME.

If you once played with agda, you will like it.

Agda 輸入法, 碼錶取材於 `agda-input.el`,
提供了大量 (數學) 符號的簡便輸入方式, 比較適用於日常記錄筆記.

## Differences from `agda-input.el`

上下標的輸入方式不需要加上前綴 `\`, 直接以 `^_` 開始就會輸入上下標的小字.

## Use with other schemas

參考 `rime-latex` 以實現如何將 `rime-agda-input` 結合其他輸入方案使用.

TODO: 給出一個結合使用的例子

## References

本輸入法參考了 rime-latex 以及 agda 的倉庫:

- [rime-latex](https://github.com/shenlebantongying/rime_latex)
- [agda-input.el](https://github.com/agda/agda/blob/master/src/data/emacs-mode/agda-input.el)