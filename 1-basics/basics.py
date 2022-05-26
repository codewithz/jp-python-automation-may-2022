from sqlite3 import paramstyle


i=10
print(i)
print(type(i))

name="Zartab"
print(name)
print(type(name))

name='Zartab'
print(name)

name="Zartab"
print(name)

paragraph="""
    India is my country
    All Indians are my brothers and sisters
    I love my country
"""

print(paragraph)

str="kitkat"

print(str[0])
print(str[-1])
print(str[1:3])

print(str[1:])

print(str[0:20])

print(str[:20])

# print(str[20])
# IndexError: string index out of range 

company="jp morgan"
print("Original:",company)
company=company.upper()
print("Upper Case:",company)

sentence="I AM HAPPY TO BE HERE"
print("Original:",sentence)
sentence=sentence.lower()
print("Lower Case:",sentence)

sentence=sentence.capitalize()
print("Capitalize:",sentence)

sentence=sentence.title()
print("Title:",sentence)

# Splitting

data="1,Tom,IT,Dev,5000"
print("O:",data)
print(type(data))
splitted_data=data.split(",")
print("Spl:",splitted_data)
print(type(splitted_data))
print(splitted_data[3])
print(splitted_data[2])

# Format Function

line="My name is Zartab, I am {} years old"
age=31

fline=line.format(age)
print("O:",line)
print("F:",fline)

line="My name is {}, I am {} years old"
name="Micheal"
age=35

fline=line.format(name,age)
print(fline)

line="Hey I am a {0}, I train my {1}, {1} asks doubts to {0}"
fline=line.format("Trainer","Trainee")
print(fline)
print("------------------------------------------")
line="He is {name},{name} is {age} years old, {name} works in {dept} dept"
fline=line.format(name="Tom",age=39,dept="Finance")
print(fline)



