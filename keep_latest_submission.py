import os
import re
import time
import shutil

folder_path = "/Users/evermal/Downloads/COMP248-P-2"

try:
    submission_folder_regex = '.*([0-9]{8}).*([0-9]{4})\-([A-z]{3})\-([0-9]{1,2})\-(\d{1,2})h(\d{1,2})m(\d{1,2})s(\d{1,3})ms'

    # walk the folder to select the latest submission
    for root, dirs, files in os.walk(folder_path):
        
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
                    # treat day because to have always 2 numbers
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
                            latest_submission = current_submission
                            previous_directory = absolute_subdirname
                        else :
                            shutil.rmtree(absolute_subdirname)
                    else:
                        latest_student_id = None
                        latest_submission = None
                        previous_directory = None

except Exception, e:
    raise e
finally:
    pass