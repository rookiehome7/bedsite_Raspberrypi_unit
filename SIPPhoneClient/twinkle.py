import sys
from subprocess import Popen, PIPE
#Twinkle Instruction
#call        Call someone
#answer      Answer an incoming call
#answerbye   Answer an incoming call or end a call
#reject      Reject an incoming call
#redirect    Redirect an incoming call
#transfer    Transfer a standing call
#bye     End a call
#hold        Put a call on-hold
#retrieve    Retrieve a held call
#conference  Join 2 calls in a 3-way conference
#mute        Mute a line
#dtmf        Send DTMF
#redial      Repeat last call
#register    Register your phone at a registrar
#deregister  De-register your phone at a registrar
#fetch_reg   Fetch registrations from registrar
#options     Get capabilities of another SIP endpoint
#line        Toggle between phone lines
#dnd     Do not disturb
#auto_answer Auto answer
#user        Show users / set active user
#message     Send an instant message
#presence    Publish your presence state
#quit        Quit
#help        Get help on a command

proc = Popen(["twinkle", "-c"], stdin=PIPE, stdout=PIPE, bufsize=2)
for line in iter(proc.stdout.readline, b''):
    print line
    if (line.find("registration succeeded") > 0):
        proc.stdin.write("\n")
    if (line.find("incoming call") > 0):
        proc.stdin.write("answer\n")
    #do whatever you want by adding code...
    if (line.find("far end ended call") > 0):
        proc.stdin.write("bye\n")  
proc.communicate()
