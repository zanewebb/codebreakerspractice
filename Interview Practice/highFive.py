# second time, smarter approach. maybe quicker
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items = sorted(items, key=lambda x: (x[0], -x[1]))
        ans = []
        
        print(items)
        
        studentID = items[0][0]
        totalscore = 0
        count = 0
        for i in items:
            if studentID != i[0]:
                ans.append([studentID, totalscore // count])
                studentID = i[0]
                totalscore = 0
                count = 0
            
            if count < 5:
                count += 1
                totalscore += i[1]
            
        ans.append([studentID, totalscore // count])
        
        return ans


# first time, probably pretty slow but
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students = collections.defaultdict(list)
        
        for test in items:
            students[test[0]].append(test[1])
         
        output = []
        
        for studentID, scores in students.items():
            #heapq.heapify(scores)
            top5avg = sum(heapq.nlargest(5, scores)) // 5
            output.append([studentID, top5avg])
        
        
        output = sorted(output, key= lambda x: x[0])
        return output