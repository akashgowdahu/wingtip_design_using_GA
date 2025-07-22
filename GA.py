import pandas as pd
import numpy as np

csv_file = 'D:\Wingtip_design project\Results\gen_5_results.csv'  # Corrected file path separator
df = pd.read_csv(csv_file)

# Define parameter ranges
param_ranges = {
    'wing': (0.16, 0.25),
    'wingtiph': (30.0, 55.0),
    'wingtipscale': (0.05, 0.12),
    'wingtipx': (115.0, 125.0),
    'wingtipz': (213.0, 223.0)
}

# Compute fitness function
def fitness(row):
    drag = row['drag']
    return 1 / drag

df['fitness'] = df.apply(fitness, axis=1)

# Parent selection
def select_parents(df, num_parents):
    df['rank'] = df['fitness'].rank(ascending=True)  # Rank individuals based on fitness

    total_rank = df['rank'].sum()
    df['selection_prob'] = (1 - (df['rank'] / total_rank))  # Assign probability based on rank

    # Normalize probabilities to sum up to 1
    df['selection_prob'] /= df['selection_prob'].sum()

    # Select parents based on probabilities
    selected_parents_indices = np.random.choice(df.index, size=num_parents, replace=False, p=df['selection_prob'])

    selected_parents = df.loc[selected_parents_indices]

    return selected_parents

# Crossover based on fitness
def crossover(parent1, parent2):            
    child = {}

    for param, (min_val, max_val) in param_ranges.items():
        probability = np.random.uniform(0, 1)

        if probability < 0.45:
            child[param] = parent1[param]
        elif 0.45 <= probability < 0.90:
            child[param] = parent2[param]
        else:
            # Generate a random value within the parameter range
            child[param] = np.random.uniform(min_val, max_val)

    return child

# Create new generation
new_generation = []

# Sort the DataFrame by fitness in descending order
df_sorted = df.sort_values(by='fitness', ascending=False)

# Select the top 25% of parents with highest fitness scores
num_top_parents = int(len(df_sorted) * 0.25)
top_parents = df_sorted.head(num_top_parents)

# Randomly select children for the remaining 75% of the population
num_children = len(df_sorted) - num_top_parents
children = []

for _ in range(num_children):
    parents = df_sorted.sample(2, weights=df_sorted['fitness'])
    offspring = crossover(parents.iloc[0], parents.iloc[1])
    children.append(offspring)

# Combine top parents and children to form the new generation
new_generation.extend(top_parents.to_dict(orient='records'))
new_generation.extend(children)

# Mutation (1% of population)
mutation_rate = 0.01
for _ in range(int(mutation_rate * len(new_generation))):
    idx = np.random.randint(len(new_generation))
    for param in param_ranges:
        new_generation[idx][param] += np.random.uniform(-0.02, 0.02)
        new_generation[idx][param] = np.clip(new_generation[idx][param], *param_ranges[param])

# Create DataFrame for new individuals
new_df = pd.DataFrame(new_generation)

# Save to CSV
output_location = input("Please provide the location where you want to save the output CSV file: ")
output_file = f"{output_location}\\output.csv"
new_df.to_csv(output_file, index=False)
print(f"New individuals saved to {output_file}")