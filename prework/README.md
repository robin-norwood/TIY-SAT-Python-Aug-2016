# Backend Engineering with Python

Read this document, and follow each of the steps below before your first day of class.

## Read The Rules

The next few sections cover rules and guidelines for a successful class.

### Three rules

There's a lot of information below, but success at The Iron Yard boils down to three things:

- Show up
- Communicate
- Be honest

### Mindset
1. Read [Fixed vs. Growth: The Two Basic Mindsets That Shape Our Lives](http://www.brainpickings.org/2014/01/29/carol-dweck-mindset/)
  - You will need to have a growth mindset to succeed in this class. Banish the words *I can't* from your mind for the next twelve weeks.

### The Class
1. Monday-Thursday, class time will begin with lecture at 9:30, and will last about three hours. Then we'll break for lunch, and resume class at 1:30 for individual and group work until 5pm.
2. Friday is individual and group work time all day. Use this time to work on your assignments and further practice.
3. Periodically we'll have guest lectures and other activities. Some of these will be optional. Your lecturer will let you know what is expected.
4. Class time is mandatory. Per The Iron Yard's guidelines, more than four absences will result in loss of career support, but you can still finish the course.
4. Being more than 5 minutes late to class will result in a tardy. Two tardies will be counted as one absence.
5. Much of the lecture time will involve live coding, and you should follow along and participate.
7. Ask questions! If something doesn't make sense to you, that's a good opportunity for you to learn by asking a question.
6. For lab and project time, please work together, ask each other questions, and help each other. I will also be available during lab time, so ask me for help if you need it. However, I'll also be grading assignments, preparing for the next day's class, and various other tasks. If you need to set aside some dedicated time to talk to me one-on-one, book time with me using calendly.
7. Everyone is expected to participate, and help the rest of the class succeed as well. Rather than list all of the things that you shouldn't do, I ask you to keep in mind how your actions affect the learning experience of the rest of the class, and do your part to make this a positive experience for everyone.
8. This course is meant to be hard. We'll be learning an incredible amount of information in a very short time, and it will be stressful for everyone. Be mindful of how you're handling the workload and stress, and if you need help, talk to one of the staff sooner rather than later.

### Homework Policy

* All assignments are due at 8am before class begins
* No assignments should include copy and pasted code
  - Working with others is encouraged, though. Even if you work together, your fingers should type everything you turn in, and more importantly, you should *understand* every line of code.
* No assignments should include code lifted or 'borrowed' from someone else without proper citation and licensing
  - For instance, Stack Exchange is a popular 'answers' site. If you use an answer to help you get a solution, provide a link to that answer. Again, please make sure you understand the code you use, even if you got help.
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

## Computer setup

You'll need a mac laptop that meets the following requirements:

* Operating system: At least OS X El Capitan
* RAM: At least 4 GB
* Processor: At least 1.4 Ghz
* HD space: At least 128 GB

Before following the steps below, make sure you have updated your mac by clicking on the 'apple' logo in the menu, 'About This Mac', and then 'Software Update'

### Install brew

We'll use software called *brew* to install the latest version of python and other software we'll need. Open the *terminal* application, then you can install brew by copy and pasting this command to the terminal window:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Once you've done that, run these commands to make sure brew is working:

```
brew doctor
brew update
```

Next, install the latest version of Python:

```
brew install python3
```

```
pip3 install ipython
pip3 install virtualenv
```

### Atom

We'll be using an editor called Atom to edit our code. Download and install it here:

https://atom.io/


