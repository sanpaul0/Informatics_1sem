def read_graph_as_edges_w():
    n = int(input())
    graph = [list(map(int, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return graph


def read_graph_as_neigh_list_w():
    edge_list = read_graph_as_edges_w()
    graph_dict = {}  # dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1], edge[2])])
    return graph_dict


def read_graph_as_neigh_matrix_w():
    edge_list = read_graph_as_edges_w()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)

    res_matrix = [[0 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] - 1
        index_2 = edge[1] - 1
        res_matrix[index_1][index_2] = edge[2]

    return res_matrix


def read_graph_as_edges_w_s():
    n = int(input())
    graph = [list(map(str, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return graph


def read_graph_as_neigh_list_w_s():
    edge_list = read_graph_as_edges_w()
    graph_dict = {}  # dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(int(edge[0]))
        vertex_set.add(int(edge[1]))
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        graph_dict[int(edge[0])] = graph_dict[int(edge[0])] | frozenset([(int(edge[1]), edge[2])])
    return graph_dict


def read_graph_as_neigh_matrix_w_s():
    edge_list = read_graph_as_edges_w()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(int(edge[0]))
        vertex_set.add(int(edge[1]))
    V_num = len(vertex_set)

    res_matrix = [[0 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = int(edge[0]) - 1
        index_2 = int(edge[1]) - 1
        res_matrix[index_1][index_2] = int(edge[2])

    return res_matrix


def print_matrix_w(matrix):
    for line in matrix:
        print(*line)


def DFS_w(graph, v, visited=[]):
    # print(v)
    visited.append(v)
    for neigh in graph[v]:
        if neigh not in visited:
            DFS_w(graph, neigh, visited)


def has_cycle_w(graph, v, visited=[]):
    result = False
    visited.append(v)
    for neigh in graph[v]:

        if neigh in visited:
            result = True
            return result

        if result == False:
            result = has_cycle_w(graph, neigh, visited)

    return result


def toplogical_sort_w(graph):
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


def bfs_w(graph, v):
    visited = []
    queue = []
    d = {}
    for keys in graph.keys():
        d[keys] = float('infinity')
    visited.append(v)
    queue.append(v)
    d[v] = 0

    while queue:
        u = queue.pop(0)
        print(u, end=" ")

        for neighdour in graph[u]:
            if neighdour not in visited:
                visited.append(neighdour)
                queue.append(neighdour)
                d[neighdour] = d[u] + 1
    return d


def Dijkstra(graph, v):
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = float('infinity')

    d[v] = 0
    visited.append([0, v])
    while visited:
        visited.sort()

        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] + neigh[1]) < d[neigh[0]]:
                    d[neigh[0]] = (d[c[1]] + neigh[1])
                visited.append(neigh[::-1])

    return d


def Dijkstra_max(graph, v):
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = float('infinity')

    d[v] = 0
    visited.append([0, v])
    while visited:
        visited.sort()

        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if max(neigh[1], d[c[1]]) < d[neigh[0]]:
                    d[neigh[0]] = max(neigh[1], d[c[1]])
                visited.append(neigh[::-1])
    return d


def Dijkstra_multiplication(graph, v):
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = float('infinity')

    d[v] = 1
    visited.append([0, v])
    while visited:
        visited.sort()

        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] * neigh[1]) < d[neigh[0]]:
                    d[neigh[0]] = (d[c[1]] * neigh[1])
                visited.append(neigh[::-1])

    d[v] = 0
    return d


def Dijkstra_for_strings(graph, v):  # ДЛЯ РАБОТЫ ЭТОЙ ФУНКЦИИ ИСПОЛЬЗОВАТЬ ФУНКЦИИ СЧИТЫВАНИЯ С ПРИПИСКОЙ _s
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = 'я' * 50

    d[v] = ''
    visited.append(['', v])
    while visited:
        visited.sort()

        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] + neigh[1]) < d[neigh[0]]:
                    d[neigh[0]] = (d[c[1]] + neigh[1])
                visited.append(neigh[::-1])
    for i in range(len(d)):
        if d[i + 1] == 'я' * 50:
            d[i + 1] = None

    return d


def Dijkstra_rev(graph, v):
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = 0

    d[v] = float('infinity')
    visited.append([0, v])
    while visited:
        visited.sort()
        c = visited.pop(-1)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if min(neigh[1], d[c[1]]) > d[neigh[0]]:
                    d[neigh[0]] = min(neigh[1], d[c[1]])
                visited.append(neigh[::-1])
    # for i in range(1, len(d) + 1):
    # d[i] = abs(d[i] - 10 ** 9)
    return d


graph = read_graph_as_neigh_list_w()
print(graph)
print(Dijkstra_rev(graph, 1))

'''
8
1 4 6
1 2 1
3 2 2
2 5 3
2 6 1
5 3 2
6 2 2
6 4 5
'''

"""
8
1 4 dcscsda
1 2 dcddwaaw
3 2 dcAdaFGRRE
2 5 gflakf
2 6 844unu8nu492i9
5 3 t53099ujgimfk
6 2 if49u09gi0w
6 4 ifmjiwf8qu9fij3
"""

"""
10
1 2 1
2 4 8
4 6 3
6 8 2
8 10 4
1 3 10
3 5 11
5 7 22
7 9 5
9 10 4
"""

"""

"""
