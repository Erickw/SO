import psutil

def main():

    print('*** Create a list of all running processes ***')

    listOfProcessNames = list()
    # Iterate over all running processes
    for proc in psutil.process_iter():
       # Get process detail as dictionary
       pInfoDict = proc.as_dict(attrs=['pid', 'name', 'username'])
       # Append dict of process detail in list
       listOfProcessNames.append(pInfoDict)

    # Iterate over the list of dictionary and print each elem
    for elem in listOfProcessNames:
        print(elem)

if __name__ == '__main__':
   main()