"""
https://adventofcode.com/2024/day/4
--- Day 4: Ceres Search ---
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?


https://adventofcode.com/2024/day/4#part2
--- Part Two ---
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?
"""

from handle_inputs import get_array_without_spaces


def get_7x7_matrix(matrix: str, pos_X: int, pos_Y: int) -> list:
  """get the 7x7 matrix around the X"""
  rows = len(matrix)
  cols = len(matrix[0]) if rows > 0 else 0
  window = []
  for i in range(pos_X - 3, pos_X + 4):
    row = []
    for j in range(pos_Y - 3, pos_Y + 4):
      if 0 <= i < rows and 0 <= j < cols:
        row.append(matrix[i][j])
      else:
        row.append(" ")
    window.append(row)
  return window


def get_all_8_directions(matrix):
  center_x, center_y = 3, 3  # Center of 7x7 matrix
  directions = [
    (0, -1),  # left
    (0, 1),  # right
    (-1, 0),  # up
    (1, 0),  # down
    (-1, -1),  # up-left
    (-1, 1),  # up-right
    (1, -1),  # down-left
    (1, 1),  # down-right
  ]
  results = []
  for dx, dy in directions:
    chars = []
    x, y = center_x, center_y
    while 0 <= x < 7 and 0 <= y < 7:
      chars.append(matrix[x][y])
      x += dx
      y += dy
    results.append("".join(chars))
  return results


def check_XMAS(reports: str, pos_X: int, pos_Y: int) -> int:
  matrix = get_7x7_matrix(reports, pos_X, pos_Y)
  possibilities = get_all_8_directions(matrix)
  return possibilities.count("XMAS")


def part_one(file_path: str) -> int:
  reports = get_array_without_spaces(file_path)
  safe_reports = 0
  for i in range(len(reports)):
    for j in range(len(reports[0])):
      if reports[i][j] == "X":
        safe_reports += check_XMAS(reports, i, j)
  return safe_reports


def get_3x3_matrix(matrix: str, pos_X: int, pos_Y: int) -> list:
  """get the 3x3 matrix around the X"""
  rows = len(matrix)
  cols = len(matrix[0]) if rows > 0 else 0
  window = []
  for i in range(pos_X - 1, pos_X + 2):
    row = []
    for j in range(pos_Y - 1, pos_Y + 2):
      if 0 <= i < rows and 0 <= j < cols:
        row.append(matrix[i][j])
      else:
        row.append(" ")
    window.append(row)
  return window


def get_X_directions(matrix):
  results = [
    matrix[0][0] + matrix[1][1] + matrix[2][2],  # up-left
    matrix[0][2] + matrix[1][1] + matrix[2][0],  # up-right
    matrix[2][0] + matrix[1][1] + matrix[0][2],  # down-left
    matrix[2][2] + matrix[1][1] + matrix[0][0],  # down-right
  ]
  return results


def check_XMAS_2(reports: str, pos_X: int, pos_Y: int) -> int:
  matrix = get_3x3_matrix(reports, pos_X, pos_Y)
  possibilities = get_X_directions(matrix)
  return 1 if possibilities.count("MAS") == 2 else 0


def part_two(file_path: str) -> int:
  reports = get_array_without_spaces(file_path)
  safe_reports = 0
  for i in range(len(reports)):
    for j in range(len(reports[0])):
      if reports[i][j] == "A":
        safe_reports += check_XMAS_2(reports, i, j)
  return safe_reports


if __name__ == "__main__":
  file_path = "inputs/day_4.txt"
  print(f"4.1: {part_one(file_path)}")
  print(f"4.2: {part_two(file_path)}")
