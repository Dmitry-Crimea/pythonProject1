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


class PCAdvanced(PCMemory):
    def __init__(self, pc_id, user_name, memory_total, memory_used, ld_avg_1m,
                 ld_avg_15m, memory_percent=None, ):
        super().__init__(pc_id, user_name, memory_total, memory_used, memory_percent)
        self.ld_avg_1m = ld_avg_1m
        self.ld_avg_15m = ld_avg_15m

    def show_load_average(self):
        return f'PC with id {self.pc_id} has load average (1m): {self.ld_avg_1m}, load average (15m): {self.ld_avg_15m}'

    def is_overloaded(self):
        if self.ld_avg_1m is not None and self.ld_avg_15m is not None:
            return self.ld_avg_1m >= 3 * self.ld_avg_15m
        else:
            return False

    def __call__(self, argument='memory'):
        if argument == 'memory':
            return self.is_enough_memory()
        elif argument == 'load':
            return self.is_overloaded()
        else:
            return None


pc_advanced_info = PCAdvanced(os.getlogin(), os.getlogin(), psutil.virtual_memory().total,
                              psutil.virtual_memory().used, psutil.getloadavg()[0], psutil.getloadavg()[2], psutil.virtual_memory().percent)

load_memory = pc_advanced_info()

print(pc_advanced_info.is_overloaded())  # 1

print(f' Состояние памяти {load_memory}')  # 2
