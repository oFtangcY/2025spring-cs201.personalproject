#pre-problem

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self, n):
        self.tail = Node(n)
        self.size = n

        prev = self.tail
        for i in range(1, n):
            prev.next = Node(i)
            prev = prev.next
        prev.next = self.tail

    def delete(self, data):
        prev, nd = self.tail, self.tail.next
        if self.tail.data == data:
            while prev.next != self.tail:
                prev = prev.next
            prev.next = nd
            self.tail = prev
        else:
            while prev.next != self.tail:
                if nd.data == data:
                    prev.next = nd.next
                    break

                prev = nd
                nd = nd.next

        self.size -= 1


while True:
    n, m = map(int, input().split())
    if n== 0 and m == 0:
        exit()

    monkeys = LinkList(n)
    point = monkeys.tail
    while monkeys.size > 1:
        for _ in range(m):
            point = point.next
        monkeys.delete(point.data)

    print(monkeys.tail.data)
