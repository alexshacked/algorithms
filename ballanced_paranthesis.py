from data_structures.stack import Stack

def isBallanced(str):
    open = '(', '[', '{'
    close = ')', ']', '}'
    st = Stack()

    for ch in str:
        if ch in open:
            st.push(ch)
        elif ch in close:
            if st.isEmpty():
                return False

            idxClose = close.index(ch)
            op = st.pop()
            idxOpen = open.index(op)
            if idxClose != idxOpen:
                return False;

    if not st.isEmpty():
        return False

    return True

print isBallanced("{([])}")