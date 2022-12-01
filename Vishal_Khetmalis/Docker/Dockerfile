FROM python
WORKDIR /D:/Vishal/Professional/Infobell IT/Infobell-Openshift-Daily-Work/Vishal_Khetmalis/Docker
COPY app.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
#CMD streamlit run app.py