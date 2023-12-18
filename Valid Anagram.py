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

def arrayStringsAreEqual(word1, word2):
    """
    :type word1: List[str]
    :type word2: List[str]
    :rtype: bool
    """

    if "".join(word1) == "".join(word2):
        return True
    else:
        return False
