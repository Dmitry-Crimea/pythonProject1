import os, psutil


class PCMemory:
    def __init__(self, pc_id, user_name, memory_total, memory_used, memory_percent=None):
        self.pc_id = pc_id
        self.user_name = user_name
        self.memory_total = memory_total
        self.memory_used = memory_used

        if memory_percent is not None:
            self.memory_percent = memory_percent
        else:
            self.memory_percent = round((self.memory_used / self.memory_total) * 100, 2)

    def show_used_percent(self):
        return f'PC with id {self.pc_id} used {self.memory_percent}% percent of memory'

    def is_enough_memory(self):
        free_memory_percent = 100 - self.memory_percent
        free_memory_gb = (self.memory_total - self.memory_used)

        if free_memory_percent >= 10 or free_memory_gb >= 1:
            return True
        else:
            return False


pc_info = PCMemory(os.getlogin(), os.getlogin(), psutil.virtual_memory().total,
                   psutil.virtual_memory().used, psutil.virtual_memory().percent)

print(pc_info.show_used_percent())
print(pc_info.is_enough_memory())

psutil.