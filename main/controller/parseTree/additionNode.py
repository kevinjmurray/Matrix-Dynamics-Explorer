from .node import Node
import numpy as np

# AdditionNode is a subclass of Node 
class AdditionNode(Node):

    def getVal(self, x):
        leftVal, rightVal = 0, 0
        if self.left != None:
            leftVal = self.left.getVal(x)

        if self.right != None:
            rightVal = self.right.getVal(x)

        if type(leftVal) != np.ndarray and type(rightVal) != np.ndarray:
            return leftVal + rightVal
        
        if type(leftVal) != np.ndarray:
            leftVal = np.multiply(leftVal, np.identity(n=x.shape[0]))

        if type(rightVal) != np.ndarray:
            rightVal = np.multiply(rightVal, np.identity(n=x.shape[0]))

        return np.add(leftVal, rightVal)
    
    def __str__(self):
        return '+'
    
    def insertInOrder(self, queue, level):
        queue.append([self.left, level+1])
        queue.append([self.right, level+1])
        

