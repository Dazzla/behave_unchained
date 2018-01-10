from behave import *
from behave_unchained.features import environment
from behave_unchained.features.lib.pages.admin_page import AdminPage
from behave_unchained.features.lib.pages.object_admin_page import ObjectAdminPage
from behave_unchained import passwords

use_step_matcher("re")

@step("I am logged in as an administrator")
def step_impl(context):
    admin_page = AdminPage(context)
    admin_page.visit(environment.ADMIN_URL)
    admin_page.log_in(environment.ADMIN_USERNAME, passwords.ADMIN_PASSWORD)
    assert(admin_page.is_logged_in())


@step("I access (?P<object_type>\w+) admin")
def step_impl(context, object_type):
    object_admin = ObjectAdminPage(context)
    object_admin.visit(environment.ADMIN_URL + object_type)
    assert (object_admin.is_displayed())
