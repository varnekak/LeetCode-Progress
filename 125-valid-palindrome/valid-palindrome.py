class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        w = re.findall(r'[a-zA-Z0-9]',s.lower())
        if w == w[::-1] : return True
        else : return False