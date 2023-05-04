def maior_elemento(list):
  maxvalor = list[0];
  for val in list:
    if maxvalor < val :
      maxvalor = int(val)
  return maxvalor

print(maior_elemento)