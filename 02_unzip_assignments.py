import sys
import os
import re
import time
import shutil
import codecs
import subprocess
import pexpect
from subprocess import Popen, PIPE
from xlwings import Workbook, Sheet, Range, Chart

root_path  = '/Users/evermal/Downloads/'
folder_path_list = ["COMP248-P-2", "COMP248-Q-2", "COMP248-R-2"]

compressed_file_regex = '.*\.zip|.*\.7z|.*\.rar'

# walk the folder to unzip all files
print 'unziping files'
for folder_path in folder_path_list:
    print 'processing' + folder_path

    for root, dirs, files in os.walk(root_path+folder_path):
        for f in files:
            absolute_file_name = os.path.join(root, f)
            compressed_file_matcher = re.match(compressed_file_regex, absolute_file_name)
            if compressed_file_matcher is not None:
                print absolute_file_name
                subprocess.call(["./unar", "-f", "-q", "-D", absolute_file_name, "-o", root])