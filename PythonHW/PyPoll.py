#!/usr/bin/env python
# coding: utf-8

# In[15]:


import os
import csv
from pathlib import Path
from statistics import mean


# In[16]:


poll_data = Path("""C:/Users/walsh/Desktop/DABC/unc-chacc-data-pt-03-2020-u-c/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv""")


# In[53]:


#variable define to find the total votes
total_votes = 0 
#list to store the candidates
candidates = []
#dictionary to hold candidates vote tally
votes_per_candidate = {}
#variable to store headers
header= []
#Read in the poll data temporarily
with open(poll_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    
    #set a variable to true so that I can read in the header row
    firstline = True
    #vc_cand1 = 1
    #vc_cand2 = 1
    #vc_cand3 = 1
    #c_cand4 = 1
    
    for rows in csvreader:
        
        #If statement to skip grab and store the header line
        if firstline:
            #store the header rows
            for i in rows:
                header.append(i)
            #reset so that the loop runs after the header row
            firstline = False
        else:
            total_votes +=1
            
            #check to see if candidate name in list, if it isn't
            if rows[2] not in candidates:
                
                #add candidate name to the list
                candidates.append(rows[2])
                
                #create vote count for candidate that is at 1
                votes_per_candidate.update({rows[2] : 1})
                
                #
            
            #if name in the list
            else:
                if rows[2] ==candidates[0]:
                    
                    #increment votes for 1st candidate
                    votes_per_candidate[candidates[0]]+=1
                    #vote_tally[votes][str(candidates[0])] +=1
                    #vc_cand1 = vc_cand1 + 1
                    
                elif rows[2] == candidates[1]:
                    
                    #increment votes for 2nd candidate
                    votes_per_candidate[candidates[1]]+=1
                    #vc_cand2 = vc_cand2 + 1
                elif rows[2] == candidates[2]:
                    votes_per_candidate[candidates[2]]+=1
                    #vc_cand3 = vc_cand3 + 1
                elif rows[2] == candidates[3]:
                    votes_per_candidate[candidates[3]]+=1
                    #vc_cand4 = vc_cand4 + 1
    print(total_votes)
    print(candidates)
  
    #print(vote_tally)
    print(votes_per_candidate)
print(header)


# In[60]:


print(votes_per_candidate[candidates[0]]/total_votes)
print(votes_per_candidate[candidates[1]]/total_votes)
print(votes_per_candidate[candidates[2]]/total_votes)
print(votes_per_candidate[candidates[3]]/total_votes)


# In[22]:


#list to store results so they could be printed by looping 
results = []


# In[48]:


#needed to reset the results after running
results.clear()


# In[54]:


#Change Candidates percentage to the proper format
c1_votes = '{percent1:.3%}'.format(percent1 = votes_per_candidate[candidates[0]]/total_votes) 
#print(c1_votes)   <---------Check to see if it worked
c2_votes = '{percent2:.3%}'.format(percent2 = votes_per_candidate[candidates[3]]/total_votes)
c3_votes ='{percent3:.3%}'.format(percent3 = votes_per_candidate[candidates[1]]/total_votes)
c4_votes = '{percent4:.3%}'.format(percent4 = votes_per_candidate[candidates[2]]/total_votes)


# In[49]:


#add results of candidates in a good format to print to my file
results.append(str(candidates[0]) + ": " + str(c1_votes) + " ("  + str(votes_per_candidate[candidates[0]]) + ")")
results.append(str(candidates[1]) + ": " + str(c2_votes) + " ("  + str(votes_per_candidate[candidates[1]]) + ")")
results.append(str(candidates[2]) + ": " + str(c3_votes) + " ("  + str(votes_per_candidate[candidates[2]]) + ")")
results.append(str(candidates[3]) + ": " + str(c4_votes) + " ("  + str(votes_per_candidate[candidates[3]]) + ")")


# In[60]:


#Print the results to the terminal
print(f'Election Results \n--------------------------- \nTotal Votes: {total_votes}\n---------------------------\n')
for i in results:
    print(i)
print("---------------------------\nWinner: Khan\n---------------------------")


# In[52]:


out_file = open("C:/Users/walsh/Desktop/DABC/PythonHW/PyPoll.txt", "w")
out_file.write(f'Election Results \n--------------------------- \nTotal Votes: {total_votes}\n---------------------------\n')
for line in results:
     out_file.write(str(line))
     out_file.write("\n")
out_file.write("---------------------------\nWinner: Khan\n---------------------------")
out_file.close()


# In[ ]:




