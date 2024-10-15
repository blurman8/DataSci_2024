results = [["test1", "success", "Monday"],
           ["test2", "success, kind of", "Tuesday"],
           ["test3", "failure, kind of", "Wednesday"],
           ["test4", "failure, utter", "Thursday"]]
# don't do this!
with open('bad_csv.txt', 'wb') as f: 
    for row in results:
        f.write(",".join(map(str, row))) # might have too many commas in it!
        f.write("\n")
