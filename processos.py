import os, signal, sys

def start():
   parent()
def child():
   print('\nA new child %d' % os.getpid())

def finish():
   print('Finishing the program...')
   sys.exit(0)

def parent():
   while True:
      newpid = os.fork()
      os.fork()
      if newpid == 0:
         child()
      else:
         print("parent: " , os.getpid())
      reply = raw_input("Insert the pid process that you want to kill or q to kill the program\n")
      if reply == 'q':
         finish()
      else:
         os.kill(int(reply), 9)
         print("The process", reply, "was killed")
         continue

start()