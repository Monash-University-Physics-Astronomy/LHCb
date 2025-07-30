# Remote code development tips

## Useful ssh configuration options

This section suggests some useful configuration options to consider placing in you `~/.ssh/config` file.

### X11 forwarding

It is possible to open graphical applications, e.g. an image/pdf viewer, on a remote server and have it displayed on your local screen.
To do this, you must ensure X11 forwarding is enabled on your ssh connection either by using the `-X` option:
```
ssh -X <username>@<remote_host>
```
Or by enabling it for all connections in your `.ssh/config` file:
```
Host *
   ForwardX11 yes
```


## Accessing and installing software

This is generally dependent on the specific remote server you are working on.

In many cases, including the nectar and lxplus machines, most of the software required for LHCb data analysis purposes is available through CVMFS.

There are two main ways to configure your environment to use CVMFS software.

### LbConda

LHCb provides wrapper scripts for accessing predefined conda environments installed in CVMFS. 
Run the LbEnv setup script:
```
source /cvmfs/lhcb.cern.ch/lib/LbEnv
```
and then use the `lb-conda` command to run programs within a specified LbConda environment. 
For example:
```
lb-conda default python
```
will launch python inside the `default` LbConda environment, which is usually the most recent release.
A specific release can be obtained by replacing `default` with `default/<version>`.

See [here](https://gitlab.cern.ch/lhcb-core/lbcondawrappers/-/blob/master/README.md) for more information, including how to use the `lb-conda-dev virtual-env` command to allow installing additional python packages on top of the base environment.


### LCGView

Choose a `platform` and `release` and then run the corresponding environment setup script:
```
source /cvmfs/sft.cern.ch/lcg/views/<release>/<platform>/setup.sh
```
A list of available platforms/releases can be found [at this link](https://lcginfo.cern.ch/).

To give a specific example,
```
source /cvmfs/sft.cern.ch/lcg/views/setupViews.sh LCG_105 x86_64-el9-gcc13-opt
```

The upside of LCGViews is that they fully configure your current environemnt, so you don't need to run any additional commands like `lb-conda` at runtime.
It is also easy if you need to install additional software on top of the base environment.
You can, for example, create an ordianry python virtual environment after setting up the LCGView,
```
python3 -m venv <my_env>
```
and use `pip install` to install whatever additional python packages you might need.


## Running jupyter notebooks on a remote server

#### From the command line

You can run a jupyter notebook on the remote server and have it displayed in your local browser.

To do this, use ssh with local port forwarding:
```
ssh -L 8000:localhost:8888 <username>@<remote_host>
```
and then specifcy the same port to run the jupyter notebook on the remote server:
```
jupyter notebook --no-browser --port=8888
```
Copy the link provided into your local browser and you should see the jupyter server running.


#### In VSCode

Jupyter notebooks can be run inside VSCode. All you have to do is select a kernel (usually near the top-right of the VSCode window).

More info can be found [here](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).

To use a custom environment, one may create python virtual environment or a conda environment with any required software and then simply select the python interpreter from that environemnt for the kernel.

However, this method seems to fail if the notebook needs to use software such as ROOT from CVMFS pre-defined environments. A solution for this is explained below.



### Jupyter notebooks that use ROOT

The command line method for running jupyter notebooks in a local browser should work with minimal modifications as long as you have ROOT installed and your environment is configured correctly.

E.g. on nectar9, ROOT is available via CVMFS. 
If using LbConda, you first need to setup your environment using the LbEnv setup script:
```
source /cvmfs/lhcb.cern.ch/lib/LbEnv
```
Note: this is probably already done by default in your `~/.bashrc` configuration file.
Then you need to run the notebook as follows:
```
lb-conda default jupyter notebook --no-browser --port=8888
```
to ensure that it runs inside the LbConda environment.

If using an LCGView, you likewise need to setup the environment with the corresponding setup script. For example:
```
source /cvmfs/sft.cern.ch/lcg/views/setupViews.sh LCG_105 x86_64-el9-gcc13-opt
```
In this case, the standard jupyter notebook command should work:
```
jupyter notebook --no-browser --port=8888
```

For running the notebook in VSCode, the most reliable method is in fact to start the jupyter server from the command line as above (modulo the port forwarding options).
Once the server has started, copy the given URL.
However, instead of pasting the URL into a web browser, paste it into the VSCode kernel selector.
To do this, follow the same instructions as described earlier for the selecting a Jupyter kernel in VSCode, but instead of directly choosing an environment/interpreter, select "Existing Jupyter Server..." and paste the URL.
