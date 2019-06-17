
import sys
from subprocess import Popen, PIPE

# ps aux | grep twinkle
# sudo kill -1 xxxx

#proc = Popen(["mosquitto_sub", "-h", "192.168.1.10", "-t", "patient"],stdin=PIPE, stdout=PIPE, bufsize=2)
#proc2 = Popen(["twinkle", "-c"], stdin=proc.stdout, stdout=PIPE, bufsize=2)
#proc2 = Popen(["twinkle", "-c"], stdin=PIPE, stdout=PIPE, bufsize=1)
#for line in iter(proc2.stdout.readline, b''):
#    print line
#    if (line.find("incoming call") > 0):
 #       print ("Hello")
  #      proc2.stdin.write("answer\n")

#proc.communicate()
#proc2.communicate()



