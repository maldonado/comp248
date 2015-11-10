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

graded_folder_path = "/Users/evermal/Downloads/COMP248-Q-2"
student_id_regex = '.*([0-9]{8}).*'

# Create a connection with a new workbook.
template_workbook = Workbook('/Users/evermal/Documents/COMP248-Assigment2/examples/COMP248_Q_F2015_GradeSheet for A2.xlsx')
template_workbook.save('/Users/evermal/Documents/COMP248-Assigment2/examples/newCOMP248_Q_F2015_GradeSheet for A2.xlsx')
template_workbook.close()

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
            print student_id
            for root, dirs, files in os.walk(graded_folder_path):
                for f in files:
                    if f == student_id+'.xlsx':
                        absolute_file_name = os.path.join(root, f)
                        print absolute_file_name
                        graded_workbook = Workbook(absolute_file_name)
                        graded_workbook.set_current()
                        a1 = str(Range('B8').value)
                        a2 = str(Range('B9').value)
                        a3 = str(Range('B10').value)
                        b1 = str(Range('B12').value)
                        b2 = str(Range('B13').value)
                        c1 = str(Range('B15').value)
                        c2 = str(Range('B16').value)
                        c3 = str(Range('B17').value)
                        c4 = str(Range('B18').value)
                        c5 = str(Range('B19').value)
                        c6 = str(Range('B20').value)
                        graded_workbook.close()

                        professors_workbook.set_current()
                        Range('E'+str(x)).value = a1
                        Range('F'+str(x)).value = a2
                        Range('G'+str(x)).value = a3
                        Range('H'+str(x)).value = b1
                        Range('I'+str(x)).value = b2
                        Range('J'+str(x)).value = c1
                        Range('K'+str(x)).value = c2
                        Range('L'+str(x)).value = c3
                        Range('M'+str(x)).value = c4
                        Range('N'+str(x)).value = c5
                        Range('O'+str(x)).value = c6

                        professors_workbook.save()