# COP4533-Dynamic-Programming

by Zach Pinet 5701-3785

## Run Instructions and Assumptions

Inputs are to be in a standalone .txt file and placed into the inputs/ folder. They must be named 'input_<#>.txt'. They are sorted numerically by #, and the program will prompt you to enter an integer 'i'. The program will then run on the 'i'th sorted file (1-indexed, to match the names). If an invalid input is entered, it defaults to the first file, input_1.txt.

The program only prints its outputs, but sample output files can be found in the outputs/ folder.

To run the program, just run the src/find_seq.py file.

## Question 1

![Runtime Graph](<HVLCS Runtimes.png>)

## Question 2

```
              { 0                                if i = 0 or j = 0
              {     { HVLCS[i-1][j]
              { max { HVLCS[i][j-1]              if A[i] = B[j]
HVLCS[i][j] = {     { HVLCS[i-1][j-1] + v(A[i])
              {
              { max { HVLCS[i-1][j]              if A[i] != B[j]
              {     { HVLCS[i][j-1]
```

This recurrance equation has 0 as the base case. Case 1, where i and j match, will either skip i, skip j, or add the match to the optimal string, and add its value. Case 2, where there is no match, will either skip i or skip j.

## Question 3

```
HVLCS-Length(A, B, value):
m = length(A)
n = length(B)

val_array = 2D array (m+1) * (n+1)
len_array = 2D array (m+1) * (n+1)

for i = 1 to m:
    for j = 1 to n:
        # Option 1: Skip i.
        best_val = val_array[i-1][j]
        best_len = len_array[i-1][j]

        # Option 2: Skip j.
        if val_array[i][j-1] > best_val
               or (val_array[i][j-1] == best-val and len_array[i][j-1] > best_len):
                best_val = val_array[i][j-1]
                best_len = len_array[i][j-1]

            # Option 3: Take match.
            if A[i] == B[j]:
                candidate_val = val_array[i-1][j-1] + value[A[i]]
                candidate_len = len_array[i-1][j-1] + 1

                if candidate_val > best_val
                   or (candidate_val == best_val and candidate_len > best_len):
                    best_val = candidate_val
                    best_len = candidate_len

            val_array[i][j] = best_val
            len_array[i][j] = best_len

    return len_array[m][n]
```

The runtime is O(m*n).