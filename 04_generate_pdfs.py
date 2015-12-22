import sys
import os
import subprocess



folder_path = "/Users/evermal/Downloads/main.COMP248-EE-2"
apple_script_path = "/Users/evermal/git/comp248/xls_to_pdf.scpt"


for root, dirs, files in os.walk(folder_path):
    for f in files:
        if ".xlsx" in f :
            absolute_file_name = os.path.join(root, f).replace('.xlsx', '').replace('/', ':').replace(':Users', 'Users')
            print absolute_file_name
            directory = subprocess.check_output(["osascript", apple_script_path, absolute_file_name])