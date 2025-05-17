"""
دمج قائمة صور إلى فيديو MP4 بجودة 720p أو 1080p
"""
from moviepy.editor import ImageSequenceClip
from typing import List

def images_to_video(
    image_paths: List[str],
    output_path: str = "static/output_video.mp4",
    fps: int = 24,
    height: int = 720
) -> str:
    clip = ImageSequenceClip(image_paths, fps=fps)
    # إعادة تحجيم حسب الارتفاع المطلوب (720 أو 1080)
    clip_resized = clip.resize(height=height)
    clip_resized.write_videofile(
        output_path,
        codec="libx264",
        audio=False,
        threads=4,
        fps=fps,
    )
    return output_path
