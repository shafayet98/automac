on run {processName}
    set appName to processName
    set startIt to false
    tell application "System Events"
        if not (exists process appName) then
            set startIt to true
        else if frontmost of process appName then
            set visible of process appName to false
        else
            set frontmost of process appName to true
        end if
    end tell
    if startIt then
        tell application appName to activate
    end if
end run