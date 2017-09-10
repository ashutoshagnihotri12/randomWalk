# Plotting file
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

f = open('output_file.dat','r')
data = f.read()
print(type(data))

fig1 = plt.figure()

