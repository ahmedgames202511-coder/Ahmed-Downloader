[app]
title = Ahmed Pro Downloader
package.name = ahmedpro
package.domain = org.ahmed
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# السطر ده هو اللي هيخلي التحميل يشتغل
requirements = python3,kivy==2.2.1,yt-dlp,requests,certifi,urllib3,idna,chardet

orientation = portrait
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
