# This is my header

### Find All Duplicates

Write a function (in python) or method (in Java) that accepts a list of integers and returns a list of only those integers that appear more than once.

### Find Duplicates - Explanation

##### Nested Loop Method

Using two nested for loops, we can compare an element to every other element that comes after it in the list. If we find a pair, we add it to a seperate list.  After we finish comparing all the elements, we then return the list with the duplicates, even if the list is empty.

Positive - Easy to understand, easy to make.
Negative - Bad time complexity (O(n^2))

##### Dictionary Method

A dictionary is a data type that does not allow duplicate values. We can add the items from the list to the dictionary, and if any value is rejected then we know we have a duplicate and we can add it to our return list. We can check if a value was rejected if the size of the dictionary does not change after attempting to insert a new value. After going through the list, we can return our list of duplicates, even if its empty.

Positive - Great time complexity (O(n))
Negative - More complex