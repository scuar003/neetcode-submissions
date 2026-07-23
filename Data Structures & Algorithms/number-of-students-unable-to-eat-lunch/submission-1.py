class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = deque(students)
        res =  n #student who did not eat 

        for snd in sandwiches:
            cnt = 0
            while cnt < n and q[0] != snd:
                curr = q.popleft()
                q.append(curr)
                cnt +=1
            if q[0] == snd:
                q.popleft()
                res -= 1
            else: 
                break 

        return res 