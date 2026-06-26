
#for i in authors:
    #print(
#uthor_dic = {"Harper Lee": "To Kill a Mockingbird","Douglas Adams": "The Hitchhiker's Guide to the Galaxy","J.K. Rowling": "Harry Potter and the Philosopher's Stone","Stephen King": "The Shining","George Orwell": "1984","J.R.R. Tolkien": "The Lord of the Rings"}
#author_dict = sorted(author_dic.items())
#print(author_dict)
import functools

new_list=[("honda",2012,3),("toyota",2006,4),("ford",2021,5),("chevy",1998,6),("nissan",2000,2)]
sorted_list = sorted(new_list,key = lambda x:x[1])
# for i in sorted_list:
#     print(i)
# print(new_list)
print(sorted_list)
year = functools.reduce(lambda x,y:x+y[1],sorted_list,0)
print(year)

