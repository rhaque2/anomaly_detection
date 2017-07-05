# anomaly_detection
Creating a social network with purchase history in order to flag anomalous purchases that are greater than 3 standard deviations away from the mean of a user network's purchases.
The code is made up of 2 Python files located in the sample_dataset folder.
The first file is called making_batch.py.
Modules needed for this code include pandas, pylab, os.path, and json.
Checkpoints were created to break up the code into steps.
The batch_log.json file was opened with json.loads and its contents were stored in "data."
Checkpoint 1 was reached and dataframe indexing was used to separate purchase, befriend, and unfriend events (Checkpoint 2).
The creation of the user social network then began with the IDs used in the befriending events. 
ID1 and ID2 were indexed out and turned into a list before getting changed into integers.
The dictionary of friends called f1 was made by appending those IDs to reach Checkpoint 3.
Since the Degree = 2, it was necessary to create a dictionary of friends of friends. 
All the possible friend connections were created with a nested for loop and stored in a variable called f2.
The IDs within the f2 dict variable were sorted and duplicates were removed.
Extraneous lists were filtered out with a while loop.
At this point, Checkpoints 4, 5, and 6 were fulfilled.
The unfriending events were then considered.
Similarly to the befriending events, these unfriending events had their IDs indexed out and turned into a list of integers. 
The remove function was applied to the f1 dict variable to eliminate friendships (reaching Checkpoint 7).
The same piece of code with making a dictionary of friends of friends was repeated in order to update the friends of friends 
network (f2) with the updated f1 variable. 
Checkpoint 8 is met and Purchase History is the next section.
The purchase IDs and their amounts were indexed out and converted into strings to reach Checkpoint 9.
A for loop was then used to turn f2 into a new variable "network" that included the user himself inside his network (Checkpoint 10).
The os.path module was used to write the entire social network to a text file (social_network.txt) to be stored in log_output
(Checkpoint 11).
Next, a nested if and for loop were deployed to append the IDs and their amounts to corresponding networks.
This long-running section of code was also set to stop at 50 purchases for each user network. 
After a long wait time, Checkpoint 12 was met and the "history" dict variable contained all the purchases. 
The user and their network's purchase history were written to a text file (purchase_history.txt) to be stored in log_output (Checkpoint
13).  
This was the end of the first Python file. The second file was called making_stream.py. 
Modules needed for this code include pandas, pylab, numpy, os.path, json, and re.
Checkpoints were also used to break up this code.
The os.path module and the readlines command were used to read the purchase_history.txt file (Checkpoint 1).
User network and purchase history information were pulled out with for and if loops (Checkpoint 2).
Dataframe columns were created and the purchases were put into a list (Checkpoint 3).
The re module was used to sparse the strings for the amounts of the purchases (Checkpoint 4).
The replace command was used to remove extraneous commas, parentheses, and apostrophes (Checkpoint 5).
A list of number strings was created with the split function. List comprehension with the float function turned the number strings into
floats. 
The numpy module was used to calculate the mean and standard deviation of the floats from lists for each of the user networks.
The floats were rounded to 2 decimal places and appended to network_mean and network_std lists (Checkpoint 6).
The os.path module was then used to read in data from the stream_log file (Checkpoint 7).
For and if loops were used to sort out the new purchases, befriendings, and unfriendings.
The re module with the findall command was used to extract strings with IDs and amounts from the new purchases. 
The join command was used to turn a list of lists into a list of strings. 
The search and group commands within the re module were deployed to extract both the first integer and first float from strings.
This pulled out the ID and amount for each of the new purchases (Checkpoint 8).
The network variable from the making_batch file was then used in sorting the new purchases into corresponding networks. 
This section of code also takes a little time but not as much as the long-running code from the previous file. 
Checkpoint 9 is reached and the variable "additions" holds all the new purchase amounts.
The strings were converted into a dictionary with floats.
The dictionary was then turned into a list of floats.
The network_mean and network_std were used to create a low and high bound for placing the new purchases.
For and if loops were used to remove all the amounts that were within 3 standard deviations (Checkpoint 10).
List comprehension was used to flatten the list of lists and call it "anomalies."
For and if loops were used to remove duplicates and list comprehension was used to get indices of anomalies.
The anomalies were turned into strings and put through a loop to extract the flagged purchases (Checkpoint 11).
From these purchases, the IDs were extracted out with previous methods like findall, join, and search.
These flagged IDs were used to find the mean and standard deviation of the flagged events.
The mean and standard deviation string was concatenated with the rest of the flagged purchase string.
This matched the example output provided (Checkpoint 12).
The os.path module was used to write the flagged purchases to the flagged_purchases.json file (Checkpoint 13).
Along with the social_network.txt and purchase_history.txt files, this flagged_purchases.json file was stored in log_output. 
