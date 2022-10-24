import utils
from argparse import ArgumentParser
file = "trading_system.json"
args = ArgumentParser()
#
#
args.add_argument('--RATE', type=str, nargs='?')
args.add_argument('AVAILABLE', type=str, nargs='?', default='')
args.add_argument('BUY XXX', type=int, nargs='?', default=0)
args.add_argument('SELL XXX', type=int, nargs='?', default=0)
args.add_argument('BUY ALL', type=str, nargs='?', default='')
args.add_argument('SELL ALL', type=str, nargs='?', default='')
args.add_argument('--NEXT', type=float, nargs='?')
args.add_argument('RESTART', type=str, nargs='?', default='')
#
args = vars(args.parse_args())
#
next = args[utils.next_roll()]
rate = args[utils.current_rate()]
print(f"NEXT: {next}")