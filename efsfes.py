import time

start = time.time()


while True:
    elapsed = time.time() - start
        
    if elapsed >= 10:
        break


    time.sleep(0.1)

print("\nStopped after 10 seconds.")

