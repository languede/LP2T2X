# ECO system project repository (by LP2T2X)

## The concept
Eco Rewards is a reward system focusing on increasing consumers’ awareness of environment protection during their daily activities. The system aims at helping people to make more eco-friendly purchases.

## Target audience
Consumers who want to contribute their efforts on protecting environment.   
Consumers who are lacking awareness of environment protection

## Overview
![image](/product%20flow.png)
https://drive.google.com/file/d/1RXOT-DT5sB8NG5My6jmeXHQK9m78LEOr/view?usp=sharing

## The Wiki
https://outline.touryx.com:9443/s/49999f0e-d491-4c2e-b02c-9cb3ae08aa84

## Install
#### I am using anaconda to manage all the packages, it is strongly recommand to install Miniconda/Anaconda on your local system before you depoly this Django project.
#### About installing Anaconda please refer to their official documents: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

### Step-by-step guide
*If using pythin env, refer to the package list in environment.yml, then use `pip install [package name]`*

1. Clone this repo by run 
```git clone https://github.com/languede/LP2T2X.git```
3. Go to the project directory 
```LP2T2X/ECO/```
4. In case you have anaconda installed, create virtual environment from the environment.yml file, run ```conda env create -f environment.yml```
5. Find and Edit **setting.py** under the path 'LP2T2X/ECO/eco/'
6. Edit the list variable **ALLOWED_HOSTS** by append/adding for example `localhost` or anyother ip you want.
7. Back to the project root directory which contain the **manage.py** file
8. In the terminal, type `python manage.py runserver` to run Django project


p.s. If there were missing pacakages, try `pip install <missing pacakage>` to fix this error

p.s. use `python manage.py runserver 0.0.0.0:8080` to make the web server listen on 0.0.0.0 and port 8080

## Note:
**For MacOS user:**  

*Since `zsh` does not support  `django-phonenumber-field[phonenumberslite]`*
Please type `bash` in mac's terminal to switch default shall to `bash`,  
That is:   
run `bash` in terminal // switch to bash shell  
refer to environment.yml in LP2T2X/ECO/ to see the packages list
```
pip3 install django-phonenumber-field
pip3 install django-simple-history
pip3 install pyzbar opencv-python
pip3 install pillow
```
direct to manage.py , type: `python3 manage.py runserver <host_address:port_number>`

## To run this Django project, you need to install following pacakages
### please refer to the *environment.yml* file to see full pacakages used in this project

#### Pillow
`pip install pillow`

#### django-phonenumber-field
`pip install django-phonenumber-field[phonenumberslite]`

#### django-simple-history
`pip install django-simple-history`

#### pyzbar and opencv-python
`pip install pyzbar opencv-python`

#### install stripes for payment
`pip install stripe3`
