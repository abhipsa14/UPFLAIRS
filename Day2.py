st="upfalirs pvt ltd"
st1='upflairs'
#single line mei lihna h, error milegi agr multiple lines mei likhe the
print(st)
st2="""upflairs pvt ltd"""
#koi khas fark nhi padta h iska
#jis format mei likha h uss format mei milta h
#Indexing
st3="Amazing"
print(st3[4:8])
print(st3[:3])#starting - 0
print(st3[2:])#stopping - end
print(st3[::1])
print(st3[::2])

#FUNCTIONS
print(st3.upper())
print(st3.lower())
print(st3.title())
print(st3.capitalize())
print(len(st3))
print(st3.count('j'))
print(st3.find('p'))#first occurence
#second occurence
print(st3.find("jaipur"))
print(st3.split()) #spaces leke divide karega 
str1="i,am,abhipsa"
print(str1.replace(',',' '))
print(str1.replace("abhipsa","anshika"))
print(str1.endswith('s'))# boolean value return karta h
print(str1.startswith('d'))


##data type ___boolean___
var1=True
var2=False
print(var1,var2)
print(type(var1),type(var2))
# var=false #error dega

## List: It is an array in python but do not works like it. It provides all the features of array.
## It is dynamic in nature.
## static, dynamic and referential.
## can store different datatypes.
#it is referential in nature.
ls= [10,20,30,40,'abhi',True]
print(ls)
print(type(ls))
## indexing is similar to strings
print(ls[2:])

#insertion and deletion
student_details=['abhipsa','anshika','animesh']
print(student_details)
#insert
student_details.append('adheesh')
#delete
print(student_details)
student_details.pop(0)
print(student_details)
student_details[-1]="animesh srivastava"
print(student_details)
student_details.insert(0,"Alok")
print(student_details)
# student_details.append()
l1=[34,33,45,55,65,33,34,23,33]
print(l1.count(33))
print(len(l1))
l1.sort()
l1.reverse()
#l1.index() # gives index postion of the element
l1.clear()
## Nested list
l2=[10,20,30,[23,'hi',True],34]
print()


## TUPLE
## it is immutable in nature.
tp1=(52,35,45,65,75,88,99,0.01,'hi')
print(tp1)
print(type(tp1))
# access==yes
# remove==no
# insert=no
# update==no
# parenthesis agr nhi lagte hain upar wale mei vo tbahi bhi usko tuple consider karega

## ________SET___________
## it is unordered collection of unique elements.
# access==yes
# remove==yes
# insert=no
# update==no
st={25,45,41,23,46,67} #unique elements..duplicates are not allowed.doesn't maintain order.
print(type(st))
#immutable type
#indexing cannot be maintained
st.remove(25) #raises error if not found
st.discard(520)#error nhi raise karega if element not found in the set
# both above function is used to remove element.
print(st)













