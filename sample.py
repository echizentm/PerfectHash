# coding: utf-8
import random
from argparse import ArgumentParser
from perfect_hash import PerfectHash


parser = ArgumentParser(
    description='sample code of PerfectHash'
)
parser.add_argument(
    '-p', '--prime',
    type=int, default=10009,
    help='universe set size (prime number)',
)
parser.add_argument(
    '-s', '--size',
    type=int, default=300,
    help='subset size to sample',
)
parser.add_argument(
    '-t', '--trials',
    type=int, default=10,
    help='number of trials',
)
args = parser.parse_args()

ph = PerfectHash()
for i in range(args.trials):
    elements = random.sample(range(1, args.prime), args.size)
    ph.make(elements, args.prime)
    if ph.check(elements, args.prime) == 1.0:
        print("Success. block size: {0}".format(ph.size()))
    else:
        print("Failure.")
