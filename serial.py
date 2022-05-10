"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 100):
        """
           Initializes an instance of SerialGenerator. 
           Keeps a record of the original starting number and initializes the first generated number.
        """
        self.seed = start
        self.next = start - 1

    def generate(self):
        """
            Generates the next number in the sequence and prints it.
        """
        self.next += 1
        print(self.next) 

    def reset(self):
        """
            Resets the sequenece back to the starting number.
        """
        self.next = self.seed - 1

