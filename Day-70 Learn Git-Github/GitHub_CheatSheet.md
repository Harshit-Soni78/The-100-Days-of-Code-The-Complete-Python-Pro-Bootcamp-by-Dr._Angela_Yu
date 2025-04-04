# GitHub CheatSheet

## CheatSheet for CLI _(Command Line Interface)_ Commands

- **cd** : to navigate through terminal
- **mkdir** : to make directory using terminal
- **rm** : remove something using terminal
- **touch** : to make new files using terminal
- **code** : to open the files in write mode
- **ls** : view the directory
- **ls -l** : view the directory list
- **ls -a** : view the directory including hidden files
- **help** : use this to know more shortcuts.
- **clear** : to clear the terminal
- **find [path] [options] [expression]** : to find any file
  - **path:** Starting directory for the search.
    - **Example**: `find /path/to/search`
  - **options:** Additional settings or conditions for the search.
    - **Example**: `find /path/to/search -type f -name "*.txt"`
  - **expression:** Criteria for filtering and locating files.
    - **Example**: `find /path/to/search -type d -name "docs"`
- **ps [options]** : The `ps` command in Linux shows running processes, and with options, it customizes the details displayed.
- **kill** : The `kill` command in Linux stops processes by sending specific signals, like termination or restart.

---

## Intro for Version Control Using Git and the Command

- Version control is to keep track of your created checkpoints (version) for code writing. If you have created some mess while coding, you can easily revert that changes and go to a previous version of that code.

---

### Let's see what are the steps to take for version control

- **git init** : to initialize the git repo at local level.
- **git add {file_name}** : to add the files to the local repo or staging area (use `.` or `*` to add all the files)
- **git status** : to check the status of the current repo and changes that made after creating the repo.
- **git commit -m "{massage}"** : to commit the changes and save the changes in the staging area **with a message**.
- **git log** : this is to see all the log or previous commits.
- **git diff {file_name}** : to see the changes made to the file after commiting the file.
- **git checkout {file_name}** : to rollback all the changes made to the file to the last commit.
- **git restore --staged {file_name}** : Remove changes from the staging area. Use `*` or `.` to remove all changes from staging area.

---

### GitHub and remote Repositories

Make an account of GitHub and then make a new repository, and copy the address of the repository.

- **git remote add origin {link}** : origin is the name of your remote. **_But we can name it as we want._**
- **git branch -M main** : The command `git branch -M main` renames the current Git branch to main, enforcing the change.
- **git push -u <origin_name> <branch_name>** : `main` branch is default branch, `-u` flag here is link the remote and local repo.

---

#### **_By this we can upload our local repositories to remote repositories._**

- **gitignore** : It is a file that prevents us from committing such files to having any confidential data such as passwords, API keys, mobile number, E-mail, etc. and files having user preferences, OS settings/details, utility files, etc.
- **touch .gitignore** : `touch` is used to make files, .gitignore is the file is which we put name of all the files that we don't want to share online.
- **code .gitignore** : `code {file_name}` is used to open the file in code editer.
- **git rm --cached -r {file_name's}** : `rm` is used to remove the commited files and send back to staging area, `-r` flag is for recursive removal of files.

```bash
Example of .gitignore:
    # This is a comment
    .env # this will ignore .env file form commiting.
    .venv # this will ignore .venv file form commiting.
    __pycache__/ # this will ignore __pycache__ folder form commiting.
    env/ # this will ignore an env folder form commiting.
    venv/ # this will ignore a venv folder form commiting.
    secrets.txt # this will ignore secrets.txt file from commiting.
    *txt # this will ignore every txt file form commiting.
```

---

### Cloning

It is copying someone else's data from remote repository to our local repository.

- **git clone {URL}**: URL is of remote GitHub repository.

---

### Branching and Merging

- **git branch** : shows the names of current branches.
- **git branch {branch_name}** : add a new branch.
- **git checkout {branch_name}** : this will change the current branch.
- **git merge {name_of_branch}** : to merge multiple branches.

---

### Forking and Pull Request

- Fork mean to copy another person's repository to our own GitHub repository online.
- Pull the request means to request the original user to commit changes that we did in their code.
- After doing this, we are now an open source contributor.
- We can do all of these in GitHub Web GUI.

---

**To learn Git/GitHub : _<https://learngitbranching.js.org/>_**

## Author

**Harshit Soni**  
GitHub: [Harshit-Soni78](https://github.com/Harshit-Soni78)

---
Made with ❤️ by Harshit Soni
