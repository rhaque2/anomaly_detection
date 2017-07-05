import pandas as pd
from pylab import *
import numpy as np
import os.path
import json
import re


save_path = 'C:/Users/Ruhul/Desktop/anomaly_detection-master/anomaly_detection-master/log_output'
purchase_history = os.path.join(save_path, "purchase_history.txt")         

f = open(purchase_history, "r")        # reading purchase history file
lines = f.readlines()

f.close()

print("Checkpoint 1")

user_network = []
purchases = []
for index in range(0, 19998):
    if index % 2 == 0:
        user_network.append(lines[index])   # getting network information 
    else:
        purchases.append(lines[index])      # getting purchase history

print("Checkpoint 2")

df = pd.DataFrame(user_network);
df['purchases'] = purchases;            # creating dataframe columns   
df['user_network'] = user_network;
df = df.iloc[:,[1,2]];   
df_purchases = df.purchases.tolist();   # turning dataframe into list 

print("Checkpoint 3")      
                                  
amounts = [];
for p in df_purchases:
    line = p.rstrip();
    x = re.findall(', .*?\)\',', line);
    amounts.append(x);

amounts2 = [''.join(q) for q in amounts];  # turns list of lists into list of strings

print("Checkpoint 4")

amounts3 = [];
for r in amounts2: 
    s1 = r.replace(",", "");      # remove all commas
    s2 = s1.replace(")", "");     # remove all end parentheses
    s3 = s2.replace("'", "");     # remove all apostrophes
    amounts3.append(s3);        

print("Checkpoint 5")

amounts4 = [];
for t in amounts3:
    u = t.split();    # turn numbers into a list
    amounts4.append(u);

network_mean = [];
network_std = [];
for v in amounts4:
    w = [float(i) for i in v];   # turn number strings into floats
    y1 = np.mean(w);          # mean of floats from lists for each user network
    y2 = np.std(w);            # standard deviation of floats from lists for each user network
    z1 = float("%.2f" % y1);    # round floats to 2 decimal places
    z2 = float("%.2f" % y2);    # round floats to 2 decimal places
    network_mean.append(z1);
    network_std.append(z2);                   

print("Checkpoint 6")


save_path2 = 'C:/Users/Ruhul/Desktop/anomaly_detection-master/anomaly_detection-master/sample_dataset'
stream_log = os.path.join(save_path2, "stream_log.txt")         

g = open(stream_log, "r")
stream = g.readlines()

g.close()
  
print("Checkpoint 7")


new_purchases = [];
new_befriends = [];
new_unfriends = [];                
for string in stream:
    if "purchase" in string:
        new_purchases.append(string);
    elif "befriend" in string:
        new_befriends.append(string);
    elif "unfriend" in string:
        new_unfriends.append(string);
           
extraction = [];
for a in new_purchases:
    b = a.rstrip();
    x = re.findall('"id": .*?\}', b);    # extract strings with ids and amounts 
    extraction.append(x);

extraction2 = [''.join(e) for e in extraction];  # turns list of lists into list of strings

extraction_id = [];
for c in extraction2: 
    d1 = re.search("\d+", c);      # extract the first integer
    d2 = d1.group();
    extraction_id.append(d2);
    
extraction_amount = [];
for i in extraction2:
    j1 = re.search("\d+\.\d+", i);    # extract the first float
    j2 = j1.group();
    extraction_amount.append(j2);

print("Checkpoint 8")


# network variable contains the social network
# extraction_id contains the user who made the purchase
# extraction_amount contains the purchase amount

speed = 0
additions = {}
for f, g in zip(extraction_id, extraction_amount): 
    for h in network:
        if f in str(network[h]):
            additions.setdefault(h, []).append(str(g))   # sorting new purchases into networks
    speed += 1;    
    if(speed % 100 == 0):
        print(speed)   # checking how fast the code is running  

print("Checkpoint 9")


additions2 = {};
for item in additions:
    w = [float(i) for i in additions[item]];    # turns strings into floats 
    additions2.setdefault(item, []).append(w);
                                  
additions3 = [];  
for a in additions2:
    for b in additions2[a]:
        additions3.append(b);      # turns dict into a list of floats
 
lower_bound = [];
higher_bound = [];              
for m, n in zip(network_mean, network_std):
    low = m - 3*n;
    high = m + 3*n;
    low2 = float("%.2f" % low);    # round floats to 2 decimal places
    high2 = float("%.2f" % high);    # round floats to 2 decimal places 
    lower_bound.append(low2);
    higher_bound.append(high2);
                    
for c in additions3:
    for d, e, f in zip(c, lower_bound, higher_bound):
        if e <= d <= f:
            c.remove(d);       # remove all amounts within 3 standard deviations

print("Checkpoint 10")

anomalies = [item for sublist in additions3 for item in sublist]; # flatten list of lists

sorted_anomalies = [];
for g in anomalies:
       if g not in sorted_anomalies:
          sorted_anomalies.append(g);   # remove duplicates from list
   
positions = [];
for z in sorted_anomalies:
    p = [r for r, x in enumerate(additions3) if z in x];  
    positions.append(p);     # get positions of anomalies

string_anomalies = [];
for h in sorted_anomalies:
    string_anomalies.append(str(h));    # turn elements into strings

flagged = [];        
for i in new_purchases:
    for j in string_anomalies:
        if j in i:
            flagged.append(i);       # pull out flagged purchases
  
print("Checkpoint 11: Get Flagged Purchases")

flagged_split = [];
for a in flagged:
    b = a.rstrip();
    x = re.findall('"id": .*?\}', b);    # extract strings with ids
    flagged_split.append(x);

flagged_string = [''.join(e) for e in flagged_split];  # turns list of lists into list of strings

flagged_id = [];
for string in flagged_string: 
    d1 = re.search("\d+", string)      # extract the first integer
    d2 = d1.group();
    d3 = int(d2);
    flagged_id.append(d3);
                                             
flagged_info = [];             # finding mean and std of the flagged events        
for number in flagged_id:
    flagged_info.append('"mean"'+': \"'+str(network_mean[number])+'\", '+'"sd"'+': \"'+str(network_std[number])+'\"}');
   
flagged_edit = [];
for r in flagged: 
    s = r.replace("}", ",");      # remove } from strings
    flagged_edit.append(s); 

flagged_events = [];
for a, b in zip(flagged_edit, flagged_info):
    flagged_events.append(a + b);     # combine event with mean and sd
 
print("Checkpoint 12: Output")
             
save_path = 'C:/Users/Ruhul/Desktop/anomaly_detection-master/anomaly_detection-master/log_output'
flagged_purchases = os.path.join(save_path, "flagged_purchases.json")         

the_file = open(flagged_purchases, "w")
for entry in flagged_events:
    the_file.write("%s\n" % entry)  # write output of flagged purchases to json file 
  
the_file.close()

print("Checkpoint 13: Output Written to flagged_purchases.json")        

          