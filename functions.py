import numpy as np
import re
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

def badMatMathv2(start,finish):
  """
    Prints a list of values that satisfy the problem's conditions to the console.
    0 is ignored for simplicity.
    This version should have a faster run time by skipping invalid combinations upon being assigned. Progress updates were also added for better transparency of the run.

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
        for w in testrange:
          for y in testrange:
              Ca = int(str(a)+str(w))
              if a*w+b*y!=Ca:
                 count+=len(testrange)**4
                 continue
              for x in testrange:
                for z in testrange:
                    Cb = int(str(b)+str(x))
                    if a*x+b*z!=Cb:
                       count+=len(testrange)**2
                       continue
                    for c in testrange:
                      for d in testrange:
                          count+=1
                          A=[a,b,c,d]
                          B=[w,x,y,z]
                          Cc=int(str(c)+str(y))
                          Cd=int(str(d)+str(z))
                          C=[Ca, Cb, Cc, Cd]
                          if matmult(A,B)==C:
                            sol.append([A,B,C])
                            print(f"Progress: {100*count/total}% Complete")
  for i in sol:
    print(i[0], i[1], i[2])
  print(len(sol), count)


filepath3x3 = "./test.txt"
def badMatMathv3(start,finish):
  testrange=range(start, finish+1)
  testrange=list(filter(lambda l:l!=0, testrange))
  count = 0
  rescount = 0
  total = len(testrange)**18
  with open(filepath3x3,'a') as file:
    for a in testrange:
       print(f'Progress: {100*count/total}% complete')
       for b in testrange:
          print(f'Progress: {100*count/total}% complete')
          for c in testrange:
            for r in testrange:
               for u in testrange:
                  for x in testrange:
                      xtest = a*r+b*u+c*x
                      if xtest != int(str(a)+str(r)):
                        # print(f'Progress: {100*count/total}% complete | {a} + {r} != {xtest}')
                        count+=len(testrange)**12
                        continue
                      for s in testrange:
                        for v in testrange:
                           for y in testrange:
                              ytest = a*s+b*v+c*y
                              if ytest != int(str(b)+str(s)):
                                  # print(f'Progress: {100*count/total}% complete | {b} + {s} != {ytest}')
                                  count+=len(testrange)**9
                                  continue
                              for t in testrange:
                                 for w in testrange:
                                    for z in testrange:
                                        ztest = a*t+b*w+c*z
                                        if ztest != int(str(c)+str(t)):
                                          # print(f'Progress: {100*count/total}% complete | {c} + {t} != {ztest}')
                                          count+=len(testrange)**6
                                          continue
                                        for d in testrange:
                                          for e in testrange:
                                             for f in testrange:
                                                dtest = d*r+e*u+f*x
                                                etest = d*s+e*v+f*y
                                                ftest = d*t+e*w+f*z
                                                if dtest != int(str(d)+str(u)):
                                                    # print(f'Progress: {100*count/total}% complete | {d} + {u} != {dtest}')
                                                    count+=len(testrange)**3
                                                    continue
                                                elif etest != int(str(e)+str(v)):
                                                    # print(f'Progress: {100*count/total}% complete | {e} + {v} != {ztest}')
                                                    count+=len(testrange)**3
                                                    continue
                                                elif ftest != int(str(f)+str(w)):
                                                    # print(f'Progress: {100*count/total}% complete | {f} + {w} != {ztest}')
                                                    count+=len(testrange)**3
                                                    continue
                                                for g in testrange:
                                                   for h in testrange:
                                                      for i in testrange:
                                                          count+=1
                                                          gtest = g*r+h*u+i*x
                                                          htest = g*s+h*v+i*y
                                                          itest = g*t+h*w+i*z
                                                          if gtest != int(str(g)+str(x)):
                                                              # print(f'Progress: {100*count/total}% complete | {g} + {x} != {ztest}')
                                                              continue
                                                          elif htest != int(str(h)+str(y)):
                                                              # print(f'Progress: {100*count/total}% complete | {h} + {y} != {ztest}')
                                                              continue
                                                          elif itest != int(str(i)+str(z)):
                                                              # print(f'Progress: {100*count/total}% complete | {i} + {z} != {ztest}')
                                                              continue
                                                          A = np.array([[a,b,c],[d,e,f],[g,h,i]])
                                                          B = np.array([[r,s,t],[u,v,w],[x,y,z]])
                                                          C = A @ B
                                                          Ctest = np.array([
                                                              [int(str(a)+str(r)),int(str(b)+str(s)),int(str(c)+str(t))],
                                                              [int(str(d)+str(u)),int(str(e)+str(v)),int(str(f)+str(w))],
                                                              [int(str(g)+str(x)),int(str(h)+str(y)),int(str(i)+str(z))]
                                                              ])
                                                          if (Ctest == C).all():
                                                              rescount+=1
                                                              print(f'Progress: {100*count/total}% complete')
                                                              Astr = str(A).replace('\n','')
                                                              Bstr = str(B).replace('\n','')
                                                              Cstr = str(C).replace('\n','')
                                                              resultstring = f"{Astr} | {Bstr} | {Cstr}"
                                                              print(resultstring)
                                                              file.write(f'#{rescount}: {resultstring}\n')
  print('run complete')

badMatMathv3(0,10)