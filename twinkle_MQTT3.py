import sys
from subprocess import Popen, PIPE


proc = Popen(["twinkle", "-c"], stdin=PIPE, stdout=PIPE, bufsize=2)

for line in iter(proc.stdout.readline, b''):
    print line 
    if (line.find("registration succeeded") > 0):
        proc.stdin.write("\n")
        
    if (line.find("incoming call") > 0):
        proc.stdin.write("answer\n")
        #proc.stdin.write("call 101\n")
    #do whatever you want by adding code...
        
    if (line.find("far end ended call") > 0):
        proc.stdin.write("bye\n") 

 
proc.communicate()







