import streamlit as st
import numpy as np
import pandas as pd

def edit_distance(source, target):
    m, n = len(source), len(target)
    dp = np.zeros((m + 1, n + 1), dtype=int)
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # Inserting j characters
            elif j == 0:
                dp[i][j] = i  # Removing i characters
            elif source[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],    # Deletion
                                   dp[i][j - 1],    # Insertion
                                   dp[i - 1][j - 1]) # Replacement
    
    edits = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and source[i - 1] == target[j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            edits.append(["Delete", source[i-1], i, "-"])
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            edits.append(["Insert", target[j-1], i+1, "-"])
            j -= 1
        else:
            edits.append(["Replace", source[i-1], i, target[j-1]])
            i -= 1
            j -= 1
    
    return dp[m][n], edits[::-1]

st.title("Minimum Edit Distance Calculator")

source = st.text_input("Enter Source String:", "")
target = st.text_input("Enter Target String:", "")

if st.button("Calculate Edit Distance"):
    if source and target:
        distance, operations = edit_distance(source, target)
        st.write(f"### Minimum Edit Distance: {distance}")
        
        if operations:
            df = pd.DataFrame(operations, columns=["Operation", "Character", "Position", "New Character"])
            st.write("### Edit Steps:")
            st.dataframe(df)
        
        st.balloons()
    else:
        st.warning("Please enter both source and target strings.")

if st.button("Show Algorithm"):
    st.write("""
    ### Minimum Edit Distance Algorithm:
    1. Create a DP table of size (m+1) x (n+1), where m and n are the lengths of source and target.
    2. Initialize base cases:
       - If source is empty, insert all target characters.
       - If target is empty, remove all source characters.
    3. Fill the table:
       - If characters match, inherit the previous value.
       - Otherwise, choose the minimum edit operation (insert, delete, replace).
    4. Backtrack to determine the exact edit operations.
    """)
