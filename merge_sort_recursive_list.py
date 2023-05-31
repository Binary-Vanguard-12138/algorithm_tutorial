def split(list):
  mid = len(list) // 2
  left = list[:mid]
  right = list[mid:]
  return left, right

def merge(left, right):
  i = 0
  j = 0
  l = []
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      l.append(left[i])
      i += 1
    else:
      l.append(right[j])
      j += 1
  
  while i < len(left):
    l.append(left[i])
    i += 1

  while j < len(right):
    l.append(right[j])
    j += 1
  
  return l

def merge_sort_recursive(list):
  if len(list) <= 1:
    return list
  left, right = split(list)
  left_sorted = merge_sort_recursive(left)
  right_sorted = merge_sort_recursive(right)
  return merge(left_sorted, right_sorted)


def verify_sorted(list):
  n = len(list)
  if n <= 1:
    return True
  for i in range(n - 1):
    if list[i] > list[i + 1]:
      return False

  return True


list = [6,3,8,4,9,7,5,2,1]
print(verify_sorted(list=list))
sorted_list = merge_sort_recursive(list)
print(sorted_list)
print(verify_sorted(list=sorted_list))

