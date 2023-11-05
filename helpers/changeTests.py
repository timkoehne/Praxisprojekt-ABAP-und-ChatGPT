import os

files = [file for file in os.listdir("tests/") if file.endswith(".txt")]
print(files)
for fileName in files:
    newContent = []
    with open("tests/" + fileName, "r") as file:
        content = file.read().splitlines()
        
        for line in content:
            indent = len(line) - len(line.lstrip())
            if "def check" in line:
                newContent.append(line)
                newContent.append(" "*(indent+4) + "passed = 0")
                newContent.append(" "*(indent+4) + "failed = 0")
            elif "assert True" in line:
                # remove assert True
                pass
            elif "assert" in line:
                newContent.append(" "*indent+"try:")
                newContent.append(" "*4 + line)
                newContent.append(" "*(indent+4) + "passed += 1")
                newContent.append(" "*indent+"except (AssertionError, TypeError):")
                newContent.append(" "*(indent+4) + "failed += 1")
            else:
                newContent.append(line)
    newContent.append("    return passed, failed")

    with open("adjustedTests/test" + fileName[:-4] + ".py", "w") as file:
        file.writelines([line +"\n" for line in newContent])
        
