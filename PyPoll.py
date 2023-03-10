# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

election_data=open(file_to_load,'r')


# To do: perform analysis.

# Close the file.
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

import os
dir(os)
print(dir(os.path))     

import csv
import os
# Assign a variable for the file to load and the path
file_to_load=os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

 # Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")  

file_to_save=os.path.join("analysis",  "election_analysis.txt")
# Use the open statement to open the file as a text file.
outfile=open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello world")
#close thefile
outfile.close()

 # Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as  txt_file:

 # Write three counties to the file
#txt_file.write("Arapahoe")
#txt_file.write("Denver")
#txt_file.write("Jefferson")

 # Write three counties to the file.
  #txt_file.write("Arapahoe, ")
  #txt_file.write("Denver, ")
  #txt_file.write("Jefferson")

 # Write three counties to the file.
 #txt_file.write("Arapahoe\nDenver\nJefferson")

 txt_file.write("counties in th election\n-------------- \nArapahoe\nDenver\nJefferson")

# Add our dependencies.
import csv 
import os
# Assign a variable to load a file from a path.
file_to_load=os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis","election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
  # Read the file object with the reader function.
  file_reader = csv.reader(election_data)
  # Print each row in the CSV file.
  #for row in file_reader:
    #print(row)
#print the header row
  headers = next(file_reader)
  print(headers)

# Add our dependencies.
import csv 
import os
# Assign a variable to load a file from a path.
file_to_load=os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis","election_analysis.txt")
# Open the election results and read the file.

#1. initialize a total vote counter
total_votes=0

#candidate options
candidate_options=[]
#declare the empty dictionary
candidate_votes ={}


with open(file_to_load) as election_data:
  # Read the file object with the reader function.
  file_reader = csv.reader(election_data)
  
  #read the header row
  headers = next(file_reader)

  #print each row in csv file
  for row in file_reader:

    #2.Add to the total vote count
      total_votes+=1

     #print total votes
 #print(total_votes) 

      #print candidate name from each row
      candidate_name=row[2]

      # If the candidate does not match any existing candidate...
      if candidate_name not in candidate_options: 
      #add candidate name to the candidate list
        candidate_options.append(candidate_name)
    # Begin tracking that candidate's vote count.
        candidate_votes[candidate_name] = 0  
     # Add a vote to that candidate's count
      candidate_votes[candidate_name] += 1

  
  with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal
        election_results = (
        f"\nElection results\n"
        f"---------------------\n"
        f"Total votes:{total_votes:,}\n"
        f"---------------------\n")
        print(election_results,end=" ")  
        # Save the final vote count to the text file.
        txt_file.write(election_results)


  #print the candidate vote dictionary
        print(candidate_votes)

      #print total votes
#print(total_votes)  

        winning_candidate = ""
        winning_count = 0
        winning_percentage = 0

 #print the candidate list
        print(candidate_options)
        print("done")

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
        for candidate_name in candidate_votes:
            # 2. Retrieve vote count of a candidate.
            votes=candidate_votes[candidate_name]
            # 3. Calculate the percentage of votes.
            vote_percentage=float(votes)/float(total_votes)*100
            # 4. Print the candidate name and percentage of votes.
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            #with open(file_to_save, "a") as txt_file:
            txt_file.write(candidate_results)


#  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count

            if(votes>winning_count) and (vote_percentage>winning_percentage):
                # If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
            # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal 

        winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
        print(winning_candidate_summary)

# Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)


  







      


