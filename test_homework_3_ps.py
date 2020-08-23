from time import sleep

import pytest


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
    py.get("#empsearch_supervisor_name").type("Bob Boss")
    py.get("#empsearch_job_title").select("QA Lead")
    py.get("#searchBtn").click()
    py.getx("//a[contains(text(),'774863')]").click()
    sleep(5)
