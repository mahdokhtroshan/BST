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
        
        
    def Delete(self , data):
        if data < self.data:
            if self.left:
                self.left = self.left.Delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.Delete(data)
        else:
            if self.left and self.right:
                mini = self.right.Minimum()
                self.data = mini
                self.right = self.right.Delete(mini)
            elif self.left:
                return self.left
            elif self.right:
                return self.right
            else:
                return None
            return self
        
    
    

            
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
        
    def Delete(self ,value):
        if self.root:
            self.root = self.root.Delete(value)
            
    def FindNext(self):
        pass
    def FindPre(self):
        pass
    
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

    
bst = BinarySearchTree()
bst.insert(10)
bst.insert(12)
bst.insert(8)
bst.insert(6)



#k = 2
#thelargest = bst.k_thelargest(k)
#print("{k The largest is :}")

#heap = MaxHeap(k)
#for n in thelargest:
    #heap.InsertMaxHeap(n)
    
#print("MaxHeap array is :" , heap.arr[:heap.heapsize])


     

while True:
    
    
    print("1.insert a node")
    print("2.find the next node")
    print("3.find the previous node")
    print("4.delete a node")
    print("5.merge 2 bst's")
    print("6.put max in maxheap")
    bst = BinarySearchTree()


    
    choice = int(input("what would you like to do?"))
    
    #if choice == 0:
        #bst.inorder_treewalk()
        
    #elif choice == 1:
           #data = input("Enter a node to Add :")
           #bst.insert(data)
              
    #elif choice == 2:
        #data = input("Enter a node to find the next :")
        #bst.find_next(data)
        
    #elif choice == 3:
        #data = input("Enter a node to find the previous :")
        #bst.find_pre(data)
        
    #elif choice == 4:
        #data = input("Enter a node to delete :")
        #bst.Delete(data)
        
    #elif choice == 5:
         
    #elif choice == 6:
        #k = input("Enter a number to create a MaxHeap :")
        #bst.k_thelargest(k)
        #heap.InsertMaxHeap(k)
        
    #else:
        #print("Error")
           
    
        
        
  

    

              
                
           

      

    
    