class BoyerMooreMajority:
  def __init__(self):
    self.guess = None
    self.counter = 0

  # Registers another element to be considered by the algorithm. This will
  # influence the majority element guess returned by `get_majority`.
  def add_next_element(self, element):
    assert(element is not None)
    #YOUR CODE HERE

    if self.counter == 0 :
        self.guess = element
        self.counter = 1

    elif self.guess == element:
        self.counter += 1

    else:
        self.counter -= 1

    majority_guess = self.get_majority()

    print("element: {} , counter: {}, majority_guess: {}".format(self.guess, self.counter, majority_guess))

  # Gives the best guess of which of the elements seen so far make up the
  # majority of the elements in set of elements. If a majority element exists,
  # this algorithm will report it correctly. Otherwise, there is no guarantee
  # about the output.
  def get_majority(self):
    #YOUR CODE HERE
    if self.counter >= 0:
        return self.guess
    else:
        return 'something went wrong'
