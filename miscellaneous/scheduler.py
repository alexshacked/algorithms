import time


# Interview question at Radband October 2018
# Problem description (aproximately): design a scheduler that receive at init time several event and their frequencies.
# When started, the scheduler begin triggering the events respecting their frequencies
class Node:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
        self.delta = freq


class Scheduler:
    def __init__(self):
        self.l = []

    def put(self, val, freq):
        n = Node(val, freq)
        pre = 0
        i = 0
        after = False
        for i in range(len(self.l)):
            tmp = pre + self.l[i].delta
            if tmp < freq:
                pre = tmp
                after = True
            elif tmp == freq:
                after = True
                break
            else:
                after = False
                break
        if pre != 0:
            n.delta = n.freq - pre
        k = i + 1 if after == True else i
        self.l.insert(k, n)

        for j in range(k + 1, len(self.l)):
            self.l[j].delta -= n.delta

    def run(self):
        now = 0
        while True:
            tm = self.l[0].delta
            time.sleep(tm)
            now += tm

            bucket = []
            while len(self.l) > 0 and tm == self.l[0].delta \
                and (now % self.l[0].freq) == 0:
                n = self.l.pop(0)
                bucket.append(n)

            while len(bucket) > 0:
                n = bucket.pop(0)
                print('%d: %s' % (now, str(n.val)))
                self.put(n.val, n.freq)
            print('------------------------------')


s = Scheduler()
s.put('a', 2)
s.put('b', 3)
s.run()
