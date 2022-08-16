# import bisect

# #initialize
# lst = [1, 3, 4, 4, 4, 6, 7]

# #using bisect() to find index to insert new element
# # returns 5 ( right most possible index )
# print ("The rightmost index to insert, so list remains sorted is  : ", end="")
# print (bisect.bisect(lst, 4))

# # using bisect_left() to find index to insert new element
# # returns 2 ( left most possible index )
# print ("The leftmost index to insert, so list remains sorted is  : ", end="")
# print (bisect.bisect_left(lst, 4))

# # using bisect_right() to find index to insert new element
# # returns 4 ( right most possible index )
# print ("The rightmost index to insert, so list remains sorted is  : ", end="")
# print (bisect.bisect_right(lst, 4, 0, 4))


# # initializing list
# li1 = [1, 3, 4, 4, 4, 6, 7]
  
# # initializing list
# li2 = [1, 3, 4, 4, 4, 6, 7]
  
# # initializing list
# li3 = [1, 3, 4, 4, 4, 6, 7]
  
# # using insort() to insert 5 at appropriate position
# # inserts at 6th position
# bisect.insort(li1, 5)
  
# print ("The list after inserting new element using insort() is : ")
# print(li1)
  
# # using insort_left() to insert 5 at appropriate position
# # inserts at 6th position
# bisect.insort_left(li2, 5)
  
# print("\r")
  
# print ("The list after inserting new element using insort_left() is : ")
# print(li2)
  
# print("\r")
  
# # using insort_right() to insert 5 at appropriate position
# # inserts at 5th position
# bisect.insort_right(li3, 5, 0, 4)
  
# print ("The list after inserting new element using insort_right() is : ")
# print(li3)


from operator import imod


ll = [1,2,3,4,4,6,6,10,12]

import bisect

print(bisect.bisect_right(ll,11))