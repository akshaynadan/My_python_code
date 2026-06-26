#store = [("Shirt",200),("Pant",250),("Suit",1500),("T-shirt",500),("Shorts",150),("Hat",999),("Glasses",800)]
#store.sort()
#print(store)
#b=lambda x:x[1]*20
#store.sort(key=b)
#print(store)
store = (("Shirt",200),("Pant",250),("Suit",1500),("T-shirt",500),("Shorts",150),("Hat",999),("Glasses",800))
b = sorted(store,key=lambda x:x[1])
print(b)
m = lambda x:(x[0],x[1]*20)
c = list(map(m,store))
c=sorted(c,key=lambda x:x[1])
print(c)

fil =lambda x:x[1]>600 
costly = list(filter(fil,store))
costly = sorted(costly,key=lambda x:x[1])
print(costly)
