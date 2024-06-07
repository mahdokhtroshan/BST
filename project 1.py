class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        #if data == self.data:
            #raise Exception("data is already exists in the tree")
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def inorder_treewalk(self):
        if self.left:
            self.left.inorder_treewalk()
        print(self.data , end=' ')
        if self.right:
            self.right.inorder_treewalk()
    
            
    def Minimum (self):
        while self.left:
            return self.left.Minimum()
        else:
            return self.data
    def Maximum(self):
        while self.right:
            return self.right.Maximum()
        else:
            return self.data
        
    def FindNext(self):
         if self.right:
             return self.right.Minimum()
    def FindPre(self):
         if self.left:
             return self.left.Maximum() 
        
  
    

            
class BinarySearchTree:
    
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data)  

    def inorder_treewalk(self):
        if self.root is not None:
            self.root.inorder_treewalk()
        else:
            print("Tree is empty")
        
    def delete(self, data):
        if self.root:
            self.root = self.Delete(self.root, data)

    def Delete(self, root, data):
        if root is None:
            return root
        if data < root.data:
            root.left = self.Delete(root.left, data)
        elif data > root.data:
            root.right = self.Delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            x = root.right
            while x.left:
                x = x.left
            root.data = x.data
            root.right = self.Delete(root.right, root.data)
        return root

  
          
    
    def FindNext(self , data):
        current = self.root
        successor = None
        while current:
            if data < current.data:
                successor = current
                current = current.left
            else:
                current = current.right
        return successor.data if successor else None
    
    def FindPre(self , data):
        current = self.root
        predecessor = None
        while current:
            if data > current.data:
                predecessor = current
                current = current.right
            else:
                current = current.left
        return predecessor.data if predecessor else None
        
    def merge(self, otherbst):
        elements = []
        self.InorderElements(self.root, elements)
        self.InorderElements(otherbst.root, elements)
        elements.sort()
        merged_bst = BinarySearchTree()
        for element in elements:
            merged_bst.insert(element)
        return merged_bst
    
    def InorderElements(self, node, elements):
        if node is None:
            return
        self._inorder_elements(node.left, elements)
        elements.append(node.data)
        self.InorderElements(node.right, elements)
        
    def k_thelargest(self, k):
      result = []
      self.Reverse(self.root, result, k)
      return result
  
    def Reverse(self, node, result, k):
        if node is None or len(result) >= k:
            return
        self.Reverse(node.right, result, k)
        if len(result) < k:
            result.append(node.data)
        self.Reverse(node.left, result, k)

    

class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.heapsize = 0
        self.arr = [None] * maxsize
    
    def parent(self, i):
        return (i  // 2)
    
    def Left(self, i):
        return (2 * i )
    
    def Right(self, i):
        return (2 * i + 1)
    
    def InsertMaxHeap(self, x):
        if self.heapsize == self.maxsize:
            print("The heap is full")
            return
        self.heapsize += 1
        i = self.heapsize - 1
        self.arr[i] = x
        
        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
            i = self.parent(i)
    
    def MaxHeapify(self, i):
        largest = i
        L = self.Left(i)
        R = self.Right(i)
        
        if L < self.heapsize and self.arr[L] > self.arr[largest]:
            largest = L
        if R < self.heapsize and self.arr[R] > self.arr[largest]:
            largest = R
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.MaxHeapify(largest)

             
        

#k = 2
#thelargest = bst.k_thelargest(k)
#print("The largest is :" , k)

#heap = MaxHeap(k)
#for n in thelargest:
    #heap.InsertMaxHeap(n)
    
#print("MaxHeap array is :" , heap.arr[:heap.heapsize])

print("1.insert a node")
print("2.find the next node")
print("3.find the previous node")
print("4.delete a node")
print("5.merge 2 bst's")
print("6.put max in maxheap")
    
bst = BinarySearchTree()
while True:
    
    choice = int(input("What would you like to do? "))
    if choice == 1:
        data = int(input("Enter a node to add: "))
        bst.insert(data)
    elif choice == 2:
        data = int(input("Enter a node to find the next: "))
        next_node = bst.find_next(data)
        if next_node is not None:
            print(f"The next node is: {next_node}")
        else:
            print("No next node found")
    elif choice == 3:
        data = int(input("Enter a node to find the previous: "))
        prev_node = bst.find_previous(data)
        if prev_node is not None:
            print(f"The previous node is: {prev_node}")
        else:
            print("No previous node found")
    elif choice == 4:
        data = int(input("Enter a node to delete: "))
        bst.delete(data)
        print("The node has been deleted")
        
    elif choice == 5:
        other_bst = BinarySearchTree()
        n = int(input("Enter the number of nodes for the second BST: "))
        for _ in range(n):
            data = int(input("Enter a node to add to the second BST: "))
            other_bst.insert(data)
        merged_bst = bst.merge(other_bst)
        print("Merged BST ): ", end='')
        merged_bst.inorder_treewalk()
        print()
         
    elif choice == 6:
        k = int(input("Enter the number of largest elements to create a MaxHeap: "))
        the_largest = bst.k_thelargest(k)
        print(f"{k} the largest elements are: {the_largest}")
        heap = MaxHeap(k)
        for n in the_largest:
            heap.InsertMaxHeap(n)
        print("Your MaxHeap Array is: ", heap.arr[:heap.heapsize])
    elif choice == 7:
        print("In-order traversal: ", end='')
        bst.inorder_treewalk()
        print()
    elif choice == 8:
        break
    else:
        print("Invalid Request")
           
    
        
        
  

    

              
                
           

      

    
    

