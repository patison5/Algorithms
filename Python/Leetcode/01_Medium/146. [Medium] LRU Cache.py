# 146. [Medium] LRU Cache


class LRUCacheDLinkedItem():
    pass
    
class LRUCacheDLinkedItem():
    def __init__(
        self, 
        key: int, 
        value: int, 
        prev: LRUCacheDLinkedItem = None, 
        next: LRUCacheDLinkedItem = None
    ):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def set_next(self, next: LRUCacheDLinkedItem) -> None:
        self.next = next
    
    def set_prev(self, prev: LRUCacheDLinkedItem) -> None:
        self.prev = prev
    
    def get_next(self) -> None:
        return self.next

    def get_prev(self) -> None:
        return self.prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        if self.head == self.tail:
            return self.head.value

        cached_item = self.cache[key]
        cached_item = self.remove(key)
        cached_item = self.add(key, cached_item.value)
        print("get")
        self.debug()
        print("end of get\n")
        return cached_item.value
        

    def put(self, key: int, value: int) -> None:
        if self.head is None:
            self.head = LRUCacheDLinkedItem(key, value, None, None)
            self.tail = self.head
            self.cache[key] = self.head
        else:
            if key in self.cache:
                self.remove(key)
                self.put(key, value)
                return

            if len(self.cache.keys()) >= self.capacity:
                print("limit!", len(self.cache.keys()), self.capacity)
                self.remove(self.head.key)

            self.add(key, value)

        print("put")
        self.debug()
        print("end of put\n")

    def remove(self, key: int) -> LRUCacheDLinkedItem:
        if not key in self.cache:
            return

        removed_node = self.cache[key]
        prev_node = removed_node.prev
        next_node = removed_node.next

        # Если хвост или голова
        if prev_node is None or next_node is None:

            # Если элемент один в списке
            if prev_node is None and next_node is None:
                self.head = None
                self.tail = None
            else:
                # Если голова
                if prev_node is None:
                    self.head = next_node
                    next_node.prev = None

                # Если хвост
                if next_node is None:
                    prev_node.next = None

        self.cache.pop(key, None)
        return removed_node

    def add(self, key: int, value: int) -> LRUCacheDLinkedItem:
        if self.head is None:
            self.head = LRUCacheDLinkedItem(key, value, None, None)
            self.tail = self.head
            self.cache[key] = self.head
            return self.head

        new_node = LRUCacheDLinkedItem(key, value, self.tail, None)
        self.tail.next = new_node
        self.tail = new_node
        self.cache[key] = new_node
        return new_node
            

    def debug(self):
        t_head = self.head
        counter = 0
        while t_head:
            print(counter, {t_head.key, t_head.value})
            t_head = t_head.next
            counter += 1

obj = LRUCache(2)
# obj.put(2, 1)
# print(obj.get(2))
# a = [
# None,
# obj.put(1,1),
# obj.put(2,2),
# obj.get(1),
# obj.put(3,3),
# obj.get(2),
# obj.put(4,4),
# obj.get(3),
# obj.get(4)]
# print(a)


# obj = LRUCache(1)
# a = [
#     obj.put(2,1),
#     obj.put(1,1),
#     obj.put(2,3),
#     obj.put(4,1),
#     obj.get(1),
#     obj.get(2)
# ]

obj = LRUCache(2)
a = [
    obj.put(2,6),
    obj.get(1),
    obj.put(1,5),
    obj.put(1,2),
    obj.get(1),
    obj.get(2)
]


print(a)

# param_1 = obj.get(11)
# param_1 = obj.get(22)
# print(param_1)
