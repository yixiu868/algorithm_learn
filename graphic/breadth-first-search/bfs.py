# BFS 深度优先搜索

from collections import deque

graph = {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"], "claire": ["thom", "jonny"],
         "anuj": [], "peggy": [], "thom": [], "jonny": []}


def person_is_seller(name):
    """
    判断是否为芒果经销商
    :param name:
    :return:
    """
    return name[-1] == 'm'


def search(name):
    """
    广度优先，查询最短路径
    运行时间：
    如果你在你的整个人际关系网中搜索芒果销售商，就意味着你将沿每条边前行，因此运行时间至少为O(边数)。
    你还是用了一个队列，其中包含要检查的每个人。将一个人添加到队列需要的时间是固定的，即O(1)，因此对每个人都这样做需要的总时间为O(人数)。所以，
    广度优先搜索的运行时间为O(人数+边数)，这通常写作O(V+E)，其中V为顶点数，E为边数。
    :param name:
    :return:
    """
    search_queue = deque()
    search_queue += graph[name]
    # 这个数组用于记录检查过的人
    searched = []
    while search_queue:
        person = search_queue.popleft()
        # 仅当这个人没检查过时才检查
        # 对检查过的人，务必不要再去检查，否则可能导致无限循环
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                # 将这个人标记为检查过
                searched.append(person)
    return False


if __name__ == '__main__':
    search("you")
