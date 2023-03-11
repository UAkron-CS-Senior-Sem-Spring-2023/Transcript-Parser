from pathlib import Path
import Course
import Student
import PDFParser
import os
import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/parse', methods=['POST'])
def runExample():
    try:
        parser = PDFParser.PDFParser()
        parser.parseInfo("jacobDPR.pdf")

        return parser.student.toJSON()
    except:
        return "Exception Occured"
