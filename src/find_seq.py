import os
import re


# This finds the optimal sequence and its value.
def find_seq(input):
    lines = input.splitlines()

    # Get K value.
    line_idx = 0
    k_val = int(lines[line_idx].strip())
    line_idx += 1

    # Get alphabet dictionary.
    alphabet = {}
    for _ in range(k_val):
        char, val = lines[line_idx].split()
        alphabet[char] = int(val)
        line_idx += 1

    # Get strings A and B.
    a_str = lines[line_idx]
    line_idx += 1
    b_str = lines[line_idx]

    # Make a table to store max solutions to subproblems.
    a_len = len(a_str)
    b_len = len(b_str)
    max_table = [[0] * (b_len + 1) for _ in range(a_len + 1)]

    # Iterate through the strings, filling up the subproblem table.
    for a_idx in range(1, a_len + 1):
        a_i = a_str[a_idx - 1]
        a_i_val = alphabet.get(a_i, 0)
        for b_idx in range(1, b_len + 1):
            if max_table[a_idx - 1][b_idx] >= max_table[a_idx][b_idx - 1]:
                max_val_no_match = max_table[a_idx - 1][b_idx]
            else:
                max_val_no_match = max_table[a_idx][b_idx - 1]

            if a_i == b_str[b_idx - 1]:
                match_val = max_table[a_idx - 1][b_idx - 1] + a_i_val
                if match_val > max_val_no_match:
                    max_val_no_match = match_val

            max_table[a_idx][b_idx] = max_val_no_match

    # Backtrack to find the optimal subsequence given the optimal value.
    backtrack_a_idx = a_len
    backtrack_b_idx = b_len
    optimal_subseq = []
    while backtrack_a_idx > 0 and backtrack_b_idx > 0:
        a_i = a_str[backtrack_a_idx - 1]
        if (
            a_i == b_str[backtrack_b_idx - 1]
            and max_table[backtrack_a_idx][backtrack_b_idx]
            == max_table[backtrack_a_idx - 1][backtrack_b_idx - 1]
            + alphabet.get(a_i, 0)
        ):
            optimal_subseq.append(a_i)
            backtrack_a_idx -= 1
            backtrack_b_idx -= 1
        elif (
            max_table[backtrack_a_idx - 1][backtrack_b_idx]
            >= max_table[backtrack_a_idx][backtrack_b_idx - 1]
        ):
            backtrack_a_idx -= 1
        else:
            backtrack_b_idx -= 1

    # Print the solutions.
    final_subseq = "".join(reversed(optimal_subseq))
    print(f"{max_table[a_len][b_len]}")
    print(f"{final_subseq}")


# This is the main function.
def main():
    root = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(root, "inputs")

    # Get the number of the input file.
    input_file_num = input("Enter input file number: ").strip()
    try:
        input_file_num = int(input_file_num) - 1
    except ValueError:
        input_file_num = 0

    # Get all the input files.
    input_files = []
    input_file_pattern = re.compile(r"^input_(\d+)\.txt$")
    for file_name in os.listdir(input_path):
        pattern_match = input_file_pattern.match(file_name)
        if pattern_match:
            file_num = int(pattern_match.group(1))
            input_files.append((file_num, os.path.join(input_path, file_name)))
    input_files.sort(key=lambda item: item[0])
    input_files = [file_path for _, file_path in input_files]

    # Find the corresponding input file.
    if input_file_num < 0 or input_file_num >= len(input_files):
        input_file = input_files[0]
    else:
        input_file = input_files[input_file_num]

    with open(input_file, "r", encoding="utf-8") as f:
        input_lines = f.read()

    find_seq(input_lines)


if __name__ == "__main__":
    main()