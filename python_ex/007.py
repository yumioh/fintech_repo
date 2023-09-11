x = [2, 5, 7, 5, 8, 3, 4, 5, 7, 6, 4]

# x[2] = 0
# x[5] = 0
# x[8] = 0

# for idx, val in enumerate(x):
#     if val == 3 or val ==7:
#         x[idx] = 0

for idx in range(len(x)):
    if x[idx] == 3 or x[idx] ==7:
        x[idx] = 0

print(x)