from abstract import *

class MSDict(DictAbstract):

  def __init__(self):
    self.__list_dict = []

  def __len__(self):
    return self._list_size

  def _sort(self):
    if len(self) > 1:
      mid = len(self) // 2
      left = self[:mid]
      right = self[mid:]

      mergeSort(left)
      mergeSort(right)

      i, j, k = 0, 0, 0

      while i < len(left) and j < len(right):
        if left[i] < right[j]:
          self[k] = left[i]
          i += 1
        else:
            self[k] = right[j]
            j += 1
        k += 1

      while i < len(left):
        self[k] = left[i]
        i += 1
        k += 1

      while i < len(right):
        self[k] = right[j]
        j += 1
        k += 1

    return self
        
  def __contains__(self, key):
    return not self._find(self._root, key) is None

  def __getitem__(self, key):
    node = self._find(self.root, key)
    if node == None:
       raise KeyError("Item does not exist")  
    return node.value

    #recursive binary search
    
  def _search(arr, low, high, key):
    if high >= low:
      mid = high + low // 2
      
      if arr[mid] == key:
        return mid
        
      elif arr[mid] > key:
        return _search(arr, low, mid - 1, key)

      else:
        return _search(arr, mid + 1, high, key)

    else: 
      return - 1

  #Ilerative
  def _search(self, arr, key):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

      mid = high + low // 2

      if arr[mid] < key:
        low = mid + 1

      elif arr[mid] > key:
        high = mid - 1

      else:
        return mid
        
    return -1

  def __setitem__(self, key, value):
    if self._root == None:
        self._root = MSDict(key, value)
        self._size += 1
    else:
        self._insert(self._root, key, value)

  def pop(self, key):
    value = self[key]
    self._head = self._remove(self._head, key)
    self._length -= 1
    return value
  
  def _remove(self, node, key):
    assert node is not None, "Does not exist"
