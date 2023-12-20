users = []

class Sample:
    def adduser(self, id, name, email, Phone, City, State, Country):
        my_dict = {
            "id": id,
            "name": name,
            "email": email,
            "Phone": Phone,
            "City": City,
            "State": State,
            "Country": Country
        }
        users.append(my_dict)

    def display_users(self):
        for user in users:
            print(user)

sample = Sample()

sample.adduser(1, "surya", "surya@gmail.com", 90003175, "chennai", "tamilnadu", "india")
sample.adduser(2, "sham", "sham@gmail.com", 80003175, "bangalore", "karnataka", "india")
sample.adduser(3, "adam", "adam@gmail.com", 70003175, "pune", "delhi", "india")
sample.adduser(4, "jhon", "jhon@gmail.com", 60003175, "cochin", "kerala", "india")

sample.display_users()


#update users:

def updateusers(id,name,email,Phone,City,State,Country):
    my_dict = {
            "id": id,
            "name": name,
            "email": email,
            "Phone": Phone,
            "City": City,
            "State": State,
            "Country": Country
        }
    def display_users(self):
        for user in users:
            print(user)
    sample = Sample()

updateusers(2,"shan","shan@gmail.com",8003175,"chennai","tamilnadu","india")

sample.display_users()