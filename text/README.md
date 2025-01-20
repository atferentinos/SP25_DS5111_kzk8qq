# Sprint 2025 Software and Automation Skills
Reading and Lab Instructions for DS5111.

# Linux Command Line

## Reading Assignment:
* [The Linux Command Line, Chapters 1-5](https://learning.oreilly.com/library/view/the-linux-command/9781492071235/)
    - Assigned at a **SKIM LEVEL** (look through the chapters in a 'would I buy this book' level first, then use a resource)
* [Mastering Python For Bioinformatics Appendix A](https://learning.oreilly.com/library/view/mastering-python-for/9781098100872/app01.html#idm45666223879840) (REQUIRED reading, and note that is ONLY Appendix A)

## Linux Command Cheat Sheet
These handfull of commands should be muscle memory and are the foundation for navigating in linux space

| Command | Description |
| -- | -- |
| ls|List directories and files in your current location |
| |`ls -la` is very common.  `l` flag displays details, `a` flag displays hidden directories |
| cd|`cd <location>` to move to a new directory |
| |`cd` by iteslt takes you to home location.  In our cloud server, that is `/home/ubuntu/` |
| |special notation for 'back up one' is `..`, and 'here in this same directory is `.` |
| pwd|present working directory, outputs to screen your current location |
| cat|`cat <filename>` will print the contents of a file to console |
| mkdir|create a directory with `mkdir <dirname>` |
| |If you want to make a nested directory use `mkdir -p <top_directory/middle_directory/target_directory>` |
