from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


ext_modules = [
    Extension("models.people",  ["models/people.py"]),
    Extension("python_example",  ["python_example.py"])
]

setup(
    name = 'people',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)