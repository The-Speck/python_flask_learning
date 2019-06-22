#### Notes
1 - powershell doesn't jive with activating another env

#### 1. Check conda is installed and in your PATH
Open a terminal client.
Enter conda -V into the terminal command line and press enter.
If conda is installed you should see somehting like the following.

$ conda -V
$ conda 3.7.0

#### 2. Check conda is up to date
In the terminal client enter
$ conda update conda
Upadate any packages if necessary by typing y to proceed.

#### 3. Create a virtual environment for your project
In the terminal client enter the following where yourenvname is the name you want to call your environment, and replace x.x with the Python version you wish to use. (To see a list of available python versions first, type conda search "^python$" and press enter.) 
$ conda create -n yourenvname python=x.x [addpakages Ex. anaconda]
Press y to proceed. This will install the Python version and all the associated anaconda packaged libraries at “path_to_your_anaconda_location/anaconda/envs/yourenvname”

#### 4. Activate your virtual environment.
To activate or switch into your virtual environment, simply type the following where yourenvname is the name you gave to your environement at creation.
$ activate yourenvname
Activating a conda environment modifies the PATH and shell variables to point to the specific isolated Python set-up you created. The command prompt will change to indicate which conda environemnt you are currently in by prepending (yourenvname). To see a list of all your environments, use the command conda info -e.

#### 5. Install additional Python packages to a virtual environment.
To install additional packages only to your virtual environment, enter the following command where yourenvname is the name of your environemnt, and [package] is the name of the package you wish to install. Failure to specify “-n yourenvname” will install the package to the root Python installation. 
$ conda install -n yourenvname [package]

#### 6. Deactivate your virtual environment.
To end a session in the current environment, enter the following. There is no need to specify the envname - which ever is currently active will be deactivated, and the PATH and shell variables will be returned to normal.
$ deactivate

#### 7. Delete a no longer needed virtual environment
To delete a conda environment, enter the following, where yourenvname is the name of the environment you wish to delete.
$ conda env remove -n yourenvname -all

#### 8. List of conda env
$ conda env list

#### 9. Export libraries
Export libraries to a text file named requirements.txt
$ conda list --export > requirements.txt

#### 10. Install from requirements.txt
$ conda install --yes --file requirements.txt

Note: flask-restful must be install using:
$ conda install -c conda-forge flask-restful
