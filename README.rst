README
======

Getting started
---------------

* Install Python3 and Sphinx
* Run the make task to build the static site: ``make website``
* Run the Python webserver: ``make server``

Installing Python3 and Sphinx on MacOS X
________________________________________

Follow these steps (works for me™):

* Install Python 3 through your package manager: ``brew install python3``
* easy_install pip: ``/usr/local/share/python3/easy_install pip``
* Symlink installed pip to pip3: ``ln -s /usr/local/share/python3/pip /usr/local/bin/pip3``
* Use pip3 to install Sphinx (this will also pull down the correct version of Jinja2): ``pip3 Sphinx``
