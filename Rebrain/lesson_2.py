
#1.
log_lst = [
    "May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated",
    "May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.",
    "May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...",
    "May 20 11:01:12 PC-00102 PackageKit: daemon start",
    "May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...",
    "May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00",
    "May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: \"/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4\"",
    "May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device",
    "May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio",
    "May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.",
    "May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users."
]

#2.1
log_dict = {'time':' '.join(log_str[:3]), 'pc_name':' '.join(log_str[3:4]), 'service_name':' '.join(log_str[4:5]), 'message':' '.join(log_str[5:])}

#2.2.
user_input = int(input("Введите номер строки: "))
log_str = log_lst[user_input].split()
log_dict = {'time':' '.join(log_str[:3]), 'pc_name':' '.join(log_str[3:4]), 'service_name':' '.join(log_str[4:5]), 'message':' '.join(log_str[5:])}
print(log_dict['pc_name'] + ':' + log_dict['message'])


# 3.1. Скопируйте к себе литерал списка:
# ['May 26 12:48:18', 'ideapad', 'systemd[1]', 'Finished Message of the Day.']
# 3.2. Создайте список ключей из пункта 2.1
# 3.3. Используя функцию zip(), создайте словарь из этих двух списков
log_key = ['time', 'pc_name', 'service_name', 'message']
log_values = ['May 26 12:48:18', 'ideapad', 'systemd[1]', 'Finished Message of the Day.']
log_dict_2 = dict(zip(log_key,log_values))
print(log_dict_2)

# 4.
log_dict_3 = []
log_dict_3.append(log_dict)
log_dict_3.append(log_dict_2)
print(log_dict_3)

# 5.
set_1 = set(log_dict.values())
set_2 = set(log_dict_2.values())
print(set_1 ^ set_2)

