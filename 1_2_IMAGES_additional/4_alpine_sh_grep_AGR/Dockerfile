FROM alpine:3.17
ARG TEXT_TOOL=grep  # sed, awk
RUN apk add --no-cache $TEXT_TOOL
COPY process.sh /home/myuser/app/process.sh
WORKDIR /home/myuser/app/
RUN chmod +x process.sh  
VOLUME /data
CMD ["/home/myuser/app/process.sh", "/data/input.txt"]

# "No TEXT_TOOL set, defaulting to grep" ?? always ($TEXT_TOOL is invisible in process.sh?)
