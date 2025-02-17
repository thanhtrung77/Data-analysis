# Correctly call value_counts on the 'target_label' column of df_non_regex
target_value_counts = df_non_regex['target_label'].value_counts()

# Filter indices where the counts are less than or equal to 5
filtered_indices = target_value_counts[target_value_counts <= 5].index.tolist()

# Print the filtered indices
print(filtered_indices)