FROM python:3.8

RUN pip install pyminifier && \
	mkdir /build

WORKDIR /build
COPY anti.py /build
RUN pyminifier --obfuscate --gzip --replacement-length 4 -o anti.min.py anti.py


FROM ubuntu

RUN apt-get update && apt-get upgrade -y && \
	apt-get install -y nmap python3-minimal

RUN useradd -ms /bin/bash anti && \
	chown -R root:root /home/anti

WORKDIR /home/anti/
COPY --from=0 /build/anti.min.py /home/anti
COPY flag.txt /home/anti/

USER anti
EXPOSE 4000
CMD ncat -l -k -p 4000 -c "python3 anti.min.py"
