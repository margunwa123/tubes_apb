# TODO : Import person.py dan semua fungsinya

def start():
  print("Selamat datang di pengolahan file desa ini, silahkan mengetikan salah satu dari komando komando di bawah ini: ")
  printHelp()
  command = input()
  while(command != "exit"):
    if(command == "add"):
      # get inputs for adding person
      # no, nama, rt, rw, email, alamat
      pass
    elif(command == "remove"):
      # get name input to remove person
      pass
    elif(command == "find"):
      # get name input to find person
      pass
    pass

def printHelp():
  # print all available command and its description
  # list of available commands : add -> menambah orang, remove -> menghapus orang, find -> mencari orang
  pass