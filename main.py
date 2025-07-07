# Импортируем WebDriver для управления браузером
from selenium import webdriver

# Для настройки запуска Chrome (установка драйвера)
from selenium.webdriver.chrome.service import Service as ChromeService

# Для поиска элементов по типам (By.ID и т.д.)
from selenium.webdriver.common.by import By

# Автоматическая загрузка драйвера Chrome
from webdriver_manager.chrome import ChromeDriverManager


# Создаем настройки браузера
options = webdriver.ChromeOptions()

# Предотвращаем закрытие браузера после выполнения скрипта
options.add_experimental_option("detach", True)

# Запускаем Chrome с автоматически установленным драйвером и заданными опциями
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Базовый URL сайта для тестирования
base_url = "http://www.saucedemo.com/"

# Логин и пароль для авторизации
user = "performance_glitch_user"
user_pass = "secret_sauce"

# Открываем сайт в браузере
driver.get(base_url)

# Разворачиваем окно на весь экран
driver.maximize_window()

# Находим поле ввода логина с помощью XPath и вводим имя пользователя
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(user)

# Находим поле ввода пароля с помощью XPath и вводим пароль
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(user_pass)

# Находим кнопку Login с помощью XPath и нажимаем на нее
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
