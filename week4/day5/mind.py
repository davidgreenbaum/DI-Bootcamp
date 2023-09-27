import curses

def main ():
    curses.initscr()
    
    window = curses.newwin(24, 80, 0, 0)
    
    window.addstr(0, 0, "Welcome to This Moment!")
    
    window.addstr(2, 0, "....take a moment.... take a breath through your nose... relax your shoulders... take another breath.... and then hit space bar to continue....")
    
    window.getch()
    
    window.addstr(2, 0, "List 3 you are witnessing unfold in front of you")
    
    user_response = window.getstr(3, 0)
    
    window.addstr(4, 0, user_response)
    
    window.refresh()
    
    window.getch()
    
    window.close()
    
    curses.endwin()
    
if __name__ == "__main__":
    main()