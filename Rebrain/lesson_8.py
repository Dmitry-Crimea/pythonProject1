# python3 -m venv venv
#
# source venv/bin/activate
#
# pip3 install psutil
#
# pip3 freeze > requirements.txt

########## lib_info.py ###########

import psutil, os

user_cred = os.getlogin()
memory = psutil.virtual_memory()

test_dict = {'user_name': user_cred, 'memory_total': memory[0], 'memory_used': memory[3], 'memory_percent': memory[2]}

#############################
from lib_info import lib_info

print(test_dict)
