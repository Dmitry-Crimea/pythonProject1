import argparse, time, logging, os

parser = argparse.ArgumentParser()
parser.add_argument('--delay', default=1, type=int, help='Задержка в секундах')
parser.add_argument('--num', default=3, type=int, help='Количество строк лога')
args = parser.parse_args()

logging.basicConfig(filename='log_file.log',
                    format='%(asctime)s  %(levelname)s  %(message)s',
                    datefmt='%b %H:%M:%S',
                    level=logging.INFO)

log_dict = {key:value for (key, value) in os.environ.items()}
print(log_dict.keys())



for i in range(args.num):
    logging.info(log_dict.keys())
    time.sleep(args.delay)
