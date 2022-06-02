# Your User class goes here
# your improved User class goes here

class User:

    posts = []

    def __init__(self, name, email, address, license, post = None):
        self.name = name
        self.email = email
        self.address = address
        self.license = license
        self.post = [] if post == None else post       

    def create(self, add_post):
        self.post.append(add_post)
        User.posts.append(add_post)
        

    def delete(self, rem_post):
        self.post.remove(rem_post)
        User.posts.remove(rem_post)
        

    @classmethod
    def print_posts(cls):
        return cls.posts


#------- Testing --------
# person1 = User('John', 'john@hotmail.com', '123 street name', '56789')
# person2 = User('Sarah', 'sarah@hotmail.com', '897 street name', '92834')
# person3 = User('Amy', 'amy@gmail.com', '456 street name', '0000')

# person1.create("This is my post")
# person2.create("Person 2 posting")
# person2.create("Person 2 second post")

# print(person1.name, person1.post)
# print(person2.name, person2.post)
# print(User.posts)

# person2.delete("Person 2 posting")

# print(person1.name, person1.post)
# print(person2.name, person2.post)
# print(User.posts)

