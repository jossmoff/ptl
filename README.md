# ptl

<a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.6-green.svg"></a>
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
**ptl**: Automatically log time in GitLab issue tracker for COMP23311 at UoM.

## Installation

```bash
# Clone the repo
joss@moff:~$: git clone https://github.com/JossMoff/ptl.git

# Change the working directory to PyRequisite
joss@moff:~$: cd ptl

# Install PyRequisite onto your system
joss@moff:~$: python3 setup.py install
```

> Sometimes the last step will require sudo as you might not has write access to /usr/local/lib/python3.6/dist-packages/

## Usage

```bash
joss@moff:~$ ptl --help
usage: ptl [-h] [-c] [-t TOKEN] [-p PROJECT_ID] [-i ISSUE_ID] [-s]

ptl: Automatically Log Time in issue tracking at UoM.

optional arguments:
  -h, --help            show this help message and exit
  -c, --config          Shows config of current ptl settings
  -t TOKEN, --token TOKEN
                        Sets private token for GitLab user
  -p PROJECT_ID, --projectid PROJECT_ID
                        Sets project id for a GitLab repository
  -i ISSUE_ID, --issueid ISSUE_ID
                        Sets issue id for an issue in a GitLab repository
  -s, --start           Start timing IDE open time.
```

In order to correctly use the tool you will need to set the TOKEN, PROJECT_ID and ISSUE_ID using: 

```bash
joss@moff:~$ ptl -t <token> -p <project_id> -i <issue_id>
```

Then open eclipse and run:

```bash
joss@moff:~$ ptl -s
```

Once eclipse has closed it will then write the time you've spent rounded up to the nearest hour in the selected issue tracker. 

## Getting Access Token
In order to gain a personal access token for to set with the -t/--token flag
![Personal Access Token](https://lh3.googleusercontent.com/LQs9VES1FwjJotwQnmPut4-4qNQPKZUIjIQnIeIvm8Itu-F4zQUMRRLkamIOrAJVDZaCU0ilhwAI)
## Further Improvements

How I plan to extend the quick project:

 - 🍎Provide switch ability to maintain multiple issues.
 - 🔒Add safety precautions to make sure you can connect to gitlab.
 - 💻Add extra terminal features
