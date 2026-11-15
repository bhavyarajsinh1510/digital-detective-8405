# Mission 6 — Git and GitHub

## 1. Task and Objective

The objective of this mission was to understand Git and GitHub, practise the basic Git workflow, create a separate branch, publish changes and create a Pull Request.

I also learned how branches and Pull Requests help developers collaborate on projects.

## 2. Task 6.1 — Basic Git Workflow

I explored the following Git operations:

| Git operation | What it does |
|---|---|
| Check repository status | `git status` displays modified, staged and untracked files. |
| Stage selected changes | `git add` selects files or changes for the next commit. |
| Create a commit | `git commit` saves staged changes in the repository history. |
| View commit history | `git log --oneline` displays recent commits in a compact format. |

### Difference between staging and committing

Staging means selecting the changes that I want to include in the next commit. Committing means saving those staged changes as a permanent record in Git's history.

## 3. Task 6.2 — Creating and Using a Branch

I created a new branch named:

`update-about`

Commands used:

```bash
git branch
git switch -c update-about
```

If the branch already existed, I switched to it using:

```bash
git switch update-about
```

I then updated the root `README.md` file by adding a section titled **My Learning**. This section describes the concepts I learned during the assignment.

After saving the changes, I checked the repository status, staged the README, committed the changes and published the branch.

```bash
git status
git add README.md
git commit -m "Add my learning progress to root README"
git push -u origin update-about
```

## 4. Task 6.3 — Pull Request

A Pull Request (PR) is a request to review and integrate changes from one branch into another branch.

I created a Pull Request with the following details:

- Source branch: `update-about`
- Target branch: `main`
- Title: `Add My Learning section`
- Purpose: To review and integrate the learning progress section added to the root README.

### Why are branches and Pull Requests useful?

Branches allow developers to work on separate features or changes without directly modifying the main branch. Pull Requests allow other contributors to review changes, discuss improvements and decide whether those changes should be merged.

### Pull Request status

Update this section after completing the activity:

- Pull Request URL: [Paste your actual GitHub PR link here]
- Status: [Open / Merged]
- Merge completed: [Yes / No]

If the Pull Request has not been merged, mention that it remains open.

## 5. Task 6.4 — Git Command Glossary

| Git command | Explanation |
|---|---|
| `git init` | Initialises a new Git repository. |
| `git status` | Shows the current state of the repository. |
| `git add` | Stages changes for committing. |
| `git commit` | Saves staged changes in Git history. |
| `git log` | Displays previous commits. |
| `git branch` | Lists branches or helps create a branch. |
| `git switch` | Switches from one branch to another. |
| `git push` | Sends local commits to a remote repository. |
| `git pull` | Retrieves and integrates changes from a remote repository. |

## 6. Commands and Tools Used

- `git status`
- `git add`
- `git commit`
- `git log --oneline`
- `git branch`
- `git switch`
- `git push`
- `git pull`
- GitHub repository interface
- GitHub Pull Requests

## 7. My Understanding

I understood that Git is a version control system that records changes in a project, while GitHub provides an online platform to host repositories and collaborate.

I learned that staging and committing are separate steps, and that branches make it possible to work on changes independently. Pull Requests provide a structured way to review changes before integrating them into the main project.

## 8. Difficulties Faced

[Write about any actual difficulty you faced while creating the branch, pushing it or creating the Pull Request.]

## 9. How I Resolved Them

[Explain the steps you actually followed to resolve the difficulty.]

## 10. Evidence and Files

- `README.md` — this mission's documentation.
- Root `README.md` — contains the My Learning section added on the `update-about` branch.
- GitHub branch — `update-about`.
- GitHub Pull Request — link and status recorded above.

## 11. Commit Details

**Suggested commit message:**

"Complete Git and GitHub collaboration mission"


The mission documentation should be committed and pushed. The branch and Pull Request activity should also be visible on GitHub.