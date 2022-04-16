<p align="center">
    <a href=#><img src="https://raw.githubusercontent.com/jbocane6/logos/main/holberton-logo.png" alt="holberton" /></a></p>
  
  <p align="center">
    <a href="https://twitter.com/juanoso07555284" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juanoso07555284" height="30" width="40" /></a>
  <a href="https://linkedin.com/in/juan-camilo-bocanegra-osorio-18b1821a6" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="juan-camilo-bocanegra-osorio-18b1821a6" height="30" width="40" /></a>
  </p>
  
  <p align="center">
    <a href=#><img src="https://raw.githubusercontent.com/jbocane6/logos/main/titulo2.png" alt="titulo" /></a></p>

0x00. Shell, basics
===================

About Bash projects
-------------------

Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/205/image.jpg)

Resources
---------

**Read or watch**:

*   [What Is “The Shell”?](http://linuxcommand.org/lc3_lts0010.php)
*   [Navigation](http://linuxcommand.org/lc3_lts0020.php)
*   [Looking Around](http://linuxcommand.org/lc3_lts0030.php)
*   [A Guided Tour](http://linuxcommand.org/lc3_lts0040.php)
*   [Manipulating Files](http://linuxcommand.org/lc3_lts0050.php)
*   [Working With Commands](http://linuxcommand.org/lc3_lts0060.php)
*   [Reading Man pages](http://linuxcommand.org/lc3_man_pages/man1.html)
*   [Keyboard shortcuts for Bash](https://www.howtogeek.com/howto/ubuntu/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/)
*   [LTS](https://wiki.ubuntu.com/LTS)
*   [Shebang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29)

**man or help**:

*   `cd`
*   `ls`
*   `pwd`
*   `less`
*   `file`
*   `ln`
*   `cp`
*   `mv`
*   `rm`
*   `mkdir`
*   `type`
*   `which`
*   `help`
*   `man`

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google**:

### General

*   What does RTFM mean?
*   What is a Shebang

### What is the Shell

*   What is the shell
*   What is the difference between a terminal and a shell
*   What is the shell prompt
*   How to use the history (the basics)

### Navigation

*   What do the commands or built-ins `cd`, `pwd`, `ls` do
*   How to navigate the filesystem
*   What are the . and .. directories
*   What is the working directory, how to print it and how to change it
*   What is the root directory
*   What is the home directory, and how to go there
*   What is the difference between the root directory and the home directory of the user root
*   What are the characteristics of hidden files and how to list them
*   What does the command `cd -` do

### Looking Around

*   What do the commands `ls`, `less`, `file` do
*   How do you use options and arguments with commands
*   Understand the ls long format and how to display it
*   [A Guided Tour](http://linuxcommand.org/lc3_lts0040.php)
*   What does the `ln` command do
*   What do you find in the most common/important directories
*   What is a symbolic link
*   What is a hard link
*   What is the difference between a hard link and a symbolic link

### Manipulating Files

*   What do the commands `cp`, `mv`, `rm`, `mkdir` do
*   What are wildcards and how do they work
*   How to use wildcards

### Working with Commands

*   What do `type`, `which`, `help`, `man` commands do
*   What are the different kinds of commands
*   What is an alias
*   When do you use the command help instead of man

### Reading Man Pages

*   How to read a man page
*   What are man page sections
*   What are the section numbers for User commands, System calls and Library functions

### Keyboard Shortcuts for Bash

*   Common shortcuts for Bash

### LTS

*   What does `LTS` mean?

Requirements
------------

### General

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your scripts will be tested on Ubuntu 20.04 LTS
*   All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
*   All your files should end with a new line ([why?](https://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
*   The first line of all your files should be exactly `#!/bin/bash`
*   A `README.md` file at the root of the repo, containing a description of the repository
*   A `README.md` file, at the root of the folder of _this_ project, describing what each script is doing
*   You are not allowed to use backticks, `&&`, `||` or `;`
*   All your scripts must be executable. To make your file executable, use the `chmod` command: `chmod u+x file`. Later, we’ll learn more about how to utilize this command.

More Info
---------

_Example of line count and first line_

    camilo@home-laptop:/tmp$ wc -l 12-file_type 
    2 12-file_type
    camilo@home-laptop:/tmp$ head -n 1 12-file_type 
    #!/bin/bash
    camilo@home-laptop:/tmp$ 
    

In order to test your scripts, you will need to use this command: `chmod u+x file`. We will see later what does `chmod` mean and do, but you can have a look at `man chmod` if you are curious.

_Example_

    camilo@home-laptop:/tmp$ ls
    12-file_type
    lll
    camilo@home-laptop:/tmp$ ls -la lll
    -rw-rw-r-- 1 camilo camilo 15 Sep 19 21:05 lll
    camilo@home-laptop:/tmp$ cat lll
    #!/bin/bash
    ls
    camilo@home-laptop:/tmp$ ls -l lll
    -rw-rw-r-- 1 camilo camilo 15 Sep 19 21:05 lll
    camilo@home-laptop:/tmp$ chmod u+x lll # you do not have to understand this yet
    camilo@home-laptop:/tmp$ ls -l lll
    -rwxrw-r-- 1 camilo camilo 15 Sep 19 21:05 lll
    camilo@home-laptop:/tmp$ ./lll
    12-file_type
    lll
    camilo@home-laptop:/tmp$ 
    

Quiz questions
--------------
#### Question #0

What command would you use to list files on Linux?

&#9744; pwd
    
&#9744; cd
    
&#9745; ls
    
&#9744; list
    
&#9744; which
    

#### Question #1

What does LTS stand for?

&#9745; Long Term Support
    
&#9744; Long Time Support
    
&#9744; Last Terrible Service
    

#### Question #2

How do you change directory on Linux?

&#9744; pwd
    
&#9745; cd
    
&#9744; ls
    
&#9744; which
    

#### Question #3

What does RTFM stand for?

&#9744; Remember The First Manipulation
    
&#9744; Read, Teach, Forget, Migrate
    
&#9745; Read The F\*\* Manual
    

Tasks
-----

### 0\. Where am I?

Mandatory

Write a script that prints the absolute path name of the current working directory.

Example:

    $ ./0-current_working_directory
    /0x00-shell_basics
    $
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`0-current_working_directory`](0-current_working_directory)

-----
### 1\. What’s in there?

Mandatory

Display the contents list of your current directory.

Example:

    $ ./1-listit
    Applications    Documents   Dropbox Movies Pictures
    Desktop Downloads   Library Music Public
    $
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`1-listit`](/1-listit)

-----
### 2\. There is no place like home

Mandatory

Write a script that changes the working directory to the user’s home directory.

*   You are not allowed to use any shell variables

Example:

    camilo@home-laptop:/tmp$ pwd
    /tmp
    camilo@home-laptop:/tmp$ echo $HOME
    /home/camilo
    camilo@home-laptop:/tmp$ source ./2-bring_me_home
    camilo@home-laptop:~$ pwd
    /home/camilo
    camilo@home-laptop:~$ 
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`2-bring_me_home`](/2-bring_me_home)

-----
### 3\. The long format

Mandatory

Display current directory contents in a long format

Example:

    $ ./3-listfiles
    total 32
    -rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
    -rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
    -rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
    -rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
    $
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`3-listfiles`](/3-listfiles)

-----
### 4\. Hidden files

Mandatory

Display current directory contents, including hidden files (starting with `.`). Use the long format.

Example:

    $ ./4-listmorefiles
    total 32
    drwxr-xr-x@ 6 sylvain staff 204 Jan 25 00:29 .
    drwxr-xr-x@ 43 sylvain staff 1462 Jan 25 00:19 ..
    -rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
    -rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
    -rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
    -rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
    -rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:41 4-listmorefiles
    $
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`4-listmorefiles`](/4-listmorefiles)

-----
### 5\. I love numbers

Mandatory

Display current directory contents.

*   Long format
*   with user and group IDs displayed numerically
*   And hidden files (starting with .)

Example:

    $ ./5-listfilesdigitonly
    total 32
    drwxr-xr-x@ 6 501 20 204 Jan 25 00:29 .
    drwxr-xr-x@ 43 501 20 1462 Jan 25 00:19 ..
    -rwxr-xr-x@ 1 501 20 18 Jan 25 00:19 0-current_working_directory
    -rwxr-xr-x@ 1 501 20 18 Jan 25 00:23 1-listfiles
    -rwxr-xr-x@ 1 501 20 19 Jan 25 00:29 2-bring_me_home
    -rwxr-xr-x@ 1 501 20 20 Jan 25 00:39 3-listfiles
    -rwxr-xr-x@ 1 501 20 18 Jan 25 00:41 4-listmorefiles
    -rwxr-xr-x@ 1 501 20 18 Jan 25 00:43 5-listfilesdigitonly
    $
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`5-listfilesdigitonly`](/5-listfilesdigitonly)

-----
### 6\. Welcome

Mandatory

Create a script that creates a directory named `my_first_directory` in the `/tmp/` directory.

Example:

    $ ./6-firstdirectory
    $ file /tmp/my_first_directory/
    /tmp/my_first_directory/: directory
    $
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`6-firstdirectory`](/6-firstdirectory)

-----
### 7\. Betty in my first directory

Mandatory

Move the file `betty` from `/tmp/` to `/tmp/my_first_directory`.

Example:

    $ ./7-movethatfile
    $ ls /tmp/my_first_directory/
    betty
    $
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`7-movethatfile`](/7-movethatfile)

-----
### 8\. Bye bye Betty

Mandatory

Delete the file `betty`.

*   The file `betty` is in `/tmp/my_first_directory`

Example:

    $ ./8-firstdelete
    $ ls /tmp/my_first_directory/
    $
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`8-firstdelete`](/8-firstdelete)

-----
### 9\. Bye bye My first directory

Mandatory

Delete the directory `my_first_directory` that is in the `/tmp` directory.

Example:

    $ ./9-firstdirdeletion
    $ file /tmp/my_first_directory
    /tmp/my_first_directory: cannot open `/tmp/my_first_directory' (No such file or directory)
    $
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`9-firstdirdeletion`](/9-firstdirdeletion)

-----
### 10\. Back to the future

Mandatory

Write a script that changes the working directory to the previous one.

    camilo@home-laptop:/tmp$ pwd
    /tmp
    camilo@home-laptop:/tmp$ cd /var
    camilo@home-laptop:/var$ pwd
    /var
    camilo@home-laptop:/var$ source ./10-back
    /tmp
    camilo@home-laptop:/tmp$ pwd
    /tmp
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`10-back`](/10-back)

-----
### 11\. Lists

Mandatory

Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format.

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`11-lists`](/11-lists)

-----
### 12\. File type

Mandatory

Write a script that prints the type of the file named `iamafile`. The file `iamafile` will be in the `/tmp` directory when we will run your script.

Example

    ubuntu@ip-172-31-63-244:~$ ./12-file_type
    /tmp/iamafile: ELF 64-bit LSB  executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=bd39c07194a778ccc066fc963ca152bdfaa3f971, stripped
    

Note that depending on the file, the output of your script will be different.

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`12-file_type`](/12-file_type)

-----
### 13\. We are symbols, and inhabit symbols

Mandatory

Create a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory.

    ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
    total 144
    drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
    drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
    ubuntu@ip-172-31-63-244:/tmp/sym$./13-symbolic_link
    ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
    total 144
    drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
    drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
    lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`13-symbolic_link`](/13-symbolic_link)

-----
### 14\. Copy HTML files

Mandatory

Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

You can consider that all HTML files have the extension `.html`

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`14-copy_html`](/14-copy_html)

-----
### 15\. Let’s move

Advanced

Create a script that moves all files beginning with an uppercase letter to the directory `/tmp/u`.

You can assume that the directory `/tmp/u` will exist when we will run your script

    ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
    total 148
    drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
    drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
    -rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 My_file
    lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
    -rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 Elif_ym
    -rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
    ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la /tmp/u
    total 8
    drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:33 .
    drwxrwxr-x 3 ubuntu ubuntu 4096 Sep 20 03:33 ..
    ubuntu@ip-172-31-63-244:/tmp/sym$ ./100-lets_move
    ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
    total 148
    drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
    drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
    lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
    -rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
    ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la /tmp/u
    total 8
    drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:33 .
    drwxrwxr-x 3 ubuntu ubuntu 4096 Sep 20 03:33 ..
    -rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:32 My_file
    -rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:32 Elif_ym
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`100-lets_move`](/100-lets_move)

-----
### 16\. Clean Emacs

Advanced

Create a script that deletes all files in the current working directory that end with the character `~`.

    ubuntu@ip-172-31-63-244:/tmp/sym$ ls
    main.c  main.c~  Makefile~
    ubuntu@ip-172-31-63-244:/tmp/sym$ ./101-clean_emacs
    ubuntu@ip-172-31-63-244:/tmp/emacs$ ls
    main.c
    ubuntu@ip-172-31-63-244:/tmp/emacs$
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`101-clean_emacs`](/101-clean_emacs)

-----
### 17\. Tree

Advanced

Create a script that creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory.

You are only allowed to use two spaces (and lines) in your script, not more.

    camilo@home-laptop:/tmp/h$ ls -l
    total 4
    -rwxrw-r-- 1 camilo camilo 44 Sep 20 12:09 102-tree
    camilo@home-laptop:/tmp/h$ wc -l 102-tree 
    2 102-tree
    camilo@home-laptop:/tmp/h$ head -1 102-tree 
    #!/bin/bash
    camilo@home-laptop:/tmp/h$ tr -cd ' ' < 102-tree | wc -c # you do not have to understand this yet, but the result should be 2, 1 or 0
    2
    camilo@home-laptop:/tmp/h$ ./102-tree 
    camilo@home-laptop:/tmp/h$ ls
    102-tree  welcome
    camilo@home-laptop:/tmp/h$ ls welcome/
    to
    camilo@home-laptop:/tmp/h$ ls -l welcome/to
    total 4
    drwxrwxr-x 2 camilo camilo 4096 Sep 20 12:11 school
    camilo@home-laptop:/tmp/h$ 
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`102-tree`](/102-tree)

-----
### 18\. Life is a series of commas, not periods

Advanced

Write a command that lists all the files and directories of the current directory, separated by commas (`,`).

*   Directory names should end with a slash (`/`)  
    
*   Files and directories starting with a dot (`.`) should be listed  
    
*   The listing should be alpha ordered, except for the directories `.` and `..` which should be listed at the very beginning
*   Only digits and letters are used to sort; Digits should come first
*   You can assume that all the files we will test with will have at least one letter or one digit
*   The listing should end with a new line  
    

    ubuntu@ubuntu:~/$ ls -a
    
    .  ..  0-commas  0-commas-checks  1-empty_casks  2-gifs  3-directories  4-zeros  5-rot13  6-odd  7-sort_rot13  Makefile  quote  .test  test_dir  test.var
    
    ubuntu@ubuntu:~/$ ./103-commas
    
    ./, ../, 0-commas, 0-commas-checks/, 1-empty_casks, 2-gifs, 3-directories, 4-zeros, 5-rot13, 6-odd, 7-sort_rot13, Makefile, quote, .test, test_dir/, test.var
    
    ubuntu@ubuntu:~/$
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`103-commas`](/103-commas)

-----
### 19\. File type: School

Advanced

Create a magic file `school.mgc` that can be used with the command `file` to detect `School` data files. `School` data files always contain the string `SCHOOL` at offset 0.

    ubuntu@ip-172-31-63-244:/tmp/magic$ cp /bin/ls .
    ubuntu@ip-172-31-63-244:/tmp/magic$ ls -la
    total 268
    drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 02:44 .
    drwxrwxrwt 11 root   root   139264 Sep 20 02:44 ..
    -rw-r--r--  1 ubuntu ubuntu    496 Sep 20 02:42 school.mgc
    -rwxr-xr-x  1 ubuntu ubuntu 110080 Sep 20 02:43 ls
    -rw-rw-r--  1 ubuntu ubuntu     50 Sep 20 02:06 thisisaschoolfile
    -rw-rw-r--  1 ubuntu ubuntu     30 Sep 20 02:16 thisisatextfile
    ubuntu@ip-172-31-63-244:/tmp/magic$ file --mime-type -m school.mgc *
    school.mgc:         application/octet-stream
    ls:                    application/octet-stream
    thisisaschoolfile: School
    thisisatextfile:       text/plain
    ubuntu@ip-172-31-63-244:/tmp/magic$ file -m school.mgc *
    school.mgc:         data
    ls:                    data
    thisisaschoolfile: School data
    thisisatextfile:       ASCII text
    ubuntu@ip-172-31-63-244:/tmp/magic$
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x00-shell_basics`](https://github.com/jbocane6/holberton-system_engineering-devops/tree/master/0x00-shell_basics)
*   File: [`school.mgc`](/school.mgc)

-----
Copyright © 2022 Holberton Inc, All rights reserved.