# apiori_onehot.py
import pandas as pd
from itertools import combinations 

# --- CONFIG --- (change these)
csv_path = "transactions_onehot_250.csv"   # put your file path here
min_support = 0.1      # fraction, e.g. 0.1 = 10% of transactions
min_confidence = 0.4

# --- 1) Load one-hot CSV and convert to transactions (sets of items) ---
df = pd.read_csv(csv_path)
# assume first column is TransactionID, rest are item columns with 0/1
item_cols = list(df.columns[1:])   # skip TransactionID
transactions = []
for _, row in df.iterrows():
    items = {col for col in item_cols if int(row[col]) == 1}
    if items:
        transactions.append(items)

N = len(transactions)
print(f"Loaded {N} transactions and {len(item_cols)} items.")

# --- 2) helper: support function ---
def support(itemset):
    c = sum(1 for t in transactions if itemset.issubset(t))
    return c / N

# --- 3) generate frequent itemsets (Apriori) ---
# 1-itemsets
items = set(it for t in transactions for it in t)
L = {frozenset([i]): support(frozenset([i])) for i in items if support(frozenset([i])) >= min_support}
all_frequent = dict(L)

k = 2
while L:
    # candidate generation (join step)
    cand = set()
    L_list = list(L.keys())
    for i in range(len(L_list)):
        for j in range(i+1, len(L_list)):
            union = L_list[i] | L_list[j]
            if len(union) == k:
                cand.add(union)
    # prune candidates whose (k-1)-subsets are not all frequent
    pruned = set()
    for c in cand:
        ok = True
        for subset in combinations(c, k-1):
            if frozenset(subset) not in L:
                ok = False
                break
        if ok:
            pruned.add(c)
    # count support
    L = {c: support(c) for c in pruned if support(c) >= min_support}
    all_frequent.update(L)
    k += 1

# --- 4) generate rules from frequent itemsets ---
rules = []
for itemset, sup in all_frequent.items():
    if len(itemset) < 2:
        continue
    items = set(itemset)
    for r in range(1, len(items)):
        for A in combinations(items, r):
            A = frozenset(A)
            B = itemset - A
            supA = all_frequent.get(A, support(A))
            if supA == 0: 
                continue
            conf = sup / supA
            if conf >= min_confidence:
                # compute lift
                supB = all_frequent.get(B, support(B))
                lift = conf / supB if supB > 0 else 0
                rules.append((set(A), set(B), round(sup,3), round(conf,3), round(lift,3)))

# --- 5) print results ---
print("\nFrequent itemsets (itemset -> support):")
for it, s in sorted(all_frequent.items(), key=lambda x: (-len(x[0]), -x[1])):
    print(set(it), "->", round(s,3))

print("\nAssociation rules (A -> B) [support, confidence, lift]:")
for A, B, s, conf, lift in sorted(rules, key=lambda x: (-x[3], -x[2]))[:50]:
    print(f"{A} -> {B}  [sup={s}, conf={conf}, lift={lift}]")
