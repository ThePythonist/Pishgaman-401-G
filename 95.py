f = open("words.txt").read().replace("\n", "")
open("One_line.txt", "w").write(f)
