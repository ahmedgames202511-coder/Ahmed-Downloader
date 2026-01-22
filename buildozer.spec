[app]
title = Ahmed Downloader
package.name = ahmed_downloader
package.domain = org.ahmed
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# التعديل هنا: ضفنا كل المكتبات المطلوبة بدقة
requirements = python3,kivy==2.2.1,yt-dlp,certifi,chardet,idna,requests,urllib3

orientation = portrait
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
