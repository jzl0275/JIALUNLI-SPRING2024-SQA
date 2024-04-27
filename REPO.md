#  Activities and lessons I learned

## 1.Unpack the project MLForensics.zip

I just download `MLForensics.zip` and unzip MLForensics.zip to a target folder

## 2.Upload project as a GitHub repo on github.com. Format of the repo name is TEAMNAME-SPRING2024-SQA

1. I use `git init` command to init the git project in the `/MLForensics-farzana` folder
2. When I use `git commit` command, git prompted me to config my email and username, I do it as instructions
3. I create a repository in github named `JIALUNLI-SPRING2024-SQA`, and follow the instruction to push my local codes


## 3.In your project repo create README.md listing your team name and team members.

I opened the exising `README.md` file and add my team name and team members.

For now, I'm the only member in my team, so I named my team name as my full name.

## 4.Apply the following activities related to software quality assurance

### 4.a. Create a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file is changed and committed.

1. I followed the instruction in `.git/hooks/pre-commit.sample`, mv the file to `pre-commit`
2. I decide to use `bandit` as the tool to check security weaknesses, and add the check command to `pre-conmmit`
3. before I commit, I manually execute the command added to `pre-commit`, and found it works well
4. I add the output csv file to `.gitignore` to avoid add to git repository
5. When I do the git commit command, I found it performs security weaknesses check

### 4.b. Create a fuzz.py file that will automatically fuzz 5 Python methods of your choice. Report any bugs you discovered by the fuzz.py file. fuzz.py will be automatically executed from GitHub actions.

1. I created fuzz 5 Python methods in the `fuzz.py`, and make sure `python fuzz.py` works well
2. I'm trying to make each push will perform `python fuzz.py` in github server, after many times trying, I found the right way to do the github actions

### 4.c. Integrate forensics by modifying 5 Python methods of your choice.

1. I replace 5 methods in `mining/mining.py` in to the `fuzz.py`
2. When I run `python fuzz.py`, I found it need to install `pd`, so I just do it and update the python package into `requirements.txt`

### 4.d. Integrate continuous integration with GitHub Actions.

1. After my commit to git repository, I found the failed with not found `pd` package error, just like my local environment, I know the server should install packages in `requirements.txt`
2. By update the github action config: `pip install -r requirements.txt` before run `python fuzz.py`, I found it works well

## 5.Report my activities and lessons learned. Put the report in your repo as REPO.md

like just what I typed, I fully overviews what I learned today.

It feels great to overcome all the errors and challenges.