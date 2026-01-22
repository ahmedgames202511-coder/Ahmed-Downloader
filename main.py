import os
os.environ['KIVY_NO_ARGS'] = '1'
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import yt_dlp

# واجهة التطبيق
kv = '''
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 10
    TextInput:
        id: url_input
        hint_text: 'ضع رابط الفيديو هنا'
        size_hint_y: None
        height: '50dp'
    Button:
        text: 'تحميل الفيديو'
        size_hint_y: None
        height: '50dp'
        on_release: app.download_video()
'''

class AhmedDownloader(App):
    def build(self):
        return Builder.load_string(kv)

    def download_video(self):
        url = self.root.ids.url_input.text
        if url:
            try:
                ydl_opts = {'format': 'best', 'outtmpl': '/sdcard/Download/%(title)s.%(ext)s'}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
            except Exception as e:
                print(f"Error: {e}")

if __name__ == '__main__':
    AhmedDownloader().run()
 
