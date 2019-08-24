# -*- coding: ISO-8859-1 -*-
import thread
import time, random
import threading

garfo = list()
for i in range(5):
   garfo.append(threading.Semaphore(1))

def filosofo(f):
   f = int(f)
   while True:
      garfo[f].acquire()
      garfo[(f + 1) % 5].acquire()
      print "Filósofo %i está comendo..." %f
      time.sleep(random.randint(1, 5))
      garfo[f].release()
      garfo[(f + 1) % 5].release()
      print "Filósofo %i está pensando..." %f
      time.sleep(random.randint(1, 10))

for i in range(5):
   print "Número do filósofo é", i
   thread.start_new_thread(filosofo, tuple([i]))

while 1: pass