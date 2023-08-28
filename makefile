files = getAllWindows.cpp
CPPFLAGS = -I$(PUBLIC_DIR)/include
CFLAGS = -g -Wall -Wextra -Werror

LANG = gcc

all:
	g++ -Wall -Wextra getAllWindows.cpp -o getAllWindows
	g++ -Wall -Wextra selectWindow.cpp -o selectWindow


help:
	echo "Figuire it out bro"

clean: 
	rm getAllWindows.exe