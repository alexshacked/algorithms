class Counter:
    def count (self, str):
        l = [ord(s) - ord('0') for s in str]
        self.doCount(l)

    def doCount(self, arr):
        startIdx = len(arr) - 2
        while True:
            self.doDigits(arr)
            if self.doOthers(arr, startIdx) == False:
                break

    def doDigits(self, arr):
        idx = len(arr) -1
        for i in range(9):
            self.show(arr)
            arr[idx] = arr[idx] + 1
        self.show(arr)
        arr[idx] = 0

    def doOthers(self, arr, startIdx):
        if startIdx == 0 and arr[startIdx] == 9:
            return False

        arr[startIdx] = arr[startIdx] + 1
        if arr[startIdx] <= 9:
            return True
        elif startIdx > 0:
            arr[startIdx] = 0
            return self.doOthers(arr, startIdx - 1)

    def show(self, arr):
        chs = [str(a) for a in arr]
        s = ''.join(chs)
        print s

if __name__ == '__main__':
    counter = Counter()
    counter.count('000')







