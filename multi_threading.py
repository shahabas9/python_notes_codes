import threading
import time

def func1(event):
    event.wait()
    event1.wait()
    current_thread = threading.current_thread()
    print("current thread name :", current_thread.name)
    for i in range(5):
        time.sleep(1)
        print("iiiii -->",i)


def func2(event,apple):
    current_thread = threading.current_thread()
    print("current thread name :", current_thread.name)
    for j in range(5):
        time.sleep(1)
        print("jjjjj --->",j)
    event1.set()

def func3(event,ball):
    event1.wait()
    current_thread = threading.current_thread()
    print("current thread name :", current_thread.name)
    for k in range(5):
        time.sleep(1)
        print("kkkkk --->",k)
    event1.set()

event = threading.Event()
event1 = threading.Event()
t1 = threading.Thread(target=func1, args=(event,))
t2 = threading.Thread(target=func2, args=(event,10))
t3 = threading.Thread(target=func3, args=(event,10))
#t2 = threading.Thread(target=func2())

t1.start()
t2.start()
t3.start()

# activate_threads = threading.enumerate()
# for k in activate_threads:
#     print(k)




    
t1.join()
t2.join()


print("alright")


    


