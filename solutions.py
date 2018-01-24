# Question1 #

def question1(s, t):
    # verify s and t are strings
    if type(s) or type(t) != str:
        return "Error: not a string"

    # verify that string s is at least equal to string t
    if len(s) == 0 or len(s) < len(t):
        return False

    # if t is empty answer should be True
    if len(t) == 0:
        return True

    # store charater count of t
    count_of_t = {}
    for i in t:
        if i in count_of_t:
            count_of_t[i] += 1
        else:
            count_of_t[i] = 1

    # store count of 1st len(t) caracters of s
    count_of_s = {}
    for i in xrange(len(t)):
        if s[i] in count_of_s:
            count_of_s[s[i]] += 1
        else:
            count_of_s[s[i]] = 1

    # compare if anagrams
    if compare(count_of_t, count_of_s.copy()):
        return True

    # compare rest of sets
    for i in xrange(len(t), len(s)):

    # add new character in set
        if s[i] in count_of_s:
            count_of_s[s[i]] += 1
        else:
            count_of_s[s[i]] = 1

    # remove old character in set
        x = i - len(t)
        count_of_s[s[x]] -= 1
        if count_of_s[s[x]] == 0:
            count_of_s.pop(s[x])

    # compare if anagrams
        if compare(count_of_t, count_of_s.copy()):
            return True

    # no anagram of t in substring of s
    return False

def test1():
    print "Example Test (udacity, ad):",
    "Pass" if True == question1('udacity', 'ad') else "Fail"
    print "Test Case (no matching substrings):",
    "Pass" if False == question1('abcdefg', 'hijklm') else "Fail"
    print "Edge Case (t longer than s):",
    "Pass" if False == question1('racecar', 'race') else "Fail"
    print "edge Case (not a string):",
    "Pass" if "Error: not a string" == question1('<786>', '7.86') else "Fail"
