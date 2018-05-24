import datetime

def get_screenshot_file_path():
    base_path ="./screenshot"
    timestamp = datetime.datetime.today().strftime("%Y-%m-%d_%H:%M:%S.%f")
    filename = "screenshot"
    filetype = "png"
    return "{}/{}_{}.{}".format(base_path, timestamp, filename, filetype)

def get_user_info():
    email = "nerocube.tw@gmail.com"
    password = "mypassword"
    return {"email":email, "password":password}

def mockup_answer():
    answers = []
    answer1 = 'answer'
    answers.append(answer1)
    return answers

def mockup_headers():
    headers = {'Content-Type':'application/json', 'Authorization': 'Token {}'.format("token")}
    return headers

def mockup_test_info():
    base_url = "base_url"
    api_url = "api_url"
    flag_login_success = "flag_login_success"
    return {"base_url":base_url, "api_url":api_url, "flag_login_success":flag_login_success}

