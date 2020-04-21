import sys
import wave
from pydub import AudioSegment


# cut wav
def getEachWav(main_wav_path, start_time, end_time, destination_wav_path_wav_path):
    start_time = int(start_time)
    end_time = int(end_time)
    sound = AudioSegment.from_wav(main_wav_path)
    word = sound[start_time:end_time]
    word.export(destination_wav_path_wav_path, format="wav")


if __name__ == '__main__':
    main_wav_path = sys.argv[1]
    start_time_min = sys.argv[2]
    end_time_min = sys.argv[3]
    destination_wav_path_wav_path = sys.argv[4]
    # second to min,because inputting is string
    start_time = int(start_time_min)*1000
    end_time = int(end_time_min)*1000
    getEachWav(main_wav_path, start_time, end_time, destination_wav_path_wav_path)

