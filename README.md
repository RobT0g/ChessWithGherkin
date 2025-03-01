# ChessWithGherkin
This repository exemplifies the use of a BDD approach for the development of a chess game.

## Pre-requisits
- Have python (at least `v3.11`) installed
- Install dependencies by using `pip install -r reqs.txt`
    - If you are using a virtual environment, you need to activate the environment to be able run the `behave` command; 
    - If you are using the main installation, make sure to add `C:\Users\{User}\AppData\Local\Programs\Python\Python313\Scripts` on PATH;


## Running tests
- Run the command `behave` to run ALL tests. Alternatively you might include:
    - `-f plain` to have a real time report for each step being executed;
    - Path to file (e.g. `Features/pawn_basic.features`) to run a specific `.feature`
- To make changes to the testing setup you can also make changes to `environment.py` by configuring the functions speficied on the [Environmental Controls Documentation Page](https://behave.readthedocs.io/en/stable/tutorial.html#environmental-controls). Functions used on this project are:
    - `after_step` this function is run after each step, I'm using it to refresh the display and add an artificial delay so the steps done on the board are visible. Change this delay length value using the variable `step_latency`;

## Test results
- After running the behave tests, you can see a small report on have many steps, scenarios and features are passed, failed or undefined;
- To look for more test details, you can locate:
    - The folder `reports` (should have been created after running the command). Here you can find `.xml` files for each `.feature` executed showing details for the tests;
    - The file `pretty.output` (also created after running the command). Shows details of the last instance of the command being executed;