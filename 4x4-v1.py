def matmult(A,B):
   """
    Basic hard-coded matrix multiplication designed only for 2x2 multiplication.
    
    Parameters:
      A, B: 2x2 Matrix entered as a 4x1 array

    Returns:
      array: Resulting matrix written as a 4x1 array
   """
   return [
      A[0]*B[0]+A[1]*B[2],
      A[0]*B[1]+A[1]*B[3],
      A[2]*B[0]+A[3]*B[2],
      A[2]*B[1]+A[3]*B[3],
   ]

def det(mat):
   """
    Hard coded function that returns the determinant of a 2x2 matrix.

    Parameters:
      mat: 2x2 matrix written as a 4x1 array

    Returns:
      int: The determinant of the entered matrix 
   """
   return mat[0]*mat[3]-mat[2]*mat[1]

def badMatMathv1(start,finish):
  """
    Prints a list of values that satisfy the problem's conditions to the console.
    0 is ignored for simplicity.

    Args:
      start: beginning number
      finish: finishing number

    Returns:
      null
  """
  testrange=range(start, finish+1)
  testrange=list(filter(lambda l:l!=0, testrange))
  sol=[]
  count = 0
  total = len(testrange)**8
  for a in testrange:
    for b in testrange:
        for c in testrange:
          for d in testrange:
              for w in testrange:
                for x in testrange:
                    for y in testrange:
                      for z in testrange:
                          count=count+1
                          A=[a,b,c,d]
                          B=[w,x,y,z]
                          # Ca = 10*a+w
                          # Cb = 10*b+x
                          # Cc = 10*c+y
                          # Cd = 10*d+z
                          Ca=int(str(a)+str(w))
                          Cb=int(str(b)+str(x))
                          Cc=int(str(c)+str(y))
                          Cd=int(str(d)+str(z))
                          C=[Ca, Cb, Cc, Cd]
                          if matmult(A,B)==C:
                            sol.append([A,B,C])
                            print(f"Progress: {100*count/total}% Complete")
  for i in sol:
    print(i[0], i[1], i[2])
  print(len(sol), count)

badMatMathv1(0,20)