import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
seconds = 4

myrec = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()
import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
seconds = 4

myrec = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()
write('The-Bad-Guys//Oh-spy.wav', fs, myrec)