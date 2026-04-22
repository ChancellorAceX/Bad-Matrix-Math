# Bad-Matrix-Math
  Repo for working on solving a matrix multiplication problem

# The Problem

  Matrices have a specific methodology for multiplication. This can be used in many ways, but very notably can be used for solving systems of equations, multidimensional problems in physics, and combinatorics.

  Assume matrices are written with the following coordinate format:
   
  $$
  \begin{bmatrix}
    (0,0) & (0,1) & (0,2) \\
    (1,0) & (1,1) & (1,2) \\
    (2,0) & (2,1) & (2,2)
  \end{bmatrix}
  $$

  Matrices multiply using a row-to-column methodology in which the first row of the first matrix (A) is multiplied piecewise by the first column of the second (B). These value are then summed to provide the value in the top left position (C(0,0)). This process is then continued until each row from A has been multiplied by each column of B.

  An exmple of multiplying 2x2 matrices:

  $$
  \begin{bmatrix}
    a & b \\
    c & d 
  \end{bmatrix}
  *
  \begin{bmatrix}
    w & x \\
    y & z
  \end{bmatrix}
  =
  \begin{bmatrix}
    aw + by & ax+bz \\
    cw + dy & cx+bz
  \end{bmatrix}
  $$

  With this being said, there are some matrices in which appear that the multiplication is much more of a transposition than following the above methodology. For example:

  $$
  \begin{bmatrix}
    3 & 4 \\
    8 & 7 
  \end{bmatrix}
  *
  \begin{bmatrix}
    7 & 2 \\
    4 & 9
  \end{bmatrix}
  =
  \begin{bmatrix}
    37 & 42 \\
    84 & 79
  \end{bmatrix}
  $$
  
  Looking at the above multiplication, it would be easily assumed that multiplying matrices is merely taking the corresponding term from each matrix and concatenating them would result in the correct result for the final multiplied matrix. ie - 3 + 7 -> 37, etc.

  However, knowing how matrix multiplication works, we know this not to be true. It merely appears as such since:

  $$
  3*7 + 4*4 = 21+16 = 37
  $$

  And this holds true for the entirety of this case. 
# The Process
  
### V1
  For our first step, we wanted to know if there were any other matrix couplings in which this would also hold true. I did so assuming only single digit inputs, and then expanded to include positive non-single digit inputs. The function in *badMatMathv1* finds the answer to that. The output of which can be seen in *1-20 results.txt*.

### V2  
  Though this worked, this was a hastily created, brute-force function that was not quick by any means. As such, I reduced its run time significantly by skipping when able (see *badMatMathv2*).

### V3
  After we had received this list of results (of which there were 211 matches between 1-20) we realized that this is way more common that we had realized. So we set out to see if we could find anything in common, or some way to pre-determine if the matrices followed this pattern. But first, we wanted to collect a little more data, and this time on 3x3 matrices. As you can see in *badMatMathv3* I expanded to handle 3x3 matrices with similar skipping and logging as in v2. I also had it export to a text file instead of holding on to the data for an output, which should help with larger number sets and their run time since less data will need to be managed at a time. It also delivers a immediately usable file for both data sharing and analysis.

  I have hardcoded the output to push to the empty *test.txt* file here in the repo if you decide you want to try it. The results for 0-10 on 3x3 matrices are in the file *3x3 1-10 results.txt*.