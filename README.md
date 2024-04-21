# AutoDock-GPU-Pipeline

## Installing AutoDock-GPU

1. To install AutoGrid, follow the same steps as described [here](https://github.com/gautam2002m/AutoDockPipeline). For faster docking on systems with GPUs, install AutoDock-GPU. 
2. To compile AutoDock-GPU, simply navigate to this [GitHub page](https://github.com/ccsb-scripps/AutoDock-GPU) and follow the provided instructions.
3. Make sure to download the MGLtools tar file compatible with your system, which is essential for running both AutoDock GUI (ADT) and AutoDock4. It is available on their [website](https://ccsb.scripps.edu/mgltools/).


Incase you face any problem compiling the software, you can use the following steps:

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
   
   ```markdown
   python3 targeted_site.py <protein_name> <ligand_name_as_mentioned_in_pdb_file> <CHAIN_ID_for_ligand>
   ```

   For example:
   <br>
   `python3 targeted_site.py 7k15.pdb VRJ A`

   This will give 7k15_site.pdb as output.

   
6. Get the Centroid of the extracted binding site:
   
   ```markdown
   python3 Centroid.py <bind_site>
   ```

   
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

```markdown 
python3 gpu_hts.py <prot_name> <x,y,z> <nrun>
```

Here <prot_name> is the protein PDB file, <x,y,z> are the coordinated and 'nrun' are the number of LGA runs. 

This initiates the docking process for the ligands located in the current working directory (cwd) with the specified protein.

If you want to run single protein-ligand docking:

```markdown 
python2 gpu_filecr.py <prot_name> <ligand_name> <x,y,z> <nrun>
```

For example:
<br>
`python2 gpu_filecr.py 7k15.pdb VRJ.pdb 1.9392312138728325,-8.92228901734104,18.28384393063584 10`

This will generate a new directory named '7k15a_VRJ'. Within this directory, you'll find all the input and output files produced during the docking.

## Ligand Screening

### Binding Energy Filteration

1. After the docking is done, we need to have the binding energy values of the docked ligand. To get the binding energy:

```markdown 
python3 binding_energy.py
```

This script will analyze the '.dlg' file for each ligand, providing the binding energy of the cluster with the highest number of conformations, along with the number of conformations in that cluster. You'll get a file named 'Energy.txt' with all the complex name and the binding energy values.

2. We're now prepared to transfer all ligands along with their corresponding docking directories into a new directory to facilitate further analysis. To accomplish this, follow these steps:

``` markdown
python3 full_dir.py
```

This will relocate the dlg files of the ligands listed in the 'Energy.txt' file. Hence, you can transfer the dlg files corresponding to the specified binding energies using the 'binding_energy.py' script followed by 'full_dir.py'.

### Filtering based on protein-ligand interactions

If you know certain important ligand-residue interactions, such as hydrogen bonding, you can check if ligands exhibit these interactions in the docked pose to filter them.

1. Generate a new PDB file with the ligand docked into the protein in the optimal docking pose as determined by the algorithm.
   
``` markdown
python3 test_outname.py 
```
This will generate complexes (protname_ligandname.pdb) for all the files that have been docked.

2. Make a new directory named 'Complex' and move all the complex PDB file there.
3. Now to check the interactions use 'PLIP'. You can download it from [here](https://github.com/pharmai/plip)
4. To check the interaction with PLIP:
``` markdown
plip -f *.pdb -t -y
```
This creates a new directory called 'protein_ligand' containing a PyMOL session file and a text file named 'report.txt' detailing all interactions.

Now, you can script in Python to identify ligands with significant interactions with protein residues. Should you encounter any difficulties with scripting, feel free to reach out to me.

## Conclusion

If you have any questions, feedback, or suggestions for improvement, please don't hesitate to reach out or open an issue. I welcome contributions from the community to enhance and expand this project. Happy docking!




   








 
