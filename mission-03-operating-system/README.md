# Mission 3 — Understand the Operating System

## 1. Mission Title

Mission 3 — Understand the Operating System

## 2. Task / Objective

The objective of this mission was to explore how an operating system manages a computer. I studied system information, running processes, available storage, file paths and permissions.

I also learned about the main responsibilities of an operating system, including process management, memory management, device management, file management and security.

## 3. Work Completed

### Task 3.1 — Explore Your Operating System

I explored the operating system environment using macOS Terminal and learned what different system details tell us.

| Information Explored | What It Tells You | Observation |
|---|---|---|
| Operating system / system details | Identifies the operating system and system environment. | My computer uses macOS. |
| Current account identity | Shows which user account is active. | A user account is currently active. Personal account details are not included for privacy. |
| Available and used storage | Shows how much disk space is occupied and how much is available. | Storage information helps monitor available disk space. |
| System activity snapshot | Shows running processes and current system activity. | Multiple applications and background processes can run simultaneously. |

### Task 3.2 — Understand Processes

A process is a program or application that is currently running on a computer.

The PID (Process Identifier) is a unique number assigned to a running process. It helps the operating system identify and manage individual processes.

Examples of processes:

1. A web browser process, such as Google Chrome.
2. A text editor process, such as Visual Studio Code.

A computer can run multiple processes at the same time. Some are visible applications, while others work in the background.

### Task 3.3 — Understand Paths and Permissions

**Absolute path vs Relative path**

An absolute path gives the complete location of a file or folder, starting from the root directory.

A relative path describes the location of a file or folder in relation to the current working directory.

| Path Type | Meaning | Example |
|---|---|---|
| Absolute path | Complete location of a file or folder. | `/Users/[redacted]/digital-detective/mission-03-operating-system/README.md` |
| Relative path | Location described from the current directory. | `mission-03-operating-system/README.md` |

**File Permissions**

File permissions control what different users can do with files and directories.

| Permission | Meaning | Example |
|---|---|---|
| `r` — Read | Allows a file's contents to be read. | Opening a text file. |
| `w` — Write | Allows a file to be modified. | Editing a text file. |
| `x` — Execute | Allows a file to be run. On a directory, it allows access or traversal. | Running a script. |

The detailed file listing in Terminal displays permission information. The first group of permission letters represents the owner's permissions.

I also learned that permissions should not be changed unnecessarily, especially for system files.

### Task 3.4 — Operating System Responsibilities

| OS Responsibility | Explanation | Example |
|---|---|---|
| Process management | The operating system manages running programs and allocates CPU time to them. | Running a browser and a code editor at the same time. |
| Memory management | It manages RAM and allocates memory to different applications. | Giving memory to a browser when it opens multiple tabs. |
| Device management | It manages connected hardware devices and allows software to communicate with them. | Managing a keyboard, trackpad or printer. |
| File management | It organises files and folders and manages how data is stored and accessed. | Creating, opening, renaming and deleting files. |
| User interface / shell | It provides ways for users to interact with the computer. | Using the macOS desktop or Terminal. |
| Security and permissions | It controls access to files and system resources. | Requiring permission before accessing protected files. |

## 4. Commands / Tools Used

| Command / Tool | Purpose |
|---|---|
| `uname` | Displays operating system and system information. |
| `whoami` | Displays the current account username. |
| `df` | Displays information about available and used disk space. |
| `top` | Displays a snapshot of running processes and system activity. |
| `ps` | Displays information about running processes. |
| `pwd` | Displays the current working directory. |
| `cd` | Changes the current directory. |
| `ls -l` | Displays a detailed listing, including file permissions. |
| Terminal | Used to explore the operating system and practise commands. |
| Visual Studio Code | Used to prepare the mission documentation. |

## 5. My Understanding

Through this mission, I understood that an operating system acts as a bridge between computer hardware, applications and the user.

It manages processes so that multiple programs can run, manages memory so applications can work properly, and handles files, devices and permissions.

I also learned that a process is an active running program and that its PID helps the operating system identify it.

Absolute and relative paths are two different ways of locating files. File permissions determine whether a user can read, modify or execute a file.

## 6. Difficulties Faced

Understanding the difference between absolute and relative paths and interpreting file permission letters was initially confusing.

It also took some effort to understand the difference between a running application and a background process.

## 7. How I Resolved Them

I reviewed the directory structure of my assignment repository and compared complete paths with paths relative to the current directory.

I studied the `r`, `w` and `x` permission letters and connected them with simple file operations.

I also used the explanations of process information and PID to understand how the operating system tracks running programs.

## 8. Evidence / Files

- `README.md` — Mission 3 documentation.
- System information observations.
- Process and PID explanations.
- Absolute path and relative path examples.
- File permission explanation.
- Operating system responsibilities table.

Personal information such as usernames and device details has been excluded from this documentation.

## 9. Commit Details 

**Commit message:** `Document operating system and file management`

The completed Mission 3 files should be staged, committed and pushed to the GitHub repository. The commit should be verified on GitHub before starting Mission 4.