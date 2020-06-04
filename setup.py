import fnmatch
from setuptools import find_packages, setup, Extension
from setuptools.command.build_py import build_py
from Cython.Build import cythonize
from Cython.Build import build_ext

from pathlib import Path
import shutil

extensions = [
    Extension('app.models.people', ['app/models/people.py'], language='c++'),
    Extension('app.python_example', ['app/python_example.py'], language='c++'),
]

cython_excludes = ['**/__init__.py']

class CustomBuild(build_ext):
    def run(self):
        build_ext.run(self)

        build_dir = Path(self.build_lib)
        root_dir = Path(__file__).parent

        target_dir = build_dir if not self.inplace else root_dir

        self.copy_file(Path('app') / 'main.py', root_dir, target_dir)

    def copy_file(self, path, source_dir, destination_dir):
        if not (source_dir / path).exists():
            return

        print(f'copy file {path} to {destination_dir}')
        shutil.copyfile(str(source_dir / path), str(destination_dir / path))

setup(
    name='app',
    version='0.1.0',
    author='Jefferson Kwak',
    packages=find_packages(exclude=('*tests',)),
    build_dir="build",
    ext_modules=cythonize(extensions, exclude=cython_excludes),
    cmdclass=dict(
        build_ext=CustomBuild
    ),
)