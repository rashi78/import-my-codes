# 1] Command to add username :-

# To add a new user, type the following command. We can use double quotes at the end of this command to add the desired username.

$git config --global user.name "USER_NAME"

# 2] Command to add email address of user :-

# To add a new user mail address, type the following command. We can use double quotes at the end of this command to add the desired user email.

$git config --global user.email "USER_MAIL@gmail.com"

# 3] Command to check username and mail id of user :-

$git config --global user.name
$git config --global user.email

# 4] Steps to create and push a git repo :-

# STEP-1 :-

# Case-1: If you already have a folder ready to push to github, simply use the command below to change the path to that folder.

$cd Directory_Name
# Case-2: If you don’t have a folder, make one and then change the directory to it.

$mkdir Directory_Name
$cd Directory_Name

# STEP-2 :-

# Initiate the repository using the following command

$git init

# STEP-3 :-

# The following command can be used to check the status of our repository after it has been initiated.

$git status

# STEP-4 :-

# If you don’t have a ready-to-commit code or file, use the command below to edit the file and then push it to the repository. We can use any editor to edit the files.

$gedit EXAMPLE.txt

# STEP-5 :-

# After the file has been edited, we must stage it (Staging is an area where files that will be committed in the future commit are inserted). To do so, run the command below. In the command below, “.”(dot) refers to the current file that we are going to push to staging area; we can also use filename instead of dot.

$git add .

# STEP-6 :-

# After staging, run the command below to commit the changes to the repository (Committing in laymen words means saving the changes made to a particular file in the mentioned repository). In the below mentioned command “-m” is used to add commit message.

$git commit -m "COMMIT MESSAGE"

# STEP-7 :-

# After completing all these steps go to github and create a repository and copy the “ git origin command “ from github.


# Creating new repository
# Login to github account and select the above shown new repository option.


# Adding the details of the repository
# Fill in the repository’s details: first, put the project’s name, then choose whether you want the repository to be public or private, and last, select the create repository option at the bottom.


# Copy the highlighted command
# Copy the highlighted command called “git origin command” from the github and paste it in the gitbash.

# STEP-8 :

# After executing all the above commands, we can now execute the push command, before executing push command it is good practice to execute pull command to get the latest version of the repository.

$git pull URL_OF_THE_GIT_REPO
$git push -u origin master 

# push command
# Execute the pull command and copy the highlighted command in the above image to execute the push command.

# REVERT COMMANDS :-
# The git reverting commands is a forward-moving undo that allows you to undo changes safely.

# There are three cases in undoing the changes. They are

# CASE-1 : Before staging

# This means that if we’ve made changes to the repository but haven’t used the git add command, we can revert the modifications using the following command.

$git checkout fileName

# CASE-2 : After staging

# This means that if we’ve made modifications to the repository and used the git add command, we’ll need to perform the commands below to undo the changes.

$git reset HEAD fileName
$git reset checkout fileName

# CASE-3 :After committing

# If we made modifications to the repository with both git add and git commit, we must use the following commands to return to the previous stage. We must first run the git log command to copy the last commit id from which we must rollback.

$git log
$git revert last_commit_id

# git branch commands :-
# Git branches are used to separate individual Git commits from the rest of your Git history.

# You can build a separate Git branch to develop new features and merge them later if your main Git history is based on the master branch.

# 1] Command to check the branch:-

# This command display the current branch.

$git branch

# 2] Command to create a branch :-

# In order to create a new branch we can employ the following command. We have to include the branch name at the end of the command.

$git branch branchName

# 3] Command to change the branch :-

# If we want to change the branch, we can use the following command and enter the destination branch name.

$git checkout destination_Branch_Name

# 4] Command to merge the commits :-

# We can merge the commits made in the branches to the master branch by following the below steps. First we have to checkout to the main branch and then we have to use git merge command.

$git checkout master
$git merge branch_Name

# Merge conflicts :-
# When more than one developer is working on the same file, and all of the developers make changes to the same lines on their own isolated branch, then try to merge to the main branch, git gets confused, and this is known as a git merge conflict.
# To fix this, we’ll need to run the following command.

$git mergetool