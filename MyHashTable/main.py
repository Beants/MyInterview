# 实现一个hash table，input数据是最长1024的ascii码，需要UT
class MyHashTable:
    def __init__(self):
        self.length = 1024  # input数据是最长1024
        self.data = [None for i in range(self.length)]  # 初始化

    # 获取哈希值
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.length

    def set(self, key, val):
        h = self.get_hash(key)
        self.data[h] = val

    def get(self, key):
        h = self.get_hash(key)
        return self.data[h]


if __name__ == '__main__':
    hash_table = MyHashTable()
    hash_table.set('a', 1)
    print(hash_table.get('a'))
