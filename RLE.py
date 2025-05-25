def rle_encode(original_string):
    counter = 0
    ans = []
    original_string+="a"
    for i in range(0,len(original_string)-1):
        counter+=1
        if original_string[i] != original_string[i+1]:
            ans.append(counter)
            ans.append(original_string[i])
            counter = 0
    return ans




def rle_decode(encoded_list):
	answer = []
	for i in range(0, len(encoded_list), 2):
		answer += encoded_list[i] * [encoded_list[i + 1]]
	return answer

def main():
	print(rle_encode( [1,1,1,0,3,5]))

if __name__ == "__main__":
    main()
