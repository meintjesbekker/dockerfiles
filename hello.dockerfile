# This is my empty dockerfile to see which editor will open it.
FROM ubuntu:18.04
RUN apt-get update && apt-get install -y
RUN apt-get update && apt-get install python3 -y
VOLUME /test
COPY . /test
WORKDIR /test
# CMD python /test/writehellotofile.py
ENTRYPOINT [ "python3" ]
CMD [ "--version" ]
