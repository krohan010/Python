# 📖 Story Continuation: The Duplicate Entries Mystery!
# The coding competition is over, but now there's another problem! The event organizers noticed that some students were accidentally registered multiple times, and some students were missing from the final list of participants.
# Principal Williams calls the Tech Club again! Alex, Mia, and Jake must use Python sets to clean up the participant data and ensure every student's participation is properly recorded.
# 🔢 Python Set Challenges
# Each challenge is a real-world problem the Tech Club needs to solve using Python sets.
# 1️⃣ Creating a Set of Participants
# The student registration system recorded duplicate entries. Convert the list of participants into a set to remove duplicates.

participants = ["Alice", "Bob", "Charlie", "Alice", "David", "Charlie", "Eve"]

#Write code here
participantSet = set(participants)                      # list converted into set
print(participantSet)
# 2️⃣ Adding a Late Entry
# Emma was accidentally left out. Add "Emma" to the set.

# #Write code here
participantSet.add("Emma")                          # Added Emma into participantSet
print(participantSet)

# 3️⃣ Removing a Participant
# Bob couldn't attend the competition. Remove "Bob" from the set.

# #Write code here
participantSet.discard("Bob")
print(participantSet)

# 4️⃣ Checking for a Student
# Check if "Alice" participated in the competition.

# #Write code here
if "Alice" in participantSet:
    print("Alice is participant in the competition")

# 5️⃣ Finding Common Participants
# The school hosted another AI challenge. Find students who participated in both competitions.

coding_competition = {"Alice", "Charlie", "David", "Eve"}
ai_challenge = {"Charlie", "David", "Frank", "Grace"}

# 6️⃣ Finding Unique Participants
# Find students who only participated in the coding competition.

# #Write code here
only_coding_competition = coding_competition.difference(ai_challenge)
print(f"Those Student who is only participated in coding competition are : {only_coding_competition}")

# 7️⃣ Finding All Participants
# Get a list of all unique participants from both competitions.

# #Write code here
# all_unique_participants = only_coding_competition.union(ai_challenge.difference(coding_competition))
all_unique_participants = list((coding_competition.symmetric_difference(ai_challenge)))
print("Below are the all unique members listed : ")
for name in all_unique_participants:
    print(name)

# 8️⃣ Checking for Subsets
# The top scorers are a subset of the competition participants. Check if one set is a subset of the other.

top_scorers = {"Charlie", "Eve"}

# #Write code here

print(f"Is {top_scorers} a subset of {coding_competition}? : {top_scorers.issubset(coding_competition)}")

# print(f"Is {top_scorers} a subset of {coding_competition}? : {top_scorers <= coding_competition}")

# 9️⃣ Checking for Disjoint Sets
# The judges should have no overlap with the participants. Verify if these two sets are disjoint.

judges = {"Mr. Smith", "Ms. Johnson"}

# #Write code here
print(f"The {judges} is not disjoint of {top_scorers}? : {judges.isdisjoint(top_scorers)}")
print(f"The {judges} is disjoint of {top_scorers}? : {len(top_scorers.intersection(judges))==0}")

# 🔟 Finding Students in One Event but Not the Other
# Find students who participated in the AI challenge but not in the coding competition.

#Write code here
ai_students_but_not_coding_competition = ai_challenge - coding_competition
print(f"AI challenge Students who not participated in the coding competition : {ai_students_but_not_coding_competition}")

# 1️⃣1️⃣ Copying a Set
# Create a copy of the participants set and modify it without changing the original.

# #Write code here
participants = {"Alice", "Grace", "Frank", "Eve"}
participants_copy = participants.copy()                     # copy of original participants

# Modify the copied participants :
participants_copy.add("David")                              # add items
participants_copy.discard("Eve")                            # remove items

# Print both see the difference :
print(participants)
print(participants_copy)

# 1️⃣2️⃣ Clearing the Participant List
# After recording results, clear the participants set without deleting the variable.

# #Write code here
participants.clear()                        # empties the set

# 1️⃣3️⃣ Converting a Set Back to a List
# Convert the participants set back into a list for further processing.

# #Write code here
participantsList = list((participants))
print(participantsList)

# 1️⃣4️⃣ Set Length
# Find out how many unique students participated in the coding competition.

# #Write code here
print(f"No of student who is participating in only one competition : {len(all_unique_participants)}")

# 1️⃣5️⃣ Set Operations in a Single Line
# Write a one-liner to:

# Find students who participated in both competitions.
print([name for name in ai_challenge.intersection(coding_competition)])


# Find students who were only in one competition.

# #Write code here
print([name for name in ai_challenge.symmetric_difference(coding_competition)])

