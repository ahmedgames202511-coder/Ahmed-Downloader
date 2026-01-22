from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import yt_dlp
 
class VideoDownloader(App):
    def build(self):
        # الواجهة الرئيسية بلون خلفية غامق واحترافي
        self.title = "Ahmed Sayed Downloader"
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
 
        # عنوان التطبيق
        layout.add_widget(Label(
            text="Video Downloader PRO", 
            font_size='28sp', 
            bold=True, 
            color=(0, 0.8, 1, 1) # لون لبني مميز
        ))
 
        # حقل إدخال الرابط
        self.url_input = TextInput(
            hint_text="انصخ الرابط هنا...", 
            multiline=False, 
            font_size='18sp',
            size_hint_y=None, 
            height=120,
            padding_y=(30, 0),
            halign='center'
        )
        layout.add_widget(self.url_input)
 
        # زر التحميل
        self.btn = Button(
            text="DOWNLOAD (1080p/720p)", 
            background_color=(0.1, 0.7, 0.3, 1), # لون أخضر جذاب
            font_size='20sp', 
            bold=True, 
            size_hint_y=None, 
            height=140
        )
        self.btn.bind(on_press=self.start_download)
        layout.add_widget(self.btn)
 
        # حالة التحميل
        self.status = Label(text="Ready to download", color=(1, 1, 1, 1))
        layout.add_widget(self.status)
 
        # اسمك في الأسفل بشكل فخم
        layout.add_widget(Label(
            text="Developed by: Ahmed Sayed", 
            font_size='18sp', 
            bold=True,
            color=(1, 0.5, 0, 1) # لون برتقالي يظهر بوضوح
        ))
 
        return layout
 
    def start_download(self, instance):
        url = self.url_input.text
        if not url:
            self.status.text = "Please enter a URL!"
            return
 
        try:
            self.status.text = "Starting Download..."
            # خيار 'best' يضمن جودة عالية مع صوت بدون الحاجة لـ FFmpeg
            ydl_opts = {
                'format': 'best', 
                'outtmpl': '/sdcard/Download/%(title)s.%(ext)s',
                'noplaylist': True,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                self.status.text = "Downloading... please wait"
                ydl.download([url])
            
            self.status.text = "Success! Saved in Downloads"
        except Exception as e:
            # محاولة حفظ في مكان آخر إذا فشل الوصول للذاكرة الخارجية
            try:
                ydl_opts['outtmpl'] = 'video_%(id)s.%(ext)s'
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                self.status.text = "Done! Saved in App Folder"
            except:
                self.status.text = "Error: Check Link or Permissions"
 
if __name__ == '__main__':
    VideoDownloader().run()
 
