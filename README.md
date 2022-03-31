# MEMZのNyanCatペイロード

取り敢えず実行できるイメージが手に入れば良いのであれば[ここ](https://github.com/ponta0/NyanCat-payload/suites/5871173302/artifacts/198103418)からダウンロードできます

## NyanCatペイロードのコンパイル方法


Makefileのオプション
| オプション | 機能 |
| --- | --- |
| build | すべてコンパイルする |
| run | 仮想マシンにてペイロードを実行する |
| clean | 生成されたファイルを削除する |


nasm,gcc,python3必須

runオプションを使う場合qemuも必要

```sh
$ pip3 install -r requirements.txt
$ make build
$ make run # QEMUにて起動します
```
