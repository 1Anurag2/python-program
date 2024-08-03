class Node():
    def __init__(self,data):
        self.data = data
        self.next_reference = None
class linkedlist():
    def __init__(self):
        self.head = None
    def traversal(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data , end=" -> ")
            current_node = current_node.next_reference
node1 = Node(5)      
node2 = Node(10)
node3 = Node(15)           # creating object of each Node
node4 = Node(20)

link = linkedlist()         # creating object of linkedlist class
link.head = node1
node1.next_reference = node2
node2.next_reference = node3
node3.next_reference = node4

link.traversal()            




# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next_refrence = None
# node1 = Node(5)
# print(node1.data)
# print(node1.next_refrence)
# print(hex(id(node1)))
# print(hex(id(node1.data)))
#  print(hex(id(node1.next_refrence)))
# class linkedlist():
#     def __init__(self):
#         self.head = None
    
#     def travers(self):
#         current_node = self.head
#         while current_node is not None:
#             print(current_node.data , end=" -> ")
#             current_node = current_node.next_refrence
# node1 = Node(5)
# node2 = Node(10)
# node3 = Node(15)
# node4 = Node(20)
# link = linkedlist()
# link.head = node1
# node1.next_refrence = node2
# node2.next_refrence = node3
# node3.next_refrence = node4
# link.travers()
# print()
# print(hex(id(node1.next_refrence)))
# print(hex(id(node2)))

# print(hex(id(node2.next_refrence)))
# print(hex(id(node3)))
        
        