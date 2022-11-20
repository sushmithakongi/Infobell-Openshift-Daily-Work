FROM python:3.7
RUN mkdir work1
RUN cd work1
COPY V1.txt V1.txt 
RUN pip install -r V1.txt
WORKDIR /work1
ADD Connection.py .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
