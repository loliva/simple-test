# export URL="http://localhost"
import os
from locust import HttpUser, task, between

class RandomUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_random_number(self):
        url = os.environ.get('URL', 'localhost')
        headers = {"Host": url,}
        self.client.get('/random_number', headers=headers)

    @task
    def get_random_string(self):
        url = os.environ.get('URL', 'localhost')
        headers = {"Host": url}
        self.client.get('/random_string', headers=headers)