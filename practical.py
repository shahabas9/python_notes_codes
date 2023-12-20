# users = []

# #adduser
# def adduser(id,name,email,Phone,City,State,Country):
#     users.append([id,name,email,Phone,City,State,Country])

# adduser(1,"surya","surya@gmail.com",90003175,"chennai","tamilnadu","india")
# adduser(2,"sham","sham@gmail.com",80003175,"bangalore","karnataka","india")
# adduser(3,"adam","adam@gmail.com",70003175,"pune","delhi","india")
# adduser(4,"jhon","jhon@gmail.com",60003175,"cochin","kerala","india")


# #update users
# def updateusers(id,name,email,Phone,City,State,Country):
#     adduser(id,name,email,Phone,City,State,Country)

# updateusers(2,"shan","shan@gmail.com",8003175,"chennai","tamilnadu","india")


#  #Delete user based on Id:

# def deleteuser(id):
#     for user in users:
#         if user[0] == id:
#             users.remove(user)
#     else:
#         print("Id not found")

# # Deleting id :
# #deleteuser(3)

# #Get all the users:

# # for user in users:
# #     print("User ID:", user[0])
# #     print("Name:", user[1])
# #     print("Email:", user[2])
# #     print("Phone:", user[3])
# #     print("City:", user[4])
# #     print("State:", user[5])
# #     print("Country:", user[6])
# #     print()



f = open("practice.py", "r")
print(f.read())