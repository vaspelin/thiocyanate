[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/vaspelin/thiocyanate/master?filepath=project_updated.ipynb)

# A forcefield parametrization of NaSCN and KSCN 

Ionic parameters appearing in the Lennard-Jones potential are optimized to reproduce thermodynamic properties obtained from experiments.

## Running the Jupyter notebook performing the analysis (files provided)
To run the notebook, follow the following instructions:


1. Install miniconda3 or anaconda3 on your computer.
2. Download the repository by downloading it directly, or by typing the following in a terminal:
```bash 
git clone https://github.com/vaspelin/thiocyanate/
```
3. When you are in the folder that you just downloaded, activate the environment contained in the file [`environment.yml`](/environment.yml) by typing the following in a terminal:
```bash 
conda env create -f environment.yml
source activate analysis
```
4. Open the Jupyter notebook `scn_si.ipynb` by typing the following in a terminal:
```bash
jupyter notebook scn_si.ipynb 
```
5. Reproduce the study by running the cells in the notebook.

## Running the Jupyter notebook performing simulations
To run this notebook, do steps 1-2 above if not already done. Then run the notebook `scn_si_sim.ipynb`. You may need to install some additional packages to run it properly.  


