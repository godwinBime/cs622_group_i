from collections import deque

class BFS_DFS:
    def __init__(self):
        #   constructs and initializes and empty graph using an
        #   adjacency list
        self.graph = {}

    def insert_edge(self, node_u, node_v):
        #   adds an edge from node u to node v
        #   If node u is not already in the graph, it initializes an empty list for node u.
        if node_u not in self.graph:
            self.graph[node_u] = []
        self.graph[node_u].append(node_v)

    def breadth_first_search(self, start_node):
        #   performs breadth first search using a queue data structure
        #   visited is a set to keep track of visited nodes.
        #   queue is initialized with the start node using deque for efficient queue operations.
        #   The while loop continues until the queue is empty.
        #   If vertex is not visited, it is marked as visited and processed
        #   The neighbors of vertex are added to the queue if they have not been visited.
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            for neighbor_node in self.graph.get(vertex, []):
                if neighbor_node not in visited:
                    visited.add(neighbor_node)
                    queue.append(neighbor_node)


    def depth_first_search(self, start_node):
        #   performs depth first search using a stack data structure from start node
        #   visited is a set to keep track of visited nodes.
        #   stack is initialized with the start node.
        #   The while loop continues until the stack is empty.
        #   In each iteration, the top vertex is popped from the stack.
        #   The neighbors of vertex are added to the stack in reversed order to maintain the correct traversal order.
        visited = set()
        stack = [start_node]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                for neighbor_node in reversed(self.graph.get(vertex, [])):
                    if neighbor_node not in visited:
                        stack.append(neighbor_node)


def main():
    graph = BFS_DFS()
    #   add nodes into the graph
    graph.insert_edge('A', 'B')
    graph.insert_edge('A', 'C')
    graph.insert_edge('B', 'D')
    graph.insert_edge('B', 'E')
    graph.insert_edge('C', 'F')
    graph.insert_edge('E', 'F')

    #   perform breadth first search
    print("Breadth first search begins:")
    graph.breadth_first_search('A')
    print("\nBreadth first search ends.")

    #   perform depth first search
    print("\nDepth first search begins:")
    graph.depth_first_search('A')
    print("\nDepth first search ends")

if __name__ == "__main__":
    main()