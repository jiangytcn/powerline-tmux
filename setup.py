import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="powerline-tmux",
    version="0.0.1",
    author="Yitao Jiang",
    author_email="jiangyt.cn@gmail.com",
    description=("An collection setting for powerline in conjunction with powerline."),  # pylint: disable=line-too-long
    license="MIT",
    keywords="pownerline tmux segments",
    url="http://packages.python.org/an_example_pypi_project",
    packages=['segments', 'segments/tmux'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
