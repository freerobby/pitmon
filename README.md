pitmon
======

pitmon is a monitor application for the
[BBQ Guru CyberQ WIFI controller](http://www.thebbqguru.com).
pitmon was written in Python as a WSGI app using the Django framework.

Dependencies
============

I develop and deploy pitmon on Debian Linux (Wheezy). It should work
on other Debian-derived Linux distributions without any problem.

Since Python is portable, this should work on other O/S as well - pull
requests are welcome.

pitmon requires the following dependencies:

* [CyberQInterface](https://github.com/thebrilliantidea/CyberQInterface)
    * Copy the 'cyberqinterface' directory (contains three .py files) to the root of this project
* Django (python-django Debian package)
* Matplotlib (python-matplotlib Debian package)
* Gunicorn (gunicorn Debian package)
* lxml - needed by CyberQInterface (python-lxml Debian package)
