
class Node(object):
    """Node of single link list.
    """
    def __init__(self, ele):
        self.ele = ele
        self.next = None

class SingleLinkList(object):
    """Single link list.
    """
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """Return True if single link list is empty, or False if not.
        """
        return self.__head is None

    def length(self):
        """Return the length of single link list.
        """
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """Ergodic and print the single link list."""
        cur = self.__head
        while cur != None:
            print(cur.ele, end=' ')
            cur = cur.next

    def add(self, item):
        """Add the item to the start of single link list.
        """
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """Append the item to the end of single link list.
        """
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
        
    def insert(self, pos, item):
        """Insert the item to the appointed position of single link list."""
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
        """Remove the first item in single link list."""
        prior = self.__head
        while prior != None:
            if prior.ele == item:    # the element of first node is item
                self.__head = prior.next
                break
            if prior.next.ele == item:
                prior.next = prior.next.next
                break
            else:
                prior = prior.next
            if prior.next is None:    # item is not in the sll
                break

    def search(self, item):
        """Return True if item is in the single link list, or False if not.
        """
        cur = self.__head
        while cur != None:
            if cur.ele == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == "__main__":
    sll = SingleLinkList()

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
    print('')

    sll.remove(6)
    sll.travel()
    print('')
    sll.remove(5)
    sll.travel()
    print('')
    sll.remove(4)
    sll.travel()
    print('')
    sll.remove(3)
    sll.travel()
    print('')
    sll.remove(8)
    sll.travel()
    print('')
    sll.remove(10)
    sll.travel()
    print('')
    sll.remove(2)
    sll.travel()
    print('')
    sll.remove(1)
    sll.travel()
    print('')
    sll.remove(300)
    sll.travel()
    print('')
    sll.remove(200)
    sll.travel()
    print('')
    sll.remove(100)
    sll.travel()
    print('')
