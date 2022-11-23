FROM python
EXPOSE 8501
WORKDIR /D:/Vishal/Professional/Infobell IT/Infobell-Openshift-Daily-Work/Vishal_Khetmalis/Kubernetes
COPY app.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
#CMD streamlit run app.py