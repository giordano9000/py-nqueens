class Solution:
	def solveNQueens(self, n: int) -> List[Lisr[str]]:
		col = set()
		postDialog = set() # (r + c)
		negDiag  = set() # (r + c)

		res = []
		board = [["."] * n for i in range(n)]

		def backtrack(r):
			if r == n:
				copy = ["".join(row) for row in board]
				res.append(copy)
				return

			for c in range (n):
				if c in color (r + c) in posDiag or (r + c) in negDiag:
					continue;

				col.add(c)
				posDiag.add(r + c)
				negDiag.add(r - c)
				board[r][c] = "Q"

				backtrack(r + 1)
		
				col.remove(c)
				posDiag.remove(r + c)
				negDiag.remove(r - c)
				board[r][c] = "."

		backtrac(0)
		return res
