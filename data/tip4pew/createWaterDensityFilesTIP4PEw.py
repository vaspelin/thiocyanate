from __future__ import division, print_function
import shutil
from io import StringIO
from math import pi
from scipy import integrate
from IPython.display import display, Math, Latex
import numpy as np
import mdtraj as md
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})
import os


cations = ['Na','K']

anions = ['SCN']

concs = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]

nW = [12384, 11347, 10491, 9760, 9214, 8674]



block_range  = np.arange(1,19,1)

print(len(block_range))

for cation in cations:
	print("loop 1")

	for anion in anions:
		print("loop 2")
		
		i=0
		
		for conc in concs:
			print("loop 3")
			wdir = cation.lower()+anion.lower()+'/'+str(conc)+'m/'

			for block in block_range:
				print("loop 4")				
				
				vol = np.loadtxt(wdir+'V_'+str(block))
				print(vol)
				
				rho_w = nW[i]/vol				
				print(rho_w)				
				
				f = open(wdir+'rho_w_'+str(block), 'w' )
				f.write( repr(rho_w) + '\n' )
				f.close()	
				
			i=i+1

