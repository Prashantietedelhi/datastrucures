class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def insert(self, root, val):
        if root==None:
            return Node(val)
        temp = root
        while root.next!=None:
            root = root.next

        root.next = Node(val)
        return temp

    def print_ll(self, root):
        while root!=None:
            print(root.val)
            root = root.next
    def reverse(self, root):
        temp = None
        next = None
        while root!=None:
            next = root.next
            root.next = temp
            temp = root
            root = next

        return temp

    def reverse_recur(self, root):
        if root ==None:
            return None

        if root.next ==None:
            # temp = root
            return root

        second  = root.next
        root.next = None
        third = self.reverse_recur(second)
        second.next = root

        return third



    def print_reverse(self, root):
        if root ==None:
            return None

        self.print_reverse(root.next)
        print(root.val)
    def merge_two_sorted(self, root1,root2):
        result =None
        if root1==None:
            return root2
        if root2==None:
            return root1
        if root1.val <root2.val:
            result  = root1
            result.next = self.merge_two_sorted(root1.next, root2)
        else:
            result = root2
            result.next = self.merge_two_sorted(root1, root2.next)
        return  result

    def reverse_pair(self, root):
        if root==None:
            return None
        if root.next ==None:
            return root
        temp = root.next
        root.next = self.reverse_pair(temp.next)
        temp.next = root
        return temp

    def reverse_k(self, root, k):
        if root==None:
            return None
        if root.next ==None:
            return root
        temp = root
        i=0
        while temp.next!=None and i<k-1:
            temp =temp.next
            i=i+1
        nextblock = temp.next
        temp.next = None
        third = self.reverse(root)
        root.next = self.reverse_k(nextblock, k)
        return third
if __name__ =="__main__":
    ll = LinkedList()
    root = None
    root=ll.insert(root, 10)
    root=ll.insert(root, 20)
    root=ll.insert(root, 30)
    root=ll.insert(root, 40)
    root=ll.insert(root, 50)
    root=ll.insert(root, 60)

    root2 = None
    root2 = ll.insert(root2, 15)
    root2 = ll.insert(root2, 25)
    root2 = ll.insert(root2, 35)
    root2 = ll.insert(root2, 45)
    root2 = ll.insert(root2, 55)
    root2 = ll.insert(root2, 65)
    # ll.print_ll(root)
    # root = ll.reverse_recur(root)
    # ll.print_reverse(root)
    # root3 = ll.merge_two_sorted(root,root2)
    # ll.print_ll(root3)
    root = ll.reverse_k(root,4)
    ll.print_ll(root)