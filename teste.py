import os, signal, sys, psutil, time, schedule
from threading import Thread


def get_process_list():
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username', 'create_time']):
        print(proc.info)


def child():
    created_processes.append(os.getpid())
    print('\n############################## New Child Created %d ##############################' % os.getpid())

def create_process():
    newpid = os.fork()
    if newpid == 0:
        child()
    else:
        print("############################## New Parent Created: ############################## " , os.getpid())

def process_manager():
    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    get_process_list()
    while True:
        print os.getpid()
        reply = raw_input("Do you want create more process? Insert y for yes, v to view current process pid or k to kill a specific process\n")

        if reply == 'y':
            create_process()
            get_process_list()

        elif reply == 'k':
            pid = raw_input("Insert the pid process you want to kill\n")
            print(int(pid))
            os.kill(os.getppid(), signal.SIGKILL)
            print("########################################## The process", pid, "was killed ##########################################")
            get_process_list()

        elif reply == 'v':
            print(os.getpid())



schedule.every(10).seconds.do(create_process)

thread1 = Thread(target=main,args=[])
thread2 = Thread(target=process_manager,args=[])

thread1.start()
thread2.start()

