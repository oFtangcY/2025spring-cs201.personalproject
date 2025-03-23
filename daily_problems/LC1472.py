class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)
        

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.curr.next = new_node
        new_node.prev = self.curr
        self.curr = new_node


    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.curr.prev:
                break

            self.curr = self.curr.prev

        return self.curr.data


    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.curr.next:
                break
            
            self.curr = self.curr.next

        return self.curr.data


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)