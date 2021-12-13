# the graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2


graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}



sample_dict = {
    "test": "a",
    "test2": "b",
}


for key,value in sample_dict.items():
    print(key)
    print(value)



print(sample_dict.popitem())