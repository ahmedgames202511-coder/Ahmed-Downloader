import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import yt_dlp

class AdvancedDownloader(App):
    def build(self):
        self.title = "Ahmed Pro Downloader"
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        self.status_label = Label(
            text="YouTube Video Downloader",
            font_size='24sp',
            bold=True,
            color=(0, 0.7, 1, 1)
        )
        
        self.url_input = TextInput(
            hint_text="Paste YouTube URL Here...",
            multiline=False,
            size_hint_y=None,
            height='55dp',
            padding_y=[15, 15]
        )
        
        download_btn = Button(
            text="DOWNLOAD NOW",
            font_size='18sp',
            bold=True,
            size_hint_y=None,
            height='60dp',
            background_color=(0, 0.6, 0.3, 1)
        )
        download_btn.bind(on_release=self.run_download)
        
        layout.add_widget(self.status_label)
        layout.add_widget(self.url_input)
        layout.add_widget(download_btn)
        
        return layout

    def run_download(self, instance):
        url = self.url_input.text
        if not url:
            self.status_label.text = "Error: Please paste a link!"
            return

        self.status_label.text = "Downloading..."
        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': '/sdcard/Download/%(title)s.%(ext)s',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.status_label.text = "Success! Saved in Downloads"
        except Exception as e:
            self.status_label.text = "Failed! Check Connection"

if __name__ == "__main__":
    AdvancedDownloader().run()
    
