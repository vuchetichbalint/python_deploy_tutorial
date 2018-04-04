[![py2 status](https://img.shields.io/badge/python2-supported-green.svg)]()
[![py3 status](https://img.shields.io/badge/python3-supported-green.svg)]()  

# python_deploy_tutorial
This repo is for educational purposes.

## Homework

This tutorial is for unix users, its course can be also done with Windows OS, however I don't know exactly how - googling for `unix command + windows` will always help! ;)

### 1.) Install a python interpreter!
I recommend [Anaconda](https://www.anaconda.com/download/) for starters.

### 2.) Install a git-based VCS!
If you haven't got any already.

### 3.) Clone this repo!
```shell
git clone git@github.com:vuchetichbalint/python_deploy_tutorial.git
```

### 4.) Create a virual environment!
```shell
virtualenv -p python3 venv
```
-p python3 = python executable  
venv = destination directory name

### 5.) Activate the virtualenv!
```shell
source venv/bin/activate
```

### 6.) Check which python packages have been installed.
```shell
pip freeze
```
Here you should see nothing.

### 7.) Try to run `tryout.py` script.
```shell
python tryout.py
```

### 8.) Install `requirements.txt`!
Check its content:
```shell
cat requirements.txt
```
Install with:
```shell
pip install -r requirements.txt
```
This could last for a few minutes.
### 9.) Check which python packages have been installed.
```shell
pip freeze
```
You should see some packages here with their version (which is identical with the requirements.txt).

### 10.) Try to run `tryout.py` script.
```shell
python tryout.py
```
You should get a nice message.



