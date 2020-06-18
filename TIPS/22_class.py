# -*- codding: utf-8 -*-
import collections

# 尽量用辅助类来维护程序的状态，而不要用字典和元组
# 字典和元组优点在于简单，但是随着需求的日益增加，其代码复杂度也会随着增加。

# 分数类
Grade = collections.namedtuple('Grader', ('score', 'weight'))


# 科目类，包含一系列考试成绩
class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.socre * grade.weight
            total_weight += grade.weight
        return total / total_weight

# 学生类，包括学生正在学习的各项课程


class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


# 考试成绩类
class GradeBook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]
