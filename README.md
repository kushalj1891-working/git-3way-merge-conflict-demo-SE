# Git 3-Way Merge Conflict Resolution Demo

## 📌 Project Overview

This project demonstrates how Git handles a **3-way merge conflict** when two branches modify the same lines of the same file.

The example uses a simple Python calculator application.

Two feature branches are created from the same starting commit:

* `feature-add`
* `feature-multiply`

Both branches modify overlapping parts of `calculator.py`. When the branches are merged into `main`, Git detects conflicting changes that cannot be automatically combined.

The conflict is then resolved manually.

---

## 🎯 Objective

The objective of this project is to demonstrate:

* Creating feature branches from a common base
* Making overlapping changes on separate branches
* Triggering a Git merge conflict
* Understanding Git conflict markers
* Manually resolving conflicting code
* Completing a successful merge
* Verifying that the final Python program works correctly

---

## 🌿 Branch Structure

The project follows this branch structure:

```text
                    feature-add
                   /
main ─────────────●
                   \
                    feature-multiply
```

Both feature branches originate from the same version of `calculator.py`.

The branches then make different changes to overlapping code.

---

## 🔀 Conflict Scenario

### Main

The original calculator contains basic arithmetic operations.

### feature-add

The branch modifies the calculator to improve the addition-related functionality.

### feature-multiply

The branch modifies the same section of the calculator to improve multiplication-related functionality.

Because both branches modify overlapping lines, Git cannot automatically determine which version should be retained.

---

## ⚠️ Git Conflict Markers

When the conflicting branches are merged, Git places conflict markers into the affected file.

A conflict may look like:

```text
<<<<<<< HEAD
Changes from the current branch
=======
Changes from the branch being merged
>>>>>>> feature-multiply
```

These markers indicate that Git needs the developer to manually choose or combine the changes.

---

## 🛠️ Conflict Resolution

The conflicting section is manually edited to produce the desired final implementation.

The conflict markers are removed and the final calculator code is checked for correctness.

The final version contains the required functionality from both branches.

---

## 🧮 Final Calculator Features

The resolved calculator supports:

* Addition
* Subtraction
* Multiplication
* Division

It also includes basic protection against division by zero.

---

## 🧪 Verification

After resolving the conflict, the Python test suite verifies the calculator functionality.

The expected result is:

```text
4 passed
```

The final Python file should also execute without syntax errors.

---

## 📊 Expected Demonstration

The demonstration should show the following sequence:

```text
1. Main branch with initial calculator
             ↓
2. Create feature-add
             ↓
3. Create feature-multiply
             ↓
4. Modify overlapping lines
             ↓
5. Merge feature-add into main
             ↓
6. Merge feature-multiply
             ↓
7. Git reports a merge conflict
             ↓
8. Open calculator.py
             ↓
9. Resolve <<<<<<< ======= >>>>>>>
             ↓
10. Complete the merge
             ↓
11. Verify clean working tree
             ↓
12. Run tests successfully
```

---

## 🏆 Learning Outcome

This project demonstrates practical Git conflict-resolution skills and shows how developers manually reconcile incompatible changes before integrating feature branches into a shared main branch.
