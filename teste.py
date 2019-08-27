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

def kill_processes():
    while True:
        time.sleep(30)
        print("########################################## The process", os.getpid(), "was killed ##########################################")
        os.kill(os.getpid(), signal.SIGKILL)
        get_process_list()
        print("========================================= Select an option: =========================================\n" +
        "====== P - for a new process ====== \n" +
        "====== V - view current process pid ======\n" +
        "====== K - to kill a specific process ======\n")

def process_manager():
    while True:
        time.sleep(10)
        create_process()
        get_process_list()
        print("========================================= Select an option: =========================================\n" +
        "====== P - for a new process ====== \n" +
        "====== V - view current process pid ======\n" +
        "====== K - to kill a specific process ======\n")

def main():
    get_process_list()
    while True:
        reply = raw_input("========================================= Select an option: =========================================\n" +
        "====== P - for a new process ====== \n" +
        "====== V - view current process pid ======\n" +
        "====== K - to kill a specific process ======\n")

        if reply == 'p':
            create_process()
            get_process_list()

        elif reply == 'k':
            pid = raw_input("Insert the pid process you want to kill\n")
            os.kill(pid, signal.SIGKILL)
            print("########################################## The process", pid, "was killed ##########################################")
            get_process_list()

        elif reply == 'v':
            print(os.getpid())

thread1 = Thread(target=main,args=[])
thread2 = Thread(target=process_manager,args=[])
thread3 = Thread(target=kill_processes,args=[])

thread1.start()
thread2.start()
thread3.start()

