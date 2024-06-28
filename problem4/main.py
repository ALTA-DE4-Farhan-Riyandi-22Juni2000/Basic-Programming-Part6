def find_max_sum_sub_array(k, arr):

  max_sum = 0
  for i in range(0, len(arr)-k+1):
    temp = 0
    for j in range(i, i+k):
      temp += arr[j]

    if temp > max_sum:
      max_sum = temp
  return max_sum

if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8