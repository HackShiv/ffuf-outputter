# ffuf-outputter
A cleaner way to save your ffuf output - consider combining it with ffuf easily.

# Usage Example
First change the directory in the python file to where you are going to be running the ffuf scan. Instead of "/home/hackershiv/tools/ffuf.json", change to your working directory.

ffuf -u "https://evil.com/FUZZ" -w ~/tools/OneListForAll/onelistforallmicro.txt -o ffuf.json && python3 ~/tools/ffufoutput.py && rm -rf ffuf.json

# Why?
You can just easily click on the URL from your terminal instead of manually typing in your browser and formatted in .json which is messy to read.

Star if you do like this or find it interesting by using this cleaner way of using ffuf.

