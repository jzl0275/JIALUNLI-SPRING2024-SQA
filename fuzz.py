"""
- Due to 4.b, Create a `fuzz.py` file that fuzz 5 Python methods of my choice.
- Due to 4.c, Integrate forensics by modifying 5 Python methods of my choice.
"""
from mining.mining import deleteRepo, dumpContentIntoFile, cloneRepo, checkPythonFile, getPythonFileCount


# fuzz python method 1
def testDeleteRepo():
    deleteRepo('file-will-never-exist', 'NONEXISTENT_DIRECTORY')

# fuzz python method 2
def testDumpContentIntoFile():
    dumpContentIntoFile("test-content", None)

# fuzz python method 3
def testCloneRepo():
    cloneRepo("JIALUNLI-SPRING2024-SQA-not-existing", '/tmp/')

# fuzz python method 4
def testCheckPythonFile():
    checkPythonFile("/path-is-not-existing/something")

# fuzz python method 5
def testGetPythonFileCount():
    getPythonFileCount("/path-is-not-existing/something")
    with open(filename, "w") as f_obj:
        json.dumps(data, f_obj)


if __name__=='__main__':
    # test cases for fuzz python method 1
    try:
        testDeleteRepo()
    except Exception as e:
        print(f"1: testDeleteRepo() Failure for: {type(e).__name__}: {str(e)}")

    # test cases for fuzz python method 2
    try:
        testDumpContentIntoFile()
    except Exception as e:
        print(f"2: testDumpContentIntoFile() Failure for: {type(e).__name__}: {str(e)}")

    # test cases for fuzz python method 3
    try:
        testCloneRepo()
    except Exception as e:
        print(f"3: testCloneRepo() Failure for: {type(e).__name__}: {str(e)}")

    # test cases for fuzz python method 4
    try:
        testCheckPythonFile()
    except Exception as e:
        print(f"4: testCheckPythonFile() Failure for: {type(e).__name__}: {str(e)}")

    # test cases for fuzz python method 5
    try:
        testGetPythonFileCount()
    except Exception as e:
        print(f"5: testGetPythonFileCount() Failure for: {type(e).__name__}: {str(e)}")
