import urllib.request
import wave
import struct
filename = "white_noise.wav"

a = 1 
fs = 8000
f0 = 440
sec = 3

samples = fs * sec
nums = ""

while samples > 0:
    with urllib.request.urlopen("https://www.random.org/integers/?num=10000&min=-32768&max=32767&col=1&base=10&format=plain&rnd=new") as res:
       html = res.read().decode("utf-8")
       nums += html + ' '
    samples -= 10000

swav = [int(i) for i in nums.split()]

binwave = struct.pack("h" * len(swav), *swav)
w = wave.Wave_write("output.wav")
p = (1, 2, 8000, len(binwave), 'NONE', 'not compressed')
w.setparams(p)
print('done')
w.writeframes(binwave)
w.close()
