import types
import inspect
from oak.Support import Singleton


class ContainerTwo(Singleton):

    _bindings = {}

    def bind(self, abstract, concrete, method=None):

        if method == None:
            self._bindings.update({abstract: concrete})
        else:
            self._bindings.update(
                {abstract: {'provider': concrete, 'method': method}})

    def make(self, abstract):

        concrete = self._bindings.get(abstract, abstract)

        if type(concrete) == types.FunctionType:
            return concrete()

        if inspect.isclass(concrete):
            return concrete()

        if type(concrete) == dict:
            provider = concrete['provider']
            method = concrete['method']
            return getattr(provider(), method)()

    def instance(self):
        pass

    def singleton(self):
        pass
