# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_user.ipynb.

# %% auto 0
__all__ = ['User']

# %% ../nbs/00_user.ipynb 4
class User():
    '''Simple user account class `User`'''
    def __init__(self, 
                 first_name: str, # first name of user
                 last_name: str): # last name of user
        self.first_name = first_name
        self.last_name = last_name
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    __repr__ = __str__
    def __eq__(self, user : 'User'): 
        return (user.first_name, user.last_name) == (self.first_name, self.last_name)
    def __lt__(self: 'User', user : 'User'):
        return self.last_name < user.last_name
    def __gt__(self: 'User', user : 'User'):
        return self.last_name > user.last_name
