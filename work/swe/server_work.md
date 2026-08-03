Working on a server with ssh.

## Screen

Starting a session: `screen`
Starting a named session: `screen -S name`
Detach: `Ctrl+A d`
Show running sessions: `screen -ls`
Reattach: `screen -r`, `screen -r name/id` (either name or id works)
Force reattach: `screen -dr name/id`


## Finding things

### Processes
Main command:
`ps aux`

The `a` means all users, `u` means it will display things like %cpu, %mem, pid, user, `x` means it displays things that are not necessarily attached to a terminal.

### Filtering

Main command:
`grep foo ~/bar.txt`

Prints the lines in `bar.txt` that match the regex pattern `foo`

Commonly used with pipes:
`ps aux | grep python`