FROM ubuntu

RUN apt-get update
RUN apt-get install -y nmap

WORKDIR /tmp

COPY vuln_actual ./

EXPOSE 4000
CMD ncat -l -k -p 4000 -e ./vuln_actual
