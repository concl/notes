
import re
from pathlib import Path
import subprocess

from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--push_or_pull", type=str, default="pull")
    return parser.parse_args()

def main():
    args = parse_args()
    command = args.push_or_pull
    
    path = Path(__file__).parent
    patt = re.compile(r"fatal:.+")
    
    while True:
        
        process = subprocess.run(["git",command],capture_output=True, cwd=path)
        stdout, stderr = process.stdout, process.stderr
        if not patt.match(stderr.decode()):
            break
        else:
            print(stderr)
        
    
if __name__ == "__main__":
    main()
