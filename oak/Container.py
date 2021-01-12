from oak.Support import Singleton


class Container(Singleton):

    _bindings = {}

    def bind(self, key, value):

        self._bindings.update({key: value})

        return self

    def resolve(self, key, default=None):

        return self._bindings.get(key, default)
