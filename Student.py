import Course

class Student:
	def __init__(self):
		self.coursesTaken = []
		self.major = ""
		self.yearJoined = -1;
		self.termJoined = ""

	def __str__(self):
		return f"{self.major} {self.yearJoined} {self.termJoined}"