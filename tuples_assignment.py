"""
program:  tuples_assignment.py
author:  Lisa Kilmer
this program uses a tuple to write name and score to the student_info text file.
uses a key word for the name and input for the scores. write_to_file opens the file
student_info and writes the information and them closes the file.  The read_from_file
reads the file and print it.
I have basics of this but I didn't have time to make it work
"""
import os as os
input_tuple = ()


def write_to_file(name, scores):
    f = open('student_info.txt', 'w')
    f.write("first line\n")
    input_tuple = ('name\t', 'scores\n')
    f.writelines(input_tuple)
    f.close()


def get_student_info(**kwargs):
    while True:
        score = int(input("Enter a score or -1 to stop: "))
        if score != -1:
            input_tuple.append()
        else:
            if not type(score) is int:
                raise ValueError('not a number')

        write_to_file(name, score)


def read_from_file():
    file_dir = os.path.dirname(__file__)
    file_name = "student_info.txt"
    f = open(os.path.join(fun_with_collections, student_info, "r"))
    line1 = f.read()
    print(line1)
    f.close()


if __name__ == '__main__':
    write_to_file('Lisa', '88') #test
    get_student_info(name='Sam', score=input(input_tuple))
    get_student_info(name='Joe', score=input(input_tuple))
    get_student_info(name='Sally', score=input(input_tuple))
    input("Press any key to end")