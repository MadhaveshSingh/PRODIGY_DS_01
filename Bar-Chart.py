
import pandas as pd
import matplotlib.pyplot as plt

# Sample data: Gender distribution
data = {
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Other', 'Female', 'Male', 'Male', 'Female', 'Other',
                'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Female','Male']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Count frequency of each category
gender_counts = df['Gender'].value_counts()

# Plot bar chart
plt.figure(figsize=(6, 4))
gender_counts.plot(kind='bar')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()



