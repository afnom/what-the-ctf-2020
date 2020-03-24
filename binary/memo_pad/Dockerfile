FROM ubuntu

RUN apt-get update
RUN apt-get install -y nmap

WORKDIR /tmp

COPY memo_pad ./
COPY flag ./

EXPOSE 4000
CMD ncat -l -k -p 4000 -e ./memo_pad
