on run {cmd}

    if (cmd as string) is equal to "volume up" then
        set volume output volume 80
    end if
    if (cmd as string) is equal to "volume down" then
        set volume output volume 35
    end if
    if (cmd as string) is equal to "light up" then
        tell application "System Events"
            repeat 10 times
                key code 144
            end repeat
        end tell
    end if
    if (cmd as string) is equal to "light down" then
        tell application "System Events"
            repeat 10 times
                key code 145
            end repeat
        end tell
    end if

end run


