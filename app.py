def check_n(a, i, j):
  count = 0
  
  for k in range(0,3):
      for v in range(0,3):
          n_i = i+k-1
          n_j = j+v-1 
          
          
          if n_i==i and n_j == j:
              continue
          if  n_i > 3 or n_j > 3 or n_i < 0 or n_j < 0:
              continue
          
          if a[n_i][n_j] == 1:
             
              count+=1
  return count
  
a =[[1, 0, 1, 1],
  [0, 1, 1, 0],
  [1, 0, 0, 0],
  [1, 0, 0, 1]]


 
for iteration in range(0,3):
  t =[[0, 0, 0, 0],
  [0, 0,0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0]]
      
  for i in range(0,4):
      for j in range(0,4):
          n = check_n(a, i, j)
          
          if a[i][j] == 1:
              if n <= 1:
                  t[i][j] = 0
              elif n >= 4:
                  t[i][j] = 0
              else:
                  t[i][j] = 1
          elif a[i][j]==0:
              if n == 3:
                  t[i][j] = 1
  for row in t:
      print(row)
  print()
  a = t.copy()
  
