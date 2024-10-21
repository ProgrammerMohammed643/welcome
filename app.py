import telebot
import yt_dlp as youtube_dl
import os
import tempfile
import time

TOKEN = '7094935198:AAERe_rYPVRGIDnZgkXxZklb7-d42RUKA-o'
bot = telebot.TeleBot(TOKEN)

def download_youtube_video(url):
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': os.path.join(tempfile.gettempdir(), 'downloaded_video.%(ext)s'),
        'noplaylist': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        for file in os.listdir(tempfile.gettempdir()):
            if file.startswith('downloaded_video'):
                return os.path.join(tempfile.gettempdir(), file)
    return None

def compress_video(input_file):
    output_file = os.path.splitext(input_file)[0] + "_compressed.mp4"
    os.system(f'ffmpeg -i "{input_file}" -vcodec libx264 -crf 28 "{output_file}"')
    return output_file

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أرسل لي رابط فيديو يوتيوب لتنزيله.")

@bot.message_handler(func=lambda message: 'youtube.com' in message.text or 'youtu.be' in message.text)
def handle_youtube_link(message):
    url = message.text
    try:
        bot.reply_to(message, "جاري تنزيل الفيديو، انتظر قليلاً...")
        video_path = download_youtube_video(url)

        if video_path and os.path.exists(video_path):
            compressed_video_path = compress_video(video_path)
            video_size = os.path.getsize(compressed_video_path) / (1024 * 1024)

            if video_size > 50:
                bot.reply_to(message, f"حجم الفيديو {video_size:.2f} ميغابايت. الحد الأقصى هو 50 ميغابايت.")
                os.remove(video_path)
                os.remove(compressed_video_path)
            else:
                time.sleep(1)  # تأخير لمدة ثانية قبل الإرسال
                with open(compressed_video_path, 'rb') as video:
                    bot.send_video(message.chat.id, video, caption="ها هو الفيديو الذي طلبته!")
                os.remove(video_path)
                os.remove(compressed_video_path)
        else:
            bot.reply_to(message, "حدث خطأ في تنزيل الفيديو.")
    except Exception as e:
        bot.reply_to(message, f"حدث خطأ: {str(e)}")

telebot.apihelper.TIMEOUT = 300  # زيادة المهلة إلى 300 ثانية
bot.polling()
