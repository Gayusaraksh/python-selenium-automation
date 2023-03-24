from pages.base_page import Page


class MainPage(Page):

    def open_main(self):
        self.open_url()

    def open_product_page(self):
        self.open_url('gp/product/B074TBCSC8')