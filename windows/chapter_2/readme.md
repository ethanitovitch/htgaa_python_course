# Chapter 2 - Python & Running Code 

## Objective
- By the end of this chapter you will know how to manage python on your local machine and run simple scripts

## Intro
So at this point we know how to install tools and run them in our terminal but what if we wanted to run a set of steps instead of manually running one thing at a time. Well that's where programming languages come in. Programming languages let you define a set of steps and then give that to the computer to run in order. 

Now here's the thing, programming languages can't actually speak to the computer directly, first they need to convert the human readable version to computer version. This is called "compiling". In a gross over simplification, Programming languages come in two flavours ones that do the compiling in an initial build stage like typescript, java and rust (static languages) and ones that do it on the fly like python or ruby(dynamic languages). 

Why choose one over the other? Well from my experience, the static ones catch a lot of errors upfront because they need to go through the whole code base before you run anything. On the other hand dynamic languages will still run your code even if they contain errors waiting to happen. While this might make it seem like static languages are clearly better, the safety comes at a cost, namely speed. In order to get a static language to run you need to do a lot more work upfront vs with dynamic languages you can get started right away. You're essentially sacrificing speed for safety. 

My mental model is: If I'm building something built for production that needs to serve customers I'd rather do the work upfront than deal with angry users (they can be very rude) - so I chose a static language like `typescript`. If I'm experimenting or working on some research project with friends (who are usually a lot nicer) I optimize for speed and go with a dynamic language like `python`. I think that's why you typically see `python` used among researchers. It's super readable and easy to work with making it the perfect choice for iterating quickly and testing lots of things.

## Installing Python
Okay enough of my rambling, lets run some python code. To do so, we need to install python on our machine. Now I know what you're thinking, you can just install it with winget or Chocolatey but there's a catch. As of writing this, python is at version `3.14` and you might start a project using version `3.14` tomorrow, but then in a few years the latest and greatest might be version `5.10` which you install on your machine. You then come back to your project which you built using version `3.14` and you run into the most classic error in software, the classic "wait I didn't change any code why is it not working all of a sudden". The reason being that code written with version `3.14` might not run with python `5.10`. The solution: We need a way to easily switch between different versions of a programming language (see... more versions!). Whenever you want to use a new language the first thing you should look for is the "language version manager". And of course python has one, it's called `pyenv-win` and this is what we will install!

To install pyenv-win, you'll need git first (which you should already have from chapter 1). Open up your PowerShell terminal (if you don't have it open already) and run `git clone https://github.com/pyenv-win/pyenv-win.git $HOME\.pyenv`. Then you need to add pyenv to your PATH. Run these commands in PowerShell:
- `[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")`
- `[System.Environment]::SetEnvironmentVariable('PYENV_ROOT',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")`
- `[System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")`
- `[System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"), "User")`

After running these, close and reopen your terminal. As always, you can see the different commands pyenv has with `pyenv --help` but lets go ahead and install python. As of writing this, the latest version is `3.14.2` which you can install with `pyenv install 3.14.2`. After the installation is complete, you can see all the versions you've installed with `pyenv versions` and you can set a version of python with `pyenv global 3.14.2`. You can confirm this worked correctly by running `python --version` and you should see something like `Python 3.14.2` printed to the console. Now for the record, this won't stop you from running into the "most classic bug" but hopefully if you ever do, you will quickly change the global version and get back to what you were doing.

## Running Python
Finally, lets run some python code. Since python is a dynamic language and will compile on the fly, we actually don't even need any code ready to run python. We can write and execute our code at the same time! This is the power of a dynamic language. To do so, go ahead and type `python` in your terminal. You now have a python shell which you can use to run python code. 

For our first command lets start with something simple, enter `1 + 1` in your python shell and hit enter, if all worked correctly you should see `2` printed to the console. This may not seem like much but personally, I find it way faster to open up a python shell than open up the calculator app on my phone when I need to do some math. Still not convinced lets try something I know you can't do on your calculator app that comes up all the time in the HTGAA course. Say I give the following DNA sequence `ATGGCTGACCTGTTCAAGGACGCTATCGAGTTCGAGCTGACCAAGTGGGACCTG` what's the fastest way you could tell me how many amino acids it codes for. In your python shell that's super easy. You could easily run `len("ATGGCTGACCTGTTCAAGGACGCTATCGAGTTCGAGCTGACCAAGTGGGACCTG") / 3`. Pretty handy right! 

Now python can be run as a shell but if the commands you want to run are saved in a file you can run the code with `python FILE_NAME`. 

Exercises:
- See what else you can do in the python shell. See what other math operations are available.
- I wrote a very simple python script in this git repo in the chapter 2 folder. Use your `cd/dir` (or `ls` in PowerShell) knowledge to find the file and run it with `python FILE_NAME` (make sure to write the whole file name including the extension)

In the next chapter we will get more familiar with python programming and see how to save our python programs to files to be run later.

## Summary
- You should now understand how to install python or any programming language on your machine
- Open up a python shell & run basic python commands
