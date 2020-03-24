FROM node

RUN useradd -ms /bin/bash past
WORKDIR /home/past

COPY main.js package.json yarn.lock flag.txt ./

RUN yarn && \
    echo "echo $(cat flag.txt) > flag.txt\nrm -f flag.txt" > .bash_history && \
    rm flag.txt

USER past
EXPOSE 4000
CMD node main.js
