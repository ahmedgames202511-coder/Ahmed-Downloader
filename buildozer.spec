[app]
title = Ahmed Downloader
package.name = ahmeddown
package.domain = org.ahmed
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,yt-dlp,certifi,requests,urllib3,idna,chardet,ffmpeg

orientation = portrait
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1
