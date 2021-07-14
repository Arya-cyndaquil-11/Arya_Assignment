from pygame import mixer
import os


def music_player():
    folder_path = os.getcwd() + "\\MashUp"      # you can use your own music path instead of it
    musics = list(filter(lambda x: x.endswith('.mp3'), os.listdir(folder_path)))
    i = 0
    mixer.init()
    mixer.music.load(folder_path+"\\" + musics[i])
    mixer.music.play()
    print("Press -> S: STOP    P: Pause    R: Resume    N: Next    F: Previous")
    while True:
        op = input().upper()
        if op == 'S':
            mixer.music.stop()
            break
        elif op == 'P':
            mixer.music.pause()
        elif op == 'R':
            mixer.music.play()
        elif op == 'N':
            mixer.music.stop()
            if i == len(musics) - 1:
                i = 0
            else:
                i += 1
            mixer.music.load(folder_path+"\\" + musics[i])
            mixer.music.play()
        elif op == 'F':
            mixer.music.stop()
            if i == 0:
                i = len(musics) - 1
            else:
                i -= 1
            mixer.music.load(folder_path+"\\" + musics[i])
            mixer.music.play()


if __name__ == '__main__':
    music_player()