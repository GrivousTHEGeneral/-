FROM python:3-onbuild
COPY requirements.txt .

RUN pip install numpy
RUN pip install pandas

ENV PATH=/root/.local:$PATH

CMD ["python", "./HW3.py" ]
