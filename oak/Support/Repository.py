from collections.abc import MutableMapping


class Repository(MutableMapping):

    def __init__(self):
        self.store = {}

    def __getitem__(self, key):
        return self.store[key]

    def __delitem__(self, key):
        value = self[key]
        del self.store[key]
        self.pop(value, None)

    def __setitem__(self, key, value):
        if key in self:
            del self[self[key]]
        if value in self:
            del self[value]
        self.store[key] = value
        self.store[value] = key

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __repr__(self):
        return f"{type(self).__name__}({self.store})"
