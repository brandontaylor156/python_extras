class DList:
    def __init__(self):
        self.firstNode = DLNode(0)
        self.lastNode = DLNode(0)

class DLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None