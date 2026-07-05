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
android.api = 31
android.minapi = 21
android.ndk = 25b
android.build_tools = 33.0.2
android.accept_sdk_license = True
