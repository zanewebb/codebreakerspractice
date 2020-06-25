
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