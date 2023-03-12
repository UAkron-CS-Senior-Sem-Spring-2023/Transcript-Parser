from pathlib import Path
import Course
import Student
import PDFParser
import os, base64
import time
import logging

import redis
from flask_cors import CORS
from flask import Flask, request


app = Flask(__name__)
CORS(app, resources=r'/*')
cache = redis.Redis(host='redis', port=6379)

@app.route('/parse', methods=['POST'])
def runExample():
	parser = PDFParser.PDFParser()
	pdfData = request.files.get('uploadfile')
	if pdfData == None:
		parser.parseInfo("jacobDPR.pdf")
		return parser.student.toJSON()
	else:
		pdfData.save("uploadedPDF.pdf")
		parser.parseInfo("uploadedPDF.pdf")
		return parser.student.toJSON()
	