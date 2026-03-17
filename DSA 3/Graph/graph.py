# def add_node(v):
#     if v in graph:
#         print(v, "is allready presented")
#     else:
#         graph[v] = []

# ## unweighted- un directed graph
# # def add_edge(v1, v2):
# #     if v1 not in graph:
# #         print(v1, "is not present")
# #     elif v2 not in graph:
# #         print(v2, "is not present")

# #     else:
# #         graph[v1].append(v2)
# #         graph[v2].append(v1)

# # weighted - undirected
# def add_edge(v1, v2, cost):
#     if v1 not in graph:
#         print(v1, "is not presented")
#     elif v2 not in graph:
#         print(v2, "not presented")
#     else:
#         list1 = [v2, cost]
#         list2 = [v1, cost]

#         graph[v1].append(list1)
#         graph[v2].append(list2)

# # delelte a vertice - unweighted
# # def delete_node(v):
# #     if v not in graph:
# #         print(v, "is not presented")
# #     else:
# #         # delete key-value pair of the node
# #         graph.pop(v)

# #         for i in graph:
# #             list1 = graph[i]
# #             if v in list1:
# #                 list1.remove(v)


# ## delete a vertice - weighted
# def delete_node(v):
#     if v not in graph:
#         print(v," is not presented")
#     else:
#         graph.pop(v)
#         for i in graph:
#             list1 = graph[i]
#             for j in list1:
#                 if v == j[0]:
#                     list1.remove(j)
#                     break



# graph = {}
# add_node("A")
# add_node("B")
# add_node("C")

# add_edge("A", "C")
# add_edge("A", "B")
# delete_node("C")    

# ## unweighted
# # add_edge("A", "C", 30)
# # add_edge("A", "B", 40)
# # delete_node("C")


# print(graph)
#---------------------------------


class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v in self.graph:
            print(v, "is presented")
        else:
            self.graph[v] = []

        
    def add_edge(self, v1, v2):
        if v1 not in self.graph:
            print(v1, "is not presented")
            #self.add_vertex(v1) add vertice
        elif v2 not in self.graph:
            print(v2, "is not presented")
            # self.add_vertex(v2)
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)


    def remove_edge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph[v1]:
            self.graph[v1].remove(v2)

        if v2 in self.graph and v1 in self.graph[v2]:
            self.gaph[v2].remove(v1)


    def remove_vertex(self, vertex):
        if vertex not in self.graph:
            print(vertex, "not presented")
        else:
            self.graph.pop(vertex)

            for i in self.graph:
                list1 = self.graph[i]
                if vertex in list1:
                    list1.remove(vertex)

    def display(self):
        for vertex in self.graph:
            print(vertex, "-->", self.graph[vertex])


        

g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")


g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")
g.add_edge("C", "D")

g.remove_vertex("C")

g.display()