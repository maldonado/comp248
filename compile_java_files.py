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

folder_path = "/Users/evermal/Downloads/COMP248-P-2/"
generic_assigment_name = 'GenericAssigmentClass'
template_feedback_workbook_path = '/Users/evermal/Documents/COMP248-Assigment2/examples/COMP248_A2Feedback_F2015.xlsx'

# student_name_regex = '(?:-([a-z\_]{2,8}))'
# assignement_date_regex = '([0-9]{4})\-([A-z]{3})\-([0-9]{1,2})\-(\d{1,2})h(\d{1,2})m'

package_regex = '.*package.*\;'
java_file_regex = '.*\.java$'
# generic_java_file_regex = '.*\.Gejava$'
student_id_regex = '.*([0-9]{8}).*'
# class_name_regex = '.*public{0,1}\s{0,1}class\s(\w[^\s]*)\s\{{0,1}.*'
class_name_regex = '\s{0,}(?:public){0,1}\s{0,1}class\s(\w[^\s]*)\s\{{0,1}.*'
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

print 'copying java files'
for root, dirs, files in os.walk(folder_path):
    for f in files:
        absolute_file_name = os.path.join(root, f)
        file_matcher = re.match(java_file_regex, absolute_file_name)
        temp_file_builder = []
        if file_matcher is not None:
            print absolute_file_name
            with open (absolute_file_name,'r') as original_java_file:
                for line in original_java_file:
                    
                    stripped = (c for c in line if 0 < ord(c) < 127)
                    stripped_line = ''.join(stripped)
                    
                    # 'removing package information from files'
                    package_matcher = re.match(package_regex, stripped_line)             
                    if package_matcher is None:
                        
                        # 'renaming class'  
                        class_name_matcher = re.match(class_name_regex, stripped_line)
                        if class_name_matcher is not None:                            
                            class_name = class_name_matcher.group(1)
                            if '{' in class_name:
                                new_line = stripped_line.replace(class_name, generic_assigment_name+'{')
                            else:    
                                new_line = stripped_line.replace(class_name, generic_assigment_name)
            
                            temp_file_builder.append(new_line)
                        else:
                    
                            temp_file_builder.append(stripped_line)
            original_java_file.close()

            # 'create temp java file' 
            temp_java_file_path = root + "/" + generic_assigment_name + ".java"
            with codecs.open(temp_java_file_path, "wb") as temp_java_file:
                temp_java_file.write("".join(temp_file_builder))
            temp_java_file.close

print 'compilation process started'
for root, dirs, files in os.walk(folder_path):
    for f in files:
        if f == generic_assigment_name+'.java':

            absolute_file_name = os.path.join(root, f)

            # feedback variables
            # Case 1 - enter name and exit without drawing the house = 0
            
            personalized_message =1
            height_validation = 1
            width_validation = 1
            drawing_of_the_house_roof = 3
            drawing_of_the_house_body = 3
            repetition_process = 0
            extra_point = 1

            personalized_message_comment = ''
            height_and_width_comment = ''
            roof_comment = ''
            body_comment = ''
            comment_5 = ''
            extra_point_comment = ''

            # 'compile temp java file'
            try:
                temp_java_file_path = root + "/" + generic_assigment_name + ".java"
                directory = subprocess.check_output(["javac",  temp_java_file_path, "-d", root])
            except Exception, e:
                personalized_message_comment = 'The program is not compiling'
                height_and_width_comment = 'The program is not compiling'
                roof_comment = 'The program is not compiling'
                body_comment = 'The program is not compiling'
                comment_5 = 'The program is not compiling'
                extra_point_comment = 'The program is not compiling'
                pass

            
            print root
            try:
                expected_personalized_messages = 0
                print '1 - Enter a name; choose to not draw a house'
                test_case_desc = '1 - Enter a name; choose to not draw a house'
                program_test = pexpect.spawn('java -cp d:"'+root+'" GenericAssigmentClass', timeout=1)
                program_test.logfile_read = sys.stdout
                index = program_test.expect(['name' , 'Name', pexpect.EOF, pexpect.TIMEOUT])
                if index == 2:
                    print "Atencaooooooooooo"
                program_test.sendline('Everton')
                index = program_test.expect(['Everton', pexpect.EOF, pexpect.TIMEOUT])
                if index == 0:
                    expected_personalized_messages = expected_personalized_messages + 1
                index = program_test.expect(['yes', 'Yes', 'YES' , 'house', pexpect.EOF, pexpect.TIMEOUT])
                if index == 5:
                    print "Atencaooooooooooo"
                program_test.sendline('no')
                index = program_test.expect(['Everton', pexpect.EOF, pexpect.TIMEOUT])
                if index == 0:
                    expected_personalized_messages = expected_personalized_messages + 1

                # extra point validation
                time.sleep(1)
                if program_test.isalive() :
                    extra_point = 0
                    extra_point_comment = extra_point_comment + test_case_desc + '- your program does not quit when expected;'
                    print extra_point_comment
                    print 'generate error for later validation'
                
                # personalized message validation
                elif expected_personalized_messages != 2:
                    personalized_message = 0
                    personalized_message_comment = personalized_message_comment + test_case_desc + '- you were expected to generate 2 personalized messages;'
                    print personalized_message_comment
  
                expected_personalized_messages = 0
                print '2 - Enter a name; choose to draw a house; pass wrong height'
                test_case_desc = '2 - Enter a name; choose to draw a house; pass wrong height'
                program_test = pexpect.spawn('java -cp d:"'+root+'" GenericAssigmentClass', timeout=1)
                program_test.logfile_read = sys.stdout
                index = program_test.expect(['name' , 'Name', pexpect.EOF, pexpect.TIMEOUT])
                if index == 2:
                    print "Atencaooooooooooo"
                program_test.sendline('Everton')
                index = program_test.expect(['Everton', pexpect.EOF, pexpect.TIMEOUT])
                if index == 0:
                    expected_personalized_messages = expected_personalized_messages + 1

                index = program_test.expect(['yes', 'Yes', 'YES' , 'house', pexpect.EOF, pexpect.TIMEOUT])
                if index == 5:
                    print "Atencaooooooooooo"
                
                program_test.sendline('yes')
                index = program_test.expect(['height and width', 'height', pexpect.EOF, pexpect.TIMEOUT])
                # try:
                height_validation_counter = 0
                if index == 0:
                    program_test.sendline('1 10')
                    index = program_test.expect(['even number', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        time.sleep(1)
                        if program_test.isalive():
                            program_test.sendline('1')
                            height_validation_counter = height_validation_counter + 1
                    index = program_test.expect(['even number', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        time.sleep(1)
                        if program_test.isalive():
                            program_test.sendline('1')
                            height_validation_counter = height_validation_counter + 1
                    index = program_test.expect(['even number', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        time.sleep(1)
                        if program_test.isalive():
                            program_test.sendline('1')
                            height_validation_counter = height_validation_counter + 1

                    index = program_test.expect(['Everton', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        expected_personalized_messages = expected_personalized_messages + 1

                elif index == 1:
                    program_test.sendline('1')
                    index = program_test.expect(['even number', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        time.sleep(1)
                        if program_test.isalive():
                            program_test.sendline('1')
                            height_validation_counter = height_validation_counter + 1
                    index = program_test.expect(['even number', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        time.sleep(1)
                        if program_test.isalive():
                            program_test.sendline('1')
                            height_validation_counter = height_validation_counter + 1
                    index = program_test.expect(['even number', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        time.sleep(1)
                        if program_test.isalive():
                            program_test.sendline('1')
                            height_validation_counter = height_validation_counter + 1
                    index = program_test.expect(['Everton', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        expected_personalized_messages = expected_personalized_messages + 1     

                if height_validation_counter != 3:
                    height_validation = 0
                    height_and_width_comment = height_and_width_comment + test_case_desc + '- you were expected to validate height 3 times;'
                    print height_and_width_comment

                time.sleep(1)
                if program_test.isalive() :
                    extra_point = 0
                    extra_point_comment = extra_point_comment + test_case_desc + '- your program does not quit when expected;'
                    print extra_point_comment

                elif expected_personalized_messages != 2:
                    personalized_message = 0
                    personalized_message_comment = personalized_message_comment + test_case_desc + '- you were expected to generate 2 personalized messages;'
                    print personalized_message_comment

                expected_personalized_messages = 0
                print '3 - Enter a name; choose to draw a house; pass wrong width'
                test_case_desc = '3 - Enter a name; choose to draw a house; pass wrong width'
                program_test = pexpect.spawn('java -cp d:"'+root+'" GenericAssigmentClass', timeout=1)
                program_test.logfile_read = sys.stdout
                index = program_test.expect(['name' , 'Name', pexpect.EOF, pexpect.TIMEOUT])
                if index == 2:
                    print "Atencaooooooooooo"
                program_test.sendline('Everton')
                index = program_test.expect(['Everton', pexpect.EOF, pexpect.TIMEOUT])
                if index == 0:
                    expected_personalized_messages = expected_personalized_messages + 1

                index = program_test.expect(['yes', 'Yes', 'YES' , 'house', pexpect.EOF, pexpect.TIMEOUT])
                if index == 5:
                    print "Atencaooooooooooo"
                
                program_test.sendline('yes')
                index = program_test.expect(['height and width', 'width', pexpect.EOF, pexpect.TIMEOUT])
                # try:
                width_validation_counter = 0
                if index == 0:
                    program_test.sendline('10 1')
                    index = program_test.expect(['even number', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        time.sleep(1)
                        if program_test.isalive():
                            program_test.sendline('1')
                            width_validation_counter = width_validation_counter + 1
                    index = program_test.expect(['even number', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        time.sleep(1)
                        if program_test.isalive():
                            program_test.sendline('1')
                            width_validation_counter = width_validation_counter + 1
                    index = program_test.expect(['even number', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        time.sleep(1)
                        if program_test.isalive():
                            program_test.sendline('1')
                            width_validation_counter = width_validation_counter + 1

                    index = program_test.expect(['Everton', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        expected_personalized_messages = expected_personalized_messages + 1

                elif index == 1:
                    program_test.sendline('1')
                    index = program_test.expect(['even number', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        time.sleep(1)
                        if program_test.isalive():
                            program_test.sendline('1')
                            width_validation_counter = width_validation_counter + 1
                    index = program_test.expect(['even number', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        time.sleep(1)
                        if program_test.isalive():
                            program_test.sendline('1')
                            width_validation_counter = width_validation_counter + 1
                    index = program_test.expect(['even number', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        time.sleep(1)
                        if program_test.isalive():
                            program_test.sendline('1')
                            width_validation_counter = width_validation_counter + 1
                    index = program_test.expect(['Everton', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        expected_personalized_messages = expected_personalized_messages + 1     

                if width_validation_counter != 3:
                    width_validation = 0
                    height_and_width_comment = height_and_width_comment + test_case_desc + '- you were expected to validate width 3 times;'
                    print height_and_width_comment

                time.sleep(1)
                if program_test.isalive() :
                    extra_point = 0
                    extra_point_comment = extra_point_comment + test_case_desc + '- your program does not quit when expected;'
                    print extra_point_comment

                elif expected_personalized_messages != 2:
                    personalized_message = 0
                    personalized_message_comment = personalized_message_comment + test_case_desc + '- you were expected to generate 2 personalized messages;'
                    print personalized_message_comment

                expected_personalized_messages = 0
                print '4 - Enter a name; choose to draw a house; pass right values; quit after one house is done'
                roof_error = False
                body_error = False
                test_case_desc = '4 - Enter a name; choose to draw a house; pass right values; quit after one house is done'
                program_test = pexpect.spawn('java -cp d:"'+root+'" GenericAssigmentClass', timeout=1)
                program_test.logfile_read = sys.stdout
                index = program_test.expect(['name' , 'Name', pexpect.EOF, pexpect.TIMEOUT])
                if index == 2:
                    print "Atencaooooooooooo"
                program_test.sendline('Everton')
                index = program_test.expect(['Everton', pexpect.EOF, pexpect.TIMEOUT])
                if index == 0:
                    expected_personalized_messages = expected_personalized_messages + 1
                index = program_test.expect(['yes', 'Yes', 'YES' , 'house', pexpect.EOF, pexpect.TIMEOUT])
                if index == 5:
                    print "Atencaooooooooooo"
                
                program_test.sendline('yes')
                index = program_test.expect(['height and width', 'height', pexpect.EOF, pexpect.TIMEOUT])
                if index == 0:
                    print 'here'
                    program_test.sendline('10 10')
                elif index == 1 :
                    program_test.sendline('10')
                    index = program_test.expect(['width', pexpect.EOF, pexpect.TIMEOUT])
                    program_test.sendline('10')

                index = program_test.expect_exact(['    **', pexpect.TIMEOUT])
                if index == 1:
                    roof_error = True
                index = program_test.expect_exact(['   /  \\', pexpect.TIMEOUT])
                if index == 1:
                    roof_error = True
                index = program_test.expect_exact(['  /    \\', pexpect.TIMEOUT])
                if index == 1:
                    roof_error = True
                index = program_test.expect_exact([' /      \\', pexpect.TIMEOUT])
                if index == 1:
                    roof_error = True
                index = program_test.expect_exact(['/        \\', pexpect.TIMEOUT])
                if index == 1:
                    roof_error = True
                index = program_test.expect_exact(['----------', pexpect.TIMEOUT])
                if index == 1:
                    body_error =  True
                index = program_test.expect_exact(['|        |', pexpect.TIMEOUT])
                if index == 1:
                    body_error =  True
                index = program_test.expect_exact(['|        |', pexpect.TIMEOUT])
                if index == 1:
                    body_error =  True
                index = program_test.expect_exact(['|        |', pexpect.TIMEOUT])
                if index == 1:
                    body_error =  True
                index = program_test.expect_exact(['|        |', pexpect.TIMEOUT])
                if index == 1:
                    body_error =  True
                index = program_test.expect_exact(['|        |', pexpect.TIMEOUT])
                if index == 1:
                    body_error =  True
                index = program_test.expect_exact(['|        |', pexpect.TIMEOUT])
                if index == 1:
                    body_error =  True
                index = program_test.expect_exact(['|        |', pexpect.TIMEOUT])
                if index == 1:
                    body_error =  True
                index = program_test.expect_exact(['|        |', pexpect.TIMEOUT])
                if index == 1:
                    body_error =  True
                index = program_test.expect_exact(['|        |', pexpect.TIMEOUT])
                if index == 1:
                    body_error =  True
                index = program_test.expect_exact(['|        |', pexpect.TIMEOUT])
                if index == 1:
                    body_error =  True
                index = program_test.expect_exact(['----------', pexpect.TIMEOUT])
                if index == 1:
                    body_error =  True

                index = program_test.expect(['Everton', 'continue', pexpect.EOF, pexpect.TIMEOUT])
                if index == 0:
                    expected_personalized_messages = expected_personalized_messages + 1
                    program_test.sendline('no')
                elif index == 1:
                    program_test.sendline('no')
                    index = program_test.expect(['Everton', pexpect.EOF, pexpect.TIMEOUT])
                    if index == 0:
                        expected_personalized_messages = expected_personalized_messages + 1
                index = program_test.expect(['Everton', pexpect.EOF, pexpect.TIMEOUT])
                if index == 0:
                    expected_personalized_messages = expected_personalized_messages + 1

                if roof_error :
                    drawing_of_the_house_roof = 0
                    roof_comment = roof_comment + test_case_desc + '- The number of rows needed to print/draw the roof is half the width of the house;'
                    print roof_comment

                if body_error :
                    drawing_of_the_house_body = 0
                    body_comment = body_comment + test_case_desc + '- The body of the house has height+2 rows. First and last row are drawn using the dash character (-). Each of the rows are made up of width characters where the first and last characters are a | and the rest are spaces.;'
                    print body_comment

                time.sleep(1)
                if program_test.isalive() :
                    extra_point = 0
                    extra_point_comment = extra_point_comment + test_case_desc + '- your program does not quit when expected;'
                    print extra_point_comment

                elif expected_personalized_messages != 3:
                    personalized_message = 0
                    personalized_message_comment = personalized_message_comment + test_case_desc + '- you were expected to generate 3 personalized messages;'
                    print personalized_message_comment

                # print '1.5 - Enter name and right measures quit after two houses - 2 personalized messages expected  - house drawing expected '
                # program_test = pexpect.spawn('java -cp d:"'+root+'" GenericAssigmentClass', timeout=1)
                # program_test.logfile_read = sys.stdout
                # index = program_test.expect(['name' , 'Name', pexpect.EOF, pexpect.TIMEOUT])
                # if index == 2:
                #     print "Atencaooooooooooo"
                
                # program_test.sendline('Everton')
                # index = program_test.expect(['Everton', pexpect.EOF, pexpect.TIMEOUT])
                # if index == 0:
                #     expected_personalized_messages = expected_personalized_messages + 1

                # index = program_test.expect(['yes', 'Yes', 'YES' , 'house', pexpect.EOF, pexpect.TIMEOUT])
                # if index == 5:
                #     print "Atencaooooooooooo"
                
                # program_test.sendline('yes')
                # index = program_test.expect(['height and width', 'height', pexpect.EOF, pexpect.TIMEOUT])
                # if index == 0:
                #     program_test.sendline('10 4')
                # elif index == 1 :
                #     program_test.sendline('10')
                #     index = program_test.expect(['width', pexpect.EOF, pexpect.TIMEOUT])
                #     program_test.sendline('4')

                #     index = program_test.expect_exact([' **', pexpect.TIMEOUT])
                #     if index == 1:
                #         print 'ERROR'
                #     index = program_test.expect_exact(['/  \\', pexpect.TIMEOUT])
                #     if index == 1:
                #         print 'ERROR'
                #     index = program_test.expect_exact(['----', pexpect.TIMEOUT])
                #     if index == 1:
                #         print 'ERROR'
                #     index = program_test.expect_exact(['|  |', pexpect.TIMEOUT])
                #     if index == 1:
                #         print 'ERROR'
                #     index = program_test.expect_exact(['|  |', pexpect.TIMEOUT])
                #     if index == 1:
                #         print 'ERROR'
                #     index = program_test.expect_exact(['|  |', pexpect.TIMEOUT])
                #     if index == 1:
                #         print 'ERROR'
                #     index = program_test.expect_exact(['|  |', pexpect.TIMEOUT])
                #     if index == 1:
                #         print 'ERROR'
                #     index = program_test.expect_exact(['|  |', pexpect.TIMEOUT])
                #     if index == 1:
                #         print 'ERROR'
                #     index = program_test.expect_exact(['|  |', pexpect.TIMEOUT])
                #     if index == 1:
                #         print 'ERROR'
                #     index = program_test.expect_exact(['|  |', pexpect.TIMEOUT])
                #     if index == 1:
                #         print 'ERROR'
                #     index = program_test.expect_exact(['|  |', pexpect.TIMEOUT])
                #     if index == 1:
                #         print 'ERROR'
                #     index = program_test.expect_exact(['|  |', pexpect.TIMEOUT])
                #     if index == 1:
                #         print 'ERROR'
                #     index = program_test.expect_exact(['|  |', pexpect.TIMEOUT])
                #     if index == 1:
                #         print 'ERROR'
                #     index = program_test.expect_exact(['----', pexpect.TIMEOUT])
                #     if index == 1:
                #         print 'ERROR'

                #     index = program_test.expect(['Everton', 'continue', pexpect.EOF, pexpect.TIMEOUT])
                #     if index == 0:
                #         expected_personalized_messages = expected_personalized_messages + 1
                #         program_test.sendline('yes')
                #     elif index == 1:
                #         program_test.sendline('yes')

                #         index = program_test.expect(['height and width', 'height', pexpect.EOF, pexpect.TIMEOUT])
                #         if index == 0:
                #             program_test.sendline('4 10')
                #         elif index == 1 :
                #             program_test.sendline('4')
                #             index = program_test.expect(['width', pexpect.EOF, pexpect.TIMEOUT])
                #             program_test.sendline('10')


                #             index = program_test.expect_exact(['    **', pexpect.TIMEOUT])
                #             if index == 1:
                #                 print 'ERROR'
                #             index = program_test.expect_exact(['   /  \\', pexpect.TIMEOUT])
                #             if index == 1:
                #                 print 'ERROR'
                #             index = program_test.expect_exact(['  /    \\', pexpect.TIMEOUT])
                #             if index == 1:
                #                 print 'ERROR'
                #             index = program_test.expect_exact([' /      \\', pexpect.TIMEOUT])
                #             if index == 1:
                #                 print 'ERROR'
                #             index = program_test.expect_exact(['/        \\', pexpect.TIMEOUT])
                #             if index == 1:
                #                 print 'ERROR'
                #             index = program_test.expect_exact(['----------', pexpect.TIMEOUT])
                #             if index == 1:
                #                 print 'ERROR'
                #             index = program_test.expect_exact(['|        |', pexpect.TIMEOUT])
                #             if index == 1:
                #                 print 'ERROR'
                #             index = program_test.expect_exact(['|        |', pexpect.TIMEOUT])
                #             if index == 1:
                #                 print 'ERROR'
                #             index = program_test.expect_exact(['|        |', pexpect.TIMEOUT])
                #             if index == 1:
                #                 print 'ERROR'
                #             index = program_test.expect_exact(['|        |', pexpect.TIMEOUT])
                #             if index == 1:
                #                 print 'ERROR'
                #             index = program_test.expect_exact(['----------', pexpect.TIMEOUT])
                #             if index == 1:
                #                 print 'ERROR'

                #             index = program_test.expect(['Everton', 'continue', pexpect.EOF, pexpect.TIMEOUT])
                #             if index == 0:
                #                 expected_personalized_messages = expected_personalized_messages + 1
                #                 program_test.sendline('no')
                #             elif index == 1: 
                #                 program_test.sendline('no')
                #             index = program_test.expect(['Everton', pexpect.EOF, pexpect.TIMEOUT])
                #             if index == 0:
                #                 expected_personalized_messages = expected_personalized_messages + 1

                time.sleep(1)
                if program_test.isalive() :
                    print 'ERROR!!!!'



                print expected_personalized_messages
                
            except Exception, e:
                personalized_message = 0
                print e
                pass


            # # create feedback workbook
            # student_id_matcher = re.match(student_id_regex, absolute_file_name)
            # student_id = student_id_matcher.group(1)
            # template_workbook = Workbook(template_feedback_workbook_path)
            # Range('B4').value = student_id
            # Range('B15').value = personalized_message
            # Range('B16').value = validation_of_height_and_with
            # Range('B17').value = drawing_of_the_house_roof
            # Range('B18').value = drawing_of_the_house_body
            # Range('B19').value = repetition_process
            # Range('B20').value = extra_point
            # Range('D15').value = personalized_message_comment
            # Range('D16').value = height_and_width_comment
            # Range('D17').value = roof_comment
            # Range('D18').value = body_comment
            # Range('D19').value = comment_5
            # Range('D20').value = extra_point_comment
            # student_feedback_workbook_path = root+'/'+student_id+'.xlsx'
            # template_workbook.save(student_feedback_workbook_path)
            # student_workbook = Workbook(student_feedback_workbook_path)
            # template_workbook.close()
            # student_workbook.close()