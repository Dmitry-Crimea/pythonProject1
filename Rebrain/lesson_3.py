hdd_base = [
    {'total': 999641890816, 'used': 228013805568},
    {'total': 61686008768, 'used': 52522710872},
    {'total': 149023482194, 'used': 83612310700},
    {'total': 498830397039, 'used': 459995976927},
    {'total': 93386008768, 'used': 65371350065},
    {'total': 988242468378, 'used': 892424683789},
    {'total': 49705846287, 'used': 9522710872},
]

user_input = int(input("Введите номер диска: "))
free_disk_spcae = hdd_base[user_input]['total'] - hdd_base[user_input]['used']
free_disk_spcae_percent = int(100 - ((hdd_base[user_input]['used'] * 100) / hdd_base[user_input]['total']))
if free_disk_spcae < 10737418240 or free_disk_spcae_percent < 5:
    print(f'на накопителе {user_input} критически мало свободного места')
elif free_disk_spcae < 32212254720 or free_disk_spcae_percent < 10:
    print(f'на накопителе {user_input} мало свободного места')
else:
    print(f'на накопителе {user_input} достаточно свободного места')
