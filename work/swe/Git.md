cheat sheet is here: https://git-scm.com/cheat-sheet


## Common Scenarios

**Scenario 1**
You have a bunch of changes on local and you want to push them as a branch to the origin:

First create a branch
```
git checkout -b branch-name
```

Then you can add and commit your changes:
```
git add .
git commit -m "changes"
```

Scenario 2
You have local code that you want to push to github (you haven't made a repo yet)
1. Make a repo on github
2. `git init` in the local code
3. `git add .` then `git commit -m "foo"` in your current repo
4. `git remote add origin <url>`
5. `git pull --allow-unrelated-histories` -- if you already have committed on the remote repo
6. git push origin main

Scenario 3: `--amend`
You committed an api key on local and you need to amend the commit before pushing your branch to remote.

If the commit was the last commit, simply remove the information (or you can even add information) and run:
```
git add .
git commit --amend
```


## Useful commands

- `git rm --cached file` removes a file from being tracked from the git (if you accidentally pushed it before changing gitignore)
- `git rm --cached -r dir/` recursively removes the entire directory
- `git branch -D branch1 branch2 ...` deletes unused branches