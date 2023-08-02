from dotenv import dotenv_values
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time

from pages.xe_coversion_page import XeConversionPage


def _get_env_values() -> dict:
    config = dotenv_values(".env")
    return {**config} if config else None


def _load_init_configs(context):
    env_values = _get_env_values()
    context.xe_conversion_page = XeConversionPage(context)
    if env_values is not None:
        context.WEB_URL = env_values.get("WEB_URL")

    else:
        raise Exception(f"Env file/values are missing")


def before_scenario(context, scenario):
    _load_init_configs(context)
    time.sleep(3)
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    context.browser = driver


def after_scenario(context, scenario):
    context.browser.quit()
