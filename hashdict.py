
from abstract import *

#HashDict - Zachary Malloy
class HTDict(DictAbstract):

  def __init__(self):
    self .list_dict = 20
    self .list_size = list_dict
    self .keys = [None] * self.__list_dict
    self .value = [None] * self.__list_dict

  def __len__(self):
    return self._list_size

  #Gotta fix
  def _get_index(self, key, value):
    while self.keys[key_index]:
      if self.__keys[key_index] == key:
        self.__value[key_index] == Value

    key_index = (index + 1) % self.list_dict

  def _find(self, parent_list, key):
    for index in range(len(parent_list)):
      node = parent_list[index]
      [key, value] = node
      if i_key == key:
        return [index, value]
    return None

  def remove(self, key):
      key_index = self.get_index(key)
      parent_list = self.data_list[key_index]
      find_result = self._find(parent_list, key)

      if find_result is not None:
        parent_list.pop(index)

  def put(self, key, value):
      key_index = self._get_index(key)
      parent_list = self.data_list[key_index]
      find_result = self._find(parent_list, key)

      if find_result is None:
          parent_list.append([key, value])
      else:
          [index, _] = find_result
          parent_list[index] = [key, value]
        
  def get(self, key):
      key_index = self._get_index(key)
      parent_list = self.data_list[key_index]
    
      find_result = self._find(parent_list, key)

      if find_result is None:
          return None

      [_, value] = find_result

      return value
