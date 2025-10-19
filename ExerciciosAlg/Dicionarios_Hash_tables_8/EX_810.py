class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def get_first(self):
        return self.first

    def get_second(self):
        return self.second

    def __hash__(self):
        return hash(self.first) + hash(self.second)
    
    def __eq__(self, other):
        if other is None or type(self) is not type(other):
            return False
        return self.first == other.first and self.second == other.second