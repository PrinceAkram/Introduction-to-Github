
start= (4)
end=(32)
print (f"prime number between {start} and {end}are: ")
for num in range (start,end+1):

        for i in range (2,num):
            if num % i ==0:
                break
        else:
            print(num)
            

#Qn4.
telecom =('MTN', '4G', 1200)
Network, Technology, Data_Usage = telecom  # unpacking tuple
print("Network: ", Network)
print(type(Network))
print("Technology: ", Technology)
print(type(Technology))
print("Data_Usage: ", Data_Usage)
print(type(Data_Usage)) 

# Qn3.
cities=[('Kigali', 2300),('Musanze', 1800), ('Huye', 1500)]
for city, signal in cities:
    print(f"city: {city}, signal strength: {signal}")
    
# Qn1.
dropped_calls = [7,9,8,15,12,16,13,14,11,10]
average= sum(dropped_calls) / len(dropped_calls)
print ("average number:", average)
total= sum(dropped_calls)
print ("total number:", total)

#Qn2.
signal_strengths= [-79,-93,-90,-77,-80]
print("Signal Strengths:", signal_strengths)
strongest_signal= max(signal_strengths)
print ("strongest_signal:", strongest_signal, "dBm")
weakest_signal= min(signal_strengths)
print ("weakest_signal:", weakest_signal, "dBm")
cell_towers=["Tw_01", "Tw_02","Tw_03", "Tw_04","Tw_05"]
# use .index() to find which tower corresponds to each value.
strongest_signal = signal_strengths.index(strongest_signal)
weakest_signal = signal_strengths.index(weakest_signal)
towers_strongest = cell_towers[strongest_signal]
towers_weakest = cell_towers[weakest_signal]
print("\nTowers with Strongest Signal:", towers_strongest)
print("Towers with Weakest Signal:", towers_weakest)
