Hints for Data Structures
	
#1. l.2	Describe what it means for two strings to be permutations of each other. Now, look at that definition you provided. Can you check the strings against that definition?
	
#2. 3.1	A stack is simply a data structure in which the most recently added elements are removed first. Can you simulate a single stack using an array? Remember that there are many possible solutions, and there are tradeoffs of each.
	
#3. 2.4	There are many solutions to this problem, most of which are equally optimal in runtime. Some have shorter, cleaner code than others. Can you brainstorm different solutions?
	
#4. 4.10	If T2 is a subtree of Tl, how will its in-order traversal compare to Tl's? What about its pre-order and post-order traversal?
	
#5. 2.6	A palindrome is something which is the same when written forwards and backwards. What if you reversed the linked list?
	
#6. 4.12	Try simplifying the problem. What if the path had to start at the root?
	
#7. 2.5	Of course, you could convert the linked lists to integers, compute the sum, and then convert it back to a new linked list. If you did this in an interview, your interviewer would likely accept the answer, and then see if you could do this without converting it to a number and back.
	
#8. 2.2	What if you knew the linked list size? What is the difference between finding the Kth-to- last element and finding the Xth element?
	
#9. 2.1	Have you tried a hash table? You should be able to do this in a single pass of the linked list.
	
#10. 4.8	If each node has a link to its parent, we could leverage the approach from question 2.7 on page 95. However, our interviewer might not let us make this assumption.
	
#11. 4.10	The in-order traversals won't tell us much. After all, every binary search tree with the same values (regardless of structure) will have the same in-order traversal. This is what in-order traversal means: contents are in-order. (And if it won't work in the specific case of a binary search tree, then it certainly won't work for a general binary tree.) The pre- order traversal, however, is much more indicative.
	
#12. 3.1	We could simulate three stacks in an array by just allocating the first third of the array to the first stack, the second third to the second stack, and the final third to the third stack. One might actually be much bigger than the others, though. Can we be more flexible with the divisions?

	
#13. 2.6    Try using a stack.


#14. 4.12	Don't forget that paths could overlap. For example, if you're looking for the sum 6, the
	        paths 1->3- >2 and 1->3->2->4->-6->2 are both valid.


#15. 3.5	One way of sorting an array is to iterate through the array and insert each element into a new array in sorted order. Can you do this with a stack?


#16. 4.8	The first common ancestor is the deepest node such that p and q are both descendants.
            Think about how you might identify this node.

#17. 1.8	If you just cleared the rows and columns as you found Os, you'd likely wind up clearing the whole matrix.Try finding the cells with zeros first before making any changes to the matrix.


#18. 4.10	You may have concluded that if T2. preorderTraversal () is a substring of Tl. preorderTraversal (), then T2 is a subtree of Tl. This is almost true, except that the trees could have duplicate values. Suppose Tl and T2 have all duplicate values but different structures. The pre-order traversals will look the same even though T2 is not a subtree of Tl.How can you handle situations like this?


#19. 4.2	A minimal binary tree has about the same number of nodes on the left of each node as on the right. Let'sfocus on just the root for now. How would you ensure that about the same number of nodes are on the left of the root as on the right?
	
#20. 2.7	You can do this in 0 (A+B) time and 0 (1) additional space. That is, you do not need a hash table (although you could do it with one).
	
#21. 4.4	Think about the definition of a balanced tree. Can you check that condition for a single node? Can you check it for every node?
	
#22. 3.6    We could consider keeping a single linked list for dogs and cats, and then iterating through it to find the first dog (or cat).What is the impact of doing this?
	
#23. 1.5   Start with the easy thing. Can you check each of the conditions separately?

#24. 2.4   Consider that the elements don't have to stay in the same relative order. We only need to ensure that elements less than the pivot must be before elements greater than the pivot. Does that help you come up with more solutions?
	
#25. 2.2   If you don't know the linked list size, can you compute it? How does this impact the runtime?
	
#26. 4.7   Build a directed graph representing the dependencies. Each node is a project and an edge exists from A to B if B depends on A (A must be built before B). You can also build it the other way if it's easier for you.
	
#27. 3.2   Observe that the minimum element doesn't change very often. It only changes when a smaller element is added, or when the smallest element is popped.
	
#28. 4.8   How would you figure out if p is a descendent of a node n?

#29. 2.6   Assume you have the length of the linked list. Can you implement this recursively?

#30. 2.5   Try recursion. Suppose you have two lists, A = 1 - >5 - >9 (representing 951) and B 2- >3- >6- >7 (representing 7632), and afunction that operates on the remainder ofthe lists (5 - >9 and 3- >6 - >7). Could you use this to create the sum method? What is the relationship between sum(1->5->9, 2->3->6->7) and sum(5->9, 3->6->7)?
