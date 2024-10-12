print('Example 1: Combining Two Lists with sameLength')
names=['AbdulAkram','FaizanKhan','SyedUzair']
Gpa=[7.26,7.21,8.5]
ziped=zip(names,Gpa)
listzipped=list(ziped)
print(f'The zip function of names and gpa{listzipped}')
print('Example 2: What Happens When the Lists Are Uneven?')
fruits=['apples','mangoes']
prices=['100','80','90']
fruitszip=zip(fruits,prices)
fruitszipped=list(fruitszip)
print(fruitszipped)
print('Example 3: Unzipping a Zipped Object')
cities=['Hyd','Srd','Zhrb']
population=[10000000,1000000,500000]
zipcitypopulation=zip(cities,population)
zipped=list(zipcitypopulation)
print(zipped)
unzipcity,unzippopulation=zip(*zipped)
print(unzipcity)
print(f'The unziping the zip function{unzippopulation}')
print('Ex-3__Zipping the more than two lists')
name=('zain','zara','mahek')
mrks=(99,98,97)
grades=('A','B','C')
zipped=zip(name,mrks,grades)
tuplezip=tuple(zipped)
print(tuplezip)
str1 = "ABC"
str2 = "1234"
# Zipping the characters together
zipped_strings = tuple(zip(str1, str2))
print(type(zipped_strings))
print('EX4__Zipping the dictionary')
dict1={'name':'Abdul','city':'hyd'}
dict2={'name':'akram','city':'srd'}
zipdict=zip(dict1,dict2)
zippeddict=list(zipdict)
print(zippeddict)
zipvalues=zip(dict1.values(),dict2.values())
zippedvalues=list(zipvalues)
print(zippedvalues)
nms=['akram','uzair','muhammed']
scorees=[56,67,89]
for name,score in zip(nms,scorees):
    print(f'{name}is scored {score}')

















