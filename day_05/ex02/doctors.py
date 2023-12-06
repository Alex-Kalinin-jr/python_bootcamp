import threading


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class RingLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def get(self, index):
      if self.head is None:
          return None
      current = self.head
      for i in range(index):
          current = current.next
      return current.data


class ScrewDriver:
  def __init__(self):
    pass


class Doctor:
  def __init__(self, id):
    self.id = id
    self.left_hand = ScrewDriver()
    self.right_hand = None
    self.lock = threading.Lock()
    self.state = False


  def grab_left(self, left_doctor):
    self.left_hand = left_doctor.right_hand
    left_doctor.right_hand = None

  def grab_right(self, right_doctor):
    self.right_hand = right_doctor.left_hand
    right_doctor.left_hand = None

  def grab(self, left_doctor, right_doctor):
    self.acquire()
    if self.state == False:
      if self.right_hand == None:
        self.grab_right(right_doctor)
      elif self.left_hand == None:
        self.grab_left(left_doctor)
    self.release()

  def blast(self):
    if self.left_hand and self.right_hand:
      self.state = True
      print(f"Doctor {self.id}: BLAST!")

  def acquire(self):
    self.lock.acquire()

  def release(self):
    self.lock.release()

def run_blast(doctors, i):
    while doctors.get(i).state == False:
      doctors.get(i).grab(doctors.get(i - 1), doctors.get(i + 1))
      doctors.get(i).blast()


def main():
  threads = []
  doctors = RingLinkedList()

  for i in range(9, 14):
    doctors.add(Doctor(i))
    thread = threading.Thread(target=run_blast, args=(doctors, i))
    threads.append(thread)

  [thread.start() for thread in threads]
  [thread.join() for thread in threads]

if __name__ == "__main__":
  main()