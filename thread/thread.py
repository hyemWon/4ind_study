import threading
import time
import cv2
from collections import deque



class ThreadA(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.queue = deque()
        self.url = url

        try:
            self.cap = cv2.VideoCapture(url)
        except:
            print('장치가 연결되지 않았습니다.')

    def run(self):
        while(True):
            ret, frame = self.cap.read()

            if ret:
                if len(self.queue) < 1:
                    self.queue.append(frame)
        
        self.cap.release()
            

class ThreadB(threading.Thread):
    def __init__(self, thread):
        threading.Thread.__init__(self)
        self.threadA = thread

    def run(self):
        start_t = time.time()
        count = 0
        while True:
            if len(self.threadA.queue) > 0:
                frame = self.threadA.queue.popleft()
                cv2.imshow('Webcam', frame)
                count += 1

                if cv2.waitKey(1) & 0xFF==ord('q'):
                    break
            # fps 출력    
            if time.time() - start_t > 1:
                print(count)
                count = 0
                start_t = time.time()
        cv2.destroyAllWindows()



if __name__=='__main__':
    A = ThreadA(0)
    B = ThreadB(A)
    A.start()
    B.start()