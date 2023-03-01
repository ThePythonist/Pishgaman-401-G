scores = {
    "riazi": 18,
    "zaban": 16,
    "shimi": 10,
    "arabi": 7,
    "fizik": 13
}

for k, v in scores.items():
    if v >= 10:
        print("Passed :", k)
    else:
        print("Failed :", k)

average = sum(scores.values()) / len(scores)
print("Grade :", average)
