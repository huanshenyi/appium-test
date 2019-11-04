# appium使用方法

### appium-client

```text
pip install Appium-Python-Client
```

### 設定例
```text
{
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "jp.co.recruit.android.rikunabi.twenty",
  "appActivity": "jp.co.recruit.android.rikunabi.twenty.activity.home.HomeActivity",
  "noReset": true
}
```

### appPackage取得方法

```text
aapt.exe dump badging (apkファイルのpath)
```

#### 方法2
```text
adb shell
```

```text
logcat | grep cmp=
```

出力例
```text
cmp=jp.co.recruit.android.rikunabi.twenty/.activity.home.HomeActivity 
```
appPackage : jp.co.recruit.android.rikunabi.twenty
appActivity: jp.co.recruit.android.rikunabi.twenty.activity.home.HomeActivity
