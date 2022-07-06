# AniRecommender

## What is it and what does it do?
	Have you ever had the problem of having so many anime in your "to watch" list but you always complain that you don't have any anime to watch? This is the problem that AniRecommender is trying to fix. The principle is very simple: if you don't know what anime to watch, it will simply give you a random anime title and then you just watch it. Sometimes the hardest part in starting a new anime is thinking about which one to choose, but having a program decide that for you eliminates that hurdle.

## How do I use it?
	First make sure you have python installed with a version of at least 3.10. On first setup run the getLinuxDependencies.sh script if you're using linux or the getWindowsDependencies.bat file if you are using windows, this will get everything else you need for the program and you only need to run it once. After that you just execute the _main.py_ file as a python script, you can do this from the terminal or cmd by writing "python main.py" whilst in the directory of the program. After that just answer the first prompt with yes/no and the name of a tag in the list if you get the second prompt.

## How does it work?
	Anime information is stored in a _database.json_ file and it stores an anime's title, tags and score. There is also a watched.txt file which stores the title of every anime you finished watching. The program itself is a python script with the name _main.py_ which will ask you if you want to watch an anime with a specific tag. If you answer no, then it will just give you a random title from the database.json file that is not in the watched.txt list, if you answer yes then it will ask you to choose a tag from among a list (such as action, adventure, romance etc.) and it will give you a random title that has that tag. If there are less than 10 titles remaining in the database with a certain tag then the program will automatically scrape the mal website to find 10 more animes that have that tag and are not in the watched.txt file.