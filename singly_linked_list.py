# Class for Empty list, where both the pointers point towards None and length of it is zero...
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


# class for singly linked list, where both the pointers point towards single elements and length is zero...
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False

        elif index == 0:
            new_node.next = self.head
            self.head = new_node

        elif self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return False

    def get(self, index):
        if 0 < index <= self.length:
            current = self.head
            for _ in range(index):
                current = current.next
            return current
        elif index < 0 or index > self.length:
            return False

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            return None
        else:
            self.head = self.head.next
            popped_node = None
        self.length -= 1
        return popped_node

    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        elif index == 0:
            return self.pop_first()

        else:
            prev_node = self.get(index - 1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0


new_linked_list = LinkedList()
print(new_linked_list.head)
print(new_linked_list.tail)
print(new_linked_list.length)

new_linked_list.append(10)
print(new_linked_list.head)
print(new_linked_list.tail)
print(new_linked_list.length)

new_linked_list.append(20)
print(new_linked_list.head)
print(new_linked_list.tail)
print(new_linked_list.length)

print(new_linked_list.head.value)
print(new_linked_list.tail.value)
new_linked_list.append(30)
new_linked_list.append(40)
print(new_linked_list)

new_linked_list.prepend(5)
new_linked_list.insert(3, 50)
print(new_linked_list)
new_linked_list.traverse()
print(new_linked_list.search(50))
print(new_linked_list.get(1))
print(new_linked_list.set_value(3, 100))
print(new_linked_list)
new_linked_list.pop_first()
print(new_linked_list)
new_linked_list.pop()
print(new_linked_list)
new_linked_list.append(200)
new_linked_list.append(15)
new_linked_list.insert(2, 50)
print(new_linked_list)
print(new_linked_list.remove(0))
print(new_linked_list)
new_linked_list.delete_all()
print(new_linked_list)