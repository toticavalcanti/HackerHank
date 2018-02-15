# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:28:18 2018

@author: toti.cavalcanti
"""

#https://www.hackerrank.com/challenges/30-inheritance/problem

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
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        total = 0

        for testScore in self.scores:
            total += testScore

        avg = total / len(self.scores)

        if 100 >= avg >= 90:
            return 'O'
        if 90 > avg >= 80:
            return 'E'
        if 80 > avg >= 70:
            return 'A'
        if 70 > avg >= 55:
            return 'P'
        if 55 > avg >= 40:
            return 'D'
        return 'T'

line = ['Heraldo', 'Memelli', '8135627']
numScores = 2
scores = [100, 80]
firstName = line[0]
lastName = line[1]
idNum = line[2]
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

#Read from stdin the first line with student first name, last name and id 
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]

#read from stdin the number of tests
numScores = int(input()) # not needed for Python

#read from stdin the scores of the student 
scores = list( map(int, input().split()) )

s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())