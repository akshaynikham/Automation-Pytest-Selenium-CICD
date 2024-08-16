# Clone this repo into your local

### Step 1: Clone the Repository to Your Local Machine

1. **Open Git Bash** (or any terminal you prefer).
  
2. **Navigate to the Directory** where you want to clone your repository:
  
  ```bash
  cd path/to/your/directory
  ```
  
3. **Clone the Repository** using the GitHub URL:
  
  ```bash
  git clone https://github.com/akshaynikham/Automation-Pytest-Selenium-CICD.git
  ```
  
4. **Navigate into the Cloned Repository**:
  
  ```bash
  cd YourRepository
  ```
  

### Step 2: Open the Project in PyCharm

1. **Open PyCharm**.
2. **Select "Open"** from the Welcome screen.
3. **Navigate to the Cloned Repository**:
  - Browse to the directory where you cloned your repository and select it.
  - Click `OK` to open the project in PyCharm.

### Step 3: Set Up a Virtual Environment in PyCharm

1. **Open the Terminal** in PyCharm (`View` > `Tool Windows` > `Terminal`).
  
2. **Create a Virtual Environment**:
  
  - Run the following command to create a virtual environment:
    
    ```bash
    python -m venv .venv
    ```
    
  - This will create a `.venv` folder in your project directory.
3. **Activate the Virtual Environment**:
  
  - **Windows**:
    
    ```bash
    .venv\Scripts\activate
    ```
    

### Step 4: Install Dependencies

1. **Install Dependencies** from `requirements.txt`:
  
  - Run the following command in the terminal:
    
    ```bash
    pip install -r requirements.txt
    ```
    

### Step 5: Configure the Python Interpreter in PyCharm

1. **Go to Settings**:
  
  - `File` > `Settings` > `Project: YourProjectName` > `Python Interpreter`.
2. **Add Your Virtual Environment**:
  
  - Click the gear icon next to the interpreter list.
  - Choose `Add...` > `Existing environment`.
  - Browse to `.venv/Scripts/python.exe`.
  - Click `OK` and then `Apply` to set this as your interpreter.

### Step 6: Verify Setup and Run Your Tests

1. **Check the Interpreter**:
  
  - Ensure your project is using the virtual environment you set up..
2. **Run Your Tests**:
  
  - Open a test file (e.g., `test_basepage.py`).
  - Right-click on the test file or inside the test function, and select `Run` to execute the tests.
  - Alternatively, you can run `pytest` from the terminal:
    
    ```bash
    pytest
    ```