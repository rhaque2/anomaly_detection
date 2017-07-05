import pandas as pd
from pylab import *
import os.path
import json


data = []
with open('batch_log.json') as f:     # opening the file
    for line in f:
        data.append(json.loads(line));    # appending data line by line

print("Checkpoint 1")

first = data[0];
D = first['D'];
T = first['T'];       
del data[0];

df = pd.DataFrame(data);

purchase = df[df['event_type'] == 'purchase'];
befriend = df[df['event_type'] == 'befriend'];
unfriend = df[df['event_type'] == 'unfriend'];
             
print("Checkpoint 2")        


# Befriending     

befriend_ids = befriend.iloc[:,[3,4]];   # index out id1 and id2

id1_list = list(befriend_ids.id1)    # turn ids into list
id2_list = list(befriend_ids.id2)
    
id1 = int64(id1_list);        # turn ids into integers
id2 = int64(id2_list);                            

f1 = {};                     # make a dictionary of friends
for m, n in zip(id1, id2):
    f1.setdefault(m, []).append(n);
    f1.setdefault(n, []).append(m);              

print("Checkpoint 3")

if D >= '2':
    f2 = {};              # make a dictionary of friends of friends
    for i in f1:
        for j in f1[i]:
            f2.setdefault(i, []).append(f1[i] + f1[j])    
            # created multiple possiblities
    print("Checkpoint 4")        
    
    for a in f2: 
        f2[a].sort(key = len);    # sorts the lists by length                  
        for b in f2[a]:
            b.remove(a)        # remove duplicate ids
            b.sort()           # sort the ids 
              
    print("Checkpoint 5")   
                     
    for c in f2:
        while len(f2[c]) > 1:
            del f2[c][0]           # delete all the extra lists

    print("Checkpoint 6: Friends of Friends Network Created")  
else:
    print("Checkpoint 4: Friends Network Created") 


# Unfriending

unfriend_ids = unfriend.iloc[:,[3,4]];   # index out id1 and id2

id1_list2 = list(unfriend_ids.id1);    # turn ids into list
id2_list2 = list(unfriend_ids.id2);
    
id1_un = int64(id1_list2);        # turn ids into integers
id2_un = int64(id2_list2);                            

for key, value in zip(id1_un, id2_un):    
    f1[key].remove(value)
    f1[value].remove(key)

print("Checkpoint 7: Unfriending Update Complete")  

f2 = {};              # make a dictionary of friends of friends
for i in f1:
    for j in f1[i]:
        f2.setdefault(i, []).append(f1[i] + f1[j])    
        # created multiple possiblities      
    
for a in f2: 
    f2[a].sort(key = len);    # sorts the lists by length                  
    for b in f2[a]:
        b.remove(a)        # remove duplicate ids
        b.sort()           # sort the ids   
                     
for c in f2:
    while len(f2[c]) > 1:      
        del f2[c][0]           # delete all the extra lists
        
print("Checkpoint 8: Friends of Friends Network with Unfriends Update")               
                           
# Purchase History 

purchase_ids = purchase.iloc[:,[0,2]];   # index out id and amount

string_ids = []
string_amounts = []
for number1, number2 in zip(purchase_ids.id, purchase_ids.amount):
    string_ids.append(str(number1));      # turn the ids into strings
    string_amounts.append(str(number2));  # turn the amounts into strings
    
print("Checkpoint 9")                         
                            
network = {} # this network dictionary will hold the user and his entire network
for user in f2:
    network.setdefault(user, []).append(str(user)+', '+str(f2[user]))  

print("Checkpoint 10") 
                   
save_path = 'C:/Users/Ruhul/Desktop/anomaly_detection-master/anomaly_detection-master/log_output'
social_network = os.path.join(save_path, "social_network.txt")         

the_file = open(social_network, "w")
for item in network:
    the_file.write("%s\n" % network[item])  # write list of users' networks to txt file 
  
the_file.close()

print("Checkpoint 11: Output Written to social_network.txt") 


speed = 0
history = {}
for f, g in zip(string_ids, string_amounts): 
    for h in network:
        if f in str(network[h]):
            history.setdefault(h, []).append('(' + str(f) + ', ' + str(g) + ')')
            if len(history[h]) > 50:
                history[h] = history[h][:50];    # stop at 50 purchases
                break
    speed += 1;    
    if(speed % 100 == 0):
        print(speed)   # checking how fast the code is running  

print("Checkpoint 12: Purchase History Updated")     
           

save_path = 'C:/Users/Ruhul/Desktop/anomaly_detection-master/anomaly_detection-master/log_output'
purchase_history = os.path.join(save_path, "purchase_history.txt")         

the_file = open(purchase_history, "w")
for entry in history:
    the_file.write("%s\n" % entry)
    the_file.write("%s\n" % history[entry])  # write list of users' networks to txt file 
  
the_file.close()

print("Checkpoint 13: Output Written to purchase_history.txt") 


       