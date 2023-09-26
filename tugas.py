# tugas 1
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

#tugas 2
student = {
 "nama" : "faqih",
 "umur" : 26,
 "tinggi" : 177.6
 }

student["hobi"] = "coding"
print(student)

#tugas 3
student = {
 "nama" : "faqih",
 "umur" : 26,
 "tinggi" : 177.6
 }
print(student)
student.update({"hobi" : "coding"})
print(student)

#tugas 4
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8
dict['School'] = "DPS School"
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

#tugas 5
student = {
 "nama" : "faqih",
 "umur" : 26,
 "tinggi" : 177.6
 }
print(student)
student["nama"] = "darmawan"
print(student)

#tugas 6
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name'] # hapus entri dengan key 'Name'
dict.clear()
del dict
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

#latihan 7
student = {
 "nama" : "faqih",
 "umur" : 26,
 "tinggi" : 177.6
 }
print(student)
student.pop("umur")
print(student)