// restoreVal = ctypes.windll.user32.ShowWindow(w._hWnd, SW_RESTORE)
// print(f'restoreVal: {restoreVal}')
// showVal = ctypes.windll.user32.ShowWindow(w._hWnd, SW_SHOW)
// print(f'showVal: {showVal}')
// setFGVal =  ctypes.windll.user32.SetForegroundWindow(w._hWnd)
// print(f'setFGVal: {setFGVal}')
#include <iostream>
// #include <WinUser.h>
// #include <iostream>
#include <Windows.h>
using namespace std;

int  main (int argc, char **argv) {
    if (argc > 1) {
        // parse up to the semicolon
        char *arg = strtok(argv[1], ":");
        int handle = atoi(arg);
        printf("arg: %s, value: %d\n", arg, handle);

        int restoreVal = ShowWindow(reinterpret_cast<HWND>(handle), SW_RESTORE);
        printf("restoreVal: %u\n", restoreVal);
        int showVal = ShowWindow(reinterpret_cast<HWND>(handle), SW_SHOW);
        printf("showVal: %u\n", showVal);
        int setFGVal = SetForegroundWindow(reinterpret_cast<HWND>(handle));
        printf("setFGVal: %u\n", setFGVal);
        // while (arg != NULL)
        // {
        //     printf("%s\n", arg);
        //     arg = strtok(NULL, ":");
        // }
        
    }
    // int i = 0;
    // for (i = 0; i < argc; i++) {
    //     printf("argv[%d] = %s\n", i, argv[i]);
    // }
    return 0;
}