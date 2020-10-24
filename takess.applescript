property N : 0
set N to N + 1
set picPath to ((POSIX path of (path to desktop)) & "Picture_" & N & ".png") as string
do shell script "screencapture -tjpg " & quoted form of picPath