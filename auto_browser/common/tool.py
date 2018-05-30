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

def mockup_headers(token, content_type="application/json", ):
    headers = {'Content-Type':content_type, 'Authorization': 'Token {}'.format(token)}
    return headers

def mockup_payload():
    lines = []
    base_path = "./data"
    file_name = "test_data.txt"
    with open("{}/{}".format(base_path, file_name)) as file:
        for line in file: 
            line = line.strip()
            if not line is "":
                lines.append(line)
    return lines

def mockup_configs():
    configs = {}
    configs['base_url'] = "base_url"
    configs['api_url'] = "api_url"
    configs['auth_url'] = "auth_url"
    configs['flag_login_success'] = "zEWidget-launcher"
    return configs

