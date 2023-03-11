import Course
import Student
import PDFParser
import os
import time

from pathlib import Path

def runExample():
	parser = PDFParser.PDFParser()
	parser.parseInfo("jacobDPR.pdf")
 
	return parser.student.toJSON()
