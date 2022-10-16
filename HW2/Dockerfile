FROM python:3-onbuild
COPY requirements.txt .

RUN pip install numpy

ENV PATH=/root/.local:$PATH

CMD ["python", "./HW2.py" ]
