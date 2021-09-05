from week2_StackADT_v1 import Stack
class NamedStack(Stack):
    '''Represent an stack in which the name of the stack is stored '''
    def __init__(self, name):
        '''(NamedStack, str) -> NoneType
        construct a stack by calling its parent's constructor 
        and then defining the name of the stack'''
        Stack.__init__(self)
        self._name = name 
    def get_name(self):
        '''(NamedStack) -> str
        returns the name of the stack'''
        return self._name
    def __str__(self):
        '''(NamedStack)-> str
        returns a st representing all the items in the stack'''
        result = ""
        for i in range (len(self._stack)):
            result = result + "\n" + str(self.pop())
        return result.strip()
    
def hanoi(n, source="A", destination="B", spare="C"):
    '''(int, str, str, str) -> NoneType

    Print the instruction on how to move the discks in order to solve the 
    problem of the Tower of Hanoi.
    '''
    # base case, where only one disk is available
    if(n == 1):
        print("move ", n , "from" , source, " -> ", destination)
    else:
        hanoi(n-1, source, spare, destination)
        print("move ", n , "from" , source, " -> ", destination)
        hanoi(n-1, spare, destination, source)

# now that we have the instruction on how to move the disks, 
#we actually move the disks using a stack
def hanoi_move(n, source, destination, spare):
    '''(int, Stack, Stack, Stack)
    solves the problem of the tower of hanoi by moving n disks from 
    the source tower to destination '''
    
    # base case: the disk from source should be moved to destination
    if (n == 1):
        destination.push(source.pop())
        print("move ", n , "from" , source.get_name(), " -> ", destination.get_name())
        
    else:
        hanoi_move(n-1, source, spare, destination)
        destination.push(source.pop())        
        print("move ", n , "from" , source.get_name(), " -> ", destination.get_name())
        hanoi_move(n-1, spare, destination, source)
        
        
        
    
if(__name__ == "__main__"):
    hanoi(3)
    print()
    source = NamedStack("A")
    destination = NamedStack("B")
    spare = NamedStack("C")
    for i in range (3, 0, -1):
        source.push(i) 
    hanoi_move(3, source, destination, spare)
    print(destination)
    
