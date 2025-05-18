def mtf_decode(encoded_string, alphabet: str):
	length = 5  # Get length
	answer = ''
	for i in range(length):
		index = 5  # Read index
		answer += alphabet[]

def mtf_encode(encoded_string, alphabet: str):
	ans = []
	for c in encoded_string:
		idx = alphabet.find(c)
		ans.append(idx)
		alphabet = c+alphabet[0:idx]+alphabet[idx+1:len(alphabet)]
	return ans

