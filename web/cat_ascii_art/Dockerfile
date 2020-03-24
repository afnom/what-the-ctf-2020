#docker build ./ --tag cat_ascii_art
#docker run cat_ascii_art
#docker kill cat_ascii_art

FROM python:3.8

RUN pip3 install flask

RUN apt-get update && apt-get upgrade -y && \
	apt-get install -y python3-minimal

WORKDIR /home/
ADD website /home/website/

WORKDIR /home/website/
EXPOSE 4000
CMD python3 app.py
