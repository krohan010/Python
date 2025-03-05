scoreboard = {
    "team_alpha" : 0,
    "team_beta" : 0,
    "team_gamma" : 0
}

for key, value in scoreboard.items():
    print(key, value)


round1_scores = {"Team Alpha": 10, "Team Beta": 5}
round2_scores = {"Team Alpha": 15, "Team Beta": 10}

# round1Score = list(round1_scores.values())
# round2Score = list(round2_scores.values())
# for i in range(len(round1Score)):
#     round1Score[i] += round2Score[i]
#
# print(round1Score)

final_scores = dict.fromkeys(round1_scores.keys(), 0)
print(final_scores)

for key in round1_scores:
    final_scores[key] = round1_scores[key] + round2_scores[key]
    # print(round1_scores[key])
print(final_scores)

