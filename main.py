import sys
import subprocess
import time
from clear import clearf
argc = len(sys.argv)
argv = sys.argv

if argc > 1:
    sentence = ""
    isFile = False
    delay = 0.05
    cowfile = "None"
    for arg in argv[1:]:
        if arg.startswith("-"):
            if(arg == "--file" or arg == '-f'):
                isFile = True
            elif(arg.startswith("--delay") or arg.startswith('-d')):
                delay = float(arg.split("=")[1])
            elif(arg.startswith("--cowfile") or arg.startswith('-c')):
                cowfile = arg.split("=")[1]
            elif(arg == "--help" or arg == '-h'):
                print("List of commands:")
                print("--help or -h: Prints the following list")
                print("--delay=value or -d=value: Changes the amount of time each character takes to be typed")
                print("--file or -f: Opens the specified file and types it out")
                print("--cowfile=value or -c=value: Changes the cowfile")
        else:
            if(isFile):
                with open(arg, "r") as f:
                    content = f.read()
            else:
                content = arg
            for c in content:
                sentence = sentence + c
                if(c == '\n'):
                    sentence = ""
                time.sleep(delay)
                clearf()
                if(cowfile == "None"):
                    subprocess.Popen(["cowsay", sentence])
                else:
                    subprocess.Popen(["cowsay","-f", cowfile, sentence])
    