import time
import pickle
import os
import platform
import math
import pytest
import allure
import random

from selenium.common.exceptions import *
from faker import Faker
from selenium import webdriver


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


os_name = platform.system()
CMD_CTRL = Keys.COMMAND if os_name == "Darwin" else Keys.CONTROL

fake = Faker()