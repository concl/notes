[[Web Scraping]], [[Regex]]


## subprocess

Automates commands ran from the terminal

Main Syntax:

```
proc = subprocess.run(args, stdin=None, stdout=None, stderr=None, capture_output=False, cwd=None, env=None) # args are a list of strings that denote the cli command and inputs. kwargs are defaults
```

- stdin, stdout, (and stderr) are the file handles for each of them respectively
- capture_output allows the stdout and stderr to be captured when the subprocess terminates.

This function is a high level convenience function that blocks the current thread until the subprocess terminates, and returns a `CompletedProcess` instance.

If capture_output is True, then the `CompletedProcess` has the attributes `stdout` and `stderr` which are strings that contain the captured data.