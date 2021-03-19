# 環境

# テスト落ちるやつ
## 実行方法
```
python failed_test.py <test_type>
```

## 引数説明
- 0: %の表記あり
- 1: %の表記なし
- 2: ゲージと%表記なし

# それっぽいインストール画面
## 参考リンク
- [genact](https://github.com/svenstaro/genact)
- [genactでターミナルで何か作業してる感を出す](https://wonderwall.hatenablog.com/entry/2018/02/05/063000_1)

## 環境構築
```
brew install genact
```

## 実行方法
```
genact -m <module> -s <speed-factor>
```

## 引数説明
moduleは色々あって、それぞれめっちゃそれっぽい文字列が出力されるようになってます。

speed-factorは文字が出力されるスピードで、1が基準となっており、速くしたい場合は数値を大きくすればできます。