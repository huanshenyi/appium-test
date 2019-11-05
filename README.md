# fiddler使用方法

## ブラウザエクステンション
SwitchyOmega

### パッケージ取得する 
File -> Capture Traffic

### パッケージファイルをロード
File -> Load Archives

### セッションのコピー
Edit ->Copy ->Session
```text
GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1
User-Agent: Fiddler/5.0.20192.25091 (.NET 4.7.1; WinNT 10.0.17763.0; ja-JP; 8xAMD64; Auto Update; Full Instance; Extensions: APITesting, AutoSaveExt, EventLog, FiddlerOrchestraAddon, HostsFile, RulesTab2, SAZClipboardFactory, SimpleFilter, Timeline)
Pragma: no-cache
Host: www.fiddler2.com
Accept-Language: ja-JP
Referer: http://fiddler2.com/client/5.0.20192.25091
Accept-Encoding: gzip, deflate
Connection: close


HTTP/1.1 200 OK
Cache-Control: private
Content-Type: text/plain; charset=utf-8
Vary: Accept-Encoding
Server: Microsoft-IIS/8.5
X-AspNet-Version: 4.0.30319
X-Powered-By: ASP.NET
Date: Sat, 02 Nov 2019 13:16:14 GMT
Connection: close
Content-Length: 880

5
0
20194
41348
5.0.20194.41348 [10/03/2019]
features:
 Ability to preserve filters in Fiddler
 New GetStarted tab
 Ability to group AutoResponder rules
 Fiddler recognizes MSEdge and Brave as web browsers
 New preference fiddler.knownbrowsers - comma-separated list with processes that Fiddler recognizes as browsers

fixes:
 Ctrl+Shift+C and Ctrl+C shortcuts do not copy
 m shortcut changes selection in AutoResponder tab
 Minor bug fixes
 
5.0.20192.25091 [06/04/2019]
 Security fix CVE-2019-12097
 Update all copyright strings to Progress Software EAD
 Various bugfixes and improvements

5.0.20182.28034 [06/27/2018]
 Publish Fiddler Chocolatey package
 Various bugfixes and improvements

@WELCOME@
Are you sweating on building JavaScript UI?

Speed up your development by using Kendo UI library for your next project - http://prgress.co/2swAPLK


```
### Sessionのマッチング

Edit -> Find Session

# adb

###macのadb path

```text
$ export PATH=$PATH:/Users/<自分のユーザー名のフォルダ>/Library/Android/sdk/platform-tools
$ adb kill-server                                                               
$ adb start-server                                                                                   
* daemon not running. starting it now on port 5037 *
* daemon started successfully *
```

### 接続デバイス一覧

```text
adb devices
```
出力例
```text
List of devices attached

TGIRP JOBFUZ)IJSW  device
127.0.0.1:62001    device
```
### デバイスshellに入る

```text
adb -s 127.0.0.1:62001 shell
```
出力例
```text
root@shamu:/ #
```

### デバイスにアプリをインストール

```text
adb -s 127.0.0.1:62001 install C:\apk\JDMALL-PC2.apk
```

### デバイスにあるアプリ一覧

```text
root@shamu:/data/app # ls
```

### デバイスアプリを削除

```text
adb -s 127.0.0.1:62001 uninstall com.tencent.mm
```

### デバイス接続

```text
adb connect 127.0.0.1:62001
```

### デバイスにファイルをアップロード

```text
adb push C:\Users\81906\Desktop\yeshen_test.txt(pcのファイルpath) /sdcard(デバイスのpath)
```

### デバイスのファイルをpcに移動

```text
adb pull /sdcard/screen.png(デバイスのpath) c:\apk\(pcのpath)
```

###デバイス使ってスクリーンショット

```text
adb shell screencap /sdcard/test.png
```

# uiautomator

## uiautomatorviewer
path
```text
C:\\Android\Sdk\tools\bin\uiautomatorviewer.bat
```

## uiautomator
https://github.com/openatx/uiautomator2

# weditor

### インストール
```text
pip install --pre weditor
```

```text
pip3 install -U uiautomator2
```

### 起動
```text
python -m weditor
```

### atx-agent使用
python -m uiautomator2 init