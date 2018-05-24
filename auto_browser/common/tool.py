import datetime

def get_screenshot_file_path():
    base_path ="./screenshot"
    timestamp = datetime.datetime.today().strftime("%Y-%m-%d_%H:%M:%S.%f")
    filename = "screenshot"
    filetype = "png"
    return "{}/{}_{}.{}".format(base_path, timestamp, filename, filetype)

def get_user_info():
    email = "nerocube.tw@gmail.com"
    password = "mypass"
    return {"email":email, "password":password}