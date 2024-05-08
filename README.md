# ffuf-outputter
A cleaner way to save your ffuf output - consider combining it with ffuf easily.

# Usage
ffuf -u "https://evil.com/FUZZ" -w ~/tools/OneListForAll/onelistforallmicro.txt -o ffuf.json && python3 ~/tools/ffufoutput.py && rm -rf ffuf.json

# Why?
You can just easily click on the URL from your terminal instead of manually typing in your browser and formatted in .json which is messy to read.

Star if you do like this or find it interesting by using this cleaner way of using ffuf.

