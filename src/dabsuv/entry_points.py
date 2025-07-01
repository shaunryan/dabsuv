import argparse
from pathlib import Path
from . import taxi


def get_taxi_count():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", nargs="?", default=None)
    args = parser.parse_args()
    print(args)
    taxi.get_taxi_count()

def get_taxis():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", nargs="?", default=None)
    args = parser.parse_args()
    print(args)
    taxi.get_taxis()