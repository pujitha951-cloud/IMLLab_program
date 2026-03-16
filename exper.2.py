import csv

def run_ce(csv_file_path='exp22.csv'):
    try:
        with open(csv_file_path, 'r') as file:
            D = list(csv.reader(file))
    except FileNotFoundError:
        print(f"Error: CSV file not found at '{csv_file_path}'.")
        print("Please ensure your data file is correctly placed.")
        return

    if not D or not D[0]:
        print("Error: CSV file is empty or improperly formatted.")
        return

    A = len(D[0]) - 1
    S = {tuple(['0'] * A)}
    G = {tuple(['?'] * A)}
    
    def consistent(h, x):
        return all(h[i] == '?' or h[i] == x[i] for i in range(A))
    
    def generalize(h, x):
        nh = list(h)
        for i in range(A):
            if nh[i] == '0': nh[i] = x[i]
            elif nh[i] != '?' and nh[i] != x[i]: nh[i] = '?'
        return tuple(nh)
    
    Dom = [set(d[i] for d in D) for i in range(A)]
    
    print("-" * 20)
    print("Initial Version Space (S0 and G0):")
    print("S0:", S)
    print("G0:", G)
    print("-" * 20)

    for idx, x_i in enumerate(D):
        x, t = x_i[:-1], x_i[-1].lower()
        print(f"\nProcessing Example {idx + 1} ({t.upper()}): {x}")
        
        if t == 'yes':
            G = {g for g in G if consistent(g, x)}
            S = {generalize(s, x) if not consistent(s, x) else s for s in S}
            
        elif t == 'no':
            S = {s for s in S if not consistent(s, x)}
            G_new = set()
            for g in G:
                if consistent(g, x):
                    for i in range(A):
                        if g[i] == '?':
                            for val in Dom[i]:
                                if val != x[i]:
                                    g_prime = list(g); g_prime[i] = val
                                    if all(consistent(g_prime, d[:-1]) for d in D if d[-1].lower() == 'yes'):
                                        G_new.add(tuple(g_prime))
                else: G_new.add(g)
            G = G_new
        
        print(f"S{idx + 1}:", S)
        print(f"G{idx + 1}:", G)
        print("-" * 20)


    print("\nFINAL OUTPUT")
    print("Final S (Specific Boundary):", S)
    print("Final G (Generic Boundary):", G)

run_ce()
