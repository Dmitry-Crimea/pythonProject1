def fileopen(file):
    with open(file, 'r') as input_file:
        open('../Rebrain/file_7.txt', 'w') as output_file:
        log_dict = input_file.readlines()
        log_str = []
        for el in log_dict:
            mounth, day, time, *other = el.split()
            if int(day) == 20:
                output_file.write(el)
    with open('../Rebrain/file_7.txt', 'r') as file:
        return input_file.read()
