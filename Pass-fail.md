'
+ [Course Schedule II](#course-schedule-ii)
+ [Course Schedule](#course-schedule)
+ [Number of Islands](#number-of-islands)
+ [Is Graph Bipartite?](#is-graph-bipartite)
+ [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)
+ [Shortest Path in Binary Matrix](#shortest-path-in-binary-matrix)
+ [Maximum Depth of N-ary Tree](#maximum-depth-of-n-ary-tree)
+ [Min Stack](#min-stack)
+ [Implement Queue using Stacks](#implement-queue-using-stacks)
+ [Implement Stack using Queues](#implement-stack-using-queues)
+ [House Robber II](#house-robber-ii)
+ [House Robber](#house-robber)
+ [Design Twitter](#design-twitter)
+ [Merge k Sorted Lists](#merge-k-sorted-lists)
+ [K Closest Points to Origin](#k-closest-points-to-origin)<---end.markdown links--->'
## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

``` python
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    if not prerequisites:
        return [i for i in range(0, numCourses)]
    nextCourseDic = {i: [] for i in range(0, numCourses)}
    pendingPrereqCountList = [0] * numCourses
    for course, prereq in prerequisites:
        nextCourseDic[prereq].append(course)
        pendingPrereqCountList[course] += 1
    coursesWithoutPrereq = [course for course, prereqCount in enumerate(pendingPrereqCountList) if prereqCount == 0]
    if not coursesWithoutPrereq:
        return []
    queue = deque([course, nextCourseDic.get(course)] for course in coursesWithoutPrereq)
    ans = []
    while queue:
        course, nextCourses = queue.popleft()
        ans.append(course)
        while nextCourses:
            nextCourse = nextCourses.pop(0)
            pendingPrereqCountList[nextCourse] -= 1
            if pendingPrereqCountList[nextCourse] == 0:
                queue.append([nextCourse, nextCourseDic[nextCourse]])
    return ans if len(ans) == numCourses else []
```
## Course Schedule

https://leetcode.com/problems/course-schedule/

``` python
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    inEdges = {i: set() for i in range(numCourses)}
    outEdges = {i: set() for i in range(numCourses)}  
    for course, reqCourse in prerequisites:
        inEdges[course].add(reqCourse)
        outEdges[reqCourse].add(course)
    q = deque()
    for sVertex in inEdges:
        if len(inEdges[sVertex]) == 0:
            q.append(sVertex)
    while q:
        sVertex = q.popleft()
        for tVertex in outEdges[sVertex]:
            inEdges[tVertex].remove(sVertex)
            if len(inEdges[tVertex]) == 0:
                q.append(tVertex)
        inEdges.pop(sVertex)
    return len(inEdges) == 0
```

## Number of Islands

https://leetcode.com/problems/number-of-islands/

``` python
def numIslands(self, grid: List[List[str]]) -> int:
    number = 0
    world = grid
    def flood(i, j):
        nonlocal world
        if world[i][j] == '1':
            world[i][j] = '0'
            if i+1 < len(world):
                flood(i+1, j)
            if j+1 < len(world[0]):
                flood(i, j+1)
            if i-1 > -1:
                flood(i-1, j)
            if j-1 > -1:
                flood(i, j-1)
    for a in range(len(world)):
        for b in range(len(world[a])):
            if world[a][b] == '1':
                number += 1
                flood(a, b)
    return number
```
## Is Graph Bipartite?

https://leetcode.com/problems/is-graph-bipartite/

``` python
def isBipartite(self, graph: List[List[int]]) -> bool:
    colors = [0]*len(graph)    
    
    def dfs(node: int, node_color: int) -> bool:    
        if colors[node] != 0:                       
            return colors[node] == node_color    
        colors[node] = node_color               
        for neighbor in graph[node]:              
            if not dfs(neighbor, -1*node_color):  
                return False                        
        return True
    for node in range(len(graph)):
        if colors[node] == 0 and not dfs(node, 1): 
            return False        
    return True
```
## Cheapest Flights Within K Stops

https://leetcode.com/problems/cheapest-flights-within-k-stops/

``` python
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    if src == dst: return 0
    if len(flights) == 0 or len(flights[0]) == 0: return -1
    dp = [float(inf)]*n
    dp[src] = 0
    for k in range(1, K+2):
        last_k = dp[:]
        for fm, to, price in flights:
            dp[to] = min(price+last_k[fm], last_k[to], dp[to])
    if dp[dst] == float(inf): return -1
    return dp[dst]
```
## Shortest Path in Binary Matrix

https://leetcode.com/problems/shortest-path-in-binary-matrix/

``` python
def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    N, M = len(grid), len(grid[0])
    if grid[0][0] == 1:
        return -1
    q = deque()
    directions = [(-1, 1), (0, 1), (1, 0), (1, 1), (0, -1), (-1 ,0), (-1, -1), (1, -1)]
    if grid[0][0] == 0:
        q.append((1, (0, 0)))
        grid[0][0] = 1
    while q:
        steps, tmp = q.popleft()
        r, c = tmp[0], tmp[1]
        if(r, c) == (N-1, M-1):
            return steps
        for i, j in directions:
            newr, newc = r+i, c+j
            if 0 <= newr < N and 0 <= newc < M and grid[newr][newc] == 0:
                q.append((steps+1, (newr, newc)))
                grid[newr][newc] = 1
    return -1
```
## Maximum Depth of N-ary Tree

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

``` python
def maxDepth(self, root: 'Node') -> int:
    if root is None:
        return 0
    else:
        maxi = 0
        for i in root.children:
            maxi = max(maxi, self.maxDepth(i))
        return 1 + maxi
```
## Min Stack

https://leetcode.com/problems/min-stack/

``` python
def __init__(self):
    self.stack = []
def push(self, val: int) -> None:
    if self.stack:
        if val <= self.stack[-1][1]:
            self.stack.append((val, val))
        else:
            self.stack.append((val, (self.stack[-1][1])))
    else:
        self.stack.append((val, val))
def pop(self) -> None:
    self.stack.pop()
def top(self) -> int:
    return self.stack[-1][0]
def getMin(self) -> int:
    return self.stack[-1][1]
```
## Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/

``` python
def __init__(self):
    """
    Initialize your data structure here.
    """
    self.stack1 = []
    self.stack2 = []
def push(self, x: int) -> None:
    """
    Push element x to the back of queue.
    """
    self.stack1.append(x)
def popUtil(self):
    if not self.stack2:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
def pop(self) -> int:
    """
    Removes the element from in front of queue and returns that element.
    """
    self.popUtil()
    return self.stack2.pop()
def peek(self) -> int:
    """
    Get the front element.
    """
    self.popUtil()
    return self.stack2[-1]
def empty(self) -> bool:
    """
    Returns whether the queue is empty.
    """
    return True if not self.stack1 and not self.stack2 else False
```
## Implement Stack using Queues

https://leetcode.com/problems/implement-stack-using-queues/

``` python
def __init__(self):
    """
    Initialize your data structure here.
    """
    self.stack = []
def push(self, x: int) -> None:
    """
    Push element x onto stack.
    """
    self.x = x
    self.stack.append(self.x) 
def pop(self) -> int:
    """
    Removes the element on top of the stack and returns that element.
    """
    return self.stack.pop()
def top(self) -> int:
    """
    Get the top element.
    """
    return self.stack[-1]
def empty(self) -> bool:
    """
    Returns whether the stack is empty.
    """
    return len(self.stack) == 0
```
## House Robber II

https://leetcode.com/problems/house-robber-ii/

``` python
def rob(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    nums_1 = nums[1:]
    nums_2 = nums[:len(nums)-1]
    prev_1 = 0
    cur_1 = nums_1[0]
    prev_2 = 0
    cur_2 = nums_2[0]
    for i in range(2, len(nums_1) + 1):
        temp = cur_1
        cur_1 = max(prev_1 + nums_1[i-1], cur_1)
        prev_1 = temp
        temp = cur_2
        cur_2 = max(prev_2 + nums_2[i-1], cur_2)
        prev_2 = temp
    return max(cur_1, cur_2)
```
## House Robber

https://leetcode.com/problems/house-robber/

``` python
def rob(self, nums: List[int]) -> int:
    prev = cur = 0
    for i in nums:
        prev, cur = cur, max(cur, prev+i)  
    return cur
```
## Design Twitter

https://leetcode.com/problems/design-twitter/

``` python
def __init__(self):
    """
    Initialize your data structure here.
    """
    self.tweetUsers = {}   
    self.timestamp = 0
def postTweet(self, userId: int, tweetId: int) -> None:
    """
    Compose a new tweet.
    """
    if userId in self.tweetUsers:
        self.tweetUsers[userId]["tweets"][tweetId] = self.timestamp
    else:
        self.tweetUsers[userId] = {}
        self.tweetUsers[userId]["tweets"] = {tweetId: self.timestamp}
        self.tweetUsers[userId]["following"] = {}
    self.timestamp += 1
def getNewsFeed(self, userId: int) -> List[int]:
    """
    Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
    """
    newsFeed = []
    if userId in self.tweetUsers:
        for tweetId in self.tweetUsers[userId]["tweets"]:
            newsFeed.append((tweetId, self.tweetUsers[userId]["tweets"][tweetId]))
        
        for followeeId in self.tweetUsers[userId]["following"]:
            for tweetId in self.tweetUsers[followeeId]["tweets"]:
                newsFeed.append((tweetId, self.tweetUsers[followeeId]["tweets"][tweetId]))
    newsFeed.sort(key=lambda x: x[1], reverse=True)
    
    if len(newsFeed) >= 10:
        newsFeed = newsFeed[:10]
    
    newsFeed = [tweetId for tweetId, timestamp in newsFeed]
    
    return newsFeed
def follow(self, followerId: int, followeeId: int) -> None:
    """
    Follower follows a followee. If the operation is invalid, it should be a no-op.
    """
    if followerId != followeeId:
        if followerId in self.tweetUsers:
            self.tweetUsers[followerId]["following"][followeeId] = True
            if followeeId not in self.tweetUsers:
                self.tweetUsers[followeeId] = {"tweets": {}, "following": {}}
        else:
            self.tweetUsers[followerId] = {"tweets": {}, "following": {followeeId: True}}
            if not followeeId in self.tweetUsers:
                self.tweetUsers[followeeId] = {"tweets": {}, "following": {}}
        
def unfollow(self, followerId: int, followeeId: int) -> None:
    """
    Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    """
    if followerId != followeeId:
        if followerId in self.tweetUsers and followeeId in self.tweetUsers[followerId]["following"]:
            del self.tweetUsers[followerId]["following"][followeeId]
```
## Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists/

``` python
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    self.nodes = []
    head = point = ListNode(0)
    for i in lists:
        while i is not None:
            self.nodes.append(i.val)
            i = i.next
    for j in sorted(self.nodes):
        point.next = ListNode(j)
        point = point.next
    return head.next
```
## K Closest Points to Origin

https://leetcode.com/problems/k-closest-points-to-origin/

``` python
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    dict = {}
    a = 0
    for i in points:
        dict[a] = (i[1]**2+i[0]**2)**(0.5)
        a += 1
    list_dict = list(dict.items())
    list_dict.sort(key=lambda i: i[1])
    j = 0
    res = []
    while j < k:
        res.append(points[list_dict[j][0]])
        j += 1
    return res
```