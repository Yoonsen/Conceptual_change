import requests
import networkx as nx


url = "https://api.nb.no/dhlab/nb_ngram_galaxies/galaxies/query"


def word_graph(word = None, cutoff = 20, corpus = 'all'):
    """ corpus = bok, avis or all"""
    params = {
        'terms':word, 
        'leaves':0,
        'limit':cutoff,
        'corpus':corpus,
    }
    r = requests.get(url, params = params)
    G = nx.DiGraph()
    edgelist = []
    if r.status_code == 200:
        #graph = json.loads(result.text)
        graph = r.json()
        #print(graph)
        nodes = graph['nodes']
        edges = graph['links']
        for edge in edges:
            from_node = nodes[edge['source']]['name']
            to_node = nodes[edge['target']]['name']
            if from_node.isalnum() and to_node.isalnum():
                edgelist += [(from_node, to_node, abs(edge['value']))]
        G.add_weighted_edges_from(edgelist)
    return G
