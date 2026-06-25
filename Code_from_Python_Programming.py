'''sms_users = {'Alice', 'Bob', 'John',' Jane', 'Zapi'} 
data_users = {'John', 'Mary', 'Alice', 'Zapi'}'''

'''num=(1,2,3,4,3,2,2,1,4,5,8)
cnt=num.count(3)
print("count of 2 is:",cnt)
cnt=num.count(10)
print("count of 10:",cnt)
print(sorted(num))
print(num.count(2))'''

'''t1=('p','y','t','o','n','p')
indx=t1.index('n')
print("indx:",t1.index('n'))
print(t1)'''


Days1={"Mon","Tue","Wed","Sat"}
Days2={"Thr","Fri","Sat","Sun","Mon"}
x=Days1&Days2
y=Days1|Days2
z=Days1-Days2
W=Days1^Days2
print("x:",Days1 & Days2)
print("Y:",Days1|Days2)
print("z:", Days1-Days2)
print("w:",Days1^Days2)
print("len of Days2:", len(Days2))
print("max of Days2:",max(Days2))
print("sorted of Days1:",sorted(Days1))
set1=set("python")
print(set1)
Days1.add("Fri")
Days1.add("Sun")
print(Days1)
Days2.update(["Tue"])
print(Days2)
