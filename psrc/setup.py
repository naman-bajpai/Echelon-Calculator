from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(name='pf_impl',
      version='1.0',
      ext_modules = cythonize(Extension("p5_impl", ["psrc/cimpl.pyx"],
                                        include_dirs=["src/."],
                                        extra_compile_args = ["-O0"],
                                        )))
