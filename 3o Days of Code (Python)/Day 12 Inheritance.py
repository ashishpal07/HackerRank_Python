# Day 12 inheritance

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
 
class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstname,lastname,id,scores):
        self.firstName = firstname
        self.lastName = lastname
        self.idNumber = id
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        a = sum(self.scores)/len(scores)
        if a >= 90:
            return 'O'
        elif 90>a>=80:
            return 'E'
        elif 80>a>=70:
            return 'A'
        elif 70>a>=55:
            return 'P'
        elif 55>a>=40:
            return 'D'
        else:
            return 'T'
 
