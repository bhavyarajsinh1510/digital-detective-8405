# Mission 6: Git and GitHub Collaboration

## 1. Mission Objective

The objective of this mission is to understand how Git and GitHub help developers track changes, manage different versions of code, and collaborate on projects.

In this mission, I learned how to create branches, make changes independently, push branches to GitHub, and create a Pull Request to propose changes to the main branch.

---

## 2. Task 6.1 – Understanding the Git Workflow

Git is a version control system that tracks changes made to files over time. GitHub is an online platform that hosts Git repositories and makes collaboration easier.

The basic Git workflow consists of the following steps:

1. **Working Directory:** The location where files are created or modified.
2. **Staging Area:** The place where changes are selected before committing.
3. **Local Repository:** Stores committed changes on the computer.
4. **Remote Repository:** The online repository hosted on GitHub.

### Important Git Commands

| Command | Purpose |
|---|---|
| `git status` | Checks the current state of the repository. |
| `git add .` | Stages all changes in the current directory. |
| `git add filename` | Stages a specific file. |
| `git commit -m "message"` | Saves staged changes as a commit. |
| `git push` | Uploads local commits to a remote repository. |
| `git pull` | Fetches and integrates changes from the remote repository. |
| `git log` | Displays the commit history. |
| `git branch` | Lists available branches. |
| `git switch branch-name` | Switches to another branch. |

---

## 3. Task 6.2 – Creating and Working with Branches

A branch is an independent line of development within a Git repository.

Branches allow developers to work on new features or modifications without directly changing the main branch.

### Step 1: Check Existing Branches

```bash
git branch
```

This command displays the available local branches.

### Step 2: Create a New Branch

```bash
git switch -c update-about
```

This creates a new branch named `update-about` and switches to it.

### Step 3: Verify the Current Branch

```bash
git branch
```

The asterisk (*) indicates the currently active branch.

### Step 4: Update the Root README

I added a new section named **My Learning** to the root `README.md` file.

The section summarizes the important concepts learned during the Digital Detective assignment, including computer fundamentals, Terminal, Python, number systems, Git, and GitHub.

### Step 5: Stage and Commit Changes

```bash
git status
git add README.md
git commit -m "Add my learning progress to root README"
```

### Step 6: Push the Branch to GitHub

```bash
git push -u origin update-about
```

This command uploads the new branch to the remote GitHub repository and establishes its upstream tracking relationship.

---

## 4. Task 6.3 – Creating a Pull Request

A Pull Request (PR) is a request to review and merge changes from one branch into another branch.

It allows developers to review modifications, discuss improvements, and identify potential problems before merging changes.

### Why Are Pull Requests Important?

- They allow code review before changes are merged.
- They help identify errors and improve code quality.
- They make collaboration between developers easier.
- They maintain an organized development workflow.
- They provide a record of proposed changes and discussions.

### Creating My Pull Request

After pushing the `update-about` branch to GitHub, I followed these steps:

1. Opened my repository on GitHub.
2. Navigated to the **Pull requests** tab.
3. Selected **New pull request**.
4. Selected `main` as the base branch.
5. Selected `update-about` as the compare branch.
6. Reviewed the changes displayed by GitHub.
7. Added a suitable title and description.
8. Created the Pull Request.

### Branch Direction

**Base branch:** `main`

**Compare branch:** `update-about`

The changes flow from `update-about` into `main` when the Pull Request is merged.

### Pull Request Details

**Title:** Add My Learning section

**Description:**

This Pull Request adds a new My Learning section to the root README.md file.

Changes include:
- Added a summary of concepts learned during the assignment.
- Documented my understanding of computer fundamentals, Terminal, Python, and Git/GitHub.
- Used a separate branch to propose changes for review.

**Pull Request URL:** https://github.com/bhavyarajsinh1510/digital-detective-8405/pull/1

**Pull Request Status:** Merged and closed:

### What Happens After Creating a Pull Request?

Once a Pull Request is created, GitHub displays the proposed changes for review.

The repository owner or collaborators can review the changes, leave comments, request modifications, and eventually approve and merge the Pull Request.

A Pull Request does not automatically merge changes. Merging is a separate action.

---

## 5. Task 6.4 – Git and GitHub Glossary

| Term | Meaning |
|---|---|
| Repository | A project directory tracked by Git. |
| Commit | A saved snapshot of changes. |
| Branch | An independent line of development. |
| Main | The primary branch of a repository. |
| Staging Area | An area where changes are prepared before committing. |
| Remote | A repository hosted on another system, such as GitHub. |
| Push | Uploading local commits to a remote repository. |
| Pull | Fetching and integrating remote changes. |
| Merge | Combining changes from different branches. |
| Pull Request | A proposal to merge changes from one branch into another. |
| Clone | Creating a local copy of a remote repository. |
| Conflict | A situation where Git cannot automatically combine changes. |

---

## 6. Commands and Tools Used

### Git Commands

```bash
git status
git branch
git switch -c update-about
git add README.md
git commit -m "Add my learning progress to root README"
git push -u origin update-about
```

### Tools Used

- **Git:** For version control and tracking file changes.
- **GitHub:** For hosting the repository and creating Pull Requests.
- **Terminal:** For executing Git commands.
- **Visual Studio Code:** For editing README files.

---

## 7. My Understanding

Through this mission, I understood how Git and GitHub work together to manage software development projects.

I learned that Git tracks changes locally, while GitHub provides an online platform to store repositories and collaborate with others.

I also understood the importance of branches. Instead of modifying the main branch directly, developers can create separate branches to work on specific features or improvements.

The most important concept I learned was the Pull Request workflow. A Pull Request allows proposed changes to be reviewed before they become part of the main branch.

This mission helped me understand how developers organize their work and collaborate on real-world software projects.

---

## 8. Difficulties Faced and How I Resolved Them

**Difficulty:** Understanding the difference between the base branch and the compare branch while creating a Pull Request.

**Resolution:** I understood that the base branch is the branch receiving the changes, while the compare branch contains the changes being proposed. Therefore, for this mission, `main` is the base branch and `update-about` is the compare branch.

**Difficulty:** Understanding why a newly created branch was not initially visible on GitHub.

**Resolution:** I learned that creating a branch locally does not automatically publish it online. Running `git push -u origin update-about` uploads the branch to GitHub.

---

## 9. Evidence and Files

The following files and activities are associated with this mission:

- `06-git-and-github/README.md` – Documentation of the Git and GitHub workflow.
- Root `README.md` – Updated with the My Learning section.
- `update-about` – Branch created for the README modification.
- Git commit – Records the changes made to the root README.
- Pull Request – Proposal to merge the `update-about` branch into `main`.

---

## 10. Commit Details

**Commit message for the root README update:**


"Add my learning progress to root README"


**Commit message for this mission documentation:**


"Complete Git and GitHub collaboration mission"


Git commits provide a record of the changes made during the mission and help maintain an organized project history.

---

## 11. Conclusion

Mission 6 introduced me to the collaborative side of software development.

I learned how to use Git branches, stage and commit changes, push branches to GitHub, and create Pull Requests.

These concepts are essential for working on larger software projects where multiple developers contribute to the same codebase.

Understanding this workflow gives me a foundation for collaborating on future programming projects.