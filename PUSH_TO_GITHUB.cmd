@echo off
setlocal
cd /d C:\AURA\AURELIS-OPEN-CORE
set GIT_TERMINAL_PROMPT=1
git remote set-url origin https://github.com/alexeyzack-design/aurelis-open-core.git
git status --short
git push -u origin HEAD:main
if errorlevel 1 (
  echo PUSH FAILED - keep the repository local; do not claim publication.
  exit /b 1
)
echo PUSH OK
git ls-remote origin HEAD
endlocal
