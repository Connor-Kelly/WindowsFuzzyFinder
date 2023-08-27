#!/bin/bash

windows=$(py getAllWindows.py)
# windows=$(python -c 'import getAllWindows; print(getAllWindows())')

selected=$(echo -e $windows | fzf)



echo "Selected: '" $selected "'"

py selectWindow.py "$selected"