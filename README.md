# pas
phone auto script

## 问题
### 手机关机之后连接不上atx：解决办法是:
    adb shell
    chmod 755 /data/local/tmp/atx-agent
    data/local/tmp/atx-agent version
    /data/local/tmp/atx-agent server -d