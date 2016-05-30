import numpy as NumPy


class Script:

	@staticmethod
	def main():
		vector = NumPy.array([5, 10, 15, 20])
		matrix = NumPy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
		vector_shape = vector.shape
		matrix_shape = matrix.shape
		print(str(vector_shape))
		print(str(matrix_shape))



Script.main()