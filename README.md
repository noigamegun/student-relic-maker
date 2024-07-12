# student-relic-maker

This program is designed to create "relics" by placing faces on images. It can work with any picture, but the results may be distorted or compressed depending on the original image.

**Disclaimer**: I am not responsible for any damage caused by using this program. Please refer to the license for more information.

## How To Use

### Prerequisites

`python3`: Make sure you have Python installed on your system. You can check by running python --version in your terminal.

`virtualenv`: This tool creates isolated Python environments. Install it using your system's package manager (e.g., sudo apt install python3-venv on Ubuntu).

`git`: This is used to download the program files. Install it using your system's package manager.

## Instructions (Mac & Linux)

### 1. Clone the Repository

```
git clone https://github.com/noigamegun/student-relic-maker.git
cd student-relic-maker
```

This downloads the program files from GitHub and enters the project directory.

### 2. Create a Virtual Environment

```
python3 -m venv ./venv/
```

This creates a virtual environment named venv within the project directory. Virtual environments help isolate project dependencies from your system-wide Python installation.

### 3. Activate the Virtual Environment

```
source ./venv/bin/activate
```

This activates the virtual environment. You should see the name of the virtual environment (e.g. `(venv)`) before your command prompt.

### 4. Install Dependencies

```
pip3 install -r requirements.txt
```

This installs the necessary libraries needed for the program to run.

### 5. Add Your Picture

Place the images you want to use in the `input` directory within the project.

### 6. Run the Program

```
python3 main.py
```

This executes the program.

The processed image will be placed in the `output` directory.
