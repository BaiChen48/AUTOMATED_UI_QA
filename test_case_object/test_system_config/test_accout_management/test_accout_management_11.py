import allure
import pytest

from common.loggerhandler import Logger
from test_case_locator.system_configuration.account_management_locator.account_management_locator import \
    AccountManagementLocator
from test_case_object.conftest import login_driver
from test_case_page.system_configuration.account_management_page import AccountManagementPage

logger = Logger()
# account,name,password,phone,area,role,remark 临时数据 字典
data = {
    "account": "test_account",
    "name": "test_name",
    "password": "test_password",
    "phone": "test_phone",
    "area": "test_area",
    "role": "test_role",
    "remark": "test_remark"
}


@allure.title("删除账号，勾选第一条数据，点击删除按钮")
@allure.feature("账号管理")
# @pytest.mark.skip(reason="")
class TestAccountManagement11():
    """
    勾选第一条数据，点击删除按钮,点击取消确认删除按钮
    """

    def test_account_management_11(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            account_management_page = AccountManagementPage(login_driver)
            account_management_page.account_management_01()
            old_first_account = account_management_page.get_first_account_text()
            account_management_page.account_management_11()
            new_first_account = account_management_page.get_first_account_text()
            assert  old_first_account == new_first_account
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
