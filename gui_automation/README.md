# Mouse and Keyboard handling with Python

Example scripts of GUI automation in Python

---

## Prerequisites

Install following module:
```console
pip install pyautogui
sudo apt-get install scrot (only on Linux)

```

pyautogui is used to interact with GUI elements by using mouse and keyboard
```python
import pyautogui
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