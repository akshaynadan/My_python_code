import time
from timer import Timer
from multiprocessing import Process,cpu_count

def counter(num):
    count=0
    while  count<num:
        count+=1


def main():
    t = Timer()
    t.start()

    a= Process(target=counter,args=(250000000,))
    b= Process(target=counter,args=(250000000,))
    c= Process(target=counter,args=(250000000,))
    d= Process(target=counter,args=(250000000,)) 
    # e= Process(target=counter,args=(100000000,))
    # f= Process(target=counter,args=(100000000,))
    # g= Process(target=counter,args=(100000000,))
    # h= Process(target=counter,args=(100000000,))
    # i= Process(target=counter,args=(100000000,))  
    # j= Process(target=counter,args=(100000000,))
    
    a.start()
    b.start()
    c.start()
    d.start()
    # e.start()
    # f.start()
    # g.start()
    # h.start()
    # i.start()
    # j.start()

    a.join()
    b.join()
    c.join()
    d.join()
    # e.join() 
    # f.join()
    # g.join()
    # h.join()
    # i.join()
    # j.join()

    
    t.stop()
   
    print(f"Finished in : seconds")
if __name__ == '__main__':
    main()


