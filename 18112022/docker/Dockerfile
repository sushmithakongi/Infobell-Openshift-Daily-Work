FROM python
COPY . .
RUN pip install mysql-connector-python
RUN pip install tk 
RUN from PIL import Image,ImageTk
RUN from tkinter import*
RUN from tkinter import ttk
RUN from tkinter import ttk
RUN !apt-get install -y xvfb
RUN import os
CMD ["python", "project.py"]
