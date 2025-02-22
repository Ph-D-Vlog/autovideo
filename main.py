import voice_finder
import video_renderer

import gc
gc.enable()


if __name__ == '__main__':

    input_video = '1.mp4'
    output_video = '上传.mp4'

    voice_intervals = voice_finder.find_voice(input_video)
    video_renderer.render_video(input_video, output_video, voice_intervals, bgm_flag=True)
