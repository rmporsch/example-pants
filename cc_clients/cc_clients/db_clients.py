import pymongo as pm
from cc_clients.settings import CCSettings
from cc_schemas.chess import Board


class DBClient(object):
    
    def __init__(self, settings: CCSettings):
        self.settings = settings
        self._client = pm.MongoClient(self.settings.mongo.db_url)
        self.db = self._client.get_database("puzzles")

    def add_board(self, board: Board):
        self.db.boards.insert_one(board.dict())