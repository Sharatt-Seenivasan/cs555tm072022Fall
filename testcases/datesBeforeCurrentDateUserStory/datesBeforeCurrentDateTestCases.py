import unittest
import pandas as pd
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date

#Test Cases for User Story 1

class UserStoryOneTestMethods(unittest.TestCase):


  def testHasBirthdayDateAfterCurrentDate(self):
      count = 0
      testData = "/content/datesBeforeCurrentDateTestData1.ged"
      f = open(testData, "r")
      lines = f.readlines()
      index = 0
      for line in lines:
        if 'BIRT' in line.split():
          date = datetime.strptime(lines[index+1].split('DATE')[1].replace('\n',''), " %d %b %Y")
          if(isDateBeforeCurrentDate(date) == False):
            count+=1
        index+=1
      self.assertEqual(count,1)


  def testHasDeathDateAfterCurrentDate(self):
      count = 0
      testData = "/content/datesBeforeCurrentDateTestData1.ged"
      f = open(testData, "r")
      lines = f.readlines()
      index = 0
      for line in lines:
        if 'DEAT' in line.split():
          date = datetime.strptime(lines[index+1].split('DATE')[1].replace('\n',''), " %d %b %Y")
          if(isDateBeforeCurrentDate(date) == False):
            count+=1
        index+=1
      self.assertEqual(count,1)

  def testHasMarriageDateAfterCurrentDate(self):
      count = 0
      testData = "/content/datesBeforeCurrentDateTestData1.ged"
      f = open(testData, "r")
      lines = f.readlines()
      index = 0
      for line in lines:
        if 'MARR' in line.split():
          date = datetime.strptime(lines[index+1].split('DATE')[1].replace('\n',''), " %d %b %Y")
          if(isDateBeforeCurrentDate(date) == False):
            count+=1
        index+=1
      self.assertEqual(count,1)

  def testHasDivorceDateAfterCurrentDate(self):
      count = 0
      testData = "/content/datesBeforeCurrentDateTestData1.ged"
      f = open(testData, "r")
      lines = f.readlines()
      index = 0
      for line in lines:
        if 'DIV' in line.split():
          date = datetime.strptime(lines[index+1].split('DATE')[1].replace('\n',''), " %d %b %Y")
          if(isDateBeforeCurrentDate(date) == False):
            count+=1
        index+=1
      self.assertEqual(count,1)

  def testAllDatesBeforeCurrentDate(self):
      count = 0
      testData = "/content/datesBeforeCurrentDateTestData2.ged"
      f = open(testData, "r")
      lines = f.readlines()
      index = 0
      for line in lines:
        if 'DATE' in line.split():
          date = datetime.strptime(line.split('DATE')[1].replace('\n',''), " %d %b %Y")
          with self.subTest(date=date):
            self.assertTrue(isDateBeforeCurrentDate(date))

testCases = UserStoryOneTestMethods()
unittest.main(argv=['first-arg-is-ignored','-v'], exit=False)