file=open('txtahmed.txt','w')
file.write('my anme is ahmed\n ')
file.write('my age is 18\n')
file.close()

fRead=open('txtahmed.txt','r')
text=fRead.read()
print(text)
fRead.close()