# Advent of Code 2023

My attempts at the AoC 2023.

## Progress/reflections

- Day 1: pleased I worked out that you can iterate once and check both ends, but level of nesting is a bit gross.
- Day 2: part 1 is straightforward using regex, part 2 is cool as you can use a look ahead
- Day 3: part 1 was relatively straightforward, part 2 I struggled with as decided to search for asterisks rather than use the existing search of numbers. Eventually looked at subreddit, where I got the idea to store + update list of gears based on number searches. Indexing the window proved finicky, but solved in the end!
- Day 4: relatively simple, using lookbehind/aheads to separate lists of numbers. In Part 2 I managed to simplify updating the cards, noting that it's not really as sequential as I first thought.
- Day 5: part 1 was easy enough. I gave up on part 2: clearly there are too many seeds to iterate through each; and you basically want to check the "pivot" points of the function, but given these are nested I wasn't entirely sure how to do so. I saw a suggestion that you could reverse the mapping, and just iterate through increasing locations to find the first seed -- I may try implement this at some point.
- Day 6: fairly straightforward: to avoid brute-forcing part 2 (and hence also revising part 1) I used the fact that the distribution of distances over holdtime is unimodal and symmetric. Could speed this code up even further by using binary searches to find the (lower) threshold.
- Day 7: fun part 1, using a merge sort (adapted using custom comparison function); not attempted part 2.
- Day 8: part 1 very easy, but used itertools.cycle to create circular list. Part 2 I had the brute-force approach but would have taken hours. Not sure why the LCM works here, but it does...
- Day 9: not sure it's the most efficient of code, but works pretty well -- part 2 was super easy change (though, intuitively, the position argument of .insert() should be the second, and not the first, argument...)
- Day 10: part 1 pretty easy -- thought maybe should send two pointers opposite ways, but not sure this is more efficient than simply tracing route and dividing length by two. Didn't attempt part 2 -- lots of discussion on reddit about floodfills and increasing the resolution...