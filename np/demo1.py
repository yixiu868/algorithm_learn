# 算法图解
# 集合覆盖问题--贪婪算法

# 包含需要覆盖的州
# 传入一个数组，转换为集合
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# 广播电台清单
stations = {'kone': set(['id', 'nv', 'ut']), 'ktwo': set(['wa', 'id', 'mt']), 'kthree': set(['or', 'nv', 'ca']),
            'kfour': set(['nv', 'ut']), 'kfive': set(['ca', 'az'])}

# 最终选择的广播台
final_stations = set()

# 最近电台组合
best_station = None
states_covered = set()

while states_needed:
    best_station = None
    states_covered = set()

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

if '__main__' == __name__:
    print(final_stations)
