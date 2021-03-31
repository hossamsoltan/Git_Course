zero=""" _ 
| |
|_|"""
one="""   
|  
|  
   """
two=""" _ 
 _|
|_ """
three=""" _ 
 _|
 _| """
four="""   
|_|
  |"""
five=""" _ 
|_ 
 _|"""
six=""" _ 
|_ 
|_|"""
seven=""" _ 
  |
  |"""
eight=""" _ 
|_|
|_|"""
nine=""" _ 
|_|
 _|"""

def ret_num(n):
    if n == "0":
        return zero
    elif n == "1":
        return one
    elif n == "2":
        return two
    elif n == "3":
        return three
    elif n == "4":
        return four
    elif n == "5":
        return five
    elif n == "6":
        return six
    elif n == "7":
        return seven
    elif n == "8":
        return eight    
    elif n == "9":
        return nine
    else :
        return zero
# print(zero)
# print(one)
# print(two)
# print(three)
# print(four)
# print(five)
# print(six)
# print(seven)
# print(eight)
# print(nine)