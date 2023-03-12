import pickle
from os import path
import os
import logging

logger = logging.getLogger(__name__)


MAX_RECORDS = os.environ.get('MAX_RECORDS', 10)
FILE = 'data'


class Records:
    records = None
    max_records = MAX_RECORDS

    def __init__(self):
        self.init_from_file()

    def update_limit_if_changed(self, old_limit):
        if old_limit != self.max_records:
            return self.max_records
        return old_limit

    def reset_if_is_full(self):
        if len(self.records) >= self.max_records:
            self.records = []

    def init_from_file(self):
        if not path.isfile(FILE):
            self.records = []
            return
        with open(FILE, 'rb') as f:
            item = pickle.load(f)
            self.records, self.max_records = item['records'], self.update_limit_if_changed(item['max_records'])

    def write(self, item: dict):
        self.reset_if_is_full()
        self.records.append(item)
        return self

    def save(self):
        with open(FILE, 'wb') as f:
            pickle.dump(dict(records=self.records, max_records=self.max_records), f)

