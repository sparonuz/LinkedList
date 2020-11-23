import Error


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        curr = self.head
        data = []
        while curr:
            data.append(repr(curr))
            curr = curr.next
        return "[" + ", ".join(data) + "]"

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def prepend(self, data):
        self.head = Node(data, next=self.head)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data=data)

    def find(self, key):
        if self.head is None:
            raise Error.EmptyLinkedList("No data found")
        curr = self.head
        while curr.next:
            if curr.data == key:
                return curr
            curr = curr.next
        raise Error.KeyNotFound("Key %s not found", str(key))

    def remove(self, key):
        if self.head is None:
            raise Error.EmptyLinkedList("No data found")
        curr = self.head
        while curr.next:
            if curr.next.data == key:
                curr.next = curr.next.next
            curr = curr.next

    def reverse(self):
        if self.head is None:
            raise Error.EmptyLinkedList("Nothing to reverse")
        curr = self.head
        next = curr.next
        prec = None
        while next:
            next = curr.next
            curr.next = prec
            prec = curr
            curr = next
        self.head = prec


if __name__ == '__main__':
     a = LinkList()
     a.prepend(23)
     a.prepend('a')
     a.prepend('b')
     a.prepend('c')
     a.prepend(33)
     a.append('q')
     a.remove('b')
     a.reverse()
     print(a)



