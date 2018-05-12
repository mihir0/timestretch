import scipy.io.wavfile as w
import numpy as np
import sys

def stretch(arr, newsamples = 1): #newsamples MUST be an integer
    size = arr.size
    new_arr = np.zeros((size * (newsamples + 1), ), dtype = arr.dtype)
    for i in range(0, size - 1):
        new_arr[i * (newsamples + 1)] = arr[i]
        for s in range(1, newsamples + 1):
            m = (float(arr[i + 1]) - float(arr[i]))/float(newsamples)
            b = float(arr[i])
            sample = np.int16(m * s + b)
            new_arr[i * (newsamples + 1) + s] = sample #interpolation method here
    return new_arr

filename = sys.argv[1]
rate, original_arr = w.read(filename)
print rate, original_arr
new_arr = stretch(original_arr, newsamples = int(sys.argv[2]))
w.write("mod.wav", rate, new_arr)