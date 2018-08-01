# docker-selenium-auto_browser
Front end test automation in docker
## Run service
```
pip3 install -r requirements.txt
python3 auto_browser/test.py
```
## Remove all screenshot
```
rm -fr ./screenshot/*
```

## Run javascript in Selenium
If the element is calendar or attributes is readonly, how to set element value? You can use the function `driver.execute_script` and run javasript in selenium to remove element attribute.

```python
driver.execute_script('document.getElementById("gwt-debug-caStatStartDate").removeAttribute("readonly")')
driver.execute_script('document.getElementById("gwt-debug-caStatStartDate").value = "2018-06-01"')
```
