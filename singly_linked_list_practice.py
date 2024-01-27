"""
class Node:

    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


def constructLL(arr: [int]) -> Node:
    n = len(arr)
    head = Node(arr[0])
    temp = head
    for i in range(1, n):
        curNode = Node(arr[i])
        temp.next = curNode
        temp = temp.next
    return head


print(constructLL([5, 2, 5, 3, 9, 6]).val)

################################################################################################

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


def construct_linked_list(arr):
    n = len(arr)
    if n == 0:
        return None

    head = Node(arr[0])
    temp = head

    for i in range(1, n):
        cur_node = Node(arr[i])
        temp.next = cur_node
        temp = temp.next
    return head


arr1 = (12, 34, 4, 30, 11, 22, 32)
arr2 = []
print(construct_linked_list(arr2))
print(construct_linked_list(arr1).value)

#####################################################################################################
# Display first node of linked list..

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


def display_first_node(arr):
    head = Node(arr[0])
    return head


arr2 = (12, 23, 34, 45, 56, 67, 78, 89)
print(construct_linked_list(arr2).value)



# Display the last node of linked list..

################################################################################################
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


def display_last_node(arr):
    tail = Node(arr[-1])
    return tail


arr2 = (12, 23, 34, 45, 56, 67, 78, 89)
print(display_last_node(arr2).value)



###############################################################################################################

# Display linked list

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
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

    def create_linked_list(self, arr: [int]) -> None:
        n = len(arr)
        if n == 0:
            return
        else:

            self.head = Node(arr[0])
            temp = self.head
            for i in range(1, n):
                current_node = Node(arr[i])
                temp.next = current_node
                temp = temp.next


linked_list = Linkedlist()
array1 = (12, 23, 34, 45, 56, 67, 78, 89, 90)
array2 = ()
linked_list.create_linked_list(arr=array1)
print(linked_list)


#########################################################################################################
# Insert a Node into linked list at initial...

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:

            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:
            temp = self.tail
            temp.next = new_node
            self.tail = temp.next
            self.length += 1


linkedlist = LinkedList()
linkedlist.append(12)
print(linkedlist)
print(linkedlist.head.value)
print(linkedlist.tail.value)

linkedlist.append(23)
print(linkedlist)
print(linkedlist.head.value)
print(linkedlist.tail.value)

linkedlist.append(43)
print(linkedlist)
print(linkedlist.head.value)
print(linkedlist.tail.value)

linkedlist.append(33)
print(linkedlist)
print(linkedlist.head.value)
print(linkedlist.tail.value)

print(linkedlist.length)
print(linkedlist.head.next.value)
print(linkedlist.head.next.next.value)




##################################################################################################
# Insert node in linked list at final..

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:
            temp = self.tail
            temp.next = new_node
            self.tail = new_node
            self.length += 1


linkedlist = LinkedList()

linkedlist.append(12)
linkedlist.append(24)
linkedlist.append(48)
linkedlist.append(60)
linkedlist.append(72)
print(linkedlist.head)
print(linkedlist.head.value)
print(linkedlist)



########################################################################################################
# Insert node in linked list at initial...

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1


linked_list = LinkedList()
linked_list.prepend(12)
linked_list.prepend(24)
linked_list.prepend(36)
linked_list.prepend(48)
print(linked_list.head)
print(linked_list.tail)
print(linked_list.head.value)
print(linked_list.tail.value)
print(linked_list)


############################################################################################################
# Insert node in linked list at given index...

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
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

    def _create_node(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self._create_node(value)
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self._create_node(value)

        else:
            temp = self.tail
            if temp:
                temp.next = new_node
                self.tail = new_node
            else:
                self._create_node(value)
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False

        elif index == 0:
            self.prepend(value)

        elif self.length == 0:
            self._create_node(value)

        elif index == (self.length - 1):
            self.append(value)

        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1



linkedlist = LinkedList()

linkedlist.insert(0, 12)
linkedlist.insert(index=1, value=24)
linkedlist.append(36)
linkedlist.prepend(6)
linkedlist.insert(2, 18)
linkedlist._create_node(100)
print(linkedlist)

"""


###############################################################################################################

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
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

    def _create_node(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length += 1

    def constructLL(self, arr: [int]) -> None:
        n = len(arr)
        if n == 0:
            self.head = None
            self.tail = None
            return None

        else:
            self.head = Node(arr[0])
            temp = self.head
            for i in range(1, n):
                current_node = Node(arr[i])
                temp.next = current_node
                temp = temp.next
            self.tail = temp
            self.length += n

    def get(self, index):
        if index < 0 or index > self.length:
            return None

        else:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            return current_node

    def pop_first(self):
        if self.length == 0:
            self.head = None
            self.tail = None

        else:
            temp = self.head
            temp = temp.next
            self.head = temp

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
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.pop_first()
        elif index == (self.length - 1):
            self.pop()
        else:
            prev_node = self.get(index - 1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
            return popped_node


linkedlist = LinkedList()
arr1 = [1, 12, 3, 4, 5, 12, 32, 20]
arr2 = []
linkedlist.constructLL(arr1)
print(linkedlist)
if linkedlist.head:
    print(linkedlist.head.value)
if linkedlist.tail:
    print(linkedlist.tail.value)
if linkedlist.length:
    print(linkedlist.length)
if linkedlist.get(3):
    print(f"Index No.3:- {linkedlist.get(5).value}")

linkedlist.pop_first()
print(linkedlist)
linkedlist.pop_first()
print(linkedlist)
print(linkedlist.pop().value)
print(linkedlist)
linkedlist.remove(2)
print(linkedlist)