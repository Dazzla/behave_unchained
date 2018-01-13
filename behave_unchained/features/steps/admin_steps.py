from behave import *
from behave_unchained.features import environment
from behave_unchained.features.lib.pages.admin_page import AdminPage
from behave_unchained.features.lib.pages.object_admin_page import AdminDashboard
from behave_unchained.features.lib.pages.questions_admin_page import QuestionsAdminPage
from behave_unchained import passwords

use_step_matcher("re")


@step("I am logged in as an administrator")
def step_impl(context):
    admin_page = AdminPage(context)
    admin_page.visit(environment.ADMIN_URL)
    admin_page.log_in(environment.ADMIN_USERNAME, passwords.ADMIN_PASSWORD)
    assert(admin_page.is_logged_in())


@step("I(?: can)? access polls admin")
def step_impl(context):
    object_admin = AdminDashboard(context)
    object_admin.visit(environment.ADMIN_URL + 'polls')
    assert (object_admin.is_displayed())


@step("I(?: can)? access questions admin")
def step_impl(context):
    object_admin = AdminDashboard(context)
    object_admin.access_question_admin_page()
    questions_admin = QuestionsAdminPage(context)
    assert(questions_admin.is_displayed())
