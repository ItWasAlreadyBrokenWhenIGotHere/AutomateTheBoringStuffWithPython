# Document Handling

Example scripts of document handling activities

---

## Prerequisites

Installation of following modules are required in this section:
```console
pip install openpyxl
pip install PyPDF2
pip install python-docx
pip install docx
```

openpyxl is used to interact with Excel workbooks
```python
import openpyxl
```

PyPDF2 module is used to interact with PDF documents
```python
import PyPDF2
```

python-docx is used to interact with Word documents
```python
import python-docx
```


---


## Other notes

If you need to install Python virtual environment manually, you need to install it using pip:
```console
pip install virtualenv
```

Once virtual environment is installed, you can create new virtual environment by executing following command in project directory:
```console
python -m venv virtual
```

To install packages to virtual environment python, for example Flask:
```console
./virtual/Scripts/pip install send2trash
```

To create requirement.txt file, use following command:
```console
pip freeze > requirement.txt
```