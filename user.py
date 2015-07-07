'''
Created on Mar 10, 2015

@author: acabreza
'''
class User(object):
    """Mock User class."""
    
    def __init__(self, user_id, username):
        """Mock user."""
        self.user_id = user_id
        self.username = username
        
    def __str__(self):
        return "( %s, %s )" % (self.user_id, self.username)