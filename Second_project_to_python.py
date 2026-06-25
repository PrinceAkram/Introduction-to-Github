# Qn5. telecom operators region
operatorA ={'kigali','musanze','bugesera','huye'}
operatorB={'kigali','rubavu','bugesera','rusizi','kayonza'}
print(operatorA&operatorB)# the regions both operator have
print(operatorA-operatorB)# the region unique to operatorA
print(operatorB-operatorA)# the region unique to operatorB
print(type("operatorA and operatorB"))# the type of both operators


# Qn6.telecom company tracks
sms_users = {'Alice', 'Bob', 'John',' Jane', 'Zapi'}
data_users = {'John', 'Mary', 'Alice', 'Zapi'}
print(sms_users & data_users)# the users  who uses both services
print(sms_users - data_users)# the users  who uses only one services
print(data_users - sms_users)# the users  who uses only one services
print(sms_users | data_users)# the users  who uses all services
print(type("sms_users & data_users"))# the type of both sevices

#Qn7. triangle
n=5
for i in range(n):
    print(str (n-i) * (i+1))
    
    
