# 加权最短路径 狄克斯特拉算法

# 节点及其邻居
graph = {'start': {}}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

# 创建开销表
infinity = float('inf')
costs = {'a': 6, 'b': 2, 'fin': infinity}

# 存储父节点的散列表
parents = {'a': 'start', 'b': 'start', 'fin': None}
processed = []


def find_lowest_cost_node(costs):
    """
    找出开销最低的节点
    :param costs:
    :return:
    """
    lowest_cost = float('inf')
    lowest_cost_node = None
    # 遍历所有的节点
    for node in costs:
        cost = costs[node]
        # 如果当前节点的开销更低，且未处理过，
        if cost < lowest_cost and node not in processed:
            # 就将其视为开销最低的节点
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra(costs):
    """
    狄克斯特拉算法Python代码
    :param costs:
    :return:
    """
    # 在未处理的节点中找出开销最小的节点
    node = find_lowest_cost_node(costs)
    # 这个while循环在所有节点都被处理过后结束
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        # 遍历当前节点的所有邻居
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # 如果经当前节点前往该邻居更近
            if costs[n] > new_cost:
                # 更新该邻居的开销
                costs[n] = new_cost
                # 同时将该邻居的父节点设置为当前节点
                parents[n] = node
        # 将当前节点标记为处理过
        processed.append(node)
        # 找出接下来要处理的节点，并循环
        node = find_lowest_cost_node(costs)


if '__main__' == __name__:
    dijkstra(costs)
    print('最短路径值', costs['fin'])
