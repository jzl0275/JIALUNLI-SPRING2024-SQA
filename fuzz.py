"""Due to 4.b,  Create a `fuzz.py` file that fuzz 5 Python methods of my choice."""

# fuzz python method 1
def divide(v1, v2):
    return v1 / v2

# fuzz python method 2
def open_file(file_path):
    with open(file_path, "r") as f_obj:
        for line in f_obj:
            print(line)

# fuzz python method 3
def write_file(file_path):
    with open(file_path, "w") as f_obj:
        f_obj.write("this is written by fuzz python method 3: write_file")

# fuzz python method 4
def append_file(file_path):
    with open(file_path, "a") as f_obj:
        f_obj.write("this is written by fuzz python method 3: write_file")

# fuzz python method 5
def dump_json_data(data, filename):
    import json
    with open(filename, "w") as f_obj:
        json.dumps(data, f_obj)


if __name__=='__main__':
    # test cases for fuzz python method1
    try:
        divide(3, 1)
    except Exception as e:
        print(f"1: divide() Failure for: {type(e).__name__}: {str(e)}")

    try:
        divide(3, 0)
    except Exception as e:
        print(f"1: divide() Failure for: {type(e).__name__}: {str(e)}")

    try:
        divide(3, "1")
    except Exception as e:
        print(f"1: divide() Failure for: {type(e).__name__}: {str(e)}")

    try:
        divide(3, "0")
    except Exception as e:
        print(f"1: divide() Failure for: {type(e).__name__}: {str(e)}")

    try:
        divide(3, True)
    except Exception as e:
        print(f"1: divide() Failure for: {type(e).__name__}: {str(e)}")

    try:
        divide(3, False)
    except Exception as e:
        print(f"1: divide() Failure for: {type(e).__name__}: {str(e)}")


    # test cases for fuzz python method2
    try:
        open_file("file-will-never-exist")
    except Exception as e:
        print(f"2: open_file() Failure for: {type(e).__name__}: {str(e)}")

    # test cases for fuzz python method3
    try:
        write_file("/tmp/")
    except Exception as e:
        print(f"3: write_file() Failure for: {type(e).__name__}: {str(e)}")

    # test cases for fuzz python method4
    try:
        append_file("/tmp/")
    except Exception as e:
        print(f"4: append_file() Failure for: {type(e).__name__}: {str(e)}")

    # test cases for fuzz python method5
    try:
        data = {
            "team": "JIALUNLI",
            "members": ["Jialun Li", "anyone else"],
        }
        dump_json_data(data, "/tmp/test_file")
    except Exception as e:
        print(f"5: dump_json_data() Failure for: {type(e).__name__}: {str(e)}")

    try:
        data = {
            "team": "JIALUNLI",
            "members": ["Jialun Li", "anyone else"],
        }
        dump_json_data(data, "/tmp/")
    except Exception as e:
        print(f"5: dump_json_data() Failure for: {type(e).__name__}: {str(e)}")
