from locust import HttpUser, task, between

class RandomUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_random_number(self):
        self.client.get('/random_number')

    @task
    def get_random_string(self):
        self.client.get('/random_string')
