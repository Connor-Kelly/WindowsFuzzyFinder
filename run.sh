#!/bin/bash
# echo "Started Fuzzy Finder"
# windows=$(./getAllWindows.exe)
# windows=$(python -c 'import getAllWindows; print(getAllWindows())')
# sleep 2
# echo -e $windows

# echo -e $windows | fzf

./selectWindow.exe "$(./getAllWindows.exe | fzf)"