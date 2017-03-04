status = False
token = None
def function():
    global status
    global token


    if token:
        print(token)
    else:
        print("none")


function()