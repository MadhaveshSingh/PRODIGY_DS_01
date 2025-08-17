
import pandas as pd
import matplotlib.pyplot as plt

# Sample data: Age distribution
data = {
    'Age': [18, 22, 25, 30, 22, 24, 27, 30, 35, 40, 45, 50, 55, 60, 30, 28, 22]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Plot histogram
plt.figure(figsize=(6, 4))
plt.hist(df['Age'], bins=8, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()