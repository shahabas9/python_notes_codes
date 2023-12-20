user =[]
class Reg:
#add_User:
    def addUser(self,data):
        user.append(data)

#update_user:
    def updateUser(selef,data,val):
        for i in user:
            if i["id"] == data:
                i.update(val)
            else:
                print("Id not found")

#delete_user:
    def deleteUser(self,data):
        for i in user:
            if i["id"] == data:
                user.remove(i)

#get_data:

    def getData(self,data):
        matchingUsers = []
        for i in user:
            if isinstance(data, str):
                for i in user:
                    if i["department"].upper() == data.upper():
                        matchingUsers.append(i)
            elif isinstance(data, int):
                for i in user:
                    if i["id"] == data:
                        matchingUsers.append(i)
            else:
                print("Invalid input type. Please provide a string or an integer.")
        return matchingUsers


obj = Reg()
obj.addUser({"id":1,"name":"chandru","department":"eee", "email":"chandru@gmail.com","phonenum":67543289,"city":"chennai","state":"tamilnadu","country":"india"})
obj.addUser({"id":2,"name":"mukesh", "department":"ECE", "email":"mukesh@gmail.com","phonenum":9080706054,"city":"kovai","state":"tamilnadu","country":"india"})
obj.addUser({"id":3,"name":"auewag", "department":"mech", "email":"mukesh@gmail.com","phonenum":9080706054,"city":"kovai","state":"tamilnadu","country":"india"})
obj.addUser({"id":4,"name":"suresg", "department":"CSE", "email":"mukesh@gmail.com","phonenum":9080706054,"city":"kovai","state":"tamilnadu","country":"india"})
obj.addUser({"id":5,"name":"ramesh", "department":"civil", "email":"mukesh@gmail.com","phonenum":9080706054,"city":"kovai","state":"tamilnadu","country":"india"})
obj.addUser({"id":6,"name":"sathish", "department":"it", "email":"mukesh@gmail.com","phonenum":9080706054,"city":"kovai","state":"tamilnadu","country":"india"})
obj.addUser({"id":7,"name":"john", "department":"it", "email":"mukesh@gmail.com","phonenum":9080706054,"city":"kovai","state":"tamilnadu","country":"india"})
obj.addUser({"id":8,"name":"david", "department":"EEE", "email":"mukesh@gmail.com","phonenum":9080706054,"city":"kovai","state":"tamilnadu","country":"india"})
obj.addUser({"id":9,"name":"stark", "department":"ECE", "email":"mukesh@gmail.com","phonenum":9080706054,"city":"kovai","state":"tamilnadu","country":"india"})
obj.addUser({"id":10,"name":"natasha", "department":"ECE", "email":"mukesh@gmail.com","phonenum":9080706054,"city":"kovai","state":"tamilnadu","country":"india"})

mixedData = obj.getData(1)
print(mixedData)




isLicencable : True