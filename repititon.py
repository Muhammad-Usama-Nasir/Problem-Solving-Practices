arr = [12, 18, 5, 11, 30, 5, 69]
new_arr = []
count = 0

for i in range(len(arr) - 1):
    
    if arr[i] in new_arr:
        count = count + 1
        continue
    else: 
        new_arr.append(arr[i])


print(new_arr)   