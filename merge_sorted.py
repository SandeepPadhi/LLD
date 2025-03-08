

def merge_recursive(l1,l2):
    if not l1:
        return l2
        
    if not l2:
        return l1
        
    if l1[0]<l2[0]:
        return [l1[0]]+merge_recursive(l1[1:],l2)
    else:
        return [l2[0]]+merge_recursive(l1,l2[1:])
        

def merge_interative(l1,l2):
    merge=[]
    i=0
    j=0
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            merge.append(l1[i])
            i+=1
        else:
            merge.append(l2[j])
            j+=1
    
    merge.extend(l1[i:])
    merge.extend(l2[j:])
    return merge
l1=[2,4,8,10]
l2=[1,3,5,7]

l_recursive_merge=merge_recursive(l1,l2)
print(f"l_merge:{l_recursive_merge}")

l_interactive_merge=merge_interative(l1,l2)
print(f"l_interative:{l_interactive_merge}")