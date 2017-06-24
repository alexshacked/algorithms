

class Binary:
    def __init__(self, bits):
        self.bits = bits # bits is a list of zeros and ones that is the binary number

    def __str__(self):
        return " ".join([str(b) for b in self.bits])

    def toDec(self):
        size = len(self.bits)
        power = 1
        num = 0
        for i in range(size):
            cur = size - 1 - i
            num = num + self.bits[cur] * power
            power = power * 2

        return num

def fromDec2Bin(dec):
    l = []
    while dec > 0:
        mod = dec % 2
        l.insert(0, mod)
        dec = dec // 2  # porting to python3

    return Binary(l)




if __name__ == '__main__':

    while True:
        print 'Enter decimal number: '
        dec = input()
        if dec == -1:
            print 'Entered -1 which means requesting to leave. We are leaving. '
            exit()

        print 'input: %d' % dec
        bn = fromDec2Bin(dec)
        print bn
        print bn.toDec()
        print '\n\n'

