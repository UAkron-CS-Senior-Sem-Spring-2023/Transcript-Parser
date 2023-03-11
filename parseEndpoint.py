from pathlib import Path
import Course
import Student
import PDFParser
import os
import time

import redis
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
CORS(app, resources=r'/*')
cache = redis.Redis(host='redis', port=6379)

@app.route('/parse', methods=['GET'])
def runExample():
	parser = PDFParser.PDFParser()
	parser.parseInfo("jacobDPR.pdf")

	return parser.student.toJSON()
