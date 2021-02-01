class Repository(object):

    def __init__(self):
        self.store = store

    def __setitem__(self, key, item):
        self.store[key] = item

    def __getitem__(self, key):
        return self.store[key]

    def __repr__(self):
        return repr(self.store)

    def __len__(self):
        return len(self.store)

    def __delitem__(self, key):
        del self.store[key]

    def clear(self):
        return self.store.clear()

    def copy(self):
        return self.store.copy()

    def has_key(self, k):
        return k in self.store

    def update(self, *args, **kwargs):
        return self.store.update(*args, **kwargs)

    def items(self):
        return self.store.items()

    def keys(self):
        return self.store.keys()

    def values(self):
        return self.store.values()
