import time
import matplotlib.pyplot as plt


def save(silence_intervals, voice_intervals):

    plt.figure(figsize=(16, 5), dpi=200)

    for start, end in silence_intervals:
        plt.barh(0.2, end - start, left=start, height=0.6, color='red')

    for start, end in voice_intervals:
        plt.barh(-0.2, end - start, left=start, height=0.6, color='royalblue')

    plt.xlim(0, max(silence_intervals[-1][-1], voice_intervals[-1][-1]))
    plt.ylim(-0.5, 0.5)

    plt.axis('off')  # 隐藏坐标轴
    plt.tight_layout()  # 去除白边

    # plt.show()
    plt.savefig(f'log/{time.strftime("%Y_%m_%d_%H%M%S")}.png', dpi=200)
    plt.close()


if __name__ == '__main__':

    pass
