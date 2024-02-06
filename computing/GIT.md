#### Removing a file or folder from a GIT repository (i.e. stop it being tracked and remove it from github)

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



[up](README.md)
[top](../README.md)
