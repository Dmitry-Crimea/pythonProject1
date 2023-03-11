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
# def disk_util(user_data):
#     for line in user_data:
#         free_disk_spcae = line['total'] - line['used']
#         free_disk_spcae_percent = int(100 - ((line['used'] * 100) / line['total']))
#         if free_disk_spcae < 10737418240 or free_disk_spcae_percent < 5:
#             user_data = {'id': line['id'], 'memory_status': 'memory_critical'}
#             yield user_data
#         elif free_disk_spcae < 32212254720 or free_disk_spcae_percent < 10:
#             user_data = {'id': line['id'], 'memory_status': 'memory_not_enough'}
#             yield user_data
#         else:
#             user_data = {'id': line['id'], 'memory_status': 'memory_ok'}
#             yield user_data
#
# status_list = []
# for line in disk_util(resource_dict):
#     status_list.append(line)
#
# final_list = []
# for a in status_list:
#     for b in resource_dict:
#         if a['id'] == b['id']:
#             b.update(a)
#             final_list.append(b)
# print(final_list)

log_lst = [
    "May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.",
    "May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated",
    "May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.",
    "May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...",
    "May 20 11:01:12 PC-00102 PackageKit: daemon start",
    "May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...",
    "May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00",
    'May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"',
    "May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device",
    "May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio",
    "May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.",

   ]

print(list(map(lambda x: x.split()[:3],
               sorted(log_lst, key=lambda el: int(el.split()[2])))))