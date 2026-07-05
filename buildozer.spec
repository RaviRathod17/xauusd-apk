[app]
title = XAUUSD Bot
package.name = xauusd
package.domain = org.ravi
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,requests,websocket-client
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

# android
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True
