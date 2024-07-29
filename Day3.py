#--------------------DICTIONARY--------------------------
#key-value pairs
dt={'A':10,'B':20,'C':30,'D':40}
print(dt)
print(type(dt))

dt1={0:10,1:20,2:30,3:40} #integer can also be key
print(dt1)
print(type(dt1))
# access has to be through key
print(dt['A'])
# Update value of key
dt['D']=400
print(dt)
# insertion
dt['E']=50
print(dt)
# deletion
dt.pop('C')
print(dt)
# to show all the keys
print(dt.keys())
# to show all the values
print(dt.values())


student_marks={"name":['manshi','ram','kishan','harsh'],"marks":[24,23,34,55],"subject":'Science'}
print(student_marks['name'])
# q1
student_marks["name"].pop()
student_marks["marks"].pop()
print(student_marks)
# q2
student_marks['name'].insert(1,"Abhishek")
student_marks['marks'].insert(1,55)
print(student_marks)          
# q3
student_marks["subject"]="Data Science"
print(student_marks)
# q4
print(len(student_marks["name"]))
# used to get all functions name
dir(student_marks)

#---------------------CONDITIONAL STATEMENTS-------------------------------------
# if,else,elif
# nested if else

# age=21
# if(age>21):
#     print("You can vote!")
# else:
#     print("You can not vote!")


###-----------------------TYPE CASTING--------------------------------------------------------
##int(),str(),float(),tuple(),list(),set(),dict()
num1=10.25
num2=int(num1)
print(num1,num2)

#list-->tuple
#tuple-->list
































