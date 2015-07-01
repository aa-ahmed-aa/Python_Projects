
while True:
    try:
        asd= int(input("what is your fav number? \n"))
        print(18/asd)
    except ValueError:
        print("make sure and enter a number !!")
    except ZeroDivisionError:
        print("Pick another number 5er Zero !!")
    except:
        break
    finally:
        print("loop complete")