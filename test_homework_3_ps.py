from time import sleep

import pytest

name = "Bob Boss"


@pytest.fixture
def visit_site(py):
    py.visit("http://hrm-online.portnov.com/symfony/web/index.php/auth/login")


@pytest.fixture
def login(py):
    py.get("#txtUsername").type("admin")
    py.get("#txtPassword").type("password")
    py.get("#btnLogin").click()


def test_successful_enter(py, visit_site, login):
    welcome_text = py.webdriver.find_element_by_id("welcome").text
    assert welcome_text == "Welcome Admin"


def test_select_bob_boss(py, visit_site, login):
    py.get("#empsearch_supervisor_name").type(name)
    py.get("#empsearch_job_title").select("QA Lead")
    py.get("#searchBtn").click()
    py.getx("//a[contains(text(),'774863')]").click()


    resume_field = py.webdriver.find_element_by_id("employeeAttachmentDelete__csrf_token")
    if resume_field.is_displayed():
        print("Mr '{0}' still  have resume".format(name))
    else:
        print("Mr '{0}' still doesn't have resume".format(name))
