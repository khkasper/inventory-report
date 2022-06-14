from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, items):
        self.items = items
        self.pos = 0

    def __next__(self):
        try:
            item = self.items[self.pos]
        except IndexError:
            raise StopIteration()
        else:
            self.pos += 1
            return item
