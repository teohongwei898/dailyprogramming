print "(e)nocde to rot13 or (d)ecode to rot13"
option = raw_input()
if option == "e":
    print "Enter plaintext to encode:"
    print raw_input().encode('rot13')
elif option == "d":
    print "Enter plaintext to deecode:"
    print raw_input().decode('rot13')
