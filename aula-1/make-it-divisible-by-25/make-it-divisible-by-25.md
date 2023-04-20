# Make it Divisible by 25

It is given a positive integer $n$. In 1 move, one can select any single digit and remove it (i.e. one selects some position in the number and removes the digit located at this position). The operation cannot be performed if only one digit remains. If the resulting number contains leading zeroes, they are automatically removed. E.g. if one removes from the number 32925 the 3-rd digit, the resulting number will be 3225. If one removes from the number 20099050 the first digit, the resulting number will be 99050 (the 2 zeroes going next to the first digit are automatically removed). What is the minimum number of steps to get a number such that it is divisible by 25 and positive? It is guaranteed that, for each $n$ occurring in the input, the answer exists. It is guaranteed that the number $n$ has no leading zeros.

</br>

## Input

The first line of input data contains an integer $t(1 \le t \le 10^{4} )$ — the number of test cases in the test. Then $t$ test cases follow

Each test case consists of one line containing one integer $n (25 \le n \le 10^18)$. It is guaranteed that, for each $n$ occurring in the input, the answer exists. It is guaranteed that the number $n$ has no leading zeros.

</br>

## Ouput

For each test case output on a separate line an integer $k (k \ge 0)$ — the minimum number of steps to get a number such that it is divisible by 25 and positive.

</br>

## Sample 1

| Input                      | Output |
| :---:                      | :---:  |
| 5                          | 0      |
| 100                        | 3      |
| 71345                      | 1      |
| 3259                       | 3      |
| 50555                      | 2      |
| 2050047                    |        |