# 加权最短路径 狄克斯特拉算法

graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs: # 遍历所有的节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # 如果当前节点的开销更低，且未处理过，
            lowest_cost = cost # 就将其视为开销最低的节点
            lowest_cost_node = node
    return lowest_cost_node


# 在未处理的节点中找出开销最小的节点
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # 遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # 如果经当前节点前往该邻居更近
            costs[n] = new_cost # 更新该邻居的开销
            parents[n] = node   # 同时将该邻居的父节点设置为当前节点
    processed.append(node)      # 将当前节点标记为处理过
    node = find_lowest_cost_node(costs)

print('最短路径值', costs['fin'])