# pdfChatbot

## setup virtual environment
```
virtualenv -p python3 pdf_cb
cd pdf_cb
source bin/activate
```
## Install all requirements

```
pip install -r requirements.txt
```
### Install AutoGPT
```
wget -q https://github.com/PanQiWei/AutoGPTQ/releases/download/v0.4.1/auto_gptq-0.4.1+cu118-cp310-cp310-linux_x86_64.whl
pip install -qqq auto_gptq-0.4.1+cu118-cp310-cp310-linux_x86_64.whl
``` 
### Install poppler-utils
```
sudo apt-get install poppler-utils
``` 
## Run server

```
python manage.py runserver
```
