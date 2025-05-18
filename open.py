from functools import cmp_to_key

def compare(a, b):
	for i in range(len(a)):
		if a[i] == '$':
			return 1
		if b[i] == '$':
			return -1
		if ord(a[i]) > ord(b[i]):
			return 1
		if ord(a[i]) < ord(b[i]):
			return -1
	return 0


def bwt_decode(encoded_string: str, end: chr = '$') -> str:
	answer = ['' for i in range(len(encoded_string))]
	for i in range(len(encoded_string)):
		temp = [encoded_string[i] + answer[i] for i in range(len(encoded_string))]
		answer = sorted(temp, key=cmp_to_key(compare))
	for string in answer:
		if string[-1] == end:
			return string
	print("error, never returned")


def mtf_decode(encoded_string, alphabet: str):
	length = 5
	answer = ''
	for i in range(length):
		pass




def main():
	print(bwt_decode("BNN^AA$A"))


if __name__ == "__main__":
	main()
