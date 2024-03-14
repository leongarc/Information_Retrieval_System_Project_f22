from abstract import DictAbstract


#HashDict - Zachary Malloy
class HTDict(DictAbstract):

    #Sets list hard limit and count
    def __init__(self):
        self.__list_dict = [[]] * 20
        self.__count = 0

    #Return number of list
    def __len__(self):
        return self.__count

    #return if key is found in dict
    def __contains__(self, key):
        return not self._search(key) is None

    def __getitem__(self, key):
        node = self._search(key)
        print("hello")
        if node == None:
            raise KeyError("Does not exist")
        return node

    #If the key is found, return information
    def _search(self, key):
        index = self.hash(key)
        list = self.__list_dict[index]
        for i in range(len(list)):
            #print(list[i])
            if key == list[i][0]:
                value = list[i][1]
                return value

        return None

    def __setitem__(self, key, value):
        index = self.hash(key)
        list = self.__list_dict[index]
        list.append([key, value])
        self.__count += 1
        #print(list)
        return

    def pop(self, key):
        pass

    #Hash Function for value
    def hash(self, key):
        if type(key) == int:
            key = int(key)
            #print(key)
            if key < 100 and key >= 0:
                return 0
            while (key >= 20):
                key = key // 20
            index = key
            #print(index)
            return index
        else:
            length = len(key)
            while (length >= 20):
                length = length // 20
            index = length
            return index
