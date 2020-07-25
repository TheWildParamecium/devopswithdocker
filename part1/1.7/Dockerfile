FROM ubuntu:16.04
WORKDIR /mydir 
COPY myscript.sh .
RUN apt-get update && apt-get install -y curl 
CMD ["/bin/bash" , "myscript.sh"]