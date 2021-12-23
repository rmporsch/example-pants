from pydantic import BaseSettings, SecretStr


class MongoSettings(BaseSettings):
    password: SecretStr
    username: SecretStr
    url: str = "chess.r63pl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    @property
    def db_url(self):
        return f"mongodb+srv://{str(self.username)}:{str(self.password)}@{self.url}"


class CCSettings(BaseSettings):
    mongo: MongoSettings
