tell application "System Events"
	set listOfProcesses to (name of every process where background only is false)
end tell

set stringOfProceess to listOfProcesses as list


(*
tell application "System Events"
    set listOfProcesses to (name of every process where background only is false)
    tell me to set selectedProcesses to choose from list listOfProcesses with multiple selections allowed
end tell
repeat with processName in selectedProcesses
    do shell script "Killall " & quoted form of processName
end repeat
*)