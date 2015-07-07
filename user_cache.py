'''
Created on Mar 10, 2015

@author: acabreza
'''
import collections

class UserCache(object):
    """This module holds active users to improve system performance.
    The cache returns an instance of the User object for a given user_id.
 
    The cache can hold at most max_users of user objects."""
    
    def __init__(self, max_users):
        """Use OrderedDict to store cache values to maintain access
        timestamp and """
        self.max_users = max_users
        self._cache = collections.OrderedDict()

    def flush(self):
        """Clear the items in the cache."""
        self._cache.clear()

    def get_user(self, user_id):
        """Get User object from cache if it exist, otherwise, 
        retrieve from datastore."""
        try:
            # Update timestamp by re-inserting
            value = self._cache.pop(user_id)
            self._cache[user_id] = value
            return value
        except KeyError:
            # Get from datastore
            user = self._get_from_datastore(user_id)
            if user is None:
                raise Exception("No such user")
            self.set_user(user_id, user)
            return user

    def get_size(self):
        """Return number of items in cache."""
        return len(self._cache)

    def set_user(self, user_id, user):
        """User object will be re-added if it exist in the cache,
        otherwise, the capacity is checked and least accessed is 
        removed."""
        try:
            self._cache.pop(user_id)
        except KeyError:
            # Max users reached; remove least accessed
            if len(self._cache) >= self.max_users:
                self._cache.popitem(last=False)
        self._cache[user_id] = user
        
    def shutdown(self):
        """Clean up routines."""
        self.flush()
        
    def _get_from_datastore(self, user_id):
        """TODO: To be implemented"""
        raise NotImplementedError
    
    def __str__(self):
        """Return cache representaiton."""
        _users = ["Cache: "]
        for key in self._cache.keys():
            _users.append("\nkey: %s, user: %s" % (key, self._cache[key]))
        return "".join(_users)