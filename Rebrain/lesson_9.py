import argparse, time, logging, os

parser = argparse.ArgumentParser()
parser.add_argument('--delay', required=True, type=int, help='Задержка в секундах')
parser.add_argument('--num', required=True, type=int, help='Количество строк лога')
args = parser.parse_args()

logging.basicConfig(filename='log_file.log',
                    format='%(asctime)s  %(levelname)s  %(message)s',
                    datefmt='%b %H:%M:%S',
                    level=logging.INFO)
count = 0
for key in os.environ:
    logging.info(key + '->' + os.environ.get(key))
    count +=1
    if count >= args.num:
        break
    time.sleep(args.delay)
