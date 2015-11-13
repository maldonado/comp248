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


folder_path = "/Users/evermal/Downloads/comp248.fall2015/P_emad/COMP248-P-2/"

compressed_file_regex = '.*\.zip|.*\.7z|.*\.rar'

# walk the folder to unzip all files
print 'unziping files'
for root, dirs, files in os.walk(folder_path):
    for f in files:
        absolute_file_name = os.path.join(root, f)
        compressed_file_matcher = re.match(compressed_file_regex, absolute_file_name)
        if compressed_file_matcher is not None:
            print absolute_file_name
            subprocess.call(["./unar", "-f", "-q", "-D", absolute_file_name, "-o", root])