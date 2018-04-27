# silver-spork
the FASTEST way to deploy a REST prediction API

# Getting Started
## References
https://csirtgadgets.com/commits/2018/3/8/hunting-for-suspicious-domains-using-python-and-sklearn  
https://csirtgadgets.com/commits/2018/3/30/hunting-for-threats-like-a-quant  
https://csirtgadgets.com/commits/2018/4/20/predicting-attacks-with-python-and-sklearn  

## The Docker Way

```bash
$ docker run -p 5000:5000 csirtgadgets/csirtg-predictd:latest
```

## The Manual Way

```bash
$ sudo [apt-get|brew|yum] install geoipupdate  # ubuntu16 or later, requires python3
$ sudo cp GeoIP.conf /etc/GeoIP.conf
$ sudo geoipupdate -v
$ easy_install distribute
$ pip3 install -r dev_requirements.txt
$ python3 setup.py develop
$ csirtg-predictd -d --fdebug
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 974-602-805
```

# Testing
Navigate to http://localhost:5000

![](https://user-images.githubusercontent.com/474878/39194869-95eed9e6-47ac-11e8-85b2-b7ee373fd55e.png?raw=true)

Or use curl
```
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

# Deploying in Production

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04
