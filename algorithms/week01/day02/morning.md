**Isomorphic Strings**

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


# Example 1:
Input: s = "egg", t = "add"
Output: true

# Example 2:
Input: s = "foo", t = "bar"
Output: false

# Example 3:
Input: s = "paper", t = "title"
Output: true

# Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.


**Is Subsequence**
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


# Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

# Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
 

# Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
