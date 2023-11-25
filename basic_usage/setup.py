from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("basic_usage/helloworld.pyx")
)

setup(ext_modules=cythonize('basic_usage/fibonacci.pyx'))