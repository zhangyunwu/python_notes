
class Node(object):
    """Node of single link list.
    """
    def __init__(self, ele):
        self.ele = ele
        self.next = None

class SingleCycleLinkList(object):
    """Single cycle link list.
    """
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """Return True if single link list is empty, or False if not.
        """
        return self.__head is None

    def length(self):
        """Return the length of single link list.
        """
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """Ergodic and print the single link list."""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.ele, end=' ')
            cur = cur.next
        print(cur.ele)

    def add(self, item):
        """Add the item in the start of single link list.
        """
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        """Append the item in the end of single link list.
        """
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
        
    def insert(self, pos, item):
        """Insert the item to the appointed position of single link list.
        """
        if pos < 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            prior = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                prior = prior.next
            node = Node(item)
            node.next = prior.next
            prior.next = node

    def remove(self, item):
        """Remove the first item in single link list.
        """
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            if cur.ele == item:   # the element of first node is item
                rear = cur
                while rear.next != self.__head:    # get the last node.
                    rear = rear.next
                self.__head = cur.next
                rear.next = self.__head
                return
            if cur.next.ele == item:
                cur.next = cur.next.next
                return
            else:
                cur = cur.next
        if cur.ele == item:    # remove the only node
            self.__head = None

    def search(self, item):
        """Return True if item is in the single link list, or False if not.
        """
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.ele == item:
                return True
            else:
                cur = cur.next
        if cur.ele == item:
            return True
        return False

if __name__ == "__main__":
    sll = SingleCycleLinkList()

    print('is sll empty?', sll.is_empty())
    print('length of sll: ', sll.length())

    sll.append(1)
    print('is sll empty?', sll.is_empty())
    print('length of sll: ', sll.length())

    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    sll.add(10)

    sll.insert(-2, 100)
    sll.insert(5, 200)
    sll.insert(10, 300)
    sll.travel()

    sll.remove(0)
    sll.travel()
    sll.remove(6)
    sll.travel()
    sll.remove(5)
    sll.travel()
    sll.remove(4)
    sll.travel()
    sll.remove(3)
    sll.travel()
    sll.remove(8)
    sll.travel()
    sll.remove(10)
    sll.travel()
    sll.remove(2)
    sll.travel()
    sll.remove(1)
    sll.travel()
    sll.remove(300)
    sll.travel()
    sll.remove(200)
    sll.travel()
    sll.remove(100)
    sll.travel()

    print('is sll empty?', sll.is_empty())
    print('length of sll: ', sll.length())