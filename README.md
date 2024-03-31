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



### Local run options

- Local run for tagged as matching test:
  ```
  pytest -m mark -sv
  ```  
- Local run with browser UI:
  ```
  DEBUG=1 pytest -sv