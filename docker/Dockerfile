FROM ubuntu:16.04
LABEL developer="Wes Young <wes@csirtgadgets.com>"

EXPOSE 5000

COPY entrypoint /
COPY GeoIP.conf /etc/

RUN apt-get update
RUN apt-get install -y geoipupdate python3-dev python3-pip python-setuptools python-pip build-essential
RUN geoipupdate -v

RUN easy_install distribute
RUN pip3 install pendulum==1.4.2
RUN pip3 install csirtg_predict_api

ENTRYPOINT ["python3"]
CMD ["/usr/local/bin/csirtg-predictd", "--listen", "0.0.0.0"]