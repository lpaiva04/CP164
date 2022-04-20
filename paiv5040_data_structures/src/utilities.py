"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-01-22"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
        
    while len(source) > 0:   
        i = source.pop()
        stack.push(i)   
            
    return

def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while stack.is_empty() == False:
        i = stack.pop()
        target.append(i)
    
    target.reverse()
    
    return 

def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    stack = Stack()

    array_to_stack(stack, source)
    
        
    print (f"Is the stack originally empty?: {stack.is_empty()}")
    print (f"Pushing 6 onto stack: {stack.push(6)}")
    print (f"is_empty on stack with data: {stack.is_empty()}")
    print (f"Value on top of Stack(should be 6): {stack.peek()}")
    print (f"Value to pop from top of stack (should be 6): {stack.pop()}")

    return


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """  
    x = len(source)
    n = 0
    for i in source:
        queue.insert(i)
    
    while n < x:
        source.pop()
        n += 1
    return

        
def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    x = len(queue)
    i = 0
    while i < x:
        n = queue.remove()
        target.append(n)
        i += 1
    
    return
def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()
    print(f"Is it empty?: {q.is_empty()}")
    print(f"insert 7: {q.insert(7)}")
    print(f"insert 7: {q.insert(7)}")
    print(f"remove from front: {q.remove()}")
    print(f"Peek: {q.peek()}")    
    print(f"Length: {len(q)}")
    
    return

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """ 
    x = len(source)
    n = 0
    for i in source:
        pq.insert(i)
    
    while n < x:
        source.pop()
        n += 1
    return
def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    x = len(pq)
    i = 0
    while i < x:
        n = pq.remove()
        target.append(n)
        i += 1
    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    
    print(pq.is_empty())
    print(pq.insert(7))
    print(pq.insert(7))
    print(pq.remove())
    print(pq.peek())

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand

    return

def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    l = len(source)
    while i < l:
        x = source.pop()
        llist.insert(0, x)
        i += 1
        
    return 

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    l = len(llist)
    while i < l:
        x = llist.pop()
        target.insert(0, x)
        i += 1
        
    return
        

def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    print (f"Is empty?: {lst.is_empty()}")
    lst.insert(0, source[0])
    lst.insert(0, source[1])
    lst.insert(0, source[1])
    print (f"Remove from index 0: {lst.remove(source[0])}")
    print (f"Number of occurences of first index: {lst.count(source[1])}")
    lst.append(source[2])
    print (f"Index location of key: {lst.index(source[2])}")
    print (f"Returns value in list that matches key: {lst.find(source[2])}")
    print (f"Max value: {lst.max()}")
    print (f"Min Value: {lst.min()}")

    return
