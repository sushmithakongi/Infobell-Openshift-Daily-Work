FROM python
WORKDIR /D:/Vishal/Professional/Infobell IT/Infobell-Openshift-Daily-Work/Vishal_Khetmalis/Docker/DB
COPY python_to_postgres.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python","./python_to_postgres.py"]
