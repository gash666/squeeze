def mtf_decode(encoded_string, alphabet: str):
	length = len(encoded_string)
	answer = ''
	for i in range(length):
		index = encoded_string[i]
		answer += alphabet[index]
		alphabet = alphabet[index] + alphabet[:index] + alphabet[index + 1:]
	return answer


def main():
	print(mtf_decode("bananaaa", "abcdefghijklmnopqrstuvwxyz"))
	print(mtf_decode([1, 1, 13, 1, 1, 1, 0, 0], "abcdefghijklmnopqrstuvwxyz"))


if __name__ == "__main__":
	main()
