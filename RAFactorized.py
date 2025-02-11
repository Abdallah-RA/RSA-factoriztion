import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as mcolors


def calculate_remainders(N, g, max_r):
    results = []
    for r in range(0, max_r + 1):
        gr = pow(g, r)
        remainder = gr % N
        results.append((r, gr, remainder))
    return results


def plot_remainders(results):
    remainders = [item[2] for item in results]
    rs = [item[0] for item in results]

   
    unique_remainders = list(set(remainders))
    colors = plt.cm.tab10.colors
    color_map = {remainder: colors[i % len(colors)] for i, remainder in enumerate(unique_remainders)}

    plt.figure(figsize=(16, 8))
    bars = plt.bar(rs, remainders, color=[color_map[remainder] for remainder in remainders], alpha=0.7)
    plt.title('Remainders Frequency Analysis')
    plt.xlabel('r', fontsize=14)
    plt.ylabel('Remainder', fontsize=14)
    plt.grid(axis='y', linestyle=' ', alpha=0.7)

  
    for bar, remainder in zip(bars, remainders):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, str(remainder),
                 ha='center', va='bottom', fontsize=10, color='black')

  
    plt.xticks(rs, fontsize=10, rotation=90)  

    plt.tight_layout()
    plt.show()


def display_table(results):
    df = pd.DataFrame(results, columns=['Exponent (r)', 'g^r', 'Remainder'])
    print(df.to_string(index=False))



N = 187
g = 7
max_r = 100

results = calculate_remainders(N, g, max_r)
plot_remainders(results)
display_table(results)
