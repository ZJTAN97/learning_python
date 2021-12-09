from collections import deque

def person_is_seller(name):
    """
    person is mango seller if the first letter is 'm' in this case
    """
    return name[-1] == 'm'


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]

    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f'{person} is a mango seller.')
            else:
                search_queue += graph[person]
                searched.add(person)

if __name__ == "__main__":
    search("you")