import requests
import allure

class ApiClient:
    def __init__(self):
        self.base_url = "https://stellarburgers.nomoreparties.site/api"
        
    @allure.step("Создание нового пользователя через API")
    def create_user(self, email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(f"{self.base_url}/auth/register", json=payload)
        return response.json()
    
    @allure.step("Удаление пользователя через API")
    def delete_user(self, token):
        headers = {"Authorization": token}
        response = requests.delete(f"{self.base_url}/auth/user", headers=headers)
        return response.json()
    
    @allure.step("Авторизация пользователя через API")
    def login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(f"{self.base_url}/auth/login", json=payload)
        return response.json() 