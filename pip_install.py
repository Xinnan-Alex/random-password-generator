#*****************************************************#
#File Name: pip_install.py
#Version/Date:  FINAL (2020-06-02)
#Programmer/ID: Ooi Kher Ning 1191100876
#Project Name: Random Password Generator
#Teammates: Teh Su Anne, Chin Pei Wern, Leong Xin-Nan
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#*****************************************************#

#this module is needed to import into our main module for isntalling external module for our program

#module such as PIL,PYPNG,PYQRCODE and PYTHON-BARCODE

import sys
import subprocess
import pkg_resources

required = {'pillow', 'pypng','pyqrcode','python-barcode'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)