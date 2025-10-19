class Name:
    def __init__(self):
        self.first = ""
        self.last = ""

    def set_name(self, first, last):
        self.first = first
        self.last = last

    def get_name(self):
        return str(self)

    def __str__(self):
        return f"{self.first} {self.last}"

    def __hash__(self):
        # Gera um valor de hash a partir dos atributos que identificam o objeto
        return hash(str(self))