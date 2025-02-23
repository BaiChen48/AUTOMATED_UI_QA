import allure
import pytest
from common.loggerhandler import logger
from test_case_page.operation_and_maintenance_workbench.management_role_page import (
    ManagementRolePage,
)



@allure.feature("运维工作台")
@allure.story("管理角色")
@allure.title("管理角色,任务过程看板切换 周/月")
class TestManagementRole04:

    @allure.description("管理角色,任务过程看板切换 周/月")
    def test_management_role_04(self, login_driver):
        management_role_page = ManagementRolePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            management_role_page.management_role_04_1()
            assert management_role_page.get_week_or_month_assert_text() == "月"
            management_role_page.management_role_04_2()
            assert management_role_page.get_week_or_month_assert_text() == "周"
            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            management_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
