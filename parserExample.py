import Course
import Student
import PDFParser
import os
import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

from pathlib import Path

@app.route('/')
def runExample():
	parser = PDFParser.PDFParser()
	parser.parseInfo("jacobDPR.pdf")
	# return parser.student.toJSON()
	for line in range (len(parser.student.coursesTaken)):
		courses = courses + (parser.student.coursesTaken[line])
	return courses