# Problem: Age Checker

**Topic:** Conditional Statements  
**Week:** Week-1  
**Day:** Day-1  

---

## 📝 Description

Write a Python program that asks the user to input their age and classifies them as a **minor**, **adult**, or **senior citizen**.

The program should follow these rules:

- If the age is **less than 18**, output: \`You are a minor.\`
- If the age is **between 18 and 64 (inclusive)**, output: \`You are an adult.\`
- If the age is **65 or older**, output: \`You are a senior citizen.\`
- If the age is invalid (negative or non-numeric), display: \`Invalid age entered.\`

---

## 🔢 Example Input

\`\`\`
Enter your age: 21
\`\`\`

### ✅ Output

\`\`\`
You are an adult.
\`\`\`

---

## ⚠️ Edge Case

### ❓ Input

\`\`\`
Enter your age: -4
\`\`\`

### 🚫 Output

\`\`\`
Invalid age entered.
\`\`\`

---

## ✨ Notes

- Use the \`input()\` function to get the user's age.
- Make sure to validate the input to handle non-numeric or negative values.
- Use \`if\`, \`elif\`, and \`else\` statements for classification.
