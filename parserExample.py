import Course
import Student
import PDFParser

from pathlib import Path

parser = PDFParser.PDFParser()
parser.parseInfo("jacobDPR.pdf")
for line in range (len(parser.student.coursesTaken)):
	print (parser.student.coursesTaken[line])