# THIS SCRIPT WILL PREPARE THE DIRECTORY STRUCTURE AND FILES NECESSARY TO SUBMIT IN ENCS WEBSITE.
# PRE-CONDITIONS:
# SELECT THE ASSIGNMENT FOLDER TO BE MARKED AND RUN keep_latest_submission.py ON IT.
# EXECUTION:
# RUN THIS SCRIPT IN THE CLEAN ASSIGMENT FOLDER TO DUPLICATE THE FOLDER STRUCTURE AND PUT THE FILES IN THE RIGHT FOLDER
# USED TO FORMATT A1 

import os
import re
import time
import shutil
import subprocess
from subprocess import Popen, PIPE

section = 'COMP248-R-2'
assigment_path = "/Users/evermal/Downloads/COMP248-R-2"
marked_files_path = "/Users/evermal/Downloads/Assignment1FeedbacksOCT_18"

student_id_regex = '.*([0-9]{8}).*'
submission_folder_regex = '.*([0-9]{8}).*([0-9]{4})\-([A-z]{3})\-([0-9]{1,2})\-(\d{1,2})h(\d{1,2})m(\d{1,2})s(\d{1,3})ms'

for assigment_root, dirs, files in os.walk(assigment_path):
    for subdirname in dirs:            
        # get absolute subdirectory name
        absolute_subdirname = os.path.join(assigment_root, subdirname)    
        # match submission folder
        folder_matcher = re.match(submission_folder_regex, absolute_subdirname)
        if folder_matcher is not None:
            
            # create folder to be uploaded
            print absolute_subdirname
            new_absolute_subdirname = absolute_subdirname.replace(section, 'marked_files/'+ section)
            subprocess.call(["mkdir", "-p",new_absolute_subdirname])

            # prepare regex to look to marked file
            student_id_matcher = re.match(student_id_regex, new_absolute_subdirname)
            student_id = student_id_matcher.group(1)
            marked_file_regex = '.*'+student_id+'{1}.*\.pdf'

            # look for marked files with the correspondent student id 
            for marked_root, dirs, files in os.walk(marked_files_path):
                for f in files:
                    absolute_file_name = os.path.join(marked_root, f)
                    file_matcher = re.match(marked_file_regex, absolute_file_name)
                    if file_matcher is not None:
                        # copy marked pdf changing name to match the encs site requeriments
                        print new_absolute_subdirname+"/"+f
                        subprocess.call(["cp", absolute_file_name, new_absolute_subdirname+"/mark.pdf"])