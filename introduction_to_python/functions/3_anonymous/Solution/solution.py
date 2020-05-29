def anomy(*l):
    result=list(filter(lambda x:(x%13==0),l))
    return result 

result=anomy(13,26,30,200,20,56,2197)
print(result)