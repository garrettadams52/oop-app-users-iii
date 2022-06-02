from users.User import User

class FreeUser(User):
    def create(self, add_post):
        if(len(self.post)>=2):
            print('Sorry, you can only have 2 posts with a free account')
        else:
            self.post.append(add_post)
            User.posts.append(add_post)
    