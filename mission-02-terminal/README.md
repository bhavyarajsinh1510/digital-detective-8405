# Mission 2 — Become Comfortable with the Terminal

## 1. Mission Title

Mission 2 — Become Comfortable with the Terminal

## 2. Task / Objective

The objective of this mission was to understand how Terminal works and learn how to use commands to manage files and folders. I also explored different command options, pipes and the role of package managers in managing software.

## 3. Work Completed

### Task 2.1 — Basic Terminal Operations

| Operation | Command | What it does | Observation |
|---|---|---|---|
| Current directory | `pwd` | Displays the location of the current directory. | It displays the full path of the folder I am working in. |
| Directory listing | `ls` | Lists files and folders. | It shows the contents of the current directory. |
| Detailed listing | `ls -l` | Displays files with additional details. | It shows information such as permissions, file size and modification date. |
| Change directory | `cd ..` | Moves to the parent directory. | The current location changes to the folder one level above. |
| Create directory | `mkdir` | Creates a new directory. | A new folder is created at the specified location. |
| Create empty file | `touch` | Creates an empty file. | A new file is created without any initial content. |
| Copy file | `cp` | Creates a copy of a file. | The original file remains while another copy is created. |
| Move or rename file | `mv` | Moves a file or changes its name. | The file appears at the new location or with the new name. |
| Display file contents | `cat` | Displays the contents of a file. | The text stored in the file appears in Terminal. |

### Task 2.2 — Practising File Changes Safely

I used a separate folder named `terminal-practice` inside my assignment repository for file-management activities.

I created a text file named `notes.txt` and added two lines of text. I then displayed the file contents using the `cat` command and created a backup named `notes-archive.txt`.

The difference between replacing and appending content is that replacing removes the previous content and writes new content, whereas appending adds new text at the end without removing what is already present.

Copying a file creates another version while keeping the original file. Moving a file changes its location, so it is no longer present in the original location.

The `pwd` command is useful because it tells me exactly where I am working. Similarly, `ls` is useful because it lets me see the available files and folders without opening them individually.

### Task 2.3 — Understanding Flags and Pipes

A flag is an option added to a command to change its behaviour or display additional information.

Some of the useful listing commands are:

| Command | Purpose |
|---|---|
| `ls` | Displays a normal directory listing. |
| `ls -l` | Displays a detailed listing. |
| `ls -a` | Includes hidden files and folders. |
| `ls -lh` | Displays detailed information with human-readable file sizes. |
| `ls -lah` | Combines detailed listing, hidden files and readable file sizes. |
| `ls -lah \| head -n 5` | Displays only the first five lines of the detailed listing. |

The pipe symbol (`|`) connects two commands. It takes the output from the command on the left and passes it as input to the command on the right.

In the command `ls -lah | head -n 5`, the first command generates the directory listing, while the second command displays only its first five lines.

### Task 2.4 — Understanding Package Managers

A package manager is a tool that helps users install, update and manage software on their computers. Homebrew is a commonly used package manager for macOS.

Two useful Homebrew commands are:

- `brew --version` — Displays the installed Homebrew version.
- `brew list` — Displays the packages managed by Homebrew.

Package managers make software management easier because users do not have to manually handle every installation and update. They can also help manage dependencies required by different applications.

## 4. Commands / Tools Used

| Command / Tool | Purpose |
|---|---|
| Terminal | To interact with the computer using text commands. |
| `pwd` | To display the current directory. |
| `ls` | To list files and folders. |
| `cd` | To navigate between directories. |
| `mkdir` | To create directories. |
| `touch` | To create empty files. |
| `cp` | To copy files. |
| `mv` | To move or rename files. |
| `cat` | To display file contents. |
| `ls -lah` | To view detailed listings, including hidden files. |
| `head` | To display the first few lines of output. |
| `brew --version` | To check the Homebrew version. |
| `brew list` | To view managed packages. |

## 5. My Understanding

This mission helped me understand that Terminal provides another way to interact with a computer apart from using the graphical interface.

I learned that different commands perform different operations, such as navigating directories, creating files and managing their contents. I also understood that flags provide additional options and pipes allow multiple commands to work together.

I found package managers interesting because they simplify the process of managing software and its dependencies.

## 6. Difficulties Faced

Initially, remembering the different Terminal commands and understanding the purpose of their options was a little confusing. Understanding the difference between copying, moving and renaming files also required some practice.

## 7. How I Resolved Them

I understood the commands by looking at their syntax and learning what each part does. Using simple examples inside my assignment folder made file operations easier to understand.

Comparing the output of normal and detailed directory listings also helped me understand how command flags work.

## 8. Evidence / Files

The following files are part of this mission:

- `README.md` — Contains the mission notes, command reference and explanations.
- `terminal-practice/notes.txt` — Contains the text used for file-management practice.
- `terminal-practice/notes-archive.txt` — Contains a backup copy of the original notes.

## 9. Commit Details

**Commit message:** `Complete Terminal and file management mission`

The mission work is organised separately so that its files and changes can be tracked through Git.