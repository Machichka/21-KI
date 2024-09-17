lst = [123, 'hello', 4.56, True, 789, False, 'world', 3.14, 100, None, [1234, 425, "gfdgd"], {123, True, None, "qwrt"}, ("apple", "banana", "cherry")]
tp = [type(value) for value in lst]
from collections import Counter
mst_type = Counter(tp).most_common()
print(Counter(tp))
print(mst_type[0])