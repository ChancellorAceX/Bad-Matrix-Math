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

  With this being said, there are some matrices in which appear that the multiplication is much more of a translation than following the above methodology. For example:

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
  
## Finding applicable matrices
### V1
  For our first step, we wanted to know if there were any other matrix couplings in which this would also hold true. I did so assuming only single digit inputs, and then expanded to include positive non-single digit inputs. The function in *badMatMathv1* finds the answer to that. The output of which can be seen in *1-20 results.txt*.

### V2  
  Though this worked, this was a hastily created, brute-force function that was not quick by any means. As such, I reduced its run time significantly by skipping when able (see *badMatMathv2*).

### V3
  After we had received this list of results (of which there were 211 matches between 1-20) we realized that this is way more common that we had realized. So we set out to see if we could find anything in common, or some way to pre-determine if the matrices followed this pattern. But first, we wanted to collect a little more data, and this time on 3x3 matrices. As you can see in *badMatMathv3* I expanded to handle 3x3 matrices with similar skipping and logging as in v2. I also had it export to a text file instead of holding on to the data for an output, which should help with larger number sets and their run time since less data will need to be managed at a time. It also delivers a immediately usable file for both data sharing and analysis.

  I have hardcoded the output to push to the empty *test.txt* file here in the repo if you decide you want to try it. The results for 0-10 on 3x3 matrices are in the file *3x3 1-10 results.txt*.

## Analysis
  With that, the current step is to analyze the data and determine a rule as to why this occurs versus when it does not. The current idea is to look at eigenvalues of the matrices to see if there is anything to be learned from them.

### textToEigenCSV / getEVs
These two functions together allow us to put all the eigenvalues and eigenvectors for the previously found matrices into a pandas dataframe/CSV file for further analysis (ie - *3x3 file analysis.csv*). A little bit of cleaning was required as naturally lots of extra space and needless extra lines are put in. However after filtering these, and unfortunately not sorting eigenvectors with imaginary components within them, we can now start to do some analysis on the attributes of the matrices. On first glance it appears as though each pairing has identical eigenvectors (even if the associated eigenvalues aren't the same). Next step of the analysis is to verify if this is the case.

### CSV Fix
Outputs were all in strings. Updates have been implemented to change output/CSV from strings to desired raw data formats to make transfer from CSV easier. Also ammended *textToEigenCSV* to ouptut the pandas dataframe for direct manipulation immediate use just in case.

### Restructuring
Restructured the dataframe to split the eigenvalues from their associated vectors. Column names still keeps them paired, however testing/manipulating the individual vectors will be easier now that they aren't tied with the eigenvalues.

### Filtering
Started using the Jupyter notebook for piecewise steps/manipulation.

Data has now been filtered to remove imaginary eigenvectors. This is only because they will have to be compared in a different way since imaginary values aren't interpretted with the same methods as real values. That being said, imaginary values have been filtered out and will now be used to do the first step of data comparison/analysis.