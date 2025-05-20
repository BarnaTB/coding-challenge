# Coding Challenge Submission
This submission contains solutions and unit tests for the three provided problem sets, with comments to provide further clarity.

## Running the Code and Tests
### Prerequisites:
- Python 3.x installed.

### No External Dependencies:
- This code uses only standard Python libraries (unittest, collections.abc, sys). No requirements.txt or dependency manifest is needed.
### Execution:
- Open your terminal or command prompt.
- Navigate to the directory where you saved the file.
- Open the map_specialties.py file in a text editor or IDE.
- Run the script using the Python interpreter: `python map_specialties.py`
- The script will execute and print the results of the mapping process. You can modify the input data in the script to test different scenarios.
- Run the test file using the Python interpreter: `python tests.py`
- The unit tests will automatically run. Output indicating test results and any warnings about malformed specialty data (if present in tests) will be printed.

## Scalability Considerations
### How might you extend your solution to process tens of millions of elements in the list of IDs? The list of specialities? Both?
- **For tens of millions of IDs**, we could consider the following strategies:
  - Using a generator to yield IDs one at a time instead of loading them all into memory at once. This would allow you to process large lists without running into memory issues.
  - Streaming/Iterative Processing for IDs: Instead of loading all IDs into memory at once, process them in chunks or as a stream. Read IDs from a file, database, or message queue in batches. This keeps memory usage for IDs constant and low.
- **For tens of millions of Specialties**, we could consider:
  - Using a more efficient data structure, such as a dataframe or a hash table, to store and look up specialties. This would allow for faster lookups and reduce the time complexity of the solution.
  - Using a database, key-value stores, or distributed system to store and query the specialties, allowing for horizontal scaling.
  - Parallel Processing: If the list of specialities is extremely large, consider using parallel processing techniques (e.g., multiprocessing in Python) to distribute the workload across multiple CPU cores or machines.
- **For tens of millions of both IDs and Specialties**, we could consider:
  - **Streaming IDs:** IDs must be processed as a stream or in batches to manage memory.
  - **External Data Store for Specialties:** The large specialty list must be stored in an external database or key-value store, indexed for efficient querying.
  - **Batching Lookups:** If the external data store supports it efficiently (e.g., SELECT ... WHERE id IN (id1, id2, ...) in SQL), process IDs in batches and perform batch lookups to reduce I/O overhead and network latency compared to one-by-one queries.
  - **Distributed Computing (For Extreme Scale/Performance):**
    - If the scale grows even larger or processing speed is paramount, frameworks like Apache Spark or Dask become relevant.
    - IDs and specialties could be loaded into distributed data structures (e.g., DataFrames).
    - ETL Transformations (cleaning IDs) and joins (matching IDs to specialties) can be performed in parallel across a cluster of machines. This is a significant architectural shift but offers maximum scalability.
