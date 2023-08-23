import os

# creates necessary directories
try:
    os.mkdir("./img")
    os.mkdir("./log")
except Exception as e:
    print(e)
