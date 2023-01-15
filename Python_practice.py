print("Hello world")
counties = ["Arapahoe","Denver","Jefferson"]
print(counties)
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1]=='Denver' :
    print(counties[1])
a=0

if a == 1:
  print("Sanil")
  print("Rahna")   
else:
  print("Mehzaan")   
  print("Manha")  
print("Outside")  

counties = ["Arapahoe","Denver","Jefferson"]
if "Elpaso" in counties:
  print("Elpaso is in list of counties")
else:
  print("Elpaso not in the list of counties")

  if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and elpaso is in counties list")
  else:
    print("Arapahoe or elpaso  not in counties list")  

  if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or elpaso is in counties list")
  else:
    print("Arapahoe and elpaso not in counties list")  

for county in counties:
  print(county)


mumbers=[0,1,2,3,4]
for num in mumbers:
    print(num)

for num in range(5):
  print(num)

for i in range(len(counties)):
  print(counties[i]) 

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
  print(county)

for county in counties_dict.keys():
   print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
     print(counties_dict[county]) 

for county in counties_dict:
   print(counties_dict.get(county))

for county,voters in counties_dict.items():
    print(f'{county} county has {voters} voters')
    print(county + " county has " + str(voters) + " voters")
    print(voters + 1)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
  print(county_dict)

print("here")

for county_dict in voting_data:
  print(county_dict)
  for value in county_dict.values():
    print(value)

for county_dict in voting_data:
   print(county_dict['county']) 

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
  print(county  +  " county has "  +  str(voters)  +  " registered voters" )
  

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
  print(f"{county}  county has {voters} registered voters")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)
