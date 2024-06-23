import urllib.request
from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine

# Download an audio file
try:
    urllib.request.urlretrieve("https://tinyurl.com/wx9amev", "metallic-drums.wav")
    urllib.request.urlretrieve("https://tinyurl.com/yx3k5kw5", "beat.wav")
except Exception as e:
    print(f"Error downloading audio files: {e}")

loop = AudioSegment.from_wav("metallic-drums.wav")
beat = AudioSegment.from_wav("beat.wav")

play(loop)

loop2 = loop * 2
fade_time = int(len(loop2) * 0.5)
faded = loop2.fade_in(fade_time).fade_out(fade_time)
play(faded)

mixed = beat[:len(loop2)].overlay(loop2)
play(mixed)

filtered = beat.low_pass_filter(3000)
play(filtered)

loop_panned = loop2.reverse().pan(-0.5).overlay(loop2.pan(0.5))
play(loop_panned)

final = filtered.overlay(loop2 - 3, loop=True)
final.export("final.mp3", format="mp3")

result = AudioSegment.silent(duration=0)
for n in range(15):
    freq = 200 * n
    sine = Sine(freq).to_audio_segment(duration=200).apply_gain(-3).fade_in(50).fade_out(100)
    result += sine

play(result)
