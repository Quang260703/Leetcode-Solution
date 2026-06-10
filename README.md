# 🧩 LeetCode Solutions

A personal collection of LeetCode problem solutions, automatically synced from LeetCode and organized by topic and difficulty.

---

## Stats

![Problems Solved](https://img.shields.io/badge/Problems%20Solved-growing-brightgreen)
![Language](https://img.shields.io/badge/Language-Python%20%7C%20C++-blue)
![Sync](https://img.shields.io/badge/Sync-LeetCode%20Auto--Sync-orange)

---

## Structure

```
Leetcode-Solution/
├── Easy/
│   ├── 0001_Two_Sum.py
│   └── ...
├── Medium/
│   ├── 0547_Number_of_Provinces.py
│   └── ...
├── Hard/
│   └── ...
└── README.md
```

Solutions are auto-synced via [LeetCode Sync](https://github.com/joshcai/leetcode-sync) and include runtime and memory stats in the commit message.

---

## Topics Covered

| Topic | Examples |
|---|---|
| Arrays & Hashing | Two Sum, Contains Duplicate |
| Two Pointers | Remove Duplicates, Valid Palindrome |
| Graphs / BFS / DFS | Number of Provinces, Clone Graph |
| Union-Find | Connected Components, Redundant Connection |
| Dynamic Programming | Climbing Stairs, Coin Change |
| Trees | Inorder Traversal, Max Depth |
| Binary Search | Search in Rotated Array |
| Sliding Window | Longest Substring Without Repeating |

---

## How to Run

Each solution is a standalone file. To run locally:

```bash
# Python
python Easy/0001_Two_Sum.py

# C++
g++ -o solution Medium/0547_Number_of_Provinces.cpp && ./solution
```

---

## Sync Setup

Solutions are automatically pushed here after each accepted submission via the [LeetCode Sync](https://github.com/joshcai/leetcode-sync) GitHub Action.

To set it up yourself:

1. Fork this repo or create a new one
2. Add your `LEETCODE_CSRF_TOKEN` and `LEETCODE_SESSION` as GitHub Secrets
3. The workflow runs on a schedule and pushes new accepted solutions automatically

---

## Goals

- [ ] Solve 300+ problems
- [ ] Cover all major topic categories
- [ ] Achieve consistent sub-50ms runtime on medium problems
- [ ] Complete NeetCode 150

---

## License

MIT
