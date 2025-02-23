import allure
from common.loggerhandler import logger
from test_case_page.work_order_management.work_order_list_page import WorkOrderListPage


@allure.feature("工单管理")
@allure.story("工单列表")
@allure.title("工单列表-查看详情")
class TestWorkOrderList05(object):

    @allure.description("工单列表-查看详情")
    def test_work_order_list_05(self, login_driver):
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.test_work_order_list_05()
            assert work_order_list_page.is_mask_dialog_exist() is False
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
