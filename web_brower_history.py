"""
 Browser History (Forward/Backward Navigation):

Scenario:
Imagine you're building a simplified web browser.
Users can navigate to different URLs.
Implement "Back" and "Forward" navigation functionality.
Requirements:
Maintain a stack to track the history of visited URLs.
The "Back" button should pop the current URL and push it onto a "Forward" stack.
The "Forward" button should pop from the "Forward" stack and push it onto the history stack.
Focus:
Simulating real-world user interface behavior.
Managing two stacks for related actions

"""


class WebBrowser:
    def __init__(self):
        self.history=[]
        self.forward=[]

    def visit(self,site):
        self.history.append(site)

    def back(self):
        page=self.history.pop()
        self.forward.append(page)
        return  page
    
    def forwardgo(self):
        page=self.forward.pop()
        self.history.append(page)
        return page

def app():
    web_browser=WebBrowser()
    web_browser.visit("A")
    web_browser.visit("B")
    web_browser.visit("C")
    web_browser.visit("D")
    print(web_browser.back())
    print(web_browser.back())
    print(web_browser.forwardgo())
    print(web_browser.back())
    print(web_browser.forwardgo())
    print(web_browser.forwardgo())
    print(web_browser.back())
    print(web_browser.history)
    


if __name__ == "__main__":
    app()

    

