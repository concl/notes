
import re
from pathlib import Path
import subprocess


def main():
    
    
    path = Path(__file__).parent
    patt = re.compile(r"fatal:.+")
    
    while True:
        
        process = subprocess.run(["git","pull"],capture_output=True)
        stdout, stderr = process.stdout, process.stderr
        if not patt.match(stderr.decode()):
            break
        else:
            print(stderr)
        
    
if __name__ == "__main__":
    main()
