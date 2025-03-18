### Creating a new branch and switching to it
Create a New Branch:

```bash
git branch <branch_name>
```
Replace <branch_name> with the desired name for your new branch.

Switch to the New Branch:

```bash
git checkout <branch_name>
```
This command switches your working directory to the newly created branch.

Alternatively, you can use a single command to create a new branch and switch to it in one go:

```bash
git checkout -b <branch_name>
```
### Deleting a local branch in GIT


To delete a local branch in Git, you can use the following command:

```bash
git branch -d <branch_name>
```
Replace <branch_name> with the name of the branch you want to delete.

If the branch has unmerged changes (i.e., changes that haven't been merged into another branch), Git will prevent you from deleting it with the -d option. In that case, you can force the deletion using the -D option:

``` bash
git branch -D <branch_name>
```
This will delete the specified branch from your local repository. Make sure you're certain you want to delete the branch, as this action cannot be undone

### Deleting a branch from GitHub

To delete a branch from GitHub, you can follow these steps:

- Locate the Repository: Go to the GitHub repository where the branch exists.
- Access the Branches Page:

  - At the top of the repository, click on the "Branches" tab. This will show you a list of all branches in the repository.
- Select the Branch:

  - Find the branch you want to delete from the list of branches and click on it to navigate to its page.
- Delete the Branch:

  - On the branch's page, there should be a button labeled "Delete branch" or a trash can icon next to the branch name. Click on this button.
- Confirmation:

  - GitHub will ask you to confirm the deletion. Confirm that you want to delete the branch.

### Removing a file or folder from a GIT repository (i.e. stop it being tracked and remove it from github)

- Locally Remove the Folder:

  - Open a terminal or command prompt.    
  - Navigate to the root directory of your local Git repository using the `cd` command.
  - Run the following command to remove the folder from the repository's history, replacing `foldername` with the name of the folder you want to remove.:

```bash
git rm -r --cached foldername
```

  - Commit the change:
```bash
git commit -m "Remove foldername from version control"
```

  - Push the changes to the remote repository on GitHub:

```bash
git push origin branchname
```



### Using git subtree

Assuming you want to clone a specific directory called subdirectory from a GitHub repository into your existing Git repository, you can use the following command:

```bash

git subtree add --prefix=path/to/destination/folder --squash <repository_url> <branch>
```
Replace the placeholders

- _path/to/destination/folder_ is the path where you want to place the cloned directory within your repository.
- _repository_url_ is the URL of the GitHub repository,
- _branch_ is the branch from which you want to clone the directory.

## Using git submodule:
If you want to maintain a separate submodule for the directory you are cloning, you can use the git submodule command. This will allow you to keep the cloned directory in a separate Git repository within your main repository.

```bash

git submodule add -b <branch> <repository_url> path/to/destination/folder
```

Replace the placeholders

- the _branch_ is the branch from which you want to clone the directory,
- _repository_url_ is the URL of the GitHub repository.
- _path/to/destination/folder_ is the path where you want to place the submodule within your repository.

After adding the submodule, you need to initialize and update it:

```bash

git submodule update --init --recursive
```

### Undo Uncommitted Changes (Modified Files)
If you modified a file but haven't staged it yet:

```bash
git checkout -- <file>
```
This will revert the file to the last committed version.

If you staged the changes (with git add), but haven't committed:

```bash
git reset HEAD <file>
```
This unstages the file, but keeps the modifications.

### Undo Last Commit (But Keep Changes)
If you want to undo the last commit but keep the changes:

```bash
git reset --soft HEAD~1
```
This moves the commit back to the staging area.

### Undo Last Commit (Discarding Changes)
If you want to delete the last commit and discard the changes:

```bash
git reset --hard HEAD~1
```
⚠ This is irreversible unless you have backups.

### Undo Last Pushed Commit
If you've already pushed the commit to a remote branch and want to undo it:

```bash
git reset --hard HEAD~1
git push --force
```
⚠ Be careful—this can rewrite history for others.

### Undo a Specific File to a Previous Commit
```bash
git checkout <commit_hash> -- <file>
```
This restores a file from an older commit but doesn’t remove it from history.





[up](README.md)
[top](../README.md)
