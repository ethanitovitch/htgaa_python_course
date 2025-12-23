# Chapter 1 - Git & Pulling code

## Objective
By the end of this chapter you will know how to pull code from github onto your machine using git

## Intro
Okay lets start with git, many people know Linus Torvalds as the creator of the linux operating system, what a lot of people don't know is that Linus Torvalds also created git.

Linux was probably one of the grandest projects at the time and while building it, Linus ran into a problem, he needed a way to track different versions of the code, work on parts in isolation to merge them in incrementally and share the code with other people. He created git to solve this problem and ended up creating two of the most important software products AT THE SAME TIME. 

![Linus Torvalds](../../images/linus.png)

As you learn more about software you will see the idea of versions comes up A LOT. Everything is tracked at different versions including: Programming languages, libraries even this code base. But don't worry we will learn about different tools for simplifying all of it. The first one being git!

## Git
Now, you probably noticed that this tutorial is on "github" but why do I keep saying "git"? Well that's because "git" is the open source standard for tracking code bases, while "github" is a cloud platform that makes it easy to share and store the git histories in the cloud. So in order to pull code from github you need "git" and to store code on "github" you need a github account. We will focus on the former in this tutorial.

Okay but before we install git we need to learn about the terminal (the place we will be using git). So, for a lot of software products an interface actually isn't all that important. The important thing is speed and what you will come to see is that a pretty interface can get in the way of that. That's why for a lot of coding products we like to do everything in the terminal which is basically a text only way of speaking directly to the operating system (pretty hardcore I know). If you're on a mac you can access this by simply searching for "terminal" in your search bar and opening the app. You can think of the terminal as the fastest most direct way to talk to your machine (without going through the ui). There are tons of commands and ways to customize things but for now there are only a few commands I want you to know:
- `ls` -> prints the folders and files in the current folder
- `cd FOLDER_NAME` -> goes into a folder
- `cd ..` -> goes back a folder
- `mkdir FOLDER_NAME` -> makes a folder in the current folder
- (Note) I have simplified each of the commands. You can add `--help` to ANY command to get more in detail description of what the command does. 

As an exercise try exploring your machine, see if you can find your way to a folder in your desktop then back up. Don't worry about getting lost you can always find your way back to where you started with `cd ~`

Now back to git, wait... homebrew first! Now that you know some basic commands on the terminal it's time to take it up a notch, sometimes we want to add new commands like say git! Well how do we get git on our terminal at the most up to date version (even git has multiple versions) well thats where a package manager comes in. Homebrew is the most well known one for mac. To install it visit https://brew.sh/ copy the install command and paste it into your terminal and hit enter. Congrats you have just installed your first new tool and a pretty powerful tool at that since homebrew is a tool for installing other tools! Every new tool from here will be smooth sailing. For instance lets install git, it's as easy as `brew install git` (you may need to restart your terminal first)

The git tool comes with a lot of commands for managing the versions of your codebase. As always you can run `git --help` to see types of things you can do, but for now the only one I want to focus on is the clone command. This lets you pull code from github onto your machine (ahuh our objective!) but first some organization. 

Personally I like to organize my code bases in a Projects Folder on my Desktop so lets set that up for you. To make sure we're all in the same spot run `cd ~`. Then lets go into your desktop with `cd Desktop`. Now for the fun part lets create a folder for our git repos with `mkdir Projects` (feel free to name it whatever you like best). Now lets go into the projects folder with `cd Projects` (or whatever you called it), Then `mkdir HtgaaBootcamp` and then cd inside. Now for the grand finale, to pull the code base, go to home page of this repo, click the code dropdown in green. Copy the url and run `git clone URL` and boom you should now have the git repo installed locally. You can confirm this with our friend `ls` and you can go into the repo with `cd htgaa_python_course`

## Advanced (optional)
I put this tutorial together pretty quickly and there could easily and most likely will be many mistakes. The Question is how can you contribute to this tutorial if you find one? Well for that we need to modify code in the github repo so you will need the github tool notice "github" not "git". 

First install it with `brew install gh` (see I told it would be smooth sailing). Then create a github account and login with `gh auth login`. Answer the following questions with:
1. Where do you use GitHub? `GitHub.com`
2. What is your preferred protocol for Git operations on this host? `HTTPS`
3. How would you like to authenticate GitHub CLI? `Login with a web browser`

Then follow the instructions to login.

If you have update access to the repo (by asking ethan) you can create a branch with `git checkout -b your-name/your-update`
If you don't have update access then you can create a fork and clone the fork to your local machine. Either way now you are on your own isolated version of the code. 

You can then make your changes, see the changed files with `git status` add them with `git add .` (. adds all the changes but sometimes you want to be more granular by naming the files you want to add directly). Commit the changed with `git commit -m'a message about your changes'` and then `git push` or `git push --set-upstream origin your-name/your-update` if you had the update access. 

Now your changes are in github but how do you merge them into the master version so everyone can now get the latest and greatest. Well go to the original repo for this tutorial. Click on the `Pull requests` tab and create a new pull request. Admins in the repo can then look at the changes and approve the pull request if they like the additions. They may also request some changes before merging.

## Summary
- You should now have a basic understanding of the terminal and be able to navigate your file system with cd/ls. 
- Be able to install tools with brew
- Have a basic understanding of git and be able to pull code