# WebScraping

Example scripts of Web scraping related activities

---

## Prerequisites

Installation of following modules are required in this section:
```console
pip install pyperclicp
pip install requests
pip install beautifulsoup4
pip install selenium
```

pyperclip is used to paste address from clipboear to browser if address is not provided as input arguments
```python
import pyperclip
```

requests is used to easily download files from the web
```python
import requests
```

beautifulsoup4 is used to parse html code scraped from web page
```python
import bs4
```

selenium is used to control web browsers
```python
from selenium import webdriver
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