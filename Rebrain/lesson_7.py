resource_dict = [
    {'id': 382, 'total': 999641890816, 'used': 228013805568},
    {'id': 385, 'total': 61686008768, 'used': 52522710872},
    {'id': 398, 'total': 149023482194, 'used': 83612310700},
    {'id': 400, 'total': 498830397039, 'used': 459995976927},
    {'id': 401, 'total': 93386008768, 'used': 65371350065},
    {'id': 402, 'total': 988242468378, 'used': 892424683789},
    {'id': 430, 'total': 49705846287, 'used': 9522710872},
]

def disk_util(user_data):
    for line in user_data:
        free_disk_spcae = line['total'] - line['used']
        free_disk_spcae_percent = int(100 - ((line['used'] * 100) / line['total']))
        if free_disk_spcae < 10737418240 or free_disk_spcae_percent < 5:
            user_data = {'id': line['id'], 'memory_status': 'memory_critical'}
            yield user_data
        elif free_disk_spcae < 32212254720 or free_disk_spcae_percent < 10:
            user_data = {'id': line['id'], 'memory_status': 'memory_not_enough'}
            yield user_data
        else:
            user_data = {'id': line['id'], 'memory_status': 'memory_ok'}
            yield user_data
