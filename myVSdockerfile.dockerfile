FROM ubuntu
COPY /home/tester/test /home/tester/test
CMD [ "python dothat.py -b build -c cli" ]