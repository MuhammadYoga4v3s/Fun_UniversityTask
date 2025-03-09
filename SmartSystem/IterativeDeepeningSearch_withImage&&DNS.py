# Nama : Muhammad Yoga Aminudin
# NIM  : 24060123130106
# Pada File ini dibuat sebuah algoritma IDS, yang mencari jarak terpendek
# antara 2 node dari sebuah graph berbobot
# Pencarian masih dalam kategori "Blind Search", hasil path mungkin tidak optimal

import networkx as nx
import matplotlib.pyplot as plt

# Prosedur : GambarGraph 
# Prosedur GambarGraph membuat sebuah citra yang menunjukkan lokasi lokasi node
# serta bobot tiap tiap jalan yang menghubungkan graph
# instal : Terminal -> pip install networkx matplotlib
def draw_graph(graph):
    # Buat sebuah obyek : Graph
    G = nx.Graph()
    
    # Tambahkan edge (jalur) ke graph berdasarkan input
    for node, Nodetetanggas in graph.items():
        for NeighborNode, cost in Nodetetanggas:
            G.add_edge(node, NeighborNode, weight=cost)

    pos = nx.spring_layout(G)  # Posisi node diatur otomatis
    labels = nx.get_edge_attributes(G, 'weight')

    # Atur ukuran gambar
    plt.figure(figsize=(6, 5))
    # # Gambar node dan edge
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", 
            node_size=750, font_size=8, font_weight="bold")
    # Tambahkan bobot pada edge
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10) 
    plt.title("🔗 Visualisasi Graph")
    plt.show()

# ================================================================================================== # 

# Function: iterative_deepening_search (IDS)
# Fungsi ini menjalankan algoritma pencarian Iterative Deepening Search (IDS)
# IDS mengulangi pencarian dengan kedalaman yang semakin bertambah sampai menemukan solusi
# Menggunakan bantuan algoritma Depth-Limited Search (DLS)
# Mengembalikan sebuah Path (dalam bentuk list), jika ada *, jika tidak ada return none
def iterative_deepening_search(graph, start, goal):
    """Melakukan pencarian IDS untuk menemukan path dari start ke goal"""
    # Kamus
    # Inisialisasi kedalaman awal
    depth = 0

    # Algoritma
    while True:
        print(f"\n{'='*60}\nIterasi Kedalaman {depth}")

        # Jalankan Depth-Limited Search (DLS) dengan kedalaman saat ini
        result = depth_limited_search(graph, start, goal, depth)
        # Jika ditemukan jalur ke goal
        if result is not None:
            print(f"\n Jalur ditemukan di kedalaman {depth}: {result}")
            return result
        # Else, Tidak ditemukan jalur ke goal
        print(f" Tidak ditemukan pada kedalaman {depth}, menaikkan kedalaman...\n")
        # Tambahkan kedalaman dan ulangi pencarian (otomatis)
        depth += 1

# ================================================================================================== # 

# Fungsi : depth_limited_search (DLS)
# Fungsi ini menjalankan pencarian dengan kedalaman terbatas (*Depth-Limited Search*).
# Jika kedalaman mencapai batas, pencarian berhenti tanpa hasil.
def depth_limited_search(graph, node, goal, limit, path=None, totalCost=0, indentasi=""):
    # Kamus
    # -- path = None # Menyimpan jalur yang sedang dieksplorasi dalam bentuk daftar (list) yang berisi tuple
    # -- totalCost = 0 # Menyimpan total bobot perjalanan dari start hingga node yang sedang dikunjung
    # -- indentasi = "" # Menyimpan total bobot perjalanan dari start hingga node yang sedang dikunjung
    #                  biar rapi, dan ketahuan level kedalamannya
    
    # Algoritma
    if path is None:
        path = []

    path = path + [(node, totalCost)]  # Simpan node dan total cost sampai saat ini

    print(f"{indentasi}🔹 Mengeksplorasi {node} (Total Bobot: {totalCost}) | Batas Kedalaman: {limit}")

    # =============== BASIS =================
    # Jika mencapai goal, kembalikan path
    if node == goal:
        print(f"{indentasi} Ditemukan jalur: {path}")
        return path
    # Jika kedalaman maksimum tercapai, hentikan pencarian (return none)
    elif limit <= 0:
        return None
    # ============ REKURENS =================
    else :
    # Eksplorasi setiap tetangga dari node saat ini ( satu level )
        for NeighborNode, cost in graph.get(node, []): # Medngambil semua tetangga dan cost
            if NeighborNode not in [p[0] for p in path]:  # Hindari siklus (looping)
                new_path = depth_limited_search(graph, NeighborNode, goal, limit - 1, 
                                                path, totalCost + cost, indentasi + "  ")
                if new_path is not None:
                    return new_path

        return None

# ================================================================================================== # 
# ================================================================================================== # 

# TestCase 1
# link gambar : https://www.geeksforgeeks.org/minimum-cost-path-in-a-directed-graph-via-given-set-of-intermediate-nodes/
# graph dibuat tak berarah bobot dijumlah
graph1 = {
    '0': [('1', 3), ('7', 3), ('3', 3)],
    '1': [('0', 3), ('4', 4)],
    '3': [('0', 3), ('5', 7)],
    '7': [('0', 3), ('4', 5), ('5', 6)],
    '4': [('1', 4), ('7', 5), ('6', 4)],
    '5': [('3', 7), ('7', 6), ('6', 2)],
    '6': [('4', 4), ('5', 2)]
}
# Tampilkan visualisasi graph
draw_graph(graph1)
# SET START AND GOAL
# Start  ='1' , goal = '6'
path1 = iterative_deepening_search(graph1, '1', '6')
print("\n Path ditemukan:", path1)

# ================================================================================================== # 
# ================================================================================================== # 

# TestCase 2
# link gambar : https://www.geeksforgeeks.org/shortest-distance-between-two-nodes-in-graph-by-reducing-weight-of-an-edge-by-half/
# graph dibuat tak berarah bobot dijumlah
graph2 = {
    'H': [('He', 4), ('N', 8)],
    'He': [('H', 4), ('Li', 8), ('N', 11)],
    'Li': [('He', 8), ('Be', 7), ('O', 2), ('F', 4)],
    'Be': [('Li', 7), ('B', 9), ('F', 14)],
    'B': [('Be', 9), ('F', 10)],
    'F': [('Li', 4), ('Be', 14), ('B', 10), ('Ne', 2)],
    'Ne': [('F', 2), ('N', 1), ('O', 6)],
    'N': [('H', 8), ('He', 11), ('Ne', 1), ('O', 7)],
    'O': [('Li', 2), ('Ne', 6), ('N', 7)]
}
# Tampilkan visualisasi graph
draw_graph(graph2)
# SET START AND GOAL
# Start  ='H' , goal = 'B'
path2 = iterative_deepening_search(graph2, 'H', 'B')
print("\n Path ditemukan:", path2)