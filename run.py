import multiprocessing as mp
import subprocess as sp
#to run Dynamo
def startDynamo() :
    #Code for Process-1
    print("Process-1 is running...")
    from main import start
    start()
#to detect Hot word
def listenHotWord() :
    #Code for Process-2
    print("Process-2 is running...")
    from engine.features import hotWord
    hotWord()
#start both processes
if __name__ == '__main__' :
    p1 = mp.Process(target = startDynamo)
    p2 = mp.Process(target = listenHotWord)
    p1.start()
    # sp.call([r'device.bat'])
    p2.start()
    p1.join()
    if p2.is_alive() :
        p2.terminate()
        p2.join()
    print("System terminated.")