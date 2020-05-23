MyList = ["a", "b", "c", "b", "c", "a", "c", "a", "c", "b"]
my_dict = {i:MyList.count(i) for i in MyList}
print(my_dict) 
