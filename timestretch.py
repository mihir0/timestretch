import scipy.io.wavfile as w
import numpy as np

def stretch(arr, newsamples = 1): #newsamples MUST be an integer
    size = arr.size
    #for i in range(0, size):
    #    arr = np.insert(arr, i * (newsamples + 1), 0)
        #print arr[i]
    #print "new size:", arr.size
    #return arr
    new_arr = np.zeros((size * (newsamples + 1), ), dtype = arr.dtype)
    for i in range(0, size - 1):
        new_arr[i * (newsamples + 1)] = arr[i]
        for s in range(1, newsamples + 1):
            m = (float(arr[i + 1]) - float(arr[i]))/float(newsamples)
            b = float(arr[i])
            #sample = np.int16((float(arr[i]) + float(arr[i + 1]))/2.0)
            sample = np.int16(m * s + b)
            new_arr[i * (newsamples + 1) + s] = sample #interpolation method here
    return new_arr

filename = 'sine_1.wav'
rate, original_arr = w.read(filename)
print original_arr.shape, original_arr.dtype
new_arr = stretch(original_arr, newsamples = 10)
w.write("mod.wav", rate, new_arr)