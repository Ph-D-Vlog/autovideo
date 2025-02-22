import time
from tqdm import tqdm
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeAudioClip

import gc
gc.enable()


def render_video(input_file, output_file, voice_intervals, bgm_flag=False):

    video = VideoFileClip(input_file)
    clips = []

    for start, end in tqdm(voice_intervals, desc='clips', ncols=100):
        clips.append(video.subclip(start, end))
    print()

    final_clip = concatenate_videoclips(clips)

    if bgm_flag:
        # 加载背景音乐
        # background_music = AudioFileClip('PELAGIC - Density & Time.mp3')
        background_music = AudioFileClip('op9no2c.mp3')
        # 设置背景音乐的持续时间与最终视频相同
        background_music = background_music.set_duration(final_clip.duration)
        # 调整背景音乐的响度到 x%
        background_music = background_music.volumex(0.05)
        # background_music = background_music.volumex(0.1)

        # 声音太小
        # final_clip.audio = final_clip.audio.volumex(4)

        # 获取最终视频的音频并与背景音乐合成
        final_audio = CompositeAudioClip([final_clip.audio, background_music])
        final_clip = final_clip.set_audio(final_audio)

    final_clip.write_videofile(
        output_file,
        ffmpeg_params=[
            '-c:v', 'h264_nvenc',
            '-r', str(video.fps),
            '-threads', '0',  # 使用所有可用的线程
        ],
    )

    video.close()  # 关闭输入视频对象
    final_clip.close()  # 关闭最终视频对象
    
    gc.collect()
    time.sleep(1)


if __name__ == '__main__':

    pass
