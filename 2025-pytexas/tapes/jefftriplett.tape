Output "/Users/jefftriplett/Projects/presentations/presentations-git/2025-pytexas/videos/jefftriplett.mp4"

Require echo

Set Theme "Dracula"
Set Shell "bash"
Set FontSize 24
Set Width 1920
Set Height 1080


Type "command claude --allowed-tools 'Bash(git:*) Edit' prompt --print 'Please run git pull and update any movies or series that are missing covers.'" Sleep 2s  Enter

Sleep 60s


Type "git status" Sleep 2s  Enter

Sleep 10s


Type "git diff" Sleep 2s  Enter

Sleep 2s
