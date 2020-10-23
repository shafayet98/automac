on run {processName}
    tell application "System Events"
        set listOfProcesses to (name of every process where background only is false)
    end tell
    
    if listOfProcesses contains processName then
        do shell script "Killall " & quoted form of processName
        return processName & " is terminated"
    else
        return "Not a running application"
    end if
    
end run
