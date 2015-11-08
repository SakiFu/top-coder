"""Mr. White is a very versatile person - absolutely everythin is interesting to him. Perhaps this is why he has many friends. 
Quite unfortunately, however, none of his friends are versatile at all. 
Each of them is interested only in two topics and refuses to talk about anything else. 
Therefore, each time Mr. White organizrs a party, it's a big problem for him to decide whom to invite do that the party is interesting eo everybody. 
Now that Mr. White has a lot of experience in organizing parties, he knows for sure that a party will be interesting 
if and only if there's a topic interesting to each of the invited friends.
You will be given lists of strings, first and second. The i-th friend of Mr. White is interested in topics first[i] and second[i]. 
Return the largest number of friends that Mr. White can invite to his party so that the party will be interesting.

Example:
first = ["snakes", "programming", "cobra", "monty"]
second = ["python", "python", "anaconda", "python"]
Output: 3
"""


def interesting_party1(first, second):
    ans = 0
    for i in range(len(first)):
        f = 0
        s = 0
        for j in range(len(first)):
            if first[i] == first[j]:
                f += 1
            if first[i] == second[j]:
                f += 1
            if second[i] == first[j]:
                s += 1
            if second[i] == second[j]:
                s += 1
        ans = max(f, s, ans)
    return ans

