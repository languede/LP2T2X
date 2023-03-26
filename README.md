# ECO system project repository (by LP2T2X)

## The concept
Eco Rewards is a reward system focusing on increasing consumers’ awareness of environment protection during their daily activities. The system aims at helping people to make more eco-friendly purchases.

## Target audience
Consumers who want to contribute their efforts on protecting environment.   
Consumers who are lacking awareness of environment protection

## Overview
![image](/product%20flow.png)
https://drive.google.com/file/d/1RXOT-DT5sB8NG5My6jmeXHQK9m78LEOr/view?usp=sharing

## Usage
1. Create a virtual environment through Anaconda or Python venv
2. Find setting.py under the path 'eco/eco/'
3. Edit the list variable ALLOWED_HOSTS by append/adding 'localhost' or anyother ip you want.
4. Back to the root directory which contain the manage.py file
5. In the terminal, type `python manage.py runserver` to run Django project


p.s. If there were missing pacakages, try `pip install <missing pacakage>` to fix this error

## Note for the team:
**For MacOS user:**  
Please type `exec bash` in mac's terminal to switch default shall to `bash`,  
That is:   
         1.  ~ > `exec bash`  // switch to bash shell  
         2.  bash >   // we are now using bash as our default shell   
         3.  bash > `pip3 install django-phonenumber-field[phonenumberslite]`   
         4.  bash > `pip3 install django-simple-history`  
         5.  bash > `pip3 install pyzbar opencv-python` 
         6.  bash > `pip3 install pillow`  
         7.  bash > `exec zsh` // back to zsh shell    
         8. to run the code:   
                  direct to manage.py , type: python3 manage.py runserver  

*Because `zsh` does not support  `django-phonenumber-field[phonenumberslite]`*


## To run this Django project, you need to install following pacakages

### Pillow
pip install pillow  

### django-phonenumber-field
pip install django-phonenumber-field[phonenumberslite]

### django-simple-history
pip install django-simple-history

### pyzbar and opencv-python
pip install pyzbar opencv-python

### install stripes for payment
pip install stripe3
