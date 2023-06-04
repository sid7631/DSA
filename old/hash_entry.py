class HashEntry:
    def __init__(self, key, data) -> None:
        # key of the entry
        self.key = key
        # data to be stored
        self.value = data
        # reference to the new entry
        self.next = None
    
    def __str__(self) -> str:
        return str(self.key) + ", " + self.value