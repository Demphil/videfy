"""
دمج ملف فيديو (بدون صوت) مع ملف صوت MP3
"""
from moviepy.editor import VideoFileClip, AudioFileClip

def merge_audio_video(
    video_path: str,
    audio_path: str,
    output_path: str = "static/final_video.mp4"
) -> str:
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)
    final = video.set_audio(audio)
    final.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac"
    )
    return output_path
