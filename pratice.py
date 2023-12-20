arr =[
    "apple",
    "orange",
    "grapes",
    "apple",
    "tony",
    "strak",
    "caption",
    "america",
    "tony",
    "thanos",
    "thor"
]

#num = []
#for a in arr:
#    if a not in num:
#        num.append(a)
#        print(a)                        #print in array         
#                                       #print softlogic as differnt letter output

num = []
for a in range(len(arr)):
    if a not in num:
        num.append(a)
        print(arr[a])