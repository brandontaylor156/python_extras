from os import remove


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, value):
        newNode = SLNode(value)
        currentHead = self.head
        newNode.next = currentHead
        self.head = newNode
        return self

    def add_to_back(self, value):
        if self.head == None:
            self.add_to_front(value)
            return self

        newNode = SLNode(value)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = newNode
        return self

    def remove_from_front(self):
        if self.head != None:
            if self.head.next == None:
                self.head = None
            else:
                self.head = self.head.next
        return self

    def remove_from_back(self):
        if self.head == None:
            return self
        elif self.head.next == None:
            self.head = None
        else:
            runner = self.head
            while (runner.next.next != None):
                runner = runner.next
            runner.next = None
        return self

    def remove_val(self, value):
        if self.head.value == value:
            self.remove_from_front()
        return self
        

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self

class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()

my_list.remove_val("Linked lists").print_values()