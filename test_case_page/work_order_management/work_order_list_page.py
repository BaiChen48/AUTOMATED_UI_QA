import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from common.base_method import BasePage
from common.loggerhandler import logger
from test_case_locator.system_configuration.account_management_locator.account_management_locator import (
    AccountManagementLocator,
)
from test_case_locator.work_order_management.work_order_list_locator import (
    WorkOrderListLocator,
)


class WorkOrderListPage(BasePage):
    """异常统计页面"""

    # 判断工单管理是否展开
    def _get_work_order_management_is_expand(self):
        return "ant-menu-submenu-open" not in self.get_attribute(
            WorkOrderListLocator.work_order_management_expand_loc, "class"
        )

    # 切换至 工单列表界面
    def switch_to_work_order_list_page(self):
        if self._get_work_order_management_is_expand():
            self.click_element(WorkOrderListLocator.work_order_management_loc)
        self.click_element(WorkOrderListLocator.work_order_list_loc)

    def test_work_order_list_02(self, order_type, name, description):
        self.click_manual_add_work_order_button()
        self.fill_work_order_data(order_type, name, description)
        self.click_element(WorkOrderListLocator.confirm_button_loc)
        time.sleep(0.5)

    # 新增 必填项效验
    def test_work_order_list_03(self):
        self.click_manual_add_work_order_button()
        self.random_sleep(0.5)
        self.click_confirm_button()
        self.random_sleep(0.5)

    # 新增 点击取消按钮
    def test_work_order_list_04_1(self, order_type, name, description):
        time.sleep(0.5)
        self.click_manual_add_work_order_button()
        time.sleep(0.5)
        self.fill_work_order_data(order_type, name, description)
        self.click_element(WorkOrderListLocator.cancel_button_loc)
        self.random_sleep(0.5)

    # 新增 点击x按钮
    @allure.step("新增 点击x按钮")
    def test_work_order_list_04_2(self, order_type, name, description):
        time.sleep(0.5)
        self.click_manual_add_work_order_button()
        time.sleep(0.5)
        self.fill_work_order_data(order_type, name, description)
        self.click_element(WorkOrderListLocator.close_button_loc)

    # 查看详情
    def test_work_order_list_05(self):
        self.click_element(WorkOrderListLocator.first_data_detail_button_loc)
        self.random_sleep(0.5)
        self.click_element(WorkOrderListLocator.detail_close_button_loc)
        self.random_sleep(0.5)

    # 删除 确认删除
    def test_work_order_list_06_1(self):
        self.test_work_order_list_02(
            "巡检工单", "test_work_order_list_06_1", "test_work_order_list_06"
        )
        time.sleep(0.5)
        self.test_case_data_recovered()

    #  删除 取消删除
    def test_work_order_list_06_2(self):
        self.click_first_data_delete_button()
        self.click_element(WorkOrderListLocator.cancel_delete_button_loc)
        self.random_sleep(0.5)

    # 不勾选数据直接点击删除
    def test_work_order_list_07_1(self):
        self.switch_to_work_order_list_page()
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.delete_work_order_loc)

    # 删除数据，点击取消删除按钮
    def test_work_order_list_07_2(self):
        # self.switch_to_work_order_list_page()
        self.click_select_all_button()
        self.click_element(WorkOrderListLocator.delete_work_order_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.cancel_button_loc)

    # 全选 验证
    def test_work_order_list_08_1(self):
        self.switch_to_work_order_list_page()
        time.sleep(0.5)
        self.click_select_all_button()

    # 单选 验证
    def test_work_order_list_08_2(self):
        self.refresh()
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.second_data_checkbox_loc)
        time.sleep(0.5)

    # 搜索功能验证
    # 发布时间 验证
    def test_work_order_list_09_1(self):
        self.switch_to_work_order_list_page()
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.publish_time_expand_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.previous_year_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.previous_month_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.start_time_1_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.next_year_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.next_month_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.end_time_28_button_loc)
        time.sleep(0.5)

    # 处理状态搜索框
    # 未完成
    def test_work_order_list_07_2_unifinished(self):
        self.click_handle_status_button_loc()
        self.random_sleep(0.5)
        self.click_handle_status_unfinished_loc()
        time.sleep(0.5)

    # 已完成
    def test_work_order_list_07_2_finished(self):
        self.click_handle_status_button_loc()
        time.sleep(0.5)
        self.click_handle_status_finished_loc()
        time.sleep(0.5)

    # 工单编号搜索
    @allure.step("输入工单编号查询条件")
    def test_work_order_list_07_3(self, work_order_number):
        self.send_keys_by_clear_and_typing(
            WorkOrderListLocator.work_order_number_input_loc, work_order_number
        )
        time.sleep(0.5)

    # 工单名称搜搜
    @allure.step("输入工单名称查询条件")
    def test_work_order_list_07_4(self, work_order_name):
        self.send_keys(
            WorkOrderListLocator.select_work_order_name_input_loc, work_order_name
        )
        time.sleep(0.5)

    # 关联项目搜索
    def test_work_order_list_07_5(self, project_name):
        self.click_element(WorkOrderListLocator.select_association_project_select_loc)
        self.random_sleep(0.5)
        try:
            # title = "南翔待实施项目"
            self.click_element((By.XPATH, f'//*[@title="{project_name}"]'))
        except:
            logger.error("未找到关联项目")
            return 1

    @allure.step("输入工单类型查询条件")
    def test_work_order_list_07_6(self, order_type):  # 定期标准巡检工单
        self.click_element(WorkOrderListLocator.work_order_type_search_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{order_type}"]'))
        self.random_sleep(0.5)

    @allure.step("获取第一条数据的工单类型")
    def get_first_data_work_order_type(self):
        try:
            return self.text(WorkOrderListLocator.first_data_work_order_type_loc)
        except:
            logger.error("未找到工单类型")
            return 1

    @allure.step("输入计划开始时间查询条件")
    def test_work_order_list_07_7(
        self,
        start_time,
    ):
        self.input_time(start_time, WorkOrderListLocator.plan_start_time_button_loc)

    @allure.step("获取第一个数据的计划开始时间")
    def get_first_data_plan_start_time(self):
        try:
            return self.text(WorkOrderListLocator.first_data_plan_start_time_loc)
        except:
            logger.error("未找到计划开始时间")
            return 1

    @allure.step("获取第二个数据的计划开始时间")
    def get_second_data_plan_start_time(self):
        try:
            return self.text(WorkOrderListLocator.second_data_plan_start_time_loc)
        except:
            logger.error("未找到计划开始时间")
            return 1

    @allure.step("输入计划结束时间查询条件")
    def test_work_order_list_07_8(self, end_time):
        self.input_time(end_time, WorkOrderListLocator.plan_end_time_button_loc)

    @allure.step("获取第一个数据的计划结束时间")
    def get_first_data_plan_end_time(self):
        try:
            return self.text(WorkOrderListLocator.first_data_plan_end_time_loc)
        except:
            logger.error("未找到计划结束时间")
            return 1

    @allure.step("获取第二个数据的计划结束时间")
    def get_second_data_plan_end_time(self):
        try:
            return self.text(WorkOrderListLocator.second_data_plan_end_time_loc)
        except:
            logger.error("未找到计划结束时间")
            return 1

    # 获取计划开始时间搜索框文本
    def get_plan_start_time_text(self):
        return self.get_attribute(
            WorkOrderListLocator.plan_start_time_button_loc, "value"
        )
        # return self.text(WorkOrderListLocator.plan_start_time_button_loc)

    # 获取计划结束时间搜索框文本
    def get_plan_end_time_text(self):
        return self.get_attribute(
            WorkOrderListLocator.plan_end_time_button_loc, "value"
        )
        # return self.text(WorkOrderListLocator.plan_end_time_button_loc)

    # 获取第一条数据的计划开始时间
    def get_first_data_plan_start_time(self):
        return self.text(WorkOrderListLocator.first_data_plan_start_time_loc)

    # 获取第一条数据的计划结束时间
    def get_first_data_plan_end_time(self):
        return self.text(WorkOrderListLocator.first_data_plan_end_time_loc)

    # 获取搜索框工单类型文本
    def get_work_order_type_text(self):
        return self.text(WorkOrderListLocator.work_order_type_loc)

    # 获取第一条数据的工单类型
    def get_first_data_work_order_type_text(self):
        return self.text(WorkOrderListLocator.first_data_work_order_type_loc)

    # 获取关联项目文本
    def get_association_project_text(self):
        return self.text(WorkOrderListLocator.select_association_project_text_loc)

    # 获取第一条数据关联项目文本
    def get_first_data_association_project_text(self):
        return self.text(WorkOrderListLocator.first_data_association_project_loc)

    # 获取第一条数据的处理状态文本
    def get_first_data_handle_status_text(self):
        return self.text(WorkOrderListLocator.first_data_handle_status_loc)

    # # 点击处理状态按钮
    def click_handle_status_button_loc(self):
        self.click_element(WorkOrderListLocator.handle_status_select_loc)

    # 选择 处理状态的未完成按钮
    def click_handle_status_unfinished_loc(self):
        self.click_element(WorkOrderListLocator.handle_status_unfinished_loc)

    # 选择 处理状态的已完成按钮
    def click_handle_status_finished_loc(self):
        self.click_element(WorkOrderListLocator.handle_status_finished_loc)

    # 点击搜索按钮
    def click_search_button(self):
        self.click_element(WorkOrderListLocator.search_button_loc)
        time.sleep(0.5)

    # 点击重置按钮
    def click_reset_button(self):
        self.click_element(WorkOrderListLocator.reset_button_loc)
        time.sleep(1)

    # 点击清除时间按钮
    def click_clear_time_button_loc(self):
        self.move_to_element(WorkOrderListLocator.publish_time_expand_button_loc)
        self.click_element(WorkOrderListLocator.clear_time_button_loc)
        time.sleep(0.5)

    # 获取勾选复选框后的数量显示
    def get_select_number_text(self):
        return self.text(WorkOrderListLocator.checkbox_number_loc)

    # 点击全选按钮
    def click_select_all_button(self):
        self.click_element(WorkOrderListLocator.select_all_loc)
        time.sleep(0.5)

    # 获取第一个工单编号
    @allure.step("获取第一个工单编号")
    def get_first_work_order_number(self):
        try:
            return self.text(WorkOrderListLocator.first_work_order_number_loc)
        except:
            self.logger.info("没有获取到第一个工单编号,返回1")
            return 1

    @allure.step("获取第二个工单编号")
    def get_second_work_order_number(self):
        try:
            return self.text(WorkOrderListLocator.second_work_order_number_loc)
        except:
            self.logger.info("没有获取到第二个工单编号,返回1")
            return 1

    # 获取第一个工单名称
    @allure.step("获取第一个工单名称")
    def get_first_work_order_name(self):
        try:
            return self.text(WorkOrderListLocator.first_data_work_order_name_loc)
        except:
            self.logger.info("没有获取到第一个工单名称,返回1")
            return 1

    @allure.step("获取第二个工单名称")
    def get_second_work_order_name(self):
        try:
            return self.text(WorkOrderListLocator.second_data_work_order_name_loc)
        except:
            self.logger.info("没有获取到第二个工单名称,返回1")
            return 1

    @allure.step("获取第一个工单关联项目 ")
    def get_first_work_order_association_project(self):
        try:
            return self.text(WorkOrderListLocator.first_data_association_project_loc)
        except:
            self.logger.info("没有获取到第一个工单关联项目,返回1")
            return 1

    @allure.step("获取第二个工单关联项目 ")
    def get_second_work_order_association_project(self):
        try:
            return self.text(WorkOrderListLocator.second_data_association_project_loc)
        except:
            self.logger.info("没有获取到第二个工单关联项目,返回1")
            return 1

    @allure.step("获取第一个工单所属区域 ")
    def get_first_work_order_area(self):
        try:
            return self.text(WorkOrderListLocator.first_data_area_loc)
        except:
            self.logger.info("没有获取到第一个工单所属区域,返回1")
            return 1

    @allure.step("输入工作所属区域查询条件")
    def test_work_order_list_07_9(self, work_area):
        self.click_element(WorkOrderListLocator.work_area_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{work_area}"]'))

    # 工单类型必填项验证文本
    def get_work_order_type_required_text(self):
        return self.text(WorkOrderListLocator.work_order_type_select_loc)

    # 工单名称必填项验证文本
    def get_work_order_name_required_text(self):
        return self.text(WorkOrderListLocator.work_order_name_required_loc)

    # 工单描述必填项验证文本
    def get_work_order_description_required_text(self):
        return self.text(WorkOrderListLocator.work_order_description_required_loc)

    # 关联项目必选项验证文本
    def get_association_project_required_text(self):
        return self.text(WorkOrderListLocator.association_project_required_loc)

    # 负责人必选项验证文本
    def get_responsible_person_required_text(self):
        return self.text(WorkOrderListLocator.responsible_person_required_loc)

    # 开始时间必选项验证文本
    def get_plan_start_time_required_text(self):
        return self.text(WorkOrderListLocator.plan_start_time_required_loc)

    # 结束时间必选项验证文本
    def get_plan_end_time_required_text(self):
        return self.text(WorkOrderListLocator.plan_end_time_required_loc)

    # 测试新增数据恢复
    @allure.step("测试新增数据恢复-删除第一条工单数据")
    def test_case_data_recovered(self):
        self.refresh()

        self.click_first_data_delete_button()
        self.click_element(WorkOrderListLocator.confirm_delete_button_loc)
        self.random_sleep(0.5)

    @allure.step("点击删除按钮")
    def click_first_data_delete_button(self):
        self.click_element(WorkOrderListLocator.first_data_delete_button_loc)
        self.random_sleep(0.5)

    # 获取界面提示
    def get_page_tip(self):
        return self.text(WorkOrderListLocator.page_tip_loc)

    # # 选择工单类型
    # def select_work_order_type(self, order_type: str):
    #     self.click_element(WorkOrderListLocator.work_order_type_select_loc)
    #     if order_type == '巡检工单':
    #         self.click_element(WorkOrderListLocator.work_order_type_inspection_loc)
    #     elif order_type == '异常工单':
    #         self.click_element(WorkOrderListLocator.work_order_type_abnormal_loc)
    #     else:
    #         self.click_element(WorkOrderListLocator.work_order_type_other_loc)
    @allure.step("点击新增按钮")
    def click_manual_add_work_order_button(self):
        self.click_element(WorkOrderListLocator.manual_add_work_order_loc)
        time.sleep(0.5)

    @allure.step("点击手工新增工单弹窗的确定按钮")
    def click_confirm_button(self):
        self.click_element(WorkOrderListLocator.confirm_button_loc)
        time.sleep(0.5)

    @allure.step("点击手工新增工单弹窗的取消按钮")
    def click_cancel_button(self):
        self.click_element(WorkOrderListLocator.cancel_button_loc)
        time.sleep(0.5)

    @allure.step("点击手工新增工单弹窗的确定按钮")
    def click_confirm_button_manual(self):
        self.click_element(WorkOrderListLocator.confirm_button_loc)
        time.sleep(0.5)

    # 填写工单数据流程
    @allure.step("填写工单数据")
    def fill_work_order_data(self, order_type, name, description):
        self.click_element(WorkOrderListLocator.work_order_type_select_loc)
        if order_type == "巡检工单":
            self.click_element(WorkOrderListLocator.work_order_type_inspection_loc)
        elif order_type == "异常工单":
            self.click_element(WorkOrderListLocator.work_order_type_abnormal_loc)
        else:
            self.click_element(WorkOrderListLocator.work_order_type_other_loc)
        self.send_keys_by_clear_and_typing(
            WorkOrderListLocator.work_order_name_input_loc, name
        )
        time.sleep(0.5)
        self.send_keys_by_clear_and_typing(
            WorkOrderListLocator.work_order_description_input_loc, description
        )
        time.sleep(0.5)  # 关联项目
        self.click_element(WorkOrderListLocator.association_project_select_loc)
        self.click_element(WorkOrderListLocator.association_project_first_loc)
        time.sleep(0.5)  # 选择负责人
        self.click_element(WorkOrderListLocator.responsible_person_select_loc)
        self.click_element(WorkOrderListLocator.responsible_person_first_loc)
        time.sleep(0.5)  # 计划开始时间
        self.click_element(WorkOrderListLocator.plan_start_time_loc)
        self.click_element(WorkOrderListLocator.plan_start_time_now_loc)
        time.sleep(1)  # 计划结束时间
        self.click_element(WorkOrderListLocator.plan_end_time_loc)
        self.click_element(WorkOrderListLocator.plan_end_time_now_loc)
        time.sleep(0.5)

    # 获取手工新增工单 按钮文本
    def get_manual_add_work_order_text(self):
        return self.text(WorkOrderListLocator.manual_add_work_order_loc)

    # 获取工单类型 系统异常工单元素文本 ，
    def get_system_abnormal_work_order_type_text(self):
        return self.text(WorkOrderListLocator.system_abnormal_work_order_loc)

    # 获取工单类型 手工异常工单元素文本 ，
    def get_manual_abnormal_work_order_type_text(self):
        return self.text(WorkOrderListLocator.manual_abnormal_work_order_loc)

    # 获取工单类型 定期标准巡检工单文本
    def get_regular_standard_inspection_work_order_type_text(self):
        return self.text(
            WorkOrderListLocator.regular_standard_inspection_work_order_loc
        )

    # 获取工单类型 手工标准巡检工单文本
    def get_manual_standard_inspection_work_order_type_text(self):
        return self.text(WorkOrderListLocator.manual_standard_inspection_work_order_loc)

    # 获取工单类型 手工非标巡检工单文本
    def get_manual_non_standard_inspection_work_order_type_text(self):
        return self.text(
            WorkOrderListLocator.manual_non_standard_inspection_work_order_loc
        )

    # 获取工单类型 其他工单文本
    def get_other_work_order_type_text(self):
        return self.text(WorkOrderListLocator.other_work_order_loc)

    # 获取工单类型 实施工单
    def get_implement_work_order_type_text(self):
        return self.text(WorkOrderListLocator.implement_work_order_loc)

    # 获取工单发起人-系统管理员元素文本，把工单发起人也加在方法中，方便调用
    def get_initiator_of_work_order_system_administrator_text(self):
        return self.text(
            WorkOrderListLocator.initiator_of_work_order_system_administrator_loc
        )

    # 获取 处理状态，已完成元素文本
    def get_handle_status_completed_text(self):
        return self.text(WorkOrderListLocator.handle_status_completed_loc)

    @allure.step("获取工单列表界面,工单编号输入框values值")
    def get_work_order_number_input_values(self):
        return self.get_attribute(
            WorkOrderListLocator.work_order_number_input_loc, "value"
        )

    # 2025 1.8 新增  后续再整合优化
    @allure.step('判断弹窗是否存在,//div[@class="ant-modal-mask"]')
    def is_mask_dialog_exist(self):
        try:
            self.visibility_of_element_located(
                WorkOrderListLocator.manual_add_work_order_dialog_mask_loc,
                timeout=5,
                frequency=1,
            )
            return True
        except:
            return False

    @allure.step("获取第一个工单的发起人")
    def get_first_work_order_initiator(self):
        try:
            return self.text(WorkOrderListLocator.first_data_initiator_loc)
        except:
            logger.error("获取第一个工单的发起人失败")
            return 1

    @allure.step("输入工单发起人查询条件")
    def input_work_order_initiator(self, initiator):
        self.click_element(WorkOrderListLocator.initiator_select_loc)
        time.sleep(1)
        # a = self.get_attribute(((By.XPATH,'(//div[@title])[7]')), 'title')
        self.click_element(WorkOrderListLocator.system_administrator_loc)
        # self.click_element((By.XPATH,'(//*[text()= "系统管理员"])[last()]'))
        self.random_sleep(0.5)

    @allure.step("输入工单接受人查询条件")
    def input_work_order_receiver(self, receiver):
        self.click_element(WorkOrderListLocator.receiver_select_loc)
        time.sleep(1)
        # a = self.get_attribute(((By.XPATH,'(//div[@title])[7]')), 'title')
        self.click_element(WorkOrderListLocator.system_administrator_loc)
        # self.click_element((By.XPATH,'(//*[text()= "系统管理员"])[last()]'))
        self.random_sleep(0.5)

    @allure.step("输入工单当前处理人查询条件")
    def input_work_order_current_handler(self, current_handler):
        self.click_element(WorkOrderListLocator.current_processor_select_loc)
        time.sleep(1)
        # a = self.get_attribute(((By.XPATH,'(//div[@title])[7]')), 'title')
        self.click_element(WorkOrderListLocator.system_administrator_loc)
        # self.click_element((By.XPATH,'(//*[text()= "系统管理员"])[last()]'))
        self.random_sleep(0.5)

    @allure.step("获取第一个工单的接受人")
    def get_first_work_order_receiver(self):
        try:
            return self.text(WorkOrderListLocator.first_data_responsible_person_loc)
        except:
            logger.error("获取第一个工单的接受人失败")
            return 1

    @allure.step("获取第一个工单的当前处理人")
    def get_first_work_order_current_handler(self):
        try:
            return self.text(WorkOrderListLocator.first_data_current_handler_loc)
        except:
            logger.error("获取第一个工单的当前处理人失败")
            return 1


    # 获取工单类型 系统异常工单 文本
    def get_work_order_type_search_entered_1_loc_text(self):
        return self.text(WorkOrderListLocator.work_order_type_search_entered_1_loc)

    def get_work_order_type_search_entered_2_loc_text(self):
        return self.text(WorkOrderListLocator.work_order_type_search_entered_2_loc)
