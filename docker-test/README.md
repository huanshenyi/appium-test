
# dockerの環境使用

devices状態の確認

```text
docker exec -it appium(コンテナの名前) adb devices
```

手動でシミュレータに接続

まずシミュレータ(もしくは本物)のIPをtcp-ipにする

````text
adb tcpip 5555
````
複数のデバイス存在する場合

```text
adb -s ip tcpip 5555
```

デバイスのipはデバイスのネットワーク設定で確認する
```text
docker exec -it appium(コンテナの名前) adb connect ip(デバイスのip:5555)
```

# log確認

```text
docker exec -it appium bash

cd /var/log

tail -f appium.log
```