# Code development

## Development environment
By far the easiest way to work on the remote `nectar` cluster is to install [Visual Studio Code](https://code.visualstudio.com/) on your laptop. It is available for Windows, Mac, Linux.

Once installed and started, go down to extensions and install [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh),  [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) 
Just search for the names in the extension tab as shown below, click on it and install.
  
![Remote - SSH extension in VS Code](images/remote-ssh.png)

> **Note:**  
> As always be careful when you install software. Check that all the etension above have the `microsoft.com` badge on them before you click install. For other extensions do your due diligence. Do they have millions of installations, is it a case of typo squatting, read the reviews!

After installing the extensions, you can now connect to the `nectar` cluster by clicking on the small set of arrows in the very bottom left of the window, then select `Connect to Host ...` and pick `nectar9` from the list. It should now open a new window where you now work on the remote `nectar9` machine. If `nectar9` is not in the list, something has been missed in the [section on obtaining an account](#obtain-an-account). The first time you connect, you might have to pick `linux` as the type for the remote.

![Remote - connect](images/connect-ssh.png) ![Connect to host](images/connect-to-host.png).

## Setup your coding area
For a given project, you only need to do everything below once.

LHCb has created an [Analysis Repository Skeleton](https://gitlab.cern.ch/lhcb-dpa/wp6-analysis-preservation-and-open-data/analysis-repo-skeleton) which provides a great place for you to start developing your code. When you eventually has to share your code with somebody else, then it becomes much easier if they see a familiar structure.
1. Follow the instructions to [set up the repository](https://gitlab.cern.ch/lhcb-dpa/wp6-analysis-preservation-and-open-data/analysis-repo-skeleton#to-set-up-the-repository)
2. [download a local copy](https://gitlab.cern.ch/lhcb-dpa/wp6-analysis-preservation-and-open-data/analysis-repo-skeleton#download-your-replica-project-locally). The commands in the last step should be executed in a terminal window on `nectar9`, see images. 
![New terminal](images/new-terminal.png)! 
![git clone in terminal](images/terminal-clone.png).
3. You can ignore the rest of the instructions on the [Analysis Repository Skeleton](https://gitlab.cern.ch/lhcb-dpa/wp6-analysis-preservation-and-open-data/analysis-repo-skeleton) page for now and come back to it later if required.
4. To setup the python environment for coding, in a terminal window set up a virtual environment that is based on the shared LHCb conda environment. See the commands below and make changes in the folder name if required. Take care of including the single quotation marks.
```bash
[nectar9] ~ % cd analysis-repo-skeleton
[nectar9] ~/analysis-repo-skeleton master  1% ./run lb-conda-dev virtual-env '$LBCONDA_DEFAULT_ENV_VERSION' lb-python
Environment created in /home/egede/analysis-repo-skeleton/lb-python
   Execute "/home/egede/analysis-repo-skeleton/lb-python/run" to launch a shell inside the environment
   Execute "/home/egede/analysis-repo-skeleton/lb-python/run my_command" to launch "my_command" inside the environment
[nectar9] ~/analysis-repo-skeleton master % lb-python/run printenv > .env
[nectar9] ~/analysis-repo-skeleton master % 
```
5. Now in the MVC window open the skeleton folder ![open folder](images/open-folder.png).
6. Type `ctrl-shift-p` and at the prompt type `Python: Select Interpreter` and then pick the line that has `lb-python` in it.

> **Note:**  
> If you do not yet have a computing account at CERN, you should just ignore step 1 above and in step 2, replace the `git clone` command with
> ```
> git clone https://gitlab.cern.ch/lhcb-dpa/wp6-analysis-preservation-and-open-data/analysis-repo-skeleton.git

## Edit and run a Jupyter notebook
To edit a Jupyter notebook, create a new file with the extension `.ipynb` in the `python` folder inside your skeleton project. To select the kernel, pick `Python environments` and then the `lb-python` option. You can try the following script. If it runs and produce a histogram, everything is good.
```python
import ROOT
import numpy as np

# Generate random numbers
data = np.random.normal(loc=0, scale=1, size=1000)

# Create a ROOT histogram
hist = ROOT.TH1F("hist", "Random Numbers Histogram", 50, -4, 4)

# Fill the histogram
for value in data:
    hist.Fill(value)

# Draw the histogram
canvas = ROOT.TCanvas("canvas", "Canvas", 800, 600)
hist.Draw()
canvas.Draw()
```
If you see red wiggly lines under the packages that you import, you might have done something wrong with setting up the environment or with selecting the kernel. If you when you run `import ROOT` see an error like `ERROR in cling::CIFactory::createCI()` you have also done something wrong in setting up the environment. You will need to fix this, even if things look like they work.

> **Note:**  
> You might get a timeout when starting the Jupyter kernel. This is because software is installed on demand from CERN and this can take a few minutes. Just click on run again (maybe a few times) and it should eventually work. For the same reason the `import ROOT` line might take several minutes the very first time you use it.

## GitHub Copilot
One of the nicer extensions to install on your [Visual Studio Code](https://code.visualstudio.com/) is the [GitHub Copilot](https://code.visualstudio.com/docs/copilot/overview) extension. This is an AI peer programming tool that can help you to write code faster, and assist in coding tasks such as generating plots.  Starting off you will be on the free plan, though through [GitHub Education](https://github.com/education) students and staff are able to get the Pro plan for **free**, which comes with helpfull [features](https://docs.github.com/en/get-started/learning-about-github/githubs-plans#github-pro). 

To start this process you must first install GitHub Copilot on your VSCode:

![Remote - SSH extension in VS Code](images/GitHub-Copilot.png)

To then access the Pro plan you will have to have a [GitHub](https://code.visualstudio.com/docs/copilot/overview) account which is linked to your Monash account, and proceed to the following [link](https://github.com/settings/education/benefits). From here you must press the 'Start an application' button and proceed as either a student or educator. You will have to provide evidence that you are in fact student or educator, and for students a picture of your transcript from [wes](https://my.monash.edu/wes/) will work. For staff, a picture from your letter of employment should work as well. There are other pieces of evidence you could also use as proof, but these are the ones that are known to work. If you are denied it will provide reason(s) it was denied and you are able to start another application again, this must be with a different image (you will have to screenshot your evidence again). Common reason(s) for being denied is simply not completing information GitHub requires and also not having two-factor authentication. The approval time takes ~1 minute, and once you are approved you should be able to see the following:

![Remote - SSH extension in VS Code](images/GitHub-Copilot-Approval.png)

Back on your VSCode, you should be able to see an icon for managing your Copilot usage in the bottom right hand corner:

![Remote - SSH extension in VS Code](images/GitHub-Copilot-VSCode.png)

This is where you can login, and once this is completed you should be able to see you are on the premium plan. To the right of the search bar, you should also be able to see the GitHub copilot icon. Here you can make a prompt to see an AI response. The AI is allowed to see your full directory structure and able to make folders/files. It can not make folders/files on the nectar machine. When on a python script or a jupyter notebook, another helpful tool is found by pressing `ctrl+i`. This will create a chat prompt which can alter the current document you are working on. You must either accept or cancel the changes.

## Connect to CERN
The setup of the `nectar9` cluster here in Australia and the `lxplus` cluster at CERN are in principle identical. In general you are better off using the `nectar9` cluster as you avoid the very long round-trip time for the connection to CERN (it is about 300ms while it is about 5ms for `nectar9`) that can make interactive work very painful. Nevertheless if you are reading data from the `/eos` filesystem at CERN it might be easier to do something on `lxplus`.

To connect by `ssh` to `lxplus.cern.ch` you can't use a public key as you need to type your password to obtain write access to your home directory. The best is to add something like the lines below to your `.ssh/config` file

```
# Ensure that you only need to type your password and 2FA once if you have parallel logins
Host lxplus
   HostName lxplus.cern.ch
   ControlPath /run/user/%i/%r@%h:%p
   ControlMaster auto

# Make sure that you can still use Gitlab at CERN with a key.
Host gitlab.cern.ch
   IdentityFile <CERN-Gitlab-key>
   StrictHostKeyChecking no
   PubkeyAuthentication yes
   GSSAPIAuthentication no
   GSSAPIDelegateCredentials no
   ForwardAgent no
   ForwardX11 no
   ForwardX11Trusted no

Host *.cern.ch
   User <user>
   PubkeyAuthentication no
   PasswordAuthentication yes
   GSSAPIAuthentication no
   GSSAPIDelegateCredentials no
   CheckHostIP no
   ControlPersist 1m
```
where you should substitute in your CERN username instead of `<user>` and `<CERN-Gitlab-key>` with the ssh public key you have uploaded to the CERN Gitlab instance. The lines above can dramatically reduce the number of times you need to type your password and 2FA codes.

If you want to use Visual Studio Code for code development on `lxplus` then read the [specific instructions](https://cern.service-now.com/service-portal?id=kb_article&n=KB0008901)