



def rle_decode(encoded_list):
	answer = []
	for i in range(0, len(encoded_list), 2):
		answer += encoded_list[i] * [encoded_list[i + 1]]
	return answer

def main():
	print(rle_encode("bananaaa", "abcdefghijklmnopqrstuvwxyz"))
	print(rle_decode([1, 1, 13, 1, 1, 1, 0, 0], "abcdefghijklmnopqrstuvwxyz"))


if __name__ == "__main__":
	main()
