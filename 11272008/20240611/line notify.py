import requests

rd = requests.post(
        f"https://notify-api.line.me/api/notify",
        headers={"Authorization": f"Bearer {'S6tgP0A2OiKbAZc8xiKa99yXtpJV604P7GVBix2NY73'}"},
        data={"message": f"{'王興集'}"})