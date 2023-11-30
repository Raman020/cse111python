




f1=open('kw.txt','w+')
f1.write('hello students')
f1.seek(2)# set the cursor at specific location
print(f1.read())
