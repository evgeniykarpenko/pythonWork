def binary_search(list, item):
  # low and high save ranges
  low = 0
  high = len(list) - 1

  while low <= high:
    # ... check the middle element
    mid = (low + high) // 2
    guess = list[mid]
    # if found
    if guess == item:
      return mid
    # if was too high.
    if guess > item:
      high = mid - 1
    # if was too low.
    else:
      low = mid + 1

  # doesn't exist
  return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # => 1

my_list = [1, 3, 5, 7, 9, 56, 67, 99]
print(binary_search(my_list, 56)) # => 1

# 'None' means nil in Python. We use to indicate that the item wasn't found.
print(binary_search(my_list, -1)) # => None
