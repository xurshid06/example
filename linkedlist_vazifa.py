class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        # listning boshiga element qo'shish
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, new_data):
        # listning ixtiyoriy nuqtasiga element qo'shish
        if prev_node is None:
            print("Error")
        # yangi element qo'shamiz
        new_node = Node(new_data)
        # yangi tugunni keyingi elementga bog'laymiz
        new_node.next = prev_node.next
        # avvalgi tugunni yangi elementga bog'laymiz
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

a = Node(9)
b = Node(45)
c = Node(55)
linked = LinkedList()
linked.head = a
a.next = b
b.next = c
linked.push(100)
linked.push(101)
linked.push(102)
linked.push(103)
linked.push(104)
print("linked 1")
linked.printList()


linked2 = LinkedList()
d = Node(200)
g = Node(202)
h = Node(204)
j = Node(206)
k = Node(208)
linked2.head = d
d.next = g
g.next = h
h.next = j
j.next = k
linked2.insert(d, 201)
linked2.insert(g, 203)
linked2.insert(h, 205)
linked2.insert(j, 207)
linked2.insert(k, 209)
linked2.printList()
print("linked listda insertni qo'llanilishi")


linked_append = LinkedList()
a = Node(300)
linked_append.head = a
linked_append.append(301)
linked_append.append(302)
linked_append.append(303)
linked_append.append(304)
linked_append.append(305)
linked_append.printList()
print("linked listda appendni qo'llanishi")
