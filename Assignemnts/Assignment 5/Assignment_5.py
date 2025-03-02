# Next Challenge: Managing Competition Scores with Dictionaries!
# Now, it's time for the Python Dictionary Challenges, where they will track and manage scores during the competition. Here are 15 engaging questions that continue the storyline.
# 📖 Story Continuation: The Scoreboard Mystery!
# The coding competition has begun, and the teams are performing well! However, the scoreboard system is malfunctioning, and scores are getting misplaced. Principal Williams calls the Tech Club once again—they must use Python dictionaries to track the scores manually.
# 🔢 Python Dictionary Challenges
# 1️⃣ Creating a Scoreboard Dictionary
# Create a dictionary named scoreboard where each team name is the key, and their initial score (0 points) is the value.

# scoreboard = { "Team Alpha": 0, "Team Beta": 0, "Team Gamma": 0 }

# #Write code here

scoreboard = {
    "team_alpha" : 0,
    "team_beta" : 0,
    "team_gamma" : 0
}

# 2️⃣ Updating Scores
# Team Alpha wins a round! Increase their score by 10 points in the dictionary.

# #Write code here
scoreboard["team_alpha"] += 10

# 3️⃣ Checking Scores
# Print the score of Team Beta using dictionary key access.

# #Write code here
print("The scores of Team beta is : ", scoreboard["team_beta"])

# 4️⃣ Adding a New Team
# A new team, Team Delta, has joined the competition. Add them to the dictionary with 0 points.

# #Write code here
# scoreboard.update({"team_delta" : 0})
scoreboard["team_delta"] = 0

# 5️⃣ Modifying Scores
# Team Gamma received bonus points! Update their score to 15.

# #Write code here
scoreboard["team_gamma"] += 15

# 6️⃣ Handling Missing Teams
# Mia accidentally tries to check the score of a non-existent team, "Team Omega". Use the .get() method to avoid an error and print "Team not found" if the team doesn't exist.

# #Write code here
if scoreboard.get("team_omega") :
    print("The team omega score is : ", scoreboard['team_omega'])
else:
    print("Team Omega not exist")

# 7️⃣ Removing a Team
# Team Beta left the competition. Remove them from the dictionary.

# #Write code here
scoreboard.pop('team_beta')

# 8️⃣ Checking if a Team Exists
# Write a condition to check if "Team Alpha" exists in the dictionary.

# #Write code here
if scoreboard.get('team_alpha'):
    print("Team Alpha is still in the competition")

# 9️⃣ Listing All Teams
# Print all the team names participating in the competition using .keys().

# #Write code here
teamNames = scoreboard.keys()
print(teamNames)

# 🔟 Listing All Scores
# Print all the scores using .values().

# #Write code here
teamScores = scoreboard.values()
print(teamScores)

# 1️⃣1️⃣ Finding the Leading Team
# Use the .items() method and a loop to find the team with the highest score.

#Write code here
leading_team = None
high_score = float('-inf')          # it stores negative infinite number.

for teamName, score in scoreboard.items():
    if score > high_score:
        high_score = score
        leading_team = teamName

print(f"The Leading team of this competition is : {leading_team} with a score of {high_score}")

# 1️⃣2️⃣ Sorting Teams by Score
# Display the teams sorted in descending order of their scores.

# #Write code here
sorted_team = sorted(scoreboard.items(), key=lambda item: item[1], reverse=True)
print("The Teams are sorted based on their scores : ")
for teamName, score in sorted_team:
    print(teamName, " : ", score)

# 1️⃣3️⃣ Resetting Scores

# Principal Williams wants to reset all scores to 0 before the final round. Update all values to 0.

# #Write code here
for keyName in scoreboard:
    scoreboard[keyName] = 0

print(scoreboard)

# 1️⃣4️⃣ Merging Scoreboards
# The competition has two different rounds stored in separate dictionaries:

# round1_scores = {"Team Alpha": 10, "Team Beta": 5}

# round2_scores = {"Team Alpha": 15, "Team Beta": 10}

# Merge both into a single dictionary where the values are their total scores.

#Write code here
round1_scores = {"Team Alpha": 10, "Team Beta": 5}
round2_scores = {"Team Alpha": 15, "Team Beta": 10}

final_scores = dict.fromkeys(round1_scores.keys(), 0)
for key in round1_scores:
    final_scores[key] = round1_scores[key] + round2_scores[key]

print("Total Scores : ", final_scores)

# 1️⃣5️⃣ Clearing the Scoreboard

# After the competition ends, clear the dictionary without deleting the variable.

# #Write code here
scoreboard.clear()              # empties the scoreboard dictionary
