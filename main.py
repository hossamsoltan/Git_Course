import digital_numbers as n
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%H:%M:%S")
h1 = dt_string[0]
h2 = dt_string[1]
m1 = dt_string[3]
m2 = dt_string[4]
s1 = dt_string[6]
s2 = dt_string[7]
h1=n.ret_num(h1)
h2=n.ret_num(h2)
m1=n.ret_num(m1)
m2=n.ret_num(m2)
s1=n.ret_num(s1)
s2=n.ret_num(s2)
print(h1[0:3]+" "+h2[0:3]+"   "+m1[0:3]+" "+m2[0:3]+"   "+s1[0:3]+" "+s2[0:3])
print(h1[4:7]+" "+h2[4:7]+" : "+m1[4:7]+" "+m2[4:7]+" : "+s1[4:7]+" "+s2[4:7])
print(h1[8:11]+" "+h2[8:11]+" : "+m1[8:11]+" "+m2[8:11]+" : "+s1[8:11]+" "+s2[8:11])
print(h1[12:15]+" "+h2[12:15]+"   "+m1[12:15]+" "+m2[12:15]+"   "+s1[12:15]+" "+s2[12:15])