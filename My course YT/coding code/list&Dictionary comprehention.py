#list comprehension
# square = [i*i for i in range(1,11)]
# print(square)

# checking=[x  if x>=20  else "NO"  for x in square ]
# print(checking)




#dictionary comprehension
city_limit={"chennai": 40,"banglore":50,"delhi":20,"goa":80,"pune":40}
city_miles ={key: x*100 for(key,x) in city_limit.items()}
print(city_miles)

city_check ={ key: value for(key ,value)in city_limit.items() if value >=40}
city_newcheck={key:value if value >=50 else "no" for(key,value) in city_limit.items()  }
print(city_check)
print(city_newcheck)
