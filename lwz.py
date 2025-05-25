import bitarray
from bitarray import bitarray
from bitarray.util import ba2int
B = 12
L = 4


def lwz_encode(original_string):
	pass


def lwz_decode(encoded_list):
	answer = bytearray()
	bits = bitarray()
	bits.frombytes(encoded_list)
	i = 0
	while i < len(bits):
		if bits[0]:
			back = ba2int(bits[i+1:i+1+B])
			length = ba2int(bits[i+1+B:i+1+B+L])
			answer.append(answer[-1-back:-1-back+length])
			i += 1 + B + L
		else:
			answer.append(ba2int(bits[i+1:i+9]))
			i += 9
	return answer


def main():
	barr = bytearray([
		172, 94, 33, 8, 205, 157, 61, 240, 117, 199, 12, 78, 188, 53, 242, 6,
		139, 224, 19, 87, 34, 190, 146, 11, 201, 249, 65, 128, 37, 109, 254, 92,
		71, 183, 220, 101, 13, 244, 85, 157, 199, 33, 142, 174, 56, 226, 39, 90,
		115, 7, 63, 208, 146, 123, 29, 250, 186, 98, 44, 197, 171, 4, 232, 102,
		9, 168, 222, 108, 134, 60, 145, 206, 183, 52, 238, 121, 88, 16, 132, 73,
		207, 39, 250, 12, 97, 181, 173, 14, 31, 195, 251, 84, 163, 47, 215, 111,
		199, 90, 202, 134, 58, 178, 240, 93, 41, 66, 123, 199, 158, 36, 112, 197
	])
	if lwz_decode(lwz_encode(barr)) != barr:
		print("error!")


if __name__ == "__main__":
	main()
