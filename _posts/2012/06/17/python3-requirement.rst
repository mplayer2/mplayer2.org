.. title: Python 3 to be required to compile from sources
.. author: Uoti Urpala

.. abstract

The build system will be changed to use Python 3. This means that you
must have python3 installed to build from git.

.. body

At the moment the scripts in the build wrapper repository use Python
version 2, and the bare player repo itself does not require Python.
I intend to update the scripts in the build wrapper repository from
Python version 2 to version 3, and change the build system in the
player repository to generate some files with python3 (there actually
already are some files that are generated with Python scripts, but
currently they're included in git rather than generated at build
time). This means that a python3 interpreter will be mandatory
requirement to be able to build from git. However, I'll probably make
it possible to build the generated files on a machine with python3
installed and then export a tarball that can be compiled without
Python.
