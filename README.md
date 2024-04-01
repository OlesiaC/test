# Test Automation Project
A small project with couple UI and API tests written in Python

### API tests

   Swagger API documentation: https://reqres.in/
 - HOST
    ```
    https://reqres.in/
    ```

### UI tests
    
   Awara Matrasses and Bedding: https://awarasleep.com/
 - HOST
    ```
    https://qa.awarasleep.com/
    ```


### Requirements

- Install dependencies from .toml file:

    ```
    poetry install
    ```
- Activate virtual environment:

    ```
    poetry shell
    ```
- Install playwright dependencies:

    ```
    poetry run playwright install
    ```


### Local run options

- Local run for tagged as matching test:
  ```
  pytest -m mark -sv
  ```  
- Local run with browser UI:
  ```
  DEBUG=1 pytest -sv