## Welcome
Hello and welcome! I'm excited to have you joining the course. This document will take you through some background and pre-work you'll need to complete to be ready for class. Please read through this material and follow the steps below **before** the first day of class. By doing this, we'll be ready to get started from day one, and not spend class time getting everyone set up. If you get stuck, send me an email (robin@theironyard.com) and I can help.


## Objectives
1. Ensure you have the growth mindset you'll need to be successful in this course.
2. Learn what to expect during class.
2. Set up your computer to be ready to start class on the first day.
3. Learn some of the basic tools and skills we'll use in class.

## Mindset
1. Read [Fixed vs. Growth: The Two Basic Mindsets That Shape Our Lives](http://www.brainpickings.org/2014/01/29/carol-dweck-mindset/)
  - You will need to have a growth mindset to succeed in this class. Banish the words "I can't" from your mind for the next twelve weeks.
3. Compose an email to me (robin@theironyard.com) answering the following questions:
  - What aspects of the Growth and Fixed mindset can you identify in your personal history? In what areas do you feel Fixed? Where do you see the most Growth?
  - What difficulties do you predict that you will encounter during our course? How have you reacted to similar situations in the past? How do you plan on reacting to these situations during the class?

## The Class
1. Monday-Thursday, class time begins at 9:00, and will last about three hours. Then we'll break for lunch, and have "lab time" until 5pm.
2. Friday is lab time all day. Use this time to work on your assignments and further practice.
3. Class time is mandatory. Per The Iron Yard's guidelines, more than four absences will result in loss of career support, but you can still finish the course.
4. Lab time is considered class time. That said, you're expected to manage your own time and energy level, so if you complete your work early, or feel more productive after a short nap or coffee break, that's totally up to you, so long as you complete your assignments.
5. Being more than 5 minutes late to class will result in a tardy. Two tardies will be counted as one absence.
6. Much of the lecture time will involve live coding, and you should follow along and participate.
7. Ask questions! If something doesn't make sense to you, that's a good opportunity for you to learn by asking a question.
8. For lab and project time, please work together, ask each other questions, and help each other. I will also be available during lab time, so ask me for help if you need it. However, I'll also be grading assignments, preparing for the next day's class, and various other tasks. If you need to set aside some dedicated time to talk to me one-on-one, book time with me using calendly.
9. Everyone is expected to participate, and help the rest of the class succeed as well. Rather than list all of the things that you shouldn't do, I ask you to keep in mind how your actions affect the learning experience of the rest of the class, and do your part to make this a positive experience for everyone.
8. This course is meant to be hard. We'll be learning an incredible amount of information in a very short time, and it will be stressful for everyone. Be mindful of how you're handling the workload and stress, and if you need help, talk to one of the staff sooner rather than later.

## Honesty
>"Honesty is more than not lying. It is truth telling, truth speaking, truth living, and truth loving."
>-James E. Faust

### Honesty Policy

* __Honest with your feedback__

* __Honest with your homework__

* __Honest with your understanding__

* __Honest with your feelings__

* __Honest with your peers__

* __Honest with yourself__

I cannot stress enough the importance of honesty and open communication.

For the sake of clarity, we'll define Honesty as:
>Honesty: sincere, blameless, fairly earned, simple, unpretentious, and free of deceit.

## Homework Policy

* All assignments are due at 8am before class begins
* No assignments should include copy and pasted code
  - Working with others is encouraged, though. Even if you work together, or find an answer online, your fingers should type everything you turn in, and more importantly, you should *understand* every line of code.
* No assignments should include code lifted or 'borrowed' from someone else without proper citation and licensing
  - For instance, Stack Exchange is a popular 'answers' site. If you use an answer to help you get a solution, provide a link to that answer. Again, please make sure you understand the code you use, even if you get help.
* Incomplete homework is better than late homework
* Late homework is better than no homework
* Asking for clarification or help on assignments is encouraged
* Turning in code that you do not understand is discouraged and should be noted so we can address those issues

### Communication Policy

* More is better than less
* A peer is better than a google search
* A google search is better than [staring into the abyss](http://blog.8thlight.com/justin-herrick/2012/09/18/adapting-to-change.html)
* Stargazing is better than giving up
* Asking for help is always encouraged
* "I don't understand" is a great answer
* Sharing is good, but always include a source. Do not spread misinformation
* Be open when you are struggling, feeling behind, or overwhelmed

## Computer Setup
### Make sure your laptop meets the minimum requirements
1. Operating System: At least OS X Mavericks (10.9)
2. RAM: At least 4GB
3. Processor: At least 1.4GHz
4. Hard Disk: At least 128GB, with at least 20GB free

If your laptop doesn't meet those requirements, you probably need to buy one. A used/refurbished laptop is fine, as long as it meets the requirements above.

### Upgrade to OS X El Capitan, if your hardware supports it
1. You'll need to sign in to the Mac App Store with you Apple ID. If you don't have one, [sign up here](https://appleid.apple.com/).
2. Download and install the El Capitan upgrade from the Apple Store: [start here](http://www.apple.com/osx/how-to-upgrade/).
3. If your mac doesn't support El Capitan, that's ok, as long as you're at least running Mavericks (10.9).

### Make sure your OS is up to date
Click on the Apple logo in the upper left of your screen, choose "About This Mac" and then the "Software Update..." button.

### Additional Software
We'll standardize on using Atom and Google Chrome as our text editor and web browser. There are plenty of other options out there, it will just be simpler if we're all using the same software.

1. Install [Atom](https://atom.io/) and run it.
  - Read sections 2.2 through 2.5 of the [atom documentation](https://atom.io/docs/v1.5.4/using-atom-moving-in-atom)
  - Use those keyboard shortcuts! Moving your hand from the keyboard to the mouse and back is slow!
  - Atom is very powerful and customizable, but it probably isn't worthwhile for you to read about the advanced features in the rest of the documentation yet.
  - Practice typing and editing some text in Atom.
2. Install [Google Chrome](https://www.google.com/intl/en/chrome/browser/).

## Python
We'll use a tool called Homebrew to install Python 3. Homebrew is useful because it (mostly) insulates us from differences between versions of Mac OS X and other software on your computer. There are a lot of steps, and depending on what state your computer is in, it's possible the steps below won't work. If that happens, just take a screenshot and email it me (robin@theironyard.com). We'll also spend some time before class starts getting your machine set up and making sure it's working.

1. Open a Terminal window by pressing Command-spacebar, typing "terminal", and hitting Enter.
2. Copy and paste the following command into the terminal window:

        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

3. Homebrew will ask you to enter your password and run several commands to set up. If everything goes well, you should see `Installation successful`
4. Run "brew doctor" in the terminal, and you should see `Your system is ready to brew.`
5. Install python 3 by typing this in the terminal window: `brew install python3`
6. Upgrade python's package manager: `pip3 install --upgrade pip setuptools`
7. Install ipython, an interactive python shell: `pip3 install ipython`
8. Make sure all of the above worked: `ipython3`
9. You should see something like:

        Python 3.5.1 (default, Jan 22 2016, 08:54:32)
        ...a few more lines of stuff...
        In [1]:

    This is an interactive python shell. A shell is an application that waits for you to type commands, and then responds to them. The Terminal application you've been using is one kind of shell, and ipython is a different kind of shell that interprets python code as you type. We'll be using it a lot in class.

10. Type `print('Hello, world!')`
11. You should see:
        Hello, world!

        In [2]:
12. Press control-D to exit.

If all of the above worked fine, you should be ready for your first day of class. If not, work with me and we'll get it fixed before class.

## Supplemental online tutorials

Spend some time working through the [Code Academy Python tutorial](http://www.codeacademy.com/en/tracks/python). We'll be covering the same material in the first few days of class, but a little practice reading and writing python will help you hit the ground running.

Do the same with the [HTML and CSS](http://www.codecademy.com/en/tracks/web
) tutorial. HTML and CSS will be covered in the course, but not to the same depth as Python.

As you go through these courses, take a note of anything that's confusing or surprising, and ask questions about those things at the appropriate time during class. A good habit to have as a software developer is that any time something surprises you, recognize it as an opportunity to learn.

## The Command Line
The command line is an interface to the internals of your computer, as opposed to the graphical user interface (GUI) that we often use. We will be using the command line a lot in class, so learning the basics now will go a long way.

Especially if you’ve never used the command line before, you may want to go through this more than once. Make sure not just to read, but really dive in and use the commands that you learn about.

1. Follow [this tutorial](http://www.davidbaumgold.com/tutorials/command-line/) on command line basics.

## Git and GitHub
Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. Version control systems are important for developers so we can keep track of the changes we make to our code and share those changes with other developers.

We'll use the shell command "git" to manage our code in GitHub, which is a web-based hosted version of Git. The objective is not to become an expert before the class, but just start to get comfortable.

## Sign up to GitHub
GitHub is a web-based hosting and communication service for software development projects that uses the Git revision control system.

1. Sign up for a GitHub account at https://github.com/.
2. Make sure to add a profile picture and your full name.
3. Email me (robin@theironyard.com) your GitHub username so I can add you to the group we'll be using for class.
4. Complete https://try.github.io/.

Check out the [GitHub Guides](https://guides.github.com/) if you want to learn how to use GitHub prior to class.

Full disclosure: git and github can be *very confusing*, even to experienced developers. We'll be learning a lot in class, including how to use git and github, but it's not unusual to get "stuck" when using git. When that happens, just like any other challenge, please ask for help. This is even more important with git, as it is possible to lose your work with poorly chosen git commands. So when in doubt, stop and ask for help.

# Typing
One of the best and worst things about being a developer is that computers will do exactly what you tell them. It's as if you have an all-powerful genie who, when you ask them to "make me a sandwich" will happily make you (into) a sandwich. As a developer, that means if you make a typo, the computer will try to do exactly what you say, even if it's nonsense. During your career, you *will* spend countless hours trying to figure out what went wrong when you typed "delete_user" instead of "delete_user()" - those parenthesis are important!

If you don't know how to touch type (type without looking at the keyboard), spend some time each day working on touch typing (you can try http://www.keybr.com/). If you already know how to touch type, I would highly recommend working through the Python lessons on http://typing.io. Typing for programming is actually a bit different than everyday typing, so getting some practice in could save you a ton of time the first few weeks of class.

# The End
Thanks for getting this far! I know the above is a lot of information and work, but please make sure you complete it all before class starts so we can all hit the ground running. I'm looking forward to having you in class soon!


