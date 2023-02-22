class_riazi = ["arshia", "ali", "pooria", "arman", "sina"]
class_shimi = ["ali", "saman", "kiarash", "pooria", "javad"]
eshterak = []

# for i in class_riazi:
#     for j in class_shimi:
#         if i == j:
#             eshterak.append(i)  # Or j

for i in class_riazi:
    if i in class_shimi:
        eshterak.append(i)

print(eshterak)
