pitmon
======

**pitmon** is a monitor application for the
[BBQ Guru CyberQ WIFI controller](http://www.thebbqguru.com).
pitmon is written in Python and Javascript using D3 to show a nice
chart of each cook. **pitmon** is still being developed, so please don't rely on
it yet for critical information. However, I have been using it to monitor my
cooks - below is a real screenshot from one of them.

![pitmon.png](https://raw.githubusercontent.com/scotte/pitmon/master/static/pitmon.png)

Status
======
Still very much a prototype.

TODO:
* Add configuration - UI for settings, and persist/load on server side
* Historical data save/load
* UI to Update cook related cyberq settings (setpoints, alarms)
* Start/stop UI polling of backend
* Adjustable data point timing

Dependencies
============

I develop and deploy pitmon on Debian Linux. It should work
on other Linux distributions without any problem.

Since Python is portable, this should work on other O/S as well but likely
require some code changes in it's current state - pull requests are welcome.

pitmon requires the following dependencies:

* [CyberQInterface](https://github.com/thebrilliantidea/CyberQInterface)
    * Copy the 'cyberqinterface' directory (contains three .py files) to the root of this project
* lxml - needed by CyberQInterface (python-lxml Debian package)

Note: Django and related components are no longer required.

Usage
=====

```
server.py [-h] [-p PORT] [-s] [cyberq]

positional arguments:
  cyberq                Cyberq IP address.

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Port for HTTP server (default=8000).
  -s, --simulate        Simulate cyberq (default=false).
```

License
=======

This project is licensed under a GNU General Public License GPLv3 license.
See the LICENSE file in the source repository and/or distribution.

This project includes the following files which are the properties of their
respective owners:

* js/bootstrap.min.js - [bootstrap](http://getbootstrap.com)
* css/bootstrap.min.css - [bootstrap](http://getbootstrap.com)
* js/jquery.min.js - [jquery](https://jquery.com)
* js/d3.v3.min.js - [d3](http://d3js.org)
* js/nv.d3.min.js - [nvd3](http://nvd3.org)
* css/nv.d3.min.css - [nvd3](http://nvd3.org)
