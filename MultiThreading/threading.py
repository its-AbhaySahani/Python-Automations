import threading

def first_thread():
    for i in range(5):
        print(f"Executing in thread: {i}")

thread = threading.Thread(target=first_thread)
thread.start()

thread.join()

print("Main thread running")
