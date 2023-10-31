class Queue():
  def __init__(self):
    self.queue = []

  def enqueue(self, item): # Add to a queue
    self.queue.append(item)

  def dequeue(self): # remove the first element of the queue
    return self.queue.pop(0)
  
  def vwqueue(self): # Made up method to view the queue. You cannot typically view the queue
    print(self.queue)


myQueue = Queue()

myQueue.enqueue(6)
myQueue.enqueue(1)

myQueue.vwqueue()
print(myQueue.dequeue())