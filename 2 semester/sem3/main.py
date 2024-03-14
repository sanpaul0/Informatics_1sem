def read_graph_as_edges():
    n = int(input())
    graph = [list(map(int, input().split())) for i in range(n)]
    return graph


def read_graph_as_neigh_list():
    edge_list = read_graph_as_edges()
    graph_dict = {}  # dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        if edge[0] not in graph_dict.keys():
            graph_dict[edge[0]] = frozenset([edge[1]])
        else:
            graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([edge[1]])
    return graph_dict


def read_graph_as_neigh_matrix():
    edge_list = read_graph_as_edges()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)

    res_matrix = [[0 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] - 1
        index_2 = edge[1] - 1
        res_matrix[index_1][index_2] = 1

    return res_matrix


def print_matrix(matrix):
    for line in matrix:
        print(*line)


def DFS(graph, v):
    global visited
    print(v)
    visited.append(v)
    for neigh in graph[v]:
        if neigh not in visited:
            DFS(graph, neigh)


def has_cycle(graph, v, visited=[]):
    result = False
    visited.append(v)

    for neigh in graph[v]:

        if neigh in visited:
            result = True
            return result

        if result == False:
            result = has_cycle(graph, neigh, visited)

    return result


def DFS_stack(graph, v, visited=[]):
    stack = []
    visited.append(v)
    stack.append(v)
    while stack:
        v = stack.pop()
        print(v)
        for neigh in graph[v]:
            if neigh not in visited:
                visited.append(neigh)
                stack.append(neigh)


def toplogical_sort(graph):
    sorted = []
    visiteed = [0 for i in range(len(graph))]

    def top_sort(graph, v, visiteed, sorted):
        visiteed[v - 1] = 1
        for j in graph[v]:
            if visiteed[j - 1] == 0:
                top_sort(graph, j, visiteed, sorted)
        sorted.insert(0, v)

    for i in range(1, len(graph) + 1):
        if visiteed[i - 1] == 0:
            top_sort(graph, i, visiteed, sorted)
    return sorted


def paths_between_vertexes(graph, u, v, ts_sort, ans=0):
    ind1 = ts_sort.index(u)
    ind2 = ts_sort.index(v)
    ts_graphs = set(ts_sort[ind1:ind2 + 1])
    s = set()
    if ts_graphs & graph[u] == set():
        return 0
    if v == u:
        return 0
    elif v in graph[u]:
        ans += 1
        for elems in graph[u]:
            ans += paths_between_vertexes(graph, elems, v, ts_sort, 0)
    else:
        for elem in graph[u]:
            ans += paths_between_vertexes(graph, elem, v, ts_sort, 0)
    return ans


def who_is_my_parent(graph, pairs) -> dict:
    ans = dict()
    a = toplogical_sort(graph)
    a.reverse()
    families = {}
    for i in graph:
        families[i] = set()

    def paths_sort(graph, u):
        if graph[u] == set():
            return set()
        else:
            families[u] |= graph[u]
            for neigh in graph[u]:
                families[u] |= families[neigh]
        return graph[u]

    for elem in a:
        paths_sort(graph, elem)
    for i in range(len(pairs)):
        if pairs[i][1] in families[pairs[i][0]]:
            ans[i] = True
        else:
            ans[i] = False
    return ans


graph = read_graph_as_neigh_list()
ts_sort = toplogical_sort(graph)
print(graph)
visited = []

print(toplogical_sort(graph))
q = int(input())
pairs = [list(map(int, input().split())) for i in range(q)]
print(who_is_my_parent(graph, pairs))
print(paths_between_vertexes(graph, 3, 5, ts_sort))
for i in graph:
    if (i not in visited) and (len(graph[i]) != 0):
        DFS(graph, i)

"""6
1 4
1 2
2 5
5 3
6 2
6 4



10
1 4
1 3
2 3
2 5
4 2
3 5
6 7
8 1
8 4
7 1
"""
