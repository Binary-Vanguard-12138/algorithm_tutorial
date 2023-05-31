def sort(list, left_pos, middle_pos, right_pos):
  left = list[left_pos: middle_pos]
  right = list[middle_pos: right_pos]

  i = left_pos
  j = 0
  k = 0
  while j < len(left) and k < len(right):
    if (left[j] < right[k]):
      list[i] = left[j]
      j += 1
      i += 1
    else:
      list[i] = right[k]
      k += 1
      i += 1

  while j < len(left):
    list[i] = left[j]
    j += 1
    i += 1
  
  while k < len(right):
    k += 1
    i += 1
  


def merge_sort(list):
  n = len(list)
  width = 1
  while width < n:
    left_pos = 0
    while left_pos < n:
      right_pos = min(left_pos + 2 * width, n)
      mid_pos = min(left_pos + width, n)
      sort(list, left_pos, mid_pos, right_pos)
      left_pos += 2 * width
    width *= 2
  return

def verify_sorted(list):
  n = len(list)
  if n <= 1:
    return True
  for i in range(n - 1):
    if list[i] > list[i + 1]:
      return False

  return True


list = [6,3,8,4,9,0,7,5,2,1]
print(verify_sorted(list=list))
merge_sort(list)
print(list)
print(verify_sorted(list=list))

