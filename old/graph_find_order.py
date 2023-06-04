from collections import deque, defaultdict

def findOrder( numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    courses = defaultdict(list)
    prereqs = [0] * numCourses
    
    # Build graph and count indegrees
    for x, y in prerequisites:
        courses[x].append(y)
        prereqs[y] += 1
        
    q = deque()
    for i, n in enumerate(prereqs):
        if n == 0:
            q.append(i)
            
    courses_taken = 0
    path = []
    
    while q:
        curr = q.popleft()
        path.append(curr)
        courses_taken += 1
        for nei in courses[curr]:
            prereqs[nei] -= 1
            if prereqs[nei] == 0:
                q.append(nei)
                
    return  path[::-1] if courses_taken == numCourses else []



findOrder(4,[[1,0],[2,0],[3,1],[3,2]])