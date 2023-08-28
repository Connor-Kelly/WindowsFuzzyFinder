#include <iostream>
// #include <WinUser.h>
// #include <iostream>
#include <Windows.h>
using namespace std;

//  These SW_ constants are used for ShowWindow() and are documented at
//  https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-showwindow#parameters
// const int SW_MINIMIZE = 6;
// const int SW_MAXIMIZE = 3;
// const int SW_HIDE = 0;
// const int SW_SHOW = 5;
// const int SW_RESTORE = 9;
// bool foreachWindow(HWND hWnd, LPARAM lparam) {
// // def foreach_window(hWnd, lParam):
//     if (IsWindowVisible(hWnd) != 0){
//         // windowObjs.append(hWnd)
//         cout << "HWND" << hWnd << endl
//     }
//     return false
// }

// int main()
// {
//     cout << "Hello, world, from Visual C++!" << endl;
//     EnumWindows(foreachWindow, 0)
// }

//  from https://stackoverflow.com/questions/10246444/how-can-i-get-enumwindows-to-list-all-windows

static BOOL CALLBACK enumWindowCallback(HWND hWnd, LPARAM lparam) {
    int length = GetWindowTextLength(hWnd);
    char* buffer = new char[length + 1];
    GetWindowText(hWnd, buffer, length + 1);
    std::string windowTitle(buffer);
    delete[] buffer;

    // List visible windows with a non-empty title
    if (IsWindowVisible(hWnd) && length != 0) {
        printf("%u: %s\n", hWnd, windowTitle.c_str());
        // std::cout << hWnd << ":  " << windowTitle << " | " << lparam << '\n';
    }
    return TRUE;
}

int main() {
    EnumWindows(enumWindowCallback, NULL);
    return 0;
}