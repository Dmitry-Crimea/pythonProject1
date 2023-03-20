import psutil, os

user_cred = os.getlogin()
memory = psutil.virtual_memory()

test_dict = {'user_name': user_cred, 'memory_total': memory[0], 'memory_used': memory[3], 'memory_percent': memory[2]}