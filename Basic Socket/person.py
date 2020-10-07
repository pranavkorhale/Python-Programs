class Person:
    def __int__(self, addr, client):
        self.addr = addr
        self.client = client
        #code
        #best
        self.name = None

    def set_name(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.addr},{self.name})"
