# -*- coding: utf-8 -*-
"""
Input file 'tuning_3.4.pickle' contains the recorded firing rates (in Hz) for 
each of four neurons. These are named neuron1, neuron2, neuron3, and neuron4.
The stimulus is in the vector named stim.

Each column of a neuron matrix contains the firing rate of that neuron (in Hz) 
in response to the corresponding stimulus value in stim.
That is, nth column of neuron1 contains the 100 trials in which we applied the 
stimulus of value stim(n) to neuron1.

@author: Estelle Baudry
"""

import pickle
import numpy as np
import matplotlib.pyplot as plt
import sys


#INPUT DATA DESERIALISATION
with open('tuning_3.4.pickle', 'rb') as f:
    data = pickle.load(f)
    

#DATA DISCOVERY
print("Type of input data: ", type(data))
print("Type of stim from data: ", type(data['stim']))

print("stim dimension: ", data['stim'].ndim)
print("stim dimension size: ", data['stim'].shape)
print("stim total size :", data['stim'].size)

print("neuron1 dimension: ", data['neuron1'].ndim)
print("neuron1 dimension size: ", data['neuron1'].shape)
print("neuron1 total size :", data['neuron1'].size)

#print("stim:\n", data['stim'])
#print("neuron1:\n", data['neuron1'])
#print("neuron2:\n", data['neuron2'])
#print("neuron3:\n", data['neuron3'])
#print("neuron4:\n", data['neuron4'])
    

#PLOT OF THE TUNING CURVE (mean firing rate as a function of the stim)
stim = data['stim']
neuron1MFR = data['neuron1'].mean(axis=0)
neuron2MFR = data['neuron2'].mean(axis=0)
neuron3MFR = data['neuron3'].mean(axis=0)
neuron4MFR = data['neuron4'].mean(axis=0)

plt.plot(stim, neuron1MFR, 'r', label="neuron1")
plt.plot(stim, neuron2MFR, 'b', label="neuron2")
plt.plot(stim, neuron3MFR, 'g', label="neuron3")
plt.plot(stim, neuron4MFR, 'black', label="neuron4")

plt.xlabel('Stimuli')
plt.ylabel('Mean f/r (Hz)')
plt.title('Tuning curve')
plt.legend()

plt.show()
print("Result is a Half wave rectified sine functions.\n")


#EVALUATION OF THE "POISSON-NESS" OF EACH NEURON
"""
A Poisson process is characterised by the fanor-factor = 1.
We will look at the evolution of the fano-factor defined as E(X)/var(X),
with E being the expected value and var the variance.
"""
neuron1var = np.var(data['neuron1'], axis=0)
neuron2var = np.var(data['neuron2'], axis=0)
neuron3var = np.var(data['neuron3'], axis=0)
neuron4var = np.var(data['neuron4'], axis=0)

#Removing warnings for output readability.
#Warnings to be managed if nxfanoFactor used somewhere else, in function, thread ...
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
    
n1fanoFactor = (neuron1MFR/neuron1var)/10
n2fanoFactor = (neuron2MFR/neuron2var)/10
n3fanoFactor = (neuron3MFR/neuron3var)/10
n4fanoFactor = (neuron4MFR/neuron4var)/10
#(We need to divide the fano-Factor by 10 because we work with f/r and not 
#spike count, recorded on a 10 seconds basis.)

plt.plot(stim, n1fanoFactor, 'r', label="n1FF")
plt.plot(stim, n2fanoFactor, 'b', label="n2FF")
plt.plot(stim, n3fanoFactor, 'g', label="n3FF")
plt.plot(stim, n4fanoFactor, 'black', label="n4FF")

plt.xlabel("Stimuli")
plt.ylabel("Neurons fanor-factor")
plt.title("Neurons fano-factor evolution")
plt.legend()

plt.show()
print("Clearly neuron3 is not Poisson.\n")
#(When f/r = 0, I chose not to show the fano-factor instead of displaying 0, 
#which could be interpreted as fanor-factor instability if one overlooks.)