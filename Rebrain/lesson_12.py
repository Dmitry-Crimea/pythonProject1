import os, psutil


class PCMemory:
    def __init__(self, pc_id, user_name, memory_total, memory_used, memory_percent=None):
        self.pc_id = pc_id  # id компьютера
        self.user_name = user_name  # имя пользователя
        self.memory_total = memory_total  # общий объем виртуальной памяти
        self.memory_used = memory_used  # используемый объем виртуальной памяти

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


memory_total = int(input('Введите общее кол-во памяти: '))
memory_used = int(input('Введите используемое кол-во памяти: '))

pc_info = PCMemory(os.getlogin(), os.getlogin(), memory_total,
                   memory_used)
