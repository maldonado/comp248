import os
import re
import time
import shutil
import subprocess
from subprocess import Popen, PIPE



    

try:
    # student_id_regex = '([0-9]{8})'
    # student_name_regex = '(?:-([a-z\_]{2,8}))'
    # assignement_date_regex = '([0-9]{4})\-([A-z]{3})\-([0-9]{1,2})\-(\d{1,2})h(\d{1,2})m'

    submission_folder_regex = '.*([0-9]{8}).*([0-9]{4})\-([A-z]{3})\-([0-9]{1,2})\-(\d{1,2})h(\d{1,2})m(\d{1,2})s(\d{1,3})ms'
    wrong_submission_file_regex = '.*\.README'

    folder_path = "/Users/evermal/Downloads/COMP248-P-2/"
    # walk the folder to remove unwanted files and folders (invisible files and third party) 
    for root, dirs, files in os.walk(folder_path):
        # print root
    
        # print dirs

        # select latest submission of student 
        latest_student_id = None
        latest_submission = None
        previous_directory = None
        for subdirname in dirs:
            # get absolute subdirectory name
            absolute_subdirname = os.path.join(root, subdirname)    
            # match submission folder
            match = re.match(submission_folder_regex, absolute_subdirname)
            if match is not None:
                if latest_student_id is None:
                    latest_student_id = match.group(1)
                    year  =  match.group(2)
                    month =  match.group(3)
                    day   =  match.group(4)
                    # treat day because to have alweys 2 numbers
                    if day == '1':
                        day = '01'
                    if day == '2':
                        day ='02'
                    if day == '3':
                        day = '03'
                    if day == '4':
                        day = '04'
                    if day == '5':
                        day = '05'
                    if day == '6':
                        day = '06'
                    if day == '7':
                        day = '07'
                    if day == '8':
                        day = '08'
                    if day == '9':
                        day = '09'
                    hour  =  match.group(5)
                    minute = match.group(6)
                    second = match.group(7)
                    latest_submission = time.strptime(year+month+day+hour+minute+second , "%Y%b%d%H%M%S")
                    previous_directory = absolute_subdirname

                else:
                    if latest_student_id == match.group(1):
                        year  =  match.group(2)
                        month =  match.group(3)
                        # treat day because to have alweys 2 numbers
                        day   =  match.group(4)
                        if day == '1':
                            day = '01'
                        if day == '2':
                            day ='02'
                        if day == '3':
                            day = '03'
                        if day == '4':
                            day = '04'
                        if day == '5':
                            day = '05'
                        if day == '6':
                            day = '06'
                        if day == '7':
                            day = '07'
                        if day == '8':
                            day = '08'
                        if day == '9':
                            day = '09'
                        hour  =  match.group(5)
                        minute = match.group(6)
                        second = match.group(7)
                        current_submission = time.strptime(year+month+day+hour+minute+second , "%Y%b%d%H%M%S")
                        if current_submission > latest_submission :
                            shutil.rmtree(previous_directory)
                        else :
                            shutil.rmtree(absolute_subdirname)
                    else:
                        latest_student_id = None
                        latest_submission = None
                        previous_directory = None

        for f in files:
            absolute_file_name = os.path.join(root, f)
            print absolute_file_name
            if re.match(wrong_submission_file_regex, absolute_file_name) is not None:
                os.unlink(absolute_file_name)
        
            subprocess.call(["unzip", "-u", "-o",  absolute_file_name, "-d", root])
                    
                
        
        # for d in dirs:
        #     match = re.match(student_id_regex, d)
        #     if match is not None:
        #         student_id = match.group(1)
        #         print student_id


            #     shutil.rmtree(os.path.join(root, d))
    # output = subprocess.Popen(['java -mx6144m -jar stanford-classifier.jar -prop '+path_to_store_data+'/dataset.prop -1.useSplitWords -1.splitWordsRegexp "\s"'], stdout=PIPE, stderr=PIPE, shell=True).communicate()
except Exception, e:
    raise e
finally:
    pass

