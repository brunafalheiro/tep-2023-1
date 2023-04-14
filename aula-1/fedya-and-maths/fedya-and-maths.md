# Fedya and Maths

Fedya studies in a gymnasium. Fedya's maths hometask is to calculate the following expression:

$(1^n+2^n+3^n+4^n)$ $mod$ $5$

for given value of $n$. Fedya managed to complete the task. Can you? Note that given number n can be extremely large (e.g. it can exceed any integer type of your programming language).

</br>

## Input

The single line contains a single integer $n (0 \le n \le 10^{10^5})$. The number doesn't contain any leading zeroes.

</br>

## Output

Print the value of the expression without leading zeros.

</br>

## Sample 1

| Input         | Output |
| :---:         | :---:  |
| 4             | 4      |

</br>

## Sample 2

| Input                       | Output |
| :---:                       | :---:  |
| 124356983594583453458888889 | 0      |

</br>

## Note

Operation x mod y means taking remainder after division x by y.

Note to the first sample:

$(1^4+2^4+3^4+4^4)$ $mod$ $5$ 

$= (1+16+81+256)$  $mod$ $5$

$= 354$ $mod$ $5$

$= 4$