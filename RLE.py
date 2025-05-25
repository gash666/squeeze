
def RLE_encode(original_string):
    counter = 0
    ans = []
    original_string.append("a")
    for i in range(0,len(original_string)-1):
        counter+=1
        if original_string[i] != original_string[i+1]:
            ans.append(counter)
            ans.append(original_string[i])
            counter = 0
    return ans

