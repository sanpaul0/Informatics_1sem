from heapq import *
import copy


def read_graph_as_edges_w():
    n = int(input())
    graph = [list(map(str, input().split())) for i in range(n)]
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


def read_graph_as_neigh_list_sp(edge_list):
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


def get_key(d, value):
    for k, v in d.items():
        if value in v:
            return k


def read_graph_as_edges_w_s():
    n = int(input())
    graph = [list(map(str, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return graph


def read_graph_as_neigh_list_w_s():
    edge_list = read_graph_as_edges_w_s()
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
    edge_list = read_graph_as_edges_w_s()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(int(edge[0]))
        vertex_set.add(int(edge[1]))
    V_num = len(vertex_set)

    res_matrix = [[0 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = int(edge[0]) - 1
        index_2 = int(edge[1]) - 1
        res_matrix[index_1][index_2] = edge[2]

    return res_matrix


def read_graph_as_neigh_matrix_w_s_special_for_problem(edge_list):
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(int(edge[0]))
        vertex_set.add(int(edge[1]))
    V_num = len(vertex_set)

    res_matrix = [[0 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = int(edge[0]) - 1
        index_2 = int(edge[1]) - 1
        res_matrix[index_1][index_2] = edge[2]

    return res_matrix


def print_matrix(matrix):
    for line in matrix:
        print(*line)


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
    return visited


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


def bfs(graph, v):
    visited = []
    queue = []
    d = {}
    for keys in graph.keys():
        d[keys] = 100000
    visited.append(v)
    queue.append(v)
    d[v] = 0
    while queue:
        u = queue.pop(0)
        print(u, end=" ")

        for neighbour in graph[u]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                d[neighbour] = d[u] + 1
    return d


def dijkstra(graph, v):
    d = {}
    visited = []
    end = []
    for elem in graph.keys():
        d[elem] = 1000000000
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


def Floyd_Warshall(graph):
    v = len(graph)
    d = [[float('infinity') for i in range(v)] for j in range(v)]
    nxt = [[-1 for i in range(v)] for j in range(v)]
    for i in range(v):
        for j in range(v):
            if graph[i][j] != 0:
                d[i][j] = graph[i][j]
                nxt[i][j] = j
    for k in range(1, v):
        for i in range(v):
            for j in range(v):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    nxt[i][j] = nxt[i][k]
    return d, nxt


def pth(i, j):
    p = [i]
    # i = nxt[i][j]
    while nxt[i - 1][j - 1] != j:
        i = nxt[i - 1][j - 1] + 1
        p.append(i)
    p.append[j]
    return p


def negative_cycle(graph):  # ТОЛЬКО В МАТРИЧНОЙ ФОРМЕ
    flag = False
    s = FB_spec(graph, 1)
    if s[0] < 0:
        return not flag
    return flag


def inequality_system():
    system = read_graph_as_edges_w_s()
    for i in range(len(system)):
        system[i][0] = int(system[i][0])
        system[i][1] = int(system[i][1])
        if system[i][2][0] == '<':
            system[i][0], system[i][1] = system[i][1], system[i][0]
        system[i][2] = int(system[i][2][1:])
    syst = read_graph_as_neigh_matrix_w_s_special_for_problem(system)
    return not negative_cycle(syst)


def FB_spec(graph, s):
    V = len(graph)
    d = [100000000000 for i in range(V)]
    d[s - 1] = 0
    for elem in graph:
        if d[elem[1]] > d[elem[0]] + elem[2]:
            d[elem[1]] = d[elem[0]] + elem[2]
    return d


def FB(graph, s):
    V = len(graph)
    d = [10000000000 for i in range(V)]
    d[s - 1] = 0
    for elem in graph:
        for edge in graph[elem]:
            if d[edge[0] - 1] > d[get_key(graph, edge) - 1] + edge[1]:
                d[edge[0] - 1] = d[get_key(graph, edge) - 1] + edge[1]
    return d


def FB_path(graph, s, t):
    v = len(graph)
    w = 0
    for elem in graph:
        w += len(elem)
    matr = [10000000 for i in range(w) for j in range(v)]
    matr[s][0] = 0
    p = matr
    path = [0 for i in range(w)]
    for i in range(1, v - 1):
        for elem in graph:
            for edge in graph[elem]:
                if matr[edge[0] - 1][i] > matr[get_key(graph, edge) - 1] + edge[1]:
                    matr[edge[0] - 1][i] = matr[get_key(graph, edge) - 1] + edge[1]
                    p[edge[0] - 1][i] = get_key(graph, edge)
    edges_in_pth = matr[t - 1].index(min(matr[t - 1]))
    while edges_in_pth > 0:
        path[edges_in_pth] = t
        t = p[t][edges_in_pth]
        edges_in_pth -= 1
    return path


def kruskal(graph):  # read_graph_as_edges
    Rs = graph
    for e in Rs:
        e[0], e[2] = e[2], e[0]
    U = set()
    D = {}
    T = []

    for r in Rs:
        if r[1] not in U or r[2] not in U:
            if r[1] not in U and r[2] not in U:
                D[r[1]] = [r[1], r[2]]
                D[r[2]] = D[r[1]]
            else:  # иначе
                if not D.get(r[1]):
                    D[r[2]].append(r[1])
                    D[r[1]] = D[r[2]]
                else:
                    D[r[1]].append(r[2])
                    D[r[2]] = D[r[1]]

            T.append(r)
            U.add(r[1])
            U.add(r[2])

    for r in Rs:
        if r[2] not in D[r[1]]:
            T.append(r)
            gr1 = D[r[1]]
            D[r[1]] += D[r[2]]
            D[r[2]] += gr1
    return T


def prim(graph):  # read_graph_as_neigh_list_w
    v = 1
    tmp = list(graph[v])
    h = []
    for e in tmp:
        h.append([e[1], e[0], v])
    heapify(h)
    tree_v = set([v])
    tree_e = []
    while h:
        e_min = heappop(h)
        if e_min[1] not in tree_v:
            tree_v.add(e_min[1])
            for e in graph[e_min[1]]:
                t = [e[1], e[0]]
                heappush(h, (list(t) + [e_min[1]]))
            v = e_min[1]
            tree_e.append(e_min)
        else:
            continue
    return tree_e


def edges_in_MST():
    n, m = map(int, input().split())
    graph = []
    g = []
    U = set()
    D = {}
    T = [set() for i in range(n)]
    ans = {}
    for i in range(m):
        ans[i + 1] = 'at least one'
    for i in range(m):
        edge = list(map(int, input().split()))
        g.append(edge)
        redge = copy.deepcopy(edge)
        redge[0], redge[1] = redge[1], redge[0]
        g.append(redge)
        edge[0], edge[2] = edge[2], edge[0]
        graph.append(copy.deepcopy(edge))
    gr = copy.deepcopy(graph)
    graph.sort()
    c = graph[0][0]
    while c < graph[-1][0]:
        for r in graph:
            if r[0] > c:
                break
            if (r[1] not in U) and (r[2] not in U):
                D[len(D) + 1] = [r]
                U.add(r[1])
                U.add(r[2])
                T[len(D) - 1].add(r[1])
                T[len(D) - 1].add(r[2])
            elif (r[1] not in U) or (r[2] not in U):
                for elem in D:
                    for e in D[elem]:
                        if ((r[1] in e) or (r[2] in e)) and ((r[1] not in T[elem - 1]) or (r[2] not in T[elem - 1])):
                            D[elem].append(r)
                            T[elem - 1].add(r[1])
                            T[elem - 1].add(r[2])
                            U.add(r[1])
                            U.add(r[2])
                            break
                    break
    for r in gr:
        for e in D:
            if (r[1] in T[e - 1]) and (r[2] in T[e - 1]) and (r not in D[e]):
                ans[gr.index(r) + 1] = 'none'

    return ans


"""
graph = read_graph_as_neigh_list_w()
print(graph)
#print(bfs(graph, 1))
print(dijkstra(graph, 1))"""
# G = read_graph_as_neigh_matrix_w()
# G_neg = read_graph_as_neigh_matrix_w()
# print(read_graph_as_edges_w_s())
# G_exp = read_graph_as_neigh_matrix_w()
# print_matrix(Floyd_Warshall(G_exp))
# g = read_graph_as_neigh_list_w()
# print(inequality_system())
# print(FB(g, 1))
graph = read_graph_as_edges_w()
print(kruskal(graph))
print(edges_in_MST())

E = kruskal(graph)
print(E)
"""
10
1 2 3
1 3 6
2 4 2
2 5 5
3 4 7
4 5 1
5 6 8
4 6 11
3 7 9
7 6 10


"""

""" exp
12
1 2 <-1
2 1 <-1
1 3 <-1
3 1 <-1
1 4 <-1
4 1 <-1
2 3 <-1
3 2 <-1
2 4 <-1
4 2 <-1
3 4 <-1
4 3 <-1
"""
""" neg 
5
1 2 1
1 3 6
3 2 -3
2 4 1
4 3 1"""
'''5
1 2 1
2 4 1
3 4 1
2 3 4
1 3 6'''
"""
8
1 4 6
1 2 1
3 2 2
2 5 3
2 6 1
5 3 1
6 2 2
6 4 1
"""
"""
14
1 4 6
4 1 6
1 2 1
2 1 1
3 2 2
2 3 2
2 5 3
5 2 3
2 6 1
6 2 1
5 3 1
3 5 1
6 4 1
4 6 1
"""
