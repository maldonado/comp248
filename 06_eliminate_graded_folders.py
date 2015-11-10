import sys
import os
import re
import time
import shutil
import codecs
import subprocess
import pexpect
import sys
from xlwings import Workbook, Sheet, Range, Chart
# from PDFWriter import PDFWriter

graded_folder_path = "/Users/evermal/Downloads/marked_files copy/COMP248-Q-2"
student_id_regex = '.*([0-9]{8}).*'

# open nem workbook to work with
professors_workbook = Workbook('/Users/evermal/Documents/COMP248-Assigment2/examples/newCOMP248_Q_F2015_GradeSheet for A2.xlsx')

# go through each line of the table
for x in xrange(7,101):
    # set the profesors spreedsheet as current workbook
    professors_workbook.set_current()
    student_id_cell = str(Range('B'+str(x)).value)
    if student_id_cell is not None:
        student_id_matcher = re.match(student_id_regex, student_id_cell)
        if student_id_matcher is not None:
            student_id = student_id_matcher.group(1)
            # print student_id


            for root, dirs, files in os.walk(graded_folder_path):
                for d in dirs:
                    directory_to_remove = os.path.join(root, d)
                    # regex to eliminate unwanted folders, like third party libraries and invisible files   
                    
                    if student_id in directory_to_remove:
                       
                        print directory_to_remove
                        shutil.rmtree(directory_to_remove)
                    # else:
                    #     directory_to_keep =  os.path.join(root, d)