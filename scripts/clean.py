import os
import shutil

print("Cleaning up the report directory")

def handler(func, path, exc_info):
	print("Error : ")
	print(exc_info)

location = "report/"
dir = "mypy/*"
path = os.path.join(location, dir)
shutil.rmtree(path,onerror=handler)

dir = "flake8/*"
path = os.path.join(location, dir)
shutil.rmtree(path,onerror=handler)

print("Done!")
