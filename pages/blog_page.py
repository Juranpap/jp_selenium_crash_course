from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class BlogPage(BasePage):

    slug = "/the-capsized-eight"
    shameless_link_locator = (By.LINK_TEXT, "Shameless")
    technology_link_locator = (By.LINK_TEXT, "Technology")
    topic_label_locator = (By.CLASS_NAME, "__highlight")
    business_link_locator = (By.LINK_TEXT, "Business")

    def navigate_to_page(self):
        self.navigate(self.slug)

    @property
    def shameless_link(self):
        return self.get_present_element(self.shameless_link_locator)

    @property
    def topic_label(self):
        return self.get_present_element(self.topic_label_locator)

    @property
    def technology_link(self):
        return self.get_present_element(self.technology_link_locator)

    @property
    def technology_label(self):
        return self.get_present_element(self.topic_label_locator)

    @property
    def business_link(self):
        return self.get_present_element(self.business_link_locator)

