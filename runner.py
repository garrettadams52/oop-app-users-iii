# Import and create your users here
from users.User import User
from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser

person1 = PremiumUser('John', 'john@hotmail.com', '123 street name', '56789')
person2 = FreeUser('Sarah', 'sarah@hotmail.com', '897 street name', '92834')
person3 = User('Amy', 'amy@gmail.com', '456 street name', '0000')

person1.create("This is my post")
person2.create("Person 2 posting")
person2.create("Person 2 second post")
#person2.create("my third post")

print(person1.name, person1.post)
print(person2.name, person2.post)
print(User.posts)

person2.delete("Person 2 posting")

print(person1.name, person1.post)
print(person2.name, person2.post)
print(User.posts)