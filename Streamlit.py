#!/usr/bin/env python
# coding: utf-8

# In[10]:


import streamlit as st

# Directed acyclic graph of complexity classes
graph = {
    'ALL': ['EXP', 'Ppoly'],
    'EXP': ['PSPACE'],
    'PSPACE': ['P#P'],
    'P#P': ['PH', 'PP'],
    'PP': ['BQP', 'MA', 'coNP'],
    'PH': ['AM', 'coNP'],
    'BQP': ['BPP'],
    'Ppoly': ['BPP'],
    'AM': ['SZK', 'MA'],
    'MA': ['BPP', 'NP'],
    'coNP': ['P'],
    'NP': ['P'],
    'BPP': ['P'],
    'P': ['NC'],
    'NC': ['L'],
    'L': ['AC0']
}

# Dictionary to store the messages for each class
messages = {('P', 'NP'): 'There exists an oracle w.r.t which P is not equal to NP',
            ('NP','P'): 'There exists an oracle w.r.t which P is not equal to NP',
           ('PH','NP'): 'There exists an oracle w.r.t which PH is not equal to NP',
            ('NP','PH'): 'There exists an oracle w.r.t which PH is not equal to NP',
           ('PH','P'): 'There exists an oracle w.r.t which PH is not equal to P',
            ('P','PH'): 'There exists an oracle w.r.t which PH is not equal to P',
           ('BQP', 'PH'): 'There exists an oracle w.r.t which BQP is not equal to PH',
            ('PH','BQP'): 'There exists an oracle w.r.t which BQP is not equal to PH',
           ('BQP','QCMA'): 'There exists an oracle w.r.t which BQP is equal to QCMA',
            ('QCMA','BQP'): 'There exists an oracle w.r.t which BQP is equal to QCMA',
           ('BQP','BPP'): 'There exists an oracle w.r.t which BPP is not equal to BQP',
            ('BPP','BQP'): 'There exists an oracle w.r.t which BPP is not equal to BQP',
           ('NP','BQP'): 'There exists an oracle w.r.t which NP is not equal to BQP',
            ('BQP','NP'): 'There exists an oracle w.r.t which NP is not equal to BQP',
           ('PPAD','BQP'): 'There exists an oracle relative to which PPAD is not contained in BQP',
            ('BQP','PPAD'):'There exists an oracle relative to which PPAD is not contained in BQP',
           ('PPP','PPAD'): 'There exists an oracle relative to which PPP is not contained in PPAD',
            ('PPAD','PPP'):'There exists an oracle relative to which PPP is not contained in PPAD',
            ('P#P','PSAPCE'):'Pspace contains P#P (P with a #P oracle)',
           ('PSPACE','P#P'):'Pspace contains P#P (P with a #P oracle)'}

# Function to perform a depth-first search
def dfs(graph, start, target, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    path = path + [start]
    if start == target:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in visited:
            newpath = dfs(graph, node, target, visited, path)
            if newpath:
                return newpath

# Function to find the shortest path between two classes
def shortest_path(graph, messages, start, target):
    # Find the shortest path using DFS
    path = dfs(graph, start, target)
    # If no path exists, try swapping the start and target classes
    if path is None:
        path = dfs(graph, target, start)
        start, target = target, start
    # If a path still doesn't exist, return an error message
    if path is None:
        return f"No path exists between {start} and {target}"
    # Print the messages associated with each edge in the shortest path
    distance = len(path)-1 
    output = f"Shortest path from {start} to {target}: {' -> '.join(path)}\n"
    for i in range(distance):
        edge = (path[i], path[i+1])
        if edge in messages:
            output += f"{edge[0]} -> {edge[1]}: {messages[edge]}\n"
    return output

# Streamlit app
st.title("Complexity Class Graph")
start_class = st.selectbox("Select start class", options=list(graph.keys()))
target_class = st.selectbox("Select target class", options=list(graph.keys()))
output = shortest_path(graph, messages, start_class, target_class)
st.text(output)


# In[ ]:





# In[ ]:




