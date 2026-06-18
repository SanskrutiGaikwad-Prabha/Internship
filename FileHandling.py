# file = open("Student.txt","x")
# file.close()

file=open("Student.txt","w")
file.write("Sanskruti Sachin Gaikwad")
file.close()

file =open("Student.txt","r")
data=file.read()
print(data)
file.close()

file=open("Student.txt","a")
file.write("\nCity : Pune")
file.close()

file =open("Student.txt","r")
data=file.readline()
print(data)
file.close()
import os
if os.path.exists("Student.txt"):
    print("File exists")
else :
    print("File not found")

file=open("Student.txt","w")
file.write("\nPriya")
file.write("\nRohan")
file.write("\nJay")
file.write("\nMayuri")
file.write("\nNeha")
file.close()

try:
    file=open("Student.txt","w")
except FileNotFoundError as e :
    print("File does not found")
finally :
    print("File operation completed")


