FROM alpine:3.17
ARG TEXT_TOOL=grep  # sed ("s/old/new/  "), awk (no such package)
RUN apk add --no-cache $TEXT_TOOL
COPY process.sh /home/myuser/app/process.sh
WORKDIR /home/myuser/app/
RUN chmod +x process.sh  
VOLUME /data
ENV TEXT_TOOL=$TEXT_TOOL
CMD ["/home/myuser/app/process.sh", "/data/input.txt"]

# ARG can be passed in CMD through ENV (not visible by)
