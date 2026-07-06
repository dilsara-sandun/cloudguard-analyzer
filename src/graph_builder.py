import os
import matplotlib
matplotlib.use('Agg')  # Force matplotlib to not use any X-windows backend (Fixes Tkinter/TclError)
import matplotlib.pyplot as plt
import networkx as nx

def build_attack_graph(findings_dict):
    G = nx.DiGraph()
    
    for username, findings in findings_dict.items():
        if findings:
            G.add_node(username, type="user", color="skyblue")
            for f in findings:
                node_name = f"{username}\n({f['name']})"
                G.add_node(node_name, type="finding", risk=f["risk"])
                G.add_edge(username, node_name)

    if len(G.nodes) == 0:
        print("[-] No escalation paths found to graph.")
        return

    color_map = []
    for node in G.nodes:
        if G.nodes[node].get("type") == "user":
            color_map.append("skyblue")
        else:
            risk = G.nodes[node].get("risk")
            color_map.append("red" if risk == "CRITICAL" else "orange")

    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G, k=0.5)
    nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=2500, font_size=8, font_weight="bold", edge_color="gray")
    
    os.makedirs("reports", exist_ok=True)
    plt.savefig("reports/attack_graph.png", bbox_inches="tight", dpi=150)
    plt.close()
