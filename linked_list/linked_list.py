from node import LinkedListNode

class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        return self.head is None

    # Insert node at the head
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    # Insert node at the tail
    def insert_at_tail(self, node):
        if self.is_empty():
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    # Get the length of the linked list
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # Delete the head node
    def delete_at_head(self):
        if self.head:
            self.head = self.head.next

    # Delete a node by its value
    def delete(self, data):
        if self.is_empty():
            print("List is Empty")
            return False

        current_node = self.head
        if current_node.data == data:
            self.delete_at_head()
            return True

        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return True
            current_node = current_node.next

        print(f"{data} not found in the list")
        return False

    # Search for a node by its value
    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return temp
            temp = temp.next
        print(f"{data} not found in the list")
        return None

    # Remove duplicate nodes
    def remove_duplicates(self):
        if self.is_empty() or self.head.next is None:
            return

        seen = set()
        current = self.head
        prev = None

        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current

            current = current.next

    # Create a linked list from a given list
    def create_linked_list(self, lst):
        for value in reversed(lst):
            self.insert_at_head(LinkedListNode(value))

    # String representation of the linked list
    def __str__(self):
        elements = []
        temp = self.head
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        return ", ".join(elements)
    
    def print_list_with_forward_arrow(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            if temp:
                print("->", end=" ")
            else:
                print("-> null", end=" ")


#sample to run
def main():
    input = (
            [2, 4, 6, 4, 2],
            [0, 3, 5, 5, 0],
            [9, 7, 4, 4, 7, 9],
            [5, 4, 7, 9, 4, 5],
            [5, 9, 8, 3, 8, 9, 5],
        )
    
    j = 1

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(j, ".\tLinked List:", end=" ", sep="")
        input_linked_list.print_list_with_forward_arrow()
        print('\n',j, ".\tRemoved Duplicate:", end=" ", sep="")
        input_linked_list.remove_duplicates()
        input_linked_list.print_list_with_forward_arrow()
        print('\n')

if __name__ == "__main__":
    main()

