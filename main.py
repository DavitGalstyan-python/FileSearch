import os, sys
from sys import platform

if platform == "linux" or platform == "linux2":
  if os.getuid() == 0:
    file_or_dir = input("File or Directory [file, dir]: ")
    file_name = input("File or directory name for search: ")
    find_dir = input("Finding directory: ")
    print()
    print("*************************************************************")
    if file_or_dir == "file":
      os.system("find " + find_dir + " -type f" + " -name " + file_name)
    elif file_or_dir == "dir":
      os.system("find " + find_dir + " -type d" + " -name " + file_name)
    print("*************************************************************")
    print()
    print("Process Compileted")
  else:
      print("ERROR: application must be run as root")
else:
    print("Necessarily Linux")
