class CheckoutPage:
    def __init__(self,page):
        self.page = page


    def fill_information(self, first, last, zipcode):
        self.page.fill("#first-name",first)
        self.page.fill("#last-name",last)
        self.page.fill("#postal-code",zipcode)
        self.page.click("#continue")


    def finish_order(self):
        self.page.click("#finish")