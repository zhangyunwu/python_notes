
class Node(object):
    """Node of double link list.
    """
    def __init__(self, ele):
        self.ele = ele
        self.next = None
        self.prev = None

class DoubleLinkList(object):
    """Double link list.
    """
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """Return True if double link list is empty, or False if not.
        """
        return self.__head is None

    def length(self):
        """Return the length of double link list.
        """
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """Ergodic and print the double link list."""
        cur = self.__head
        while cur != None:
            print(cur.ele, end=' ')
            cur = cur.next

    def add(self, item):
        """Add the item in the start of double link list.
        """
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        """Append the item in the end of double link list.
        """
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur
        
    def insert(self, pos, item):
        """Insert the item to the appointed position of double link list.
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
            node.prev = prior
            prior.next.prev = node
            prior.next = node
            
    def remove(self, item):
        """Remove the first item in double link list."""
        cur = self.__head
        while cur != None:
            if cur.ele == item:
                if cur == self.__head:    # the first node of DLL
                    self.__head = cur.next
                    if cur.next:    # the first node but not only node
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:    # not the last node
                        cur.next.prev = cur.prev
                return
            else:
                cur = cur.next

    def search(self, item):
        """Return True if item is in the double link list, or False if not.
        """
        cur = self.__head
        while cur != None:
            if cur.ele == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == "__main__":
    dll = DoubleLinkList()

    print('is dll empty?', dll.is_empty())
    print('length of sll: ', dll.length())

    dll.append(1)
    print('is dll empty?', dll.is_empty())
    print('length of sll: ', dll.length())

    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    dll.add(10)

    dll.insert(-2, 100)
    dll.insert(5, 200)
    dll.insert(10, 300)
    dll.travel()
    print('')

    dll.remove(0)
    dll.travel()
    print('')
    dll.remove(6)
    dll.travel()
    print('')
    dll.remove(5)
    dll.travel()
    print('')
    dll.remove(4)
    dll.travel()
    print('')
    dll.remove(3)
    dll.travel()
    print('')
    dll.remove(8)
    dll.travel()
    print('')
    dll.remove(10)
    dll.travel()
    print('')
    dll.remove(2)
    dll.travel()
    print('')
    dll.remove(1)
    dll.travel()
    print('')
    dll.remove(300)
    dll.travel()
    print('')
    dll.remove(200)
    dll.travel()
    print('')
    dll.remove(100)
    dll.travel()
    print('')

    print('is dll empty?', dll.is_empty())
    print('length of dll: ', dll.length())