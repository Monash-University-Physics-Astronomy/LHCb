# Contributing

This page is a work in progress and we welcome contributions of all kinds:

- Useful tips for analyses;
- Problems/Fixes to existing documentation;
- Useful links.

## How to Contribute

There are 3 ways one can contribute to the page:

1. If you do not have a [GitHub](https://github.com) account, you can write an email. However,
    we will be able to respond more quickly if you use one of the other methods described below.

2. If you have a [GitHub](https://github.com) account, or are willing to [create one](https://github.com/join), but do not know how to use Git, you can report problems or suggest improvements by [creating an issue](https://github.com/Monash-University-Physics-Astronomy/LHCb/issues).

3. If you are comfortable with Git, and would like to add or change material, we use a [fork and pull](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project) model to manage changes. Instructions for doing this are [included below](#using-github).

## Using GitHub

If you choose to contribute via GitHub, the following link details how contribute to the documentation [How to Contribute to an Open Source Project on GitHub](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project). There is also a rough guide [below](#step-by-step-contribution-process). Once a contributor has succesfully completed a pull request, it is up to the maintainers to merge the changes into the documentation.

### Step-by-Step Contribution Process

1. **Fork the Repository**  
    Start by forking the repository to your own GitHub account. For each change you plan to make, create a new branch in your fork. This helps keep your changes organized and makes it easier to submit pull requests.

2. **Make Changes**  
    You can make changes directly on your new branch using GitHub's web interface, or you can clone your forked repository to your local machine for more control.

3. **Local Development (Optional)**  
    If you have cloned your fork, you can edit files locally.  
    - To preview documentation changes, you can build the documentation locally:
      - Create a Python virtual environment:
         ```bash
         python -m venv venv
         source venv/bin/activate
         ```
      - Install the required packages:
         ```bash
         pip install sphinx sphinx-rtd-theme myst-parser sphinx-autobuild
         ```
      - Create a separate folder (e.g., `build/`) outside your source repo for the build output.
      - Build the documentation:
         ```bash
         sphinx-build -b html LHCb/ build/
         ```
         Or use live development:
         ```bash
         sphinx-autobuild LHCb/ build/
         ```

4. **Commit and Push Changes**  
    After making and testing your changes, commit them to your branch and push to your fork on GitHub.

5. **Submit a Pull Request**  
    Open a pull request from your branch to the main repository. The maintainers will review your changes and, if appropriate, merge them.


