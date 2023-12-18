def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if ''.join(sorted(s)) == ''.join(sorted(t)):
        return True
    else:
        return False

