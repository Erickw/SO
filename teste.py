import os, signal, sys, psutil, time
from threading import Thread


def get_process_list():
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username', 'create_time']):
        print(proc.info)


def child():
    print('                   \n############################## New Child Created %d ##############################                   ' % os.getpid())

def create_process():
    newpid = os.fork()
    if newpid == 0:
        child()
    else:
        print("                   \n############################## New Parent Created %d ##############################                   " , os.getpid())

def process_manager():
    while True:
        time.sleep(10)
        create_process()
        get_process_list()

def main():
    get_process_list()
    while True:
        reply = raw_input("========================================= Do you want create more process? Insert y for yes, v to view current process pid or k to kill a specific process =========================================\n")

        if reply == 'y':
            create_process()
            get_process_list()

        elif reply == 'k':
            pid = raw_input("Insert the pid process you want to kill\n")
            print(int(pid))
            os.kill(os.getppid(), signal.SIGTERM)
            print("########################################## The process", pid, "was killed ##########################################")
            get_process_list()

        elif reply == 'v':
            print(os.getpid())

thread1 = Thread(target=main,args=[])
thread2 = Thread(target=process_manager,args=[])

thread1.start()
thread2.start()

