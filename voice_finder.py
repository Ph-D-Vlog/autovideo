import vis
import numpy as np
from tqdm import tqdm
from moviepy.editor import VideoFileClip


def merge_intervals(intervals, duration_threshold):  # leetcode 56

    merged = [intervals[0]]

    for interval in intervals[1:]:
        if np.abs(interval[0] - merged[-1][1]) <= duration_threshold + 1e-4:  # 去掉太小的段，排除浮点误差
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
        else:
            merged.append(interval)

    return merged


def find_voice(input_video, duration_threshold=0.1):  # 每 0.1s 截断一次

    video = VideoFileClip(input_video)
    audio = video.audio  # 获取视频的音频

    # 计算动态阈值
    mean_list = []
    for i, chunk in tqdm(enumerate(audio.iter_chunks(chunk_duration=duration_threshold)), desc='mean_list', ncols=100):
        mean_list.append(np.abs(chunk).mean())
        max_index = i

    silence_threshold = np.percentile(mean_list, 10)  # 最后10% 作为阈值，自然一些

    # 查找静音部分
    voice_intervals = []
    silence_intervals = []
    for i, mean in tqdm(enumerate(mean_list), desc='mean_list', ncols=100):

        if i == max_index: break  # 最后一个不要

        start = i * duration_threshold
        end = start + duration_threshold

        if mean > silence_threshold:  # 比 最后x% 大
            voice_intervals.append((start, end))
        else:
            silence_intervals.append((start, end))

    voice_intervals = merge_intervals(voice_intervals, duration_threshold)
    silence_intervals = merge_intervals(silence_intervals, duration_threshold)

    print('len(voice_intervals) =', len(voice_intervals))
    print('len(silence_intervals) =', len(silence_intervals))
    print()

    vis.save(silence_intervals, voice_intervals)

    return voice_intervals


if __name__ == '__main__':

    pass
