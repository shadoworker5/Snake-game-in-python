from login import *

if __name__ == "__main__":
    start = Login()
    start.bind("<Return>", start.enter)
    start.mainloop()        