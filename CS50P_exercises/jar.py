class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        self.size = self.size + n

    def withdraw(self, n):
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Invalid capacity")
        self._capacity = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value < 0 or value > self._capacity:
            raise ValueError("Invalid number of cookies")
        self._size = value

def main():
    jar=Jar(10)
    jar.deposit(5)
    print(jar)
    jar.withdraw(7)
    print(jar)

if __name__=="__main__":
    main()
