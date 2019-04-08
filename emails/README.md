# File handling with Python

Example scripts of different kind of file handling operations in Python

---

## Prerequisites

Install following module:
```console
pip install imapclient
pip install pyzmail36
```

smtplib is used while connecting to SMTP server which is used for sending emails
```python
import smtplib
```

imapclient is used to fetch emails in raw message format from server
```python
import imapclient
```

pyzmail36 (this might be deprecated module) is used parse email to more readable form
```python
import pyzmail36
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