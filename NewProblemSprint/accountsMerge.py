#I keep forgetting the deque part of the solution. Need to use a set and queue to BFS the graph
#  
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailtoname = {}
        emailtoemails = collections.defaultdict(set)
        
        
        for a in accounts:
            name = a[0]
            emails = a[1:]
            
            for e in emails:
                emailtoname[e] = name
                emailtoemails[emails[0]].add(e)
                emailtoemails[e].add(emails[0])
                
        print(emailtoemails)
        
        ans = []
        seen = set()
        
        for k in emailtoemails:
            if k not in seen:
                seen.add(k)
                accts = []
                queue = deque([k])
                while queue:
                    a = queue.pop()
                    accts.append(a)
                    
                    for e in emailtoemails[a]:
                        if e not in seen:
                            seen.add(e)
                            queue.append(e)
                
                ans.append([emailtoname[k]]+sorted(accts)) 
        
        return ans
        
        
        


# so close, still screwed it up
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailtoname = {}
        graph = collections.defaultdict(set)
        
        for a in accounts:
            for e in sorted(a[1:]):
                emailtoname[e] = a[0]
                graph[a[1]].add(e)
                graph[e].add(a[1])
        
        # print(graph)
        
        ans = []
        seen = set()
        
        for k in graph:
            if k not in seen:
                seen.add(k)
                accts = []
                queue = deque([k])
                while queue:
                    a = queue.pop()
                    accts.append(a)
                    
                    for e in graph[a]:
                        if e not in seen:
                            seen.add(e)
                            queue.append(e)
                
                ans.append([emailtoname[k]]+sorted(accts))    
        
        return ans
        
        


# still having a hard time remembering this solution

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailtoname = {}
        emailtoemail = collections.defaultdict(set)
        
        for a in accounts:
            name = a[0]
            accts = a[1:]
            
            for e in accts:
                emailtoname[e] = name
                emailtoemail[accts[0]].add(e)
                emailtoemail[e].add(accts[0])
                
        seen = set()
        ans = []
        for e in emailtoemail:
            if e not in seen:
                stack = [e]
                acct = []
                seen.add(e)
                # stack.append[list(emailtoemail[e])]
                
                while len(stack) > 0:
                    email = stack.pop()
                    acct.append(email)
                    
                    for linkedemail in emailtoemail[email]:
                        if linkedemail not in seen:
                            seen.add(linkedemail)
                            stack.append(linkedemail)
                ans.append([emailtoname[e]] + sorted(acct))
        
        return ans
        


# didnt remember the better solution, dam
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        people = collections.defaultdict(list)
        
        '''
        The datastructure should be
        {
            John: [
                {"johnsmith@mail.com", "john00@mail.com", "john_newyork@mail.com"},
                {"johnnybravo@mail.com"}
            ],
            Mary: [
                {"mary@mail.com"}
            ]
        }
        '''
        
        # look through our accounts
        for a in accounts:
            name = a[0]
            # if we have this person on file potentially
            if name in people:
                added = False
                # check each email set
                for emailset in people[name]:
                    # verify that this is the same person we're referring to
                    for e in a[1:]:
                        if e in emailset:
                            # union the emails from this account
                            # and the known emails for this person
                            people[name].remove(emailset)
                            emailset = emailset.union(set(a[1:]))
                            people[name].append(emailset)
                            added = True
                            
                if not added:
                    people[name].append(set(a[1:]))    
            else:
                people[name].append(set(a[1:]))
        
        
        ans = []
        for p in people:
            for es in people[p]:
                ans.append([p] + sorted(list(es)))
        
        return ans


# weird dfs solution, think of it as a graph
class Solution(object):
    def accountsMerge(self, accounts):
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name

        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans


# couldnt get it to work

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = collections.defaultdict(list)
        '''
        {
            "name": [set()]
        }
        '''
        
        # iterate over the accounts
        for a in accounts:
            # if the name isnt in the dict then add all emails
            # as a set within a list as a value to the key of the name
            if a[0] not in emails:
                # convert all the emails into a set
                emails[a[0]].append(self.emailsToSet(a[1:]))
                
                continue
                
            
            # if we find the name, iterate over the list of sets
            added = False
            for es in emails[a[0]]:
                # if the intersection of this account's emails 
                # and the current set has a len > 0
                # update this set to be the union of the two
                emailset = self.emailsToSet(a[1:])
                if len(emailset.intersection(es)) > 0:
                    emails[a[0]].remove(es)
                    emails[a[0]].append(emailset.union(es))
                    added = True
                    break
                    
            # if we didnt add it as a union then we add it to the list
            if not added:
                emails[a[0]].append(self.emailsToSet(a[1:]))
                
        # construct the output
        ans = []
        for name in emails.keys():
            for emailset in emails[name]:
                emaillist = list(emailset)
                acct = [name] + sorted(emaillist)
                ans.append(acct)
        
        return ans
    
    
    
    
        
    def emailsToSet(self, a):
        if len(a) > 1:
            emailset = set(a)

        # if theres only one email then just add it
        else:
            emailset = set()
            emailset.add(a[0])
        
        return emailset