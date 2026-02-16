# Resource Demand Classification & Personalization

This project is a Python program that classifies resource requests into different demand categories, validates them, and applies a personalization logic based on the user's name.

---

## 📌 Features
- Accepts a list of resource requests from user input.
- Classifies requests into:
  - **Low Demand** (1–20)
  - **Medium Demand** (21–50)
  - **High Demand** (>50)
- Identifies **invalid requests** (negative values).
- Handles **zero demand** requests separately.
- Applies **personalized removal logic** based on the length of the user's name:
  - If `len(name) - spaces % 3 == 0` → remove all low demand requests.
  - If `== 1` → remove all high demand requests.
  - If `== 2` → remove both low and high demand requests.
- Displays summary statistics:
  - Total valid requests
  - Total invalid requests
  - Requests removed due to personalization
  - Final demand distribution after personalization

---

## 🛠️ How It Works
1. User enters the number of requests (`m`).
2. User inputs `m` resource values.
3. Program classifies and validates requests.
4. Personalized logic is applied using the name `"kundana kartika chowdary"`.
5. Results are printed with demand categories before and after personalization.

---