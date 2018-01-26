# Question1 #

def compare(set1, set2):

    # check if set1 and set2 are equal
    for i in set1:
        if i in set2:
            if set1[i] == set2[i]:
                set2.pop(i)
            else:
                return False
        else:
            return False
    if len(set2) == 0:
        return True
    else:
        return False

def question1(s, t):

    # make sure (s) and (t) are strings, check each separately for better error results
    if type(s) != str:
        return "Error: s not string!"

    if type(t) != str:
        return "Error: t not string!"

    # make sure (s) is greater than (t)
    if len(s) == 0 or len(s) < len(t):
        return False

    # if (t) is empty, the answer should always be True
    if len(t) == 0:
        return True

    # store all character counts of (t)
    counts_of_t = {}
    for i in t:
        if i in counts_of_t:
            counts_of_t[i] += 1
        else:
            counts_of_t[i] = 1

    # store character counts of first len(t) characters of (s)
    counts_of_s = {}
    for i in xrange(len(t)):
        if s[i] in counts_of_s:
            counts_of_s[s[i]] += 1
        else:
            counts_of_s[s[i]] = 1

    # compare if they are anagrams
    if compare(counts_of_t, counts_of_s.copy()):
        return True

    # compare the rest of sets
    for i in xrange(len(t), len(s)):

        # add new character
        if s[i] in counts_of_s:
            counts_of_s[s[i]] += 1
        else:
            counts_of_s[s[i]] = 1

        # remove old character
        x = i - len(t)
        counts_of_s[s[x]] -= 1
        if counts_of_s[s[x]] == 0:
            counts_of_s.pop(s[x])
 
        # compare if they are anagrams
        if compare(counts_of_t, counts_of_s.copy()):
            return True

    # no matching anagram of (t) in substring of (s)
    return False

def test1():
    print "Test 1"
    print "Example test (udacity, ad):", "Pass" if question1("udacity", "ad") == True else "Fail"
    print "Edge case (not a string):", "Pass" if question1(123, 1.23) == "Error: s not string!" else "Fail"
    print "Edge case (t > s):", "Pass" if question1("ad", "udacity") == False else "Fail"
    print "Test (s = t):", "Pass" if question1("abcd", "abcd") == True else "Fail"
    print "Test (no matching substrings):", "Pass" if question1("abeeeeeeecd", "abcd") == False else "Fail"


# Question 2 #

def longest_palindrome(a, left_idx, right_idx):

    # find the longest palindrome if centered at idx.
    # idx can be in between elements.
    # left_idx and right_idx are the left and the right element of idx

    l = left_idx
    r = right_idx
    while l >= 0 and r < len(a):
        if a[l] == a[r]:
            l -= 1
            r += 1
        else:
            return l, r
    return l, r

def question2(a):

    # make sure (a) is a string
    if type(a) != str:
        return "Error: a not string!"

    # make sure (a) has at least 2 characters
    if len(a) < 2:
        return a

    # check for all possible centers
    left = 0
    right = 1
    for i in xrange(len(a)-1):
    
    # check palindrome centered at (i)
        l, r = longest_palindrome(a, i, i)
        if r-l-1 > right - left:
            right = r
            left = l+1

    # check palindrome centered between (i) and (i)+1
        l, r = longest_palindrome(a, i, i+1)
        if r-l-1 > right - left:
            right = r
            left = l+1
    return a[left:right]

def test2():
    print "\nTesting 2"
    print "Edge case (not string):", "Pass" if question2(123)== "Error: a not string!" else "Fail"
    print "Edge case (empty string):", "Pass" if question2("") == "" else "Fail"
    print "Case (a = \"a\"):", "Pass" if "a" == question2("a") else "Fail"
    print "Case (a = \"aa\"):", "Pass" if "aa" == question2("aa") else "Fail"
    print "Case (a = \"racecar\"):", "Pass" if question2("racecar") == "racecar" else "Fail"


# Question3 #

def question3(G):

    # Using Kruskal's algorithm

    # make sure G is dictionary
    if type(G) != dict:
        return "Error: G is not dictionary"

    # make sure G has more than one node
    if len(G) < 2:
        return "Error: not enough vertices to form edges"

    # get a set of vertices
    verts = G.keys()

    # get unique set of edges
    edges = set()
    for i in verts:
        for x in G[i]:
            if i > x[0]:
                edges.add((x[1], x[0], i))
            elif i < x[0]:
                edges.add((x[1], i, x[0]))

    # sort by weight
    edges = sorted(list(edges))

    # loop through edges and only store needed ones
    output_edges = []
    verts = [set(i) for i in verts]
    for i in edges:
    # get indices of both vertices
        for x in xrange(len(verts)):
            if i[1] in verts[x]:
                i1 = x
            if i[2] in verts[x]:
                i2 = x

    # store union in smaller and pop the larger index
    # also store edge in output_edges
        if i1 < i2:
            verts[i1] = set.union(verts[i1], verts[i2])
            verts.pop(i2)
            output_edges.append(i)
        if i1 > i2:
            verts[i2] = set.union(verts[i1], verts[i2])
            verts.pop(i1)
            output_edges.append(i)

    # terminate early when all vertices are in graph
        if len(verts) == 1:
            break

    # generate the ouput graph from output_edges
    output_graph = {}
    for i in output_edges:
        if i[1] in output_graph:
            output_graph[i[1]].append((i[2], i[0]))
        else:
            output_graph[i[1]] = [(i[2], i[0])]

        if i[2] in output_graph:
            output_graph[i[2]].append((i[1], i[0]))
        else:
            output_graph[i[2]] = [(i[1], i[0])]
    return output_graph


def test3():
    G = {'A': [('B', 2)],
         'B': [('A', 2), ('C', 5)],
         'C': [('B', 5)]}
    print "\nTest 3"
    print "Edge case (not dictionary):", "Pass" if question3(123) == "Error: G is not dictionary"  else "Fail"
    print "Edge case (empty dictionary):", "Pass" if question3({}) == "Error: not enough vertices" else "Fail"
    print "Example test:", "Pass" if question3(G) == G else "Fail"
    G = {'A': [('B', 7), ('D', 5)],
         'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
         'C': [('B', 8), ('E', 5)],
         'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
         'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
         'F': [('D', 6), ('E', 8), ('G', 11)],
         'G': [('E', 9), ('F', 11)]}
    H = {'A': [('D', 5), ('B', 7)],
         'B': [('A', 7), ('E', 7)],
         'C': [('E', 5)],
         'D': [('A', 5), ('F', 6)],
         'E': [('C', 5), ('B', 7), ('G', 9)],
         'F': [('D', 6)],
         'G': [('E', 9)]}
    print "Case (Wikipedia example):", "Pass" if H == question3(G) else "Fail"


# Question4 #

class Tree_Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def BST_search(r, n):

    # search if n is in tree
    current_node = r
    while current_node.left != None or current_node.right != None:

    # go left if current node is greater than (n)
        if current_node.data > n:

    # make sure left node exist
            if current_node.left != None:
                current_node = current_node.left
            else:
                return False

    # go right if current node is less than (n)
        elif current_node.data < n:

    # make sure right node exist
            if current_node.right != None:
                current_node = current_node.right
            else:
                return False

    # current node is (n), return True
        else:
            return True

    # check if (n) is in the lowest level
    if current_node.data == n:
        return True
    else:
        return False

def question4(r, n1, n2):

    # make sure (r) is a tree node
    if type(r) != Tree_Node:
        return "Error: r not Tree_Node!"

    # make sure (n1) and (n2) are integers
    if type(n1) != int:
        return "Error: n1 not integer!"
    if type(n2) != int:
        return "Error: n2 not integer!"

    # make sure (n1) and (n2) in the tree
    if not BST_search(r, n1):
        return "Error: n1 not in the tree!"
    if not BST_search(r, n2):
        return "Error: n2 not in the tree!"

    current_node = r
    while current_node.left != None or current_node.right != None:

    # if both vales are less than the current node, go left
        if current_node.data > n1 and current_node.data > n2:
            current_node = current_node.left

    # if both vales are greater than the current node, go right
        elif current_node.data < n1 and current_node.data < n2:
            current_node = current_node.right

    # we find the answer, return it
        else:
            return current_node.data

    # (n1) equal to (n2) at the lowest level
    return current_node.data

def test4():
    n1, n3, n5, n7 = Tree_Node(1), Tree_Node(3), Tree_Node(5), Tree_Node(7)
    n9, n11, n13, n15 = Tree_Node(9), Tree_Node(11), Tree_Node(13), Tree_Node(15)
    n2, n6, n10, n14 = Tree_Node(2), Tree_Node(6), Tree_Node(10), Tree_Node(14)
    n2.left, n2.right = n1, n3
    n6.left, n6.right = n5, n7
    n10.left, n10.right = n9, n11
    n14.left, n14.right = n13, n15
    n4, n12 = Tree_Node(4), Tree_Node(12)
    n4.left, n4.right = n2, n6
    n12.left, n12.right = n10, n14
    r = Tree_Node(8)
    r.left, r.right = n4, n12

    print "\nTesting 4"
    print "Edge case (r not Tree_Node):", "Pass" if question4(123, 111, 111) == "Error: r not Tree_Node" else "Fail"
    print "Edge case (n1 not in the tree):", "Pass" if question4(r, -1, 5) =="Error: n1 not in the tree"  else "Fail"
    print "Case (n1 = 8 and n2 = 1):", "Pass" if question4(r, 8, 1) == 8 else "Fail" 
    print "Case (n1 = 1 and n2 = 3):", "Pass" if question4(r, 1, 3) == 2 else "Fail"
    print "Case (n1 = 9 and n2 = 15):", "Pass" if question4(r, 9, 15) == 12 else "Fail"
    print "Case (n1 = 1 and n2 = 11):", "Pass" if question4(r, 1, 11) == 8 else "Fail"


# Question 5 #

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    # get the length of ll checking whether the linked list is circular
    # return -1 if the linked list is circular
def get_length(ll):
    if ll.next == None:
        return 1

    length_ll = 0
    node1 = ll
    node2 = ll.next
    while node1 != None and node1 != node2:
        node1 = node1.next
        if node2 != None:
            node2 = node2.next
        if node2 != None:
            node2 = node2.next
        length_ll += 1

    if node1 == None:
        return length_ll
    else:
        return -1

def question5(ll, m):

    # make sure ll is a Node
    if type(ll) != Node:
        return "Error: ll not a Node"

    # make sure (m) is an integer
    if type(m) != int:
        return "Error: m not an integer"

    # get the length of ll
    length_ll = get_length(ll)

    # make sure ll is not circular
    if length_ll == -1:
        return "Error: circular linked list"

    # make sure (m) <= length of ll
    if length_ll < m:
        return "Error: m > length of ll"

    # traverse to the last (m)th element
    node1 = ll
    for i in xrange(length_ll - m):
        node1 = node1.next

    return node1.data

def test5():
    n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)
    n4.next = n5
    n3.next = n4
    n2.next = n3
    n1.next = n2
    n5.next = n1
    
    print "\nTest 5"
    print "Edge case (ll not Node):", "Pass" if question5(123, 111) == "Error: ll not a Node" else "Fail"
    print "Edge case (m > length of ll):", "Pass" if question5(n1, 6) == "Error: m > length of ll" else "Fail"
    print "Case (ll = n1 and m = 3):", "Pass" if question5(n1, 3) == 3 else "Fail" 
    print "Case (circular linked list):", "Pass" if question5(n1, 3) == "Error: circular linked list" else "Fail" 

test1()
test2()
test3()
test4()
test5()
