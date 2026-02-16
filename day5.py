m=int(input("enter size"))
resources=[]
for i in range (m) :
    n=int(input("enter values"))
    resources=resources+[n]
print(resources)
name="kundana kartika chowdary"
l=len(name)-name.count(" ")
valid_requests=0
removed_requests=0
invalid_request=0
low_demand=[]
medium_demand=[]
high_demand=[]
invalid_requests=[]
for i in range (m) :
    if resources[i]<0 :
        invalid_requests=invalid_requests+[resources[i]]
        invalid_request+=1
    elif resources[i]==0 :
        print(resources[i],"no demand")
        valid_requests+=1
    elif resources[i]>0 and resources[i]<=20 :
        valid_requests+=1
        low_demand=low_demand+[resources[i]]
    elif resources[i]>20 and resources[i]<=50 :
        valid_requests+=1
        medium_demand=medium_demand+[resources[i]]
    else :
        valid_requests+=1
        high_demand=high_demand+[resources[i]]
print("low demand :",low_demand)
print("medium demand :",medium_demand)
print("high demand :",high_demand)
pli=l%3
if pli==0 :
    removed_requests+=len(low_demand)
    low_demand=[]
elif pli==1 :
    removed_requests+=len(high_demand)
    high_demand=[]
elif pli==2 :
    removed_requests+=len(low_demand)+len(high_demand)
    low_demand=[]
    high_demand=[]
print("total valid requests :",valid_requests)
print("total invalid requests :",invalid_request)
print(name)
print("l :",l)
print("pli :",pli)
print("total removed due to personalization :",removed_requests)
print("after applying personalized logic :")
print("low demand :",low_demand)
print("medium demand :",medium_demand)
print("high demand :",high_demand)





