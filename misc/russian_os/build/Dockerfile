FROM ubuntu:16.04

# Expose port for shell
EXPOSE 1111

# Install requirements
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "python3", "python3-pip", "sudo", "-y"]
RUN ["pip3", "install", "colorama"]

# Create groups for privesc
RUN ["groupadd", "officers"]
RUN ["groupadd", "comrades"]

# Create user comrade and add to comrades group
RUN ["useradd", "comrade"]
RUN ["usermod", "-a" , "-G", "comrades", "comrade"]

# Make some aliases
RUN mkdir /home/comrade/
RUN touch /home/comrade/.bashrc
RUN echo "alias ll='ls -alF'" >> /root/.bashrc
RUN echo "alias la='ls -A'" >> /root/.bashrc

# Copy files accross
COPY russia.py /home/comrade/
COPY wisdom.py /usr/bin/wisdom
COPY wisdom /home/comrade/wisdom
COPY flag.txt /home/comrade/flag.txt

# Setup permissions
RUN ["chgrp", "officers", "/home/comrade/flag.txt"]
RUN ["chmod", "070", "/home/comrade/flag.txt"]
RUN ["chgrp", "officers", "/usr/bin/wisdom"]

RUN ["cp", "/usr/bin/head", "/opt/head"]
RUN ["chgrp", "officers", "/opt/head"]
RUN ["chmod", "g+s", "/opt/head"]

RUN ["chgrp", "comrade", "/home/comrade/"]
RUN ["chmod", "g+w", "/home/comrade/"]

ENV quotes_file /home/comrade/wisdom

USER comrade
CMD echo "server running"
CMD ["/home/comrade/russia.py"]
