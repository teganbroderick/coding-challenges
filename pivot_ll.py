class LinkedList(object):
    """Singly-Linked list."""

    def __init__(self, values=None):
        """Set up list with optional starting data."""

        self.head = None
        self.tail = None

        if values:
            for value in values:
                self.add_data(value)

    def add_data(self, value):
        """Add node with given data.

            >>> ll = LinkedList()
            >>> ll.add_data(2)
            >>> ll.add_data(1)
            >>> ll.print_list()
            2 1 
        """

        node = Node(value)
        self.add_node(node)

    def add_node(self, node):
        """Add node.

            >>> ll = LinkedList()
            >>> ll.add_node(Node(2))
            >>> ll.add_node(Node(1))
            >>> ll.print_list()
            2 1 
            >>> ll.tail.data
            1
        """

        if self.head is None:
            self.head = node

        else:
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = node

        self.tail = node

    def print_list(self):
        """Print list as space-separated data."""

        curr = self.head

        while curr:
            print(curr.data, end=' ')
            curr = curr.next

        print()

    def pivot(self, pivot):
        """Pivot list around value."""

        ll1 = LinkedList()
        ll2 = LinkedList()

        current = self.head
        while current != None:
            if current.data < pivot:
                ll1.add_data(current.data)
            else:
                ll2.add_data(current.data)

        ll1.tail.next = ll2.head

        #From HB answer
        # Fix this list to use a and b
        self.head = a.head
        self.tail = b.tail


