import types
import inspect
from oak.Support import Singleton


class ContainerTwo(Singleton):

    _bindings = {}

    _instances = {}

    def bind(self, abstract, concrete, shared=False):

        self._bindings.update({
            abstract: {
                'concrete': concrete,
                'shared': shared,
            }
        })

    def instance(self, abstract, instance):
        self._instances[abstract] = instance

    def singleton(self, abstract, concrete):
        self.bind(abstract, concrete, True)

    def make(self, abstract):

        # 1. If the type has already been resolved as a singleton, just return it
        if(abstract in self._instances):
            return self._instances[abstract]

        # 2. Get the registered concrete resolver for this type, otherwise we'll assume we were passed a concretion that we can instantiate
        concrete = self._bindings.get(abstract, abstract)

        if concrete != abstract:
            concrete = concrete['concrete']

        # 3. If the concrete is either a closure, or we didn't get a resolver, then we'll try to instantiate it.
        if type(concrete) == types.FunctionType or concrete == abstract:
            obj = self.build(concrete)

        # 4. Otherwise the concrete must be referencing something else so we'll recursively resolve it until we get either a singleton instance, a closure, or run out of references and will have to try instantiating it.
        else:
            obj = self.make(concrete)

        # 5. If the class was registered as a singleton, we will hold the instance so we can always return it.
        if abstract in self._bindings:

            if self._bindings[abstract].get('shared', False):
                self._instances[abstract] = obj

        return obj

    def build(self, concrete):

        if type(concrete) == types.FunctionType:
            return concrete()

        if inspect.isclass(concrete):

            signature = inspect.signature(concrete)

            if signature.empty():
                return concrete()

            else:
                print('has a sign')
                quit()

    def flush(self):
        self._bindings = {}
        self._instances = {}
