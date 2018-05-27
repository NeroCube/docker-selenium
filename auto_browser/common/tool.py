import datetime, requests, os

def get_screenshot_file_path(filename="screenshot", filetype="png"):
    base_path = "./screenshot"
    timestamp = datetime.datetime.today().strftime("%Y-%m-%d_%H:%M:%S.%f")
    return "{}/{}_{}.{}".format(base_path, timestamp, filename, filetype)

def mockup_user():
    user = {}
    user['email'] = "nerocube.tw@gmail.com"
    user['password'] = "mypassword"
    return user

def mockup_headers(content_type="application/json", token):
    headers = {'Content-Type':content_type, 'Authorization': 'Token {}'.format(token)}
    return headers

def mockup_configs():
    configs = {}
    configs['base_url'] = "base_url"
    configs['api_url'] = "api_url"
    configs['auth_url'] = "auth_url"
    configs['flag_login_success'] = "zEWidget-launcher"
    return configs

