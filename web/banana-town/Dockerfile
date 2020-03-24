FROM ubuntu:18.04

RUN apt-get update && \
    apt-get -y install nginx openssl

COPY crypt /etc/nginx/

COPY deploy/nginx /etc/nginx/sites-available/wt.ctf
RUN ln -sf /etc/nginx/sites-available/wt.ctf /etc/nginx/sites-enabled/ && \
    rm /etc/nginx/sites-enabled/default

RUN mkdir -p /var/www/wt.ctf
COPY site /var/www/wt.ctf/

EXPOSE 80
EXPOSE 443
CMD nginx -g "daemon off;";
