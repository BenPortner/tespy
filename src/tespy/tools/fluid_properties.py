# backend = "coolprop"
backend = "pyromat"

if backend == "coolprop":
    from .fluid_property_backends.coolprop import *
elif backend == "pyromat":
    from .fluid_property_backends.pyromat import *
else:
    raise NotImplementedError(f"Invalid fluid property backend: {backend}.")
