'''
Created on Mar 10, 2015

@author: acabreza
'''
import unittest
import user_cache
import user


class TestUserCache(unittest.TestCase):
    """Test the UserCache module."""

    def setUp(self):
        """Instantiate a UserCache; simulate startup of module."""
        self.max_capacity = 3
        self.user_cache = user_cache.UserCache(self.max_capacity)

    def tearDown(self):
        """Call cleanup routine."""
        self.user_cache.shutdown()

    def _fill_cache(self, size):
        """Fill cache helper."""
        for item in xrange(1, size):
            user_num = str(item)
            self.user_cache.set_user(user_num, user.User(user_num, "user%s" % user_num))        

    def testCapacity(self):
        """Test the capacity of the cache."""
        self._fill_cache(self.max_capacity + 2)
        self.assertEqual(self.user_cache.get_size(), self.max_capacity)

    def testDatastoreFetch(self):
        """Test access to datastore."""
        self.user_cache.flush()
        self._fill_cache(self.max_capacity+1)
        for item in xrange(1, self.max_capacity+1):
            user_num = str(item)
            self.user_cache.get_user(user_num)
        self.assertRaises(NotImplementedError, self.user_cache.get_user, str(item+1))

    def testLeastUsed(self):
        """Test the least recently used removal."""
        self.user_cache.flush()
        self._fill_cache(self.max_capacity+1)
        for item in xrange(1, self.max_capacity+1):
            user_num = str(item)
            self.user_cache.get_user(user_num)
        self.user_cache.get_user("2")
        self.user_cache.get_user("1")
        self.user_cache.set_user("4", user.User("4", "user4"))
        self.assertRaises(NotImplementedError, self.user_cache.get_user, "3")


if __name__ == "__main__":
    unittest.main()