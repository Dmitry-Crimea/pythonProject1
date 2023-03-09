# #1.
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

# #2*.
def log_print(user_data = [], *list_str):
    dict_lst = []
    for line in list_str:
        log_str = line.split()
        dict_str = {'time': ' '.join(log_str[:3]), 'pc_name': ' '.join(log_str[3:4]),
                'service_name': ' '.join(log_str[4:5:2]), 'message': ' '.join(log_str[5:])}
        user_dict.append(dict_str)
    print(user_dict)

dict_log = []
log_print(dict_log, "May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated",
          "May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.",
          "May 20 11:01:12 PC-00102 PackageKit: daemon start")

#3-4*.
# resource_dict = [
#     {'id': 382, 'total': 999641890816, 'used': 228013805568},
#     {'id': 385, 'total': 61686008768, 'used': 52522710872},
#     {'id': 398, 'total': 149023482194, 'used': 83612310700},
#     {'id': 400, 'total': 498830397039, 'used': 459995976927},
#     {'id': 401, 'total': 93386008768, 'used': 65371350065},
#     {'id': 402, 'total': 988242468378, 'used': 892424683789},
#     {'id': 430, 'total': 49705846287, 'used': 9522710872},
# ]
#
# def resource_utility(dict = []):
#     list_1 = []
#     list_2 = []
#     list_3 = []
#     for line in dict:
#         free_disk_spcae = line['total'] - line['used']
#         free_disk_spcae_percent = int(100 - ((line['used'] * 100) / line['total']))
#         if free_disk_spcae < 10737418240 or free_disk_spcae_percent < 5:
#             list_1.append(line['id'])
#         elif free_disk_spcae < 32212254720 or free_disk_spcae_percent < 10:
#             list_2.append(line['id'])
#         else:
#             list_3.append(line['id'])
#     utility_dict = {'memory_critical': list_1, 'memory_not_enough': list_2, 'memory_ok': list_3 }
#     return utility_dict
# print(resource_utility(resource_dict))