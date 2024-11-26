# cintel-06-custom

## Module 6

1. clone git repo using `git clone [url]`

2. create a virtual environment using `py -m venv .venv`

## Run Locally - Initial Start

After cloning your project down to your Documents folder, open the project folder for editing in VS Code.

Create a local project virtual environment named .venv, activate it, and install the requirements.

When VS Code asks to use it for the workspace, select Yes.
If you miss the window, after installing, select from the VS Code menu, View / Command Palette, and type "Python: Select Interpreter" and select the .venv folder.

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands (for Windows - the activate command is slightly different Linux/Mac).

```shell
py -m venv .venv
.venv\Scripts\Activate
py -m pip install --upgrade pip setuptools
py -m pip install --upgrade -r requirements.txt
```

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands.

```shell
shiny run --reload --launch-browser dashboard/app.py
```

Open a browser to <http://127.0.0.1:8000/> and test the app.

## Run Locally - Subsequent Starts

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands.

```shell
.venv\Scripts\Activate
shiny run --reload --launch-browser dashboard/app.py
```

## After Making Changes, Export to Docs Folder

Export to docs folder and test GitHub Pages locally.

Open a terminal (VS Code menu "Terminal" / "New Terminal") in the root project folder and run these commands.

```shell
.venv\Scripts\Activate
shiny static-assets remove
shinylive export dashboard docs
py -m http.server --directory docs --bind localhost 8008
```

Open a browser to <http://[::1]:8008/> and test the Pages app.

## Push Changes back to GitHub

Open a terminal (VS Code menu "Terminal" / "New Terminal") in the root project folder and run these commands.

```shell
git add .
git commit -m "Useful commit message"
git push -u origin main
```

## Enable GitHub Pages (One-Time)

Go to your GitHub repository settings. 
Scroll down to the Pages tab.
Enable GitHub Pages from the **main** branch and from the **docs** folder and click Save.
Wait to see what you new URL is for the hosted app.

When it's ready, go to the About section of your GitHub repo and set the URL to your GitHub Pages site.