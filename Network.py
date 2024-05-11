import time

def readiness():
        ready = 0
        while ready <= 100:
            print(ready)
            time.sleep(0.1)
            ready += 1

        return ready

readiness()

