class Course:
	def __init__(self):
		self.year = -1
		self.term = ""
		self.subject = ""
		self.catalogNum = ""
		self.title = ""
		self.grade = ""
		self.units = -1.0
		self.courseType = ""

	def __str__(self):
		return f"{self.year} {self.term} {self.subject} {self.catalogNum} {self.title} {self.grade} {self.units} {self.courseType}"
