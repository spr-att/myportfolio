from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    self.__dq = get_deque()

  def __str__(self):
    return str(self.__dq)

  def __len__(self):
    return len(self.__dq)

  def push(self, val):
    self.__dq.push_front(val)

  def pop(self):
    pop_val = self.__dq.pop_front()
    return pop_val

  def peek(self):
    peek_val = self.__dq.peek_front()
    return peek_val

# Unit tests make the main section unnecessary.
#if __name__ == '__main__':
#  pass
