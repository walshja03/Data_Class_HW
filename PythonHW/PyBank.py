#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import csv
from pathlib import Path
from statistics import mean


# In[4]:


budget_file = Path("""C:/Users/walsh/Desktop/DABC/unc-chacc-data-pt-03-2020-u-c/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv""")


# In[5]:


budget_file


# In[7]:


#variable to store the headers in
header = []
#list to store the changes so that I could calculate average change
changes = [] 

# open the csv file to read
with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    #define total months to count how many records
    total_months = 0
    # define total profit/loss
    total_profit = float(0.00)
    
    #variable so that I can do an if to bypass the first line because it didn't have data
    firstline = True
    #variable so that I could skip first line of data because when I calculated change I had to start with the second row
    secondline = True
 
    #used to store so that I could find change by doing previous-current
    previous = 0.00
    
    #iterate through row by row
    for row in csvreader:
        
        
        # initial credit Stack overflow (https://stackoverflow.com/questions/14674275/skip-first-linefield-in-loop-using-csv-file)
        if firstline:
            #for loop to store the header
            for i in row:
                header.append(i)
            #reset so that the loop runs after the header row
            firstline = False
        else:
            #Find the total profit
            total_profit = total_profit + float(row[1])
            
            #count the number of months
            total_months +=1
            
            if secondline:
                secondline = False
                previous = float(row[1])
            else:
                #add the change into a list
                changes.append((float(row[1]))-previous)
                #Change previous to next value before next loop
                previous = float(row[1])
    
    #print(total_months)  <---- Check
    #print(str(total_profit))  <---- Check
    #print(str(test))  <---- Check
    #print(str(previous))  <---- Check
    #print(int(len(avg_change)))  <---- Check
    #print(header)  <---- Check and look I stored the headers


# In[24]:


#looked this up to store the different rows to reference.  Oddly looking now (3/26) Steve showed this looping to fill 
# a list yesterday and now I understand what the code is doing
with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    data_ref =[r for r in csvreader]


# In[35]:


#check that above code worked
#print(data_ref)


# In[16]:


#This little section I added after I realized I probably shouldn't have used a library to get mean.  Just here to show how I could have done it.
#sum_avg_change= sum(changes)
#print(sum_avg_change)
#average_change = sum_avg_change/(total_months -1)
#print(average_change)


# In[36]:


#check that the avg change was correct.  Since the data set was small I compared to the excel sheet I did the calcs in
#print(avg_change)


# In[17]:


#Calculation to find the average change
average = mean(changes)
print(average)  


# In[18]:


#calculaiton to find the greatest decrease
greatest_decrease = min(changes)
#print(greatest_decrease) <---- Check


# In[19]:


#calculation to find the greatest increase
greatest_increase = max(changes)
#print(greatest_increase)  <---- Check


# In[21]:


#practice finding the index of the greatest increase before putting into the results. 
#Realized I had to do +2 to account for the fact that there was a header row and 1st row which couldn't calculate
changes.index(greatest_increase)


# In[22]:


#practice finding the index of the greatest decrease before putting into the results
changes.index(greatest_decrease)


# In[25]:


# Create results list to make it easy to iterate through and display
results=[]
results.append(str("Total Months: " + str(total_months)))
results.append(str(("Total: $" + str(int(total_profit)))))
results.append(str("Average Change: $" + str(round(average,2))))
results.append(str("Greatest Increase in Profits: " + str(data_ref[changes.index(greatest_increase)+2][0]) +" ($"+str(int(greatest_increase))+")"))
results.append(str("Greatest Decrease in Profits: " + str(data_ref[changes.index(greatest_decrease)+2][0]) +" ($"+str(int(greatest_decrease))+")"))



# In[26]:


print(f"Financial Analysis \n--------------------------------------\n")
#Loop to print results to the terminal in a orderly fashion
for line in results:
    print(line)


# In[49]:


#Create file and write the results to it
out_file = open("C:/Users/walsh/Desktop/DABC/PythonHW/PyBank.txt", "w")
#print the header row
out_file.write(f"Financial Analysis \n--------------------------------------\n")
#Loop to print results line by line
for line in results:
    out_file.write(line)
    out_file.write("\n")
out_file.write(f"\n \n \n headers {header[0]}: {header[1]}")
out_file.close()


# In[ ]:




