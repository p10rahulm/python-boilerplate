'''
In the 2SAT problem, you are given a set of clauses, where each clause is the disjunction of two
literals (a literal is a Boolean variable or the negation of a Boolean variable). You are looking
for a way to assign a value "true" or "false" to each of the variables so that all clauses are satisfied
--- that is, there is at least one true literal in each clause. For this problem, design an algorithm
that determines whether or not a given 2SAT instance has a satisfying assignment. (Your algorithm
does not need to exhibit a satisfying assignment, just decide whether or not one exists.) Your
algorithm should run in O(m+n) time, where m and n are the number of clauses and variables, respectively.
[Hint: strongly connected components.]
'''
#http://codeforces.com/blog/entry/16205
#https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2269

