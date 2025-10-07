Output /Users/jefftriplett/Projects/presentations/presentations-git/2025-pytexas/videos/upgradedjango-dot-com.mp4

Require echo

Set Theme "Dracula"
Set Shell "bash"
Set FontSize 24
Set Width 1920
Set Height 1080


Type "command claude --allowed-tools 'Bash(git:*) Edit' prompt --print 'Please read https://www.djangoproject.com/weblog/2025/oct/01/security-releases/ and then update our Django 5.2, 5.1, and 4.2 files.'" Sleep 2s  Enter

Sleep 60s


Type "git status" Sleep 2s  Enter

Sleep 10s


Type "git diff data/releases/5.2.json" Sleep 2s  Enter

Sleep 2s
