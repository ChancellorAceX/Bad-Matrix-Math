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
  
  For our first step, we wanted to know if there were any other matrix couplings in which this would also hold true. The function in *madMatMathv1* finds the answer to that. The output of which can be seen in *1-20.txt*.

  Though this worked, this was a hastily created, brute-force function that was not quick by any means. As such, I reduced its run time significantly by skipping when able.