import sys
from xlwings import Workbook, Sheet, Range, Chart
from PDFWriter import PDFWriter

#
# Create a connection with a new workbook.
template_workbook = Workbook('/Users/evermal/Documents/COMP248-Assigment2/examples/COMP248_A2Feedback_F2015.xlsx')
Range('B4').value = 'student_id'
template_workbook.save('/Users/evermal/Documents/COMP248-Assigment2/examples/newCOMP248_A2Feedback_F2015.xlsx')
template_workbook.close()


# Create the Excel data.
# Column 1.
# Range('A1').value = 'Foo 1'
# Range('A2').value = 'Foo 2'
# Range('A3').value = 'Foo 3'
# Column 2.
# Range('B1').value = 'Bar 1'
# Range('B2').value = 'Bar 2'
# Range('B3').value = 'Bar 3'

# print Range('A1..D21').value


# pw = PDFWriter("text.pdf")
# pw.setFont("Courier", 10)

# # pw.setHeader("Testing Excel conversion to PDF with xlwings and xtopdf")
# # pw.setFooter("xlwings: http://xlwings.org --- xtopdf: http://slid.es/vasudevram/xtopdf")

# # print Range('A1').table.value

# for row in Range('A1..D21').value:
#     s = ''
#     for col in row:
#         s += str(col).replace(None, '\t') + ' | '
#     pw.writeLine(s)

# pw.close()