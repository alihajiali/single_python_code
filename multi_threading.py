from concurrent.futures import ThreadPoolExecutor
import time
import datetime
import threading

#یک فانکشن داریم که انرا در دو حالت با و بدون مالتی تردینگ اجرا میکنیم
def func(args):
    print(f"start {args}")
    time.sleep(3)
    print(f"stop {args}")

#-------------------------------------------------------------------------

# حالت اول بدون مالتی تردینگ
t1 = datetime.datetime.now()
a = func("one")
b = func("two")
print(datetime.datetime.now() - t1)

#-------------------------------------------------------------------------
print("*"*80)
#-------------------------------------------------------------------------

# حالت دوم با مالتی تردینگ
# روش اول
t1 = datetime.datetime.now()
thread1 = threading.Thread(target=func, args=("one", ))
thread2 = threading.Thread(target=func, args=("two", ))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(datetime.datetime.now() - t1)

#-------------------------------------------------------------------------
print("*"*80)
#-------------------------------------------------------------------------

# حالت دوم با مالتی تردینگ
# روش دوم
t1 = datetime.datetime.now()
with ThreadPoolExecutor(max_workers=3)as exe:   #  ماکس ورکر تعداد ترد همزمان هستش
    names=["one", "two", "three", "four", "five", "six", "seven"]
    exe.map(func, names)
print(datetime.datetime.now() - t1)