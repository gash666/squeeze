



def rle_decode(encoded_list):
	answer = []
	for i in range(0, len(encoded_list), 2):
		answer += encoded_list[i] * [encoded_list[i + 1]]
	return answer

def main():
	print(rle_encode([[1, 1, 1, 2, 3, 5, 4, 5, 5, 5, 5]]))
	print(rle_decode(rle_encode([[1, 1, 1, 2, 3, 5, 4, 5, 5, 5, 5]])))


if __name__ == "__main__":
	main()
