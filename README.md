# NyanCatペイロードのコンパイル方法


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
