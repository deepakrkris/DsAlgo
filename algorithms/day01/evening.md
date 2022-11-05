**sliding window pattern**

Given an integer array and a window of size w, find the current maximum value in the window as it slides through the entire array.
Note: If the window size is greater than the array size, we consider the entire array as a single window.

Constraints:
1 ≤ array.length ≤ 10^3
−10 ≤ array[i] ≤ 10^4
1 ≤ w


What should be the output if the following input is given?
w = 2
array = [-4, 5, 4, -4, 4, 6, 7]
 
A)
[5, -4, 6]

B)
[5, 4, 6]

C)
[5, 5, 4, 4, 6, 7]

D)
[5, 5, 4, 6, 6] 



**Minimum Window Subsequence**

Given strings str1 and str2, find the minimum (contiguous) substring sub_str of str1, such that every character of str2 appears in sub_str in the same order as it is present in str2.

If there is no window in str1 that covers all characters in str2, return an empty string.
If there are multiple minimum-length windows, return the one with the leftmost starting index.

1 ≤ str1.length ≤ 2 * 10^3
1 ≤ str2.length ≤ 100
str1 and str2 consist of uppercase and lowercase English letters.

The strings "bcde" and "bdde" are both minimumsubsequences, but "bcde" occurs before "bdde".The substring “deb” is the shortest to contain all therequired characters, but they do not appear in therequired order.

