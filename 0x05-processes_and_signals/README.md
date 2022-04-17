<p align="center">
    <a href=#><img src="https://raw.githubusercontent.com/jbocane6/logos/main/holberton-logo.png" alt="holberton" /></a></p>
  
  <p align="center">
    <a href="https://twitter.com/juanoso07555284" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juanoso07555284" height="30" width="40" /></a>
  <a href="https://linkedin.com/in/juan-camilo-bocanegra-osorio-18b1821a6" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="juan-camilo-bocanegra-osorio-18b1821a6" height="30" width="40" /></a>
  </p>
  
  <p align="center">
    <a href=#><img src="https://raw.githubusercontent.com/jbocane6/logos/main/titulo2.png" alt="titulo" /></a></p>

0x05. Processes and signals
===========================

About Bash projects
-------------------

Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.

Resources
---------

**Read or watch**:

*   [Linux PID](http://www.linfo.org/pid.html)
*   [Linux process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
*   [Linux signal](https://www.thegeekstuff.com/2012/03/linux-signals-fundamentals/)

**man or help**:

*   `ps`
*   `pgrep`
*   `pkill`
*   `kill`
*   `exit`
*   `trap`

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google**:

### General

*   What is a PID
*   What is a process
*   How to find a process’ PID
*   How to kill a process
*   What is a signal
*   What are the 2 signals that cannot be ignored

Requirements
------------

### General

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted on Ubuntu 20.04 LTS
*   All your files should end with a new line
*   A `README.md` file, at the root of the folder of the project, is Mandatory
*   All your Bash script files must be executable
*   Your Bash script must pass `Shellcheck` (version `0.7.0` via `apt-get`) without any error
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
*   The second line of all your Bash scripts should be a comment explaining what is the script doing

More Info
---------

For those who want to know more and learn about all signals, check out [this article](https://www.computerhope.com/unix/signals.htm).

Tasks
-----

### 0\. What is my PID

Mandatory

Write a Bash script that displays its own PID.

    camilo@home-laptop$ ./0-what-is-my-pid
    4120
    camilo@home-laptop$
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x05-processes_and_signals`](/0x05-processes_and_signals)
*   File: [`0-what-is-my-pid`](0-what-is-my-pid)

-----
### 1\. List your processes

Mandatory

Write a Bash script that displays a list of currently running processes.

Requirements:

*   Must show all processes, for all users, including those which might not have a TTY
*   Display in a user-oriented format
*   Show process hierarchy

Example:

    camilo@home-laptop$ ./1-list_your_processes | head -50
    USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    root         2  0.0  0.0      0     0 ?        S    Feb13   0:00 [kthreadd]
    root         3  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [ksoftirqd/0]
    root         4  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/0:0]
    root         5  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kworker/0:0H]
    root         7  0.0  0.0      0     0 ?        S    Feb13   0:02  \_ [rcu_sched]
    root         8  0.0  0.0      0     0 ?        S    Feb13   0:03  \_ [rcuos/0]
    root         9  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [rcu_bh]
    root        10  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [rcuob/0]
    root        11  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [migration/0]
    root        12  0.0  0.0      0     0 ?        S    Feb13   0:02  \_ [watchdog/0]
    root        13  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [khelper]
    root        14  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kdevtmpfs]
    root        15  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [netns]
    root        16  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [writeback]
    root        17  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kintegrityd]
    root        18  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [bioset]
    root        19  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kworker/u3:0]
    root        20  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kblockd]
    root        21  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [ata_sff]
    root        22  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [khubd]
    root        23  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [md]
    root        24  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [devfreq_wq]
    root        25  0.0  0.0      0     0 ?        S    Feb13   0:41  \_ [kworker/0:1]
    root        27  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [khungtaskd]
    root        28  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kswapd0]
    root        29  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [vmstat]
    root        30  0.0  0.0      0     0 ?        SN   Feb13   0:00  \_ [ksmd]
    root        31  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [fsnotify_mark]
    root        32  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [ecryptfs-kthrea]
    root        33  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [crypto]
    root        45  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kthrotld]
    root        46  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/u2:1]
    root        65  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [deferwq]
    root        66  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [charger_manager]
    root       108  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kpsmoused]
    root       125  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [scsi_eh_0]
    root       126  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/u2:2]
    root       172  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [jbd2/sda1-8]
    root       173  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [ext4-rsv-conver]
    root       409  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [iprt]
    root       549  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kworker/u3:1]
    root       808  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kauditd]
    root       834  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [rpciod]
    root       846  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [nfsiod]
    root         1  0.0  0.4  33608  2168 ?        Ss   Feb13   0:00 /sbin/init
    root       373  0.0  0.0  19472   408 ?        S    Feb13   0:00 upstart-udev-bridge --daemon
    root       378  0.0  0.2  49904  1088 ?        Ss   Feb13   0:00 /lib/systemd/systemd-udevd --daemon
    root       518  0.0  0.1  23416   644 ?        Ss   Feb13   0:00 rpcbind
    statd      547  0.0  0.1  21536   852 ?        Ss   Feb13   0:00 rpc.statd -L
    camilo@home-laptop$
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x05-processes_and_signals`](/0x05-processes_and_signals)
*   File: [`1-list_your_processes`](1-list_your_processes)

-----
### 2\. Show your Bash PID

Mandatory

Using your previous exercise command, write a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.

Requirements:

*   You cannot use `pgrep`
*   The third line of your script must be `# shellcheck disable=SC2009` (for more info about ignoring `shellcheck` error [here](/rltoken/BYXAGPH5zbPpsqIR84ndFQ "here"))

Example:

    camilo@home-laptop$ camilo@home-laptop$ ./2-show_your_bash_pid
    camilo   4404  0.0  0.7  21432  4000 pts/0    Ss   03:32   0:00          \_ -bash
    camilo   4477  0.0  0.2  11120  1352 pts/0    S+   03:40   0:00              \_ bash ./2-show_your_bash_PID
    camilo   4479  0.0  0.1  10460   912 pts/0    S+   03:40   0:00                  \_ grep bash
    camilo@home-laptop$ 
    

Here we can see that my Bash PID is `4404`.

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x05-processes_and_signals`](/0x05-processes_and_signals)
*   File: [`2-show_your_bash_pid`](2-show_your_bash_pid)

-----
### 3\. Show your Bash PID made easy

Mandatory

Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

Requirements:

*   You cannot use `ps`

Example:

    camilo@home-laptop$ ./3-show_your_bash_pid_made_easy
    4404 bash
    4555 bash
    camilo@home-laptop$ ./3-show_your_bash_pid_made_easy
    4404 bash
    4557 bash
    camilo@home-laptop$ 
    

Here we can see that:

*   For the first iteration: `bash` PID is `4404` and that the `3-show_your_bash_pid_made_easy` script PID is `4555`
*   For the second iteration: `bash` PID is `4404` and that the `3-show_your_bash_pid_made_easy` script PID is `4557`

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x05-processes_and_signals`](/0x05-processes_and_signals)
*   File: [`3-show_your_bash_pid_made_easy`](3-show_your_bash_pid_made_easy)

-----
### 4\. To infinity and beyond

Mandatory

Write a Bash script that displays `To infinity and beyond` indefinitely.

Requirements:

*   In between each iteration of the loop, add a `sleep 2`

Example:

    camilo@home-laptop$ ./4-to_infinity_and_beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    ^C
    camilo@home-laptop$ 
    

Note that I `ctrl+c` (killed) the Bash script in the example.

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x05-processes_and_signals`](/0x05-processes_and_signals)
*   File: [`4-to_infinity_and_beyond`](4-to_infinity_and_beyond)

-----
### 5\. Don't stop me now!

Mandatory

We stopped our `4-to_infinity_and_beyond` process using `ctrl+c` in the previous task, there is actually another way to do this.

Write a Bash script that stops `4-to_infinity_and_beyond` process.

Requirements:

*   You must use `kill`

Terminal #0

    camilo@home-laptop$ ./4-to_infinity_and_beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    Terminated
    camilo@home-laptop$ 
    

Terminal #1

    camilo@home-laptop$ ./5-dont_stop_me_now 
    camilo@home-laptop$ 
    

I opened 2 terminals in this example, started by running my `4-to_infinity_and_beyond` Bash script in terminal #0 and then moved on terminal #1 to run `5-dont_stop_me_now`. We can then see in terminal #0 that my process has been terminated.

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x05-processes_and_signals`](/0x05-processes_and_signals)
*   File: [`5-dont_stop_me_now`](5-dont_stop_me_now)

-----
### 6\. Stop me if you can

Mandatory

Write a Bash script that stops `4-to_infinity_and_beyond` process.

Requirements:

*   You cannot use `kill` or `killall`

Terminal #0

    camilo@home-laptop$ ./4-to_infinity_and_beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    Terminated
    camilo@home-laptop$ 
    

Terminal #1

    camilo@home-laptop$ ./6-stop_me_if_you_can
    camilo@home-laptop$ 
    

I opened 2 terminals in this example, started by running my `4-to_infinity_and_beyond` Bash script in terminal #0 and then moved on terminal #1 to run `6-stop_me_if_you_can`. We can then see in terminal #0 that my process has been terminated.

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x05-processes_and_signals`](/0x05-processes_and_signals)
*   File: [`6-stop_me_if_you_can`](6-stop_me_if_you_can)

-----
### 7\. Highlander

Mandatory

Write a Bash script that displays:

*   `To infinity and beyond` indefinitely
*   With a `sleep 2` in between each iteration
*   `I am invincible!!!` when receiving a `SIGTERM` signal

Make a copy of your `6-stop_me_if_you_can` script, name it `67-stop_me_if_you_can`, that kills the `7-highlander` process instead of the `4-to_infinity_and_beyond` one.

Terminal #0

    camilo@home-laptop$ ./7-highlander
    To infinity and beyond
    To infinity and beyond
    I am invincible!!!
    To infinity and beyond
    I am invincible!!!
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    I am invincible!!!
    To infinity and beyond
    ^C
    camilo@home-laptop$ 
    

Terminal #1

    camilo@home-laptop$ ./67-stop_me_if_you_can 
    camilo@home-laptop$ ./67-stop_me_if_you_can
    camilo@home-laptop$ ./67-stop_me_if_you_can
    camilo@home-laptop$ 
    

I started `7-highlander` in Terminal #0 and then run `67-stop_me_if_you_can` in terminal #1, for every iteration we can see `I am invincible!!!` appearing in terminal #0.

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x05-processes_and_signals`](/0x05-processes_and_signals)
*   File: [`7-highlander`](7-highlander)

-----
### 8\. Beheaded process

Mandatory

Write a Bash script that kills the process `7-highlander`.

Terminal #0

    camilo@home-laptop$ ./7-highlander 
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    Killed
    camilo@home-laptop$ 

Terminal #1

    camilo@home-laptop$ ./8-beheaded_process
    camilo@home-laptop$ 
    
I started `7-highlander` in Terminal #0 and then run `8-beheaded_process` in terminal #1 and we can see that the `7-highlander` has been killed.

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x05-processes_and_signals`](/0x05-processes_and_signals)
*   File: [`8-beheaded_process`](8-beheaded_process)

-----
### 9\. Process and PID file

Advanced

Write a Bash script that:

*   Creates the file `/var/run/myscript.pid` containing its PID
*   Displays `To infinity and beyond` indefinitely
*   Displays `I hate the kill command` when receiving a SIGTERM signal
*   Displays `Y U no love me?!` when receiving a SIGINT signal
*   Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/d8ecfe9109334898b9540ffd20cf64d1c06f0c09.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220417%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220417T024056Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c8a9a79cfce9aee4923bc4a7c4ab6870bb82d5b7fbd1c1ba51161c87eefe9e53)

    camilo@home-laptop$ sudo ./100-process_and_pid_file
    To infinity and beyond
    To infinity and beyond
    ^CY U no love me?!
    

Executing the `100-process_and_pid_file` script and killing it with `ctrl+c`.

Terminal #0

    camilo@home-laptop$ sudo ./100-process_and_pid_file
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    To infinity and beyond
    I hate the kill command
    camilo@home-laptop$ 
    

Terminal #1

    camilo@home-laptop$ sudo pkill -f 100-process_and_pid_file
    camilo@home-laptop$     

Starting `100-process_and_pid_file` in the terminal #0 and then killing it in the terminal #1.

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x05-processes_and_signals`](/0x05-processes_and_signals)
*   File: [`100-process_and_pid_file`](100-process_and_pid_file)

-----
### 10\. Manage my process

Advanced

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/37975393ead381f4d27f268f7337c6d3013b4991.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220417%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220417T024056Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4a849ee7ace772734afc7e8be020ea0061c7b32694bbbca2e626e83ee212cbca)

Read:

*   [&](https://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html)
*   [init.d](https://www.ghacks.net/2009/04/04/get-to-know-linux-the-etcinitd-directory/)
*   [Daemon](https://en.wikipedia.org/wiki/Daemon_%28computing%29)
*   [Positional parameters](https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html)

man: `sudo`

Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: `start`, `restart` and `stop`. The most popular way of doing so on Unix system is to use the init scripts.

Write a `manage_my_process` Bash script that:

*   Indefinitely writes `I am alive!` to the file `/tmp/my_process`
*   In between every `I am alive!` message, the program should pause for 2 seconds

Write Bash (init) script `101-manage_my_process` that manages `manage_my_process`. (both files need to be pushed to git)

Requirements:

*   When passing the argument `start`:
    *   Starts `manage_my_process`
    *   Creates a file containing its PID in `/var/run/my_process.pid`
    *   Displays `manage_my_process started`
*   When passing the argument `stop`:
    *   Stops `manage_my_process`  
        
    *   Deletes the file `/var/run/my_process.pid`
    *   Displays `manage_my_process stopped`
*   When passing the argument `restart`
    *   Stops `manage_my_process`  
        
    *   Deletes the file `/var/run/my_process.pid`
    *   Starts `manage_my_process`
    *   Creates a file containing its PID in `/var/run/my_process.pid`
    *   Displays `manage_my_process restarted`
*   Displays `Usage: manage_my_process {start|stop|restart}` if any other argument or no argument is passed

Note that this init script is far from being perfect (but good enough for the sake of manipulating process and PID file), for example we do not handle the case where we check if a process is already running when doing `./101-manage_my_process start`, in our case it will simply create a new process instead of saying that it is already started.

    camilo@home-laptop$ sudo ./101-manage_my_process
    Usage: manage_my_process {start|stop|restart}
    camilo@home-laptop$ sudo ./101-manage_my_process start
    manage_my_process started
    camilo@home-laptop$ tail -f -n0 /tmp/my_process 
    I am alive!
    I am alive!
    I am alive!
    I am alive!
    ^C
    camilo@home-laptop$ sudo ./101-manage_my_process stop
    manage_my_process stopped
    camilo@home-laptop$ cat /var/run/my_process.pid 
    cat: /var/run/my_process.pid: No such file or directory
    camilo@home-laptop$ tail -f -n0 /tmp/my_process 
    ^C
    camilo@home-laptop$ sudo ./101-manage_my_process start
    manage_my_process started
    camilo@home-laptop$ cat /var/run/my_process.pid 
    11864
    camilo@home-laptop$ sudo ./101-manage_my_process restart
    manage_my_process restarted
    camilo@home-laptop$ cat /var/run/my_process.pid 
    11918
    camilo@home-laptop$ tail -f -n0 /tmp/my_process 
    I am alive!
    I am alive!
    I am alive!
    ^C
    camilo@home-laptop$ 
    

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x05-processes_and_signals`](/0x05-processes_and_signals)
*   File: [`101-manage_my_process, manage_my_process`](101-manage_my_process, manage_my_process)

-----
### 11\. Zombie

Advanced

[![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/255/C6mO7b3.jpg)](http://fineartamerica.com/featured/zombie-seahorse-lauren-b.html)

Read [what a zombie process is](https://zombieprocess.wordpress.com/what-is-a-zombie-process/).

Write a C program that creates 5 zombie processes.

Requirements:

*   For every zombie process created, it displays `Zombie process created, PID: ZOMBIE_PID`
*   Your code should use the Betty style. It will be checked using `betty-style.pl` and `betty-doc.pl`
*   When your code is done creating the parent process and the zombies, use the function bellow

Example:

    int infinite_while(void)
    {
        while (1)
        {
            sleep(1);
        }
        return (0);
    }
    

Example:

Terminal #0

    camilo@home-laptop$ gcc 102-zombie.c -o zombie
    camilo@home-laptop$ ./zombie 
    Zombie process created, PID: 13527
    Zombie process created, PID: 13528
    Zombie process created, PID: 13529
    Zombie process created, PID: 13530
    Zombie process created, PID: 13531
    ^C
    camilo@home-laptop$
    

Terminal #1

    camilo@home-laptop$ ps aux | grep -e 'Z+.*<defunct>'
    camilo  13527  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
    camilo  13528  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
    camilo  13529  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
    camilo  13530  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
    camilo  13531  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
    camilo  13533  0.0  0.1  10460   964 pts/2    S+   01:19   0:00 grep --color=auto -e Z+.*<defunct>
    camilo@home-laptop$ 
    

In Terminal #0, I start by compiling `102-zombie.c` and executing `zombie` which creates 5 zombie processes. In Terminal #1, I display the list of processes and look for lines containing `Z+.*<defunct>` which catches zombie process.

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x05-processes_and_signals`](/0x05-processes_and_signals)
*   File: [`102-zombie.c`](102-zombie.c)

-----
### 12\. Screencast

Advanced

Now that you have mastered signals, how about sharing your knowledge?

Create a screencast where you live-code/demo something related to Unix signals.

Requirements:

*   Step by step video
*   Two minutes of above
*   Done in English
*   Published to Youtube

While you are free to choose the recording system to record the screencast, I highly recommend [screencast-o-matic](https://screencast-o-matic.com). (Only for Windows & Mac)

If you are using Linux, you can have a look at [Kazam](https://launchpad.net/kazam).

Once you are done, please share the Youtube URL in your answer file and below.

We’ll be watching you!

![](https://media.giphy.com/media/l0MYEI1kqBRBrpEdO/giphy.gif)

Depending on what you do, we could even get your video published in a technical publication, reach out to me if you are interested.

Please, remember that these blogs must be recorded in English to further your technical ability in a variety of settings.

**It is your responsibility to request a review for your video from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.**

**Repo:**

*   GitHub repository: [`holberton-system_engineering-devops`](https://github.com/jbocane6/holberton-system_engineering-devops)
*   Directory: [`0x05-processes_and_signals`](/0x05-processes_and_signals)
*   File: [`103-screencast_unix_signal`](103-screencast_unix_signal)

-----
Copyright © 2022 Holberton Inc, All rights reserved.