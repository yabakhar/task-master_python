import os 
import time 
import sys 

# mainPid = os.getpid() 
# print("Main Pid: %s" % mainPid) 

pid = os.fork() 

if pid > 0: 
    time.sleep(3) 
    print("Main process quit") 
    sys.exit(0) 

os.setsid() 
print("Main process quit") 
# for x in range(1, 10): 
#  print("spid: %s, ppid: %s pgid: %s" % (os.getpid(), os.getppid(), os.getpgid(0))) 
#  time.sleep(1) 