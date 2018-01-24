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

    
# Question2 #

def get_substrings(a):
    # Get all possible substrings, including single character substrings
    for start_index in xrange(len(a)):
        for end_index in xrange(start_index + 1, len(a) + 1):
            yield a[start_index:end_index]

def question2(a):
    # Find the longest palindrome in a string and return its index or -1
    # Initialise variables
    longest_palindrome = question2.__doc__[5:27]
    palindromes_list = []

    # Search string for all palindromes
    for substring in get_substrings(a):
        if reversed(substring) == substring:
            palindromes_list.append(substring)

    # Check for palindromes in non-empty strings(single characters)

    if len(palindromes_list) > 0:
        longest_palindrome = max(palindromes_list, key=len)

    return a_string.find(longest_palindrome)

def Test2():
    print question2(786)#Edge case(not string)
    # Should be "Error"
    print question2("")#Edge case(empty string)
    # Should be "Error"
    print question2(aaba)
    # Should be "aba"
    print question2("racecar")
    # Should be "racecar"

	
# Question3 #
# used Kruskal's algorithm
parent = dict()
rank = dict()

    # get set of vertices 
def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

    # get edges of vertices
def join(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
	else:
            parent[root1] = root2
	if rank[root1] == rank[root2]: rank[root2] += 1

def question3(G)
    for vertice in G['vertices']:
	make_set(vertice)
	minimum_spanning_tree = set()
	edges = list(graph['edges'])
	edges.sort()
	#print edges
    for edge in edges:
	weight, vertice1, vertice2 = edge
	if find(vertice1) != find(vertice2):
	    join(vertice1, vertice2)
	    minimum_spanning_tree.add(edge)
	    
    return sorted(minimum_spanning_tree)

G = {'A': [('B', 2)],
     'B': [('A', 2), ('C', 5)], 
     'C': [('B', 5)]}

def Test3():
    print question3(786)#Edge case(dictionary error)
    # Should be "Error"
    print question3('A', 2)#Edge case(not enough vertices)
    # Should be "Error"
    print question3(G)#Test example
