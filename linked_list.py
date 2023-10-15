#PYTHON 
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def contains(self, key):
        current = self.head
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def add_last(self, key):
        if self.contains(key):
            return
        new_node = Node(key)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def add_first(self, key):
        if self.contains(key):
            return 
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def add_after(self, key, target_key):
        if self.contains(key):
            return
        new_node = Node(key)
        current = self.head
        while current:
            if current.key == target_key:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def add_before(self, key, target_key):
        if self.contains(key):
            return
        new_node = Node(key)
        if self.head and self.head.key == target_key:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current and current.next:
                if current.next.key == target_key:
                    new_node.next = current.next
                    current.next = new_node
                    break
                current = current.next

    def remove(self, key):
        if not self.contains(key):
            return
        if self.head and self.head.key == key:
            self.head = self.head.next
            return
        current = self.head
        while current and current.next:
            if current.next.key == key:
                current.next = current.next.next
                break
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_keys(self):
        keys = []
        current = self.head
        while current:
            keys.append(str(current.key))
            current = current.next
        print(" ".join(keys))

n = int(input())
keys = list(map(int, input().split()))
linked_list = LinkedList()

for key in keys:
    linked_list.add_last(key)

while True:
    command = input().strip()
    if command == "#":
        break
    parts = command.split()
    if parts[0] == "addlast":
        k = int(parts[1])
        linked_list.add_last(k)
    elif parts[0] == "addfirst":
        k = int(parts[1])
        linked_list.add_first(k)
    elif parts[0] == "addafter":
        u, v = int(parts[1]), int(parts[2])
        linked_list.add_after(u, v)
    elif parts[0] == "addbefore":
        u, v = int(parts[1]), int(parts[2])
        linked_list.add_before(u, v)
    elif parts[0] == "remove":
        k = int(parts[1])
        linked_list.remove(k)
    elif parts[0] == "reverse":
        linked_list.reverse()

linked_list.print_keys()
