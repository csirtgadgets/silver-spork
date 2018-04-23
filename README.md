# silver-spork
the FASTEST way to deploy a REST prediction API

```bash
$ sudo [apt-get|brew|yum] install geoipupdate
$ pip install -r dev_requirements.txt
$ python setup.py develop
$ csirtg_predictd -d --fdebug

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

$ curl 'localhost:5000/ip/?q=122.2.223.242,6'  # ip, hour of day observed [optional]
{
    "data": "1"
}

...
```
