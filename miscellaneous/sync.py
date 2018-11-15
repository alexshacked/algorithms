import threading
import time

'''
This is an implementatition of an interveiew question asked at RedHat Raanana on November 2018. The interviewing team
was reaponsible for the Vdsm linux daemon which is part of the oVirt product.
The question: Implement a dresssing room that can accept an unlimited number of people, with the constraint that males
and females are not allowed in the room together. At a given moment the room can contain only men or only women or be
empty.
'''

class Room():
    def __init__(self):
        self.l = threading.Lock()
        self.l1 = threading.Lock()
        self.e = threading.Event()
        self.status = 'empty' # status: 'empty', 'male', 'female'
        self.people = 0

    def _get(self, who):
        if self.status not in ['empty', who]:
            return False
        self.status = who
        self.people += 1
        return True

    def _put(self, who):
        if self.status != who:
            raise Exception('Invalid room state. %s tried to leave but room was booked by %s' % (who, self.status))
        self.people -= 1
        if self.people == 0:
            self.status = 'empty'
            self.e.set()
            time.sleep(2)
            self.e.clear()

    def enter(self, who):
        self.l.acquire()
        mayI = self._get(who)
        self.l.release()
        if mayI:
           return
        self.e.wait()
        self.l1.acquire() # protect all threads being released on the event to ovewrite each other
        # we cant use self.l, because the it is currently used by the releasing thread to block newcomers of its own kind
        self._get(who)
        self.l1.release()

    def leave(self, who):
        self.l.acquire()
        self._put(who)
        self.l.release()

def thrA(room):
    room.enter('male')
    for i in range(4):
        print('maleA working')
        time.sleep(1)
    room.leave('male')

def thrB(room):
    room.enter('male')
    for i in range(4):
        print('maleB working')
        time.sleep(1)
    room.leave('male')

def thrB1(room):
    room.enter('male')
    for i in range(4):
        print('maleB1 working')
        time.sleep(1)
    room.leave('male')

def thrC(room):
    room.enter('female')
    HThread(room, thrB1).start()
    for i in range(4):
        print('femaleC working')
        time.sleep(1)
    room.leave('female')

def thrD(room):
    room.enter('female')
    for i in range(4):
        print('femaleD working')
        time.sleep(1)
    room.leave('female')

def thrE(room):
    room.enter('female')
    for i in range(4):
        print('femaleE working')
        time.sleep(1)
    room.leave('female')

class HThread(threading.Thread):
    def __init__(self, obj, func):
        self.obj = obj
        self.func = func
        threading.Thread.__init__(self)

    def run(self):
        self.func(self.obj)

if __name__ == '__main__':
    the_r = Room()
    for f in [thrA, thrB, thrC, thrD, thrE]:
        HThread(the_r, f).start()