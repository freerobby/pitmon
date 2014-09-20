pitmon
======

**pitmon** is a monitor application for the
[BBQ Guru CyberQ WIFI controller](http://www.thebbqguru.com).
pitmon is written in Python and Javascript using D3 to show a nice
chart of each cook. **pitmon** is still being developed and not in a generally
usable state.

![pitmon.png](https://raw.githubusercontent.com/scotte/pitmon/master/static/pitmon.png)

Status
======
Unstable! Still very much a prototype.

TODO:
* Add configuration - UI for settings, and persist/load on server side
* Historical data save/load
* Replace django with a super basic HTTP server, once it's all static content and JSON
* UI to Update cook related cyberq settings (setpoints, alarms)

Dependencies
============

I develop and deploy pitmon on Debian Linux. It should work
on other Debian-derived Linux distributions without any problem.

Since Python is portable, this should work on other O/S as well - pull
requests are welcome.

pitmon requires the following dependencies:

* [CyberQInterface](https://github.com/thebrilliantidea/CyberQInterface)
    * Copy the 'cyberqinterface' directory (contains three .py files) to the root of this project
* Django (python-django Debian package)
* Gunicorn (gunicorn Debian package)
* lxml - needed by CyberQInterface (python-lxml Debian package)

License
=======

This project is licensed under a GNU General Public License GPLv3 license.
See the LICENSE file in the source repository and/or distribution.

This project includes the following files which are the properties of their
respective owners:

* js/bootstrap.min.js - [bootstrap](http://getbootstrap.com)
* css/bootstrap.min.css - [bootstrap](http://getbootstrap.com)
* js/jquery.min.js - [jquery](https://jquery.com)
* js/d3.v3.js - [d3](http://d3js.org)
* js/nv.d3.js - [nvd3](http://nvd3.org)
* css/nv.d3.css - [nvd3](http://nvd3.org)
