# ffuf-outputter
A cleaner way to save your ffuf output - consider combining it with ffuf easily.

# Usage Example
First change the directory in the python file to where you are going to be running the ffuf scan. Instead of "/home/hackershiv/tools/ffuf.json", change to your working directory.

ffuf -u "https://evil.com/FUZZ" -w ~/tools/OneListForAll/onelistforallmicro.txt -o ffuf.json && python3 ~/tools/ffufoutput.py && rm -rf ffuf.json

# Why?
You can just easily click on the URL from your terminal instead of manually typing in your browser and formatted in .json which is messy to read.

If you find yourself using this, please do star and follow me on github ;)

# Donations ❤️
<a href="https://www.buymeacoffee.com/hackshiv" target="_blank"><img src="https://uc18a5d6fa18c7a6e6bcf0c8ac68.previews.dropboxusercontent.com/p/thumb/ACSeWjaYon3DD9ybIl1P0_kUMesC-433mJdEs6lWeL4Ff_4trWI-XsOTC6s3Z6iVNaKRXjVXGhIj3WcJuVMVk1BJDj1EHgJWuk0KfKIV1QcQ8iRJlFbD0WuJAj26Bquqhh65f5_7LlaLRmoBETr8GrXy1CqKeATM49xaGG1WZJKfiwKMUfaBklfajnIwqVMOIxYT7cwKqz39KHsj3OpVpY-vdnRyAhr6R350TFwvTGYJm36Wm3nmH6RjUya1ozVpN07d8Vs4TY0nQguKwqQYhgE_rAXvrQsCSPMAaKGYrNECDE88vnLnRiErq8O1lKsoHZLoo37fg4EBK1vG8SWBr0So/p.png" alt="Buy Me A Coffee" height="41" width="174"></a>

