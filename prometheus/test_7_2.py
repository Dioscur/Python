import sys
import math

class Student(object):
    name = ''
    marks = {}
    config = {}

    def __init__ (self, name, conf = {'exam_max': float, 'lab_max': float, 'lab_num': int, 'k': float,}):
        self.name = name
        self.exam_max = conf['exam_max']
        self.lab_max = conf['lab_max']
        self.lab_num = conf['lab_num']
        self.k = conf['k']
        self.labs = []
        self.exam = 0
        for i in range(self.lab_num):
            self.labs.append(0)

    def make_lab(self, m, n=-1):
        if n == -1:
            if 0 in self.labs:
                self.labs[self.labs.index(0)] = min (m, self.lab_max)
            else: return self
        elif n > self.lab_num - 1:
            return self
        else:
            self.labs[n] = min (m, self.lab_max)
        return self

    def make_exam(self, m):
        self.exam = min (m, self.exam_max)
        return self

    def is_certified(self):
        max_sum = self.lab_max * self.lab_num + self.exam_max
        mark = sum(self.labs) + self.exam
        return (mark, mark >= (max_sum * self.k))



conf = {'exam_max': 30, 'lab_max': 7, 'lab_num': 10, 'k': 0.61,}
oleg = Student ('Oleg', conf)
oleg.make_lab(1)
oleg.make_lab(8,0)
oleg.make_lab(1)
oleg.make_lab(10,7)
oleg.make_lab(4,1)
oleg.make_lab(5)
oleg.make_lab(6.5,10)
oleg.make_lab(6.5)
oleg.make_exam(32)
print oleg.labs
print 'Exam =', oleg.exam
print oleg.is_certified()
oleg.make_lab(7,1)
print oleg.labs
print oleg.is_certified()
