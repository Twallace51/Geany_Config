# bash script to find examples for module ....

# Press F5 key now to run and find ....
#ls -lA --color ../../../Demos

cd ../../../Demos
#geany $( egrep -l --recursive "...." --include=*.gny --include=*.py )
geany $(egrep -l --recursive "...." --include=*.py)

