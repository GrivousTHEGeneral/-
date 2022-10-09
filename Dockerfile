FROM python:3-onbuild

RUN pip install numpy

CMD ["python", "./HW1.py"]
