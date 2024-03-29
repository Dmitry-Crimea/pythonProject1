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
#2.
list_dict = []
for values in log_lst:
    log_str = values.split()
    log_dict = {'time':' '.join(log_str[:3]), 'pc_name':' '.join(log_str[3:4]), 'service_name':' '.join(log_str[4:5]), 'message':' '.join(log_str[5:])}
    list_dict.append(log_dict)
#3.
print([dict_value['time'] for dict_value in list_dict])

#4.
for dict_str in list_dict:
    dict_str['date'] = dict_str['time'][:6]
    dict_str['time'] = dict_str['time'][6:]
    print(dict_str['time'])

#5.
print([dict_value['message'] for dict_value in list_dict if dict_value['pc_name'] == 'PC0078'])

#6,7
super_new_dict = {key:value for key in range(100, 110) for value in list_dict}
print(super_new_dict[104])