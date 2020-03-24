FROM ubuntu 
 
# install required software
RUN apt-get update && apt-get upgrade -y && \
	apt-get install -y openssh-server python3-minimal

# user management
RUN mkdir /var/run/sshd && \
	useradd -ms /bin/shashell sha && \
	chown -R root:root /home/sha && \
	chmod 555 /home/sha && \
	chmod 3773 /tmp && \
	echo "sha:ilikehashbrowns" | chpasswd

# important files
COPY shashell /bin/shashell
COPY flag.txt /home/sha/

# run the ssh server
RUN chmod -x /etc/update-motd.d/* && \
	truncate -s 0 /etc/legal && \
	rm -f /etc/motd
EXPOSE 22
CMD /usr/sbin/sshd -D
