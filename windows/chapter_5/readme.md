# Chapter 5 - The greatest line of code python has to offer

## Objective
By the end of this chapter you should feel comfortable debugging and using the `breakpoint()` function

## Introduction
So up to now you've done a ton of work and I'm happy to say the worst is behind us. Pat yourself on the back! For this last chapter, I wanted to go over what I think is the most underrated feature of python or really any dynamic programming language. This will be super quick but so important I figured I'd dedicate a whole chapter to it. That feature is the `breakpoint()` function

## Breakpoint
In chapter_2 I spoke about how dynamic programming languages run the code line by line. This can be dangerous because it allows us to run potentially incorrect code but at the same time, it also allows us to do crazy things like open up a python shell in our terminal and give it the lines to run on the fly. This allows us to do something even crazier like open a python shell from anywhere in your code using `breakpoint()`!!!

Why is this so useful? Well say you write some code or copy paste some AI slop and realize it doesn't work as expected. What most people (even experts) do is start writing print statements all over the place to try and track down the state of the code throughout the program. What's infinitely more efficient is to throw a breakpoint into your code and walk through it line by line.

I wrote a quick snippet of code in `chapter_5/bug.py` to illustrate how you might use the breakpoint line. If you run the file you will see `ZeroDivisionError`. So how can you easily debug this using breakpoint? Well first uncomment the breakpoint and now run the file.

The first thing you will notice is the code stopped at your breakpoint! Sometimes you have multiple breakpoints set up so to see where you are run `l` or `ll` for more lines. 

You can then go to the next line with `n` and the next with `n`. It might get annoying to keep running `n` so you can run until a line with `until`. Go to line 12 with `until 12`. 

Now here is where it gets interesting, which branch of code did our code go down? The if or the else? Well we can know if the if condition is true by running it. Run `x > 5` in the shell. Oh the output is False, it must have gone down the else! 

Okay let's continue with `n` and then `n` again. Now we're at a function call. We can print the variables that will be passed in with `p z` and `p y` (p for print). Wait? 0 divided by 2 is returning a `ZeroDivisionError`??? but how? Let's step inside the function call with `s` to see. 

Then hit `n`, `n` & `n` to get to the right line. We're now at line 4. Let's see the variables `p a` & `p b`. Ohhh I see, divide switched the variables around. Easy fix... don't do that. You can now exit the breakpoint shell with `c` (for continue) or `exit()`

Pretty simple example but I hope you see the power of the breakpoint and how easy it makes debugging code. Breakpoint comes with a lot of commands but the ones I've shown here are the most common ones I use.

But yah, that's all I have for you! If you made it this far, congrats and thank you for listening to my rambling, I hope it was useful! Good luck with the rest of the HTGAA course.

## Summary
- You should now feel comfortable debugging code with the `breakpoint()` function call and feel my disappointment if you debug with print statements lol

