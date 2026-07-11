class MyHashMap:

    def __init__(self):
        self.hash_list=[[] for i in range(10000)]

    def put(self, key: int, value: int) -> None:
        index=key%10000

        if self.hash_list[index]:
            self.hash_list[index][0][1]=value
        else:
            self.hash_list[index].append([key,value])


    def get(self, key: int) -> int:
        index=key%10000

        if not self.hash_list[index]:
            return -1
        else:
            return self.hash_list[index][0][1]

    def remove(self, key: int) -> None:
        index=key%10000

        if self.hash_list[index]:
           del self.hash_list[index][0]
         
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)