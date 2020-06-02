from array import array
my_array = array('i', [10, 20, 30, 100, 50])
buffer_info = (my_array.buffer_info())
print(buffer_info)

