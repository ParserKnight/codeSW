FROM ubuntu
RUN apt-get update && apt-get install -y python3 
COPY . /home/code
CMD ["python3", "/home/code/script.py", "/home/code/access.log", "/home/code/output.json","--mflip", "--efip", "--eps", "--bytes"]