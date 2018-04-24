# silver-spork
the FASTEST way to deploy a REST prediction API

# Getting Started
```bash
$ sudo [apt-get|brew|yum] install geoipupdate  # ubuntu16 or later, requires python3
$ sudo geoipupdate -v
$ easy_install distribute
$ pip install -r dev_requirements.txt
$ python setup.py develop
$ csirtg-predictd -d --fdebug
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 974-602-805
```

# Testing
# navigate to http://localhost:5000 or..

$ curl localhost:5000/domain/?q=google.com
{
    "data": "0"
}

$ curl localhost:5000/domain/?q=go0gle.com
{
    "data": "1"
}

$ curl localhost:5000/ip/?q=141.142.164.33
{
    "data": "0"
}

$ curl localhost:5000/ip/?q=122.2.223.242,6  # ip, hour of day observed [optional]
{
    "data": "1"
}
```

# Next steps

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04
