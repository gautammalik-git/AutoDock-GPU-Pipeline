# AutoDock-GPU-Pipeline

This pipeline facilitates setting up ligand docking against a protein using AutoDock-GPU. It streamlines the process of docking a ligand library onto a protein structure, leveraging the enhanced performance of AutoDock-GPU for faster results.

## Installing AutoDock-GPU

1. To install AutoGrid, follow the same steps as described [here](https://github.com/gautam2002m/AutoDockPipeline). For faster docking on systems with GPUs, install AutoDock-GPU. 
2. To compile AutoDock-GPU, simply navigate to this [GitHub page](https://github.com/ccsb-scripps/AutoDock-GPU) and follow the provided instructions.
3. Make sure to download the MGLtools tar file compatible with your system, which is essential for running both AutoDock GUI (ADT) and AutoDock4. It is available on their [website](https://ccsb.scripps.edu/mgltools/).


Incase you face anyproblem compiling the software, you can use the following steps:

**Make sure you have OPENCL installed**

```markdown
 
wget https://github.com/ccsb-scripps/AutoDock-GPU/archive/refs/heads/develop.zip

unzip develop.zip

cd AutoDock-GPU-develop/

make DEVICE=GPU NUMWI=128

export GPU_INCLUDE_PATH=/usr/include

export GPU_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu

```
---

## Setting up AutoDock GPU

To ensure clarity, create a new directory and move the unzipped AutoDock, and MGLTools files there. Also move 'AutoDock-GPU-develop' folder into this directory. Follow these steps:

1. Create another directory named 'Repository':

```markdown

mkdir Repository
cp ./<autodock-directory>/autogrid ./Repository
cp ./AutoDock-GPU-develop/bin/autodock_gpu_128wi ./Repository
cp -r <mgltools-directory> ./Repository
cp ./<mgltools-directory>/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_*4.py ./Repository

```
Replace `<autodock-directory>` and `<mgltools-directory>` with the directories you extracted from the respective tar files.

## Pre-Docking Steps

Ensure Python2 and Python3 are installed on your system.

1. Create a directory containing all your ligand PDB files and your protein PDB file.
2. Add 'Repository' in your current working directory (cwd).
3. Copy all the Python scripts provided in this repository to your cwd.
4. Extract the binidng pocket out from the protein PDB file-
   
   `python3 targeted_site.py <protein_name> <ligand_name_as_mentioned_in_pdb_file> <CHAIN_ID_for_ligand>`

   For example:
   <br>
   `python3 targeted_site.py 7k15.pdb VRJ A`

   This will give 7k15_site.pdb as output.

   
5. Get the Centroid of the extracted binding site:
   
   `python3 Centroid.py <bind_site>`

   
   For example:
   <br>
   `python3 Centroid.py 7k15_site.pdb`

   This will print out the <x,y,z> coordinated.

 ## Docking

 1. Change path:

```markdown

export PATH=<PATH_TO_CWD>/Repository/mgltools_x86_64Linux2_1.5.6/bin:$PATH

export PYTHONPATH=<PATH_TO_CWD>/Repository/mgltools_x86_64Linux2_1.5.6/MGLToolsPckgs/:$PYTHONPATH

```
Replace <PATH_TO_CWD> with the path of your working directory. You can get it using command 'pwd' in your terminal.

3. Perform docking:

Make sure you are in the working directory with all the ligand PDB files, protein PDB file, 'Repository' and all the python scripts attached with this github repository.

`python3 gpu_hts.py <prot_name> <x,y,z> <nrun>`

Here <prot_name> is the protein PDB file, <x,y,z> are the coordinated and <nrun> are the number of LGA runs. 

This initiates the docking process for the ligands located in the current working directory (cwd) with the specified protein.

If you want to run single protein-ligand docking:

`python2 gpu_filecr.py <prot_name> <ligand_name> <x,y,z> <nrun>`

For example:
<br>
`python2 gpu_filecr.py 7k15.pdb VRJ.pdb 1.9392312138728325,-8.92228901734104,18.28384393063584 10`

This will generate a new directory named '7k15a_VRJ'. Within this directory, you'll find all the input and output files produced during the docking.


   








 
