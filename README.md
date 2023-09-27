## Installation

1. Install Python

2. Create and activate your virtual environment following the [instructions](https://docs.python.org/3/tutorial/venv.html)

3. Install the `requirements.txt` dependencies using the commands:
```
cd ./scada_system
pip install -r requirements.txt
```

4. Install the package in editable mode:
```
pip install -e .
```

4. To generate documentation in HTML format, you need to run the following commands:
```
cd ./docs
make html
```
