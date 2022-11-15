from unittest import TestCase

from sqlalchemy import inspect
from sqlalchemy.schema import DropConstraint, DropTable, MetaData, Table

from main import app, db


class BaseTestCase(TestCase):
    def setUp(self):
        self.app = app
        self.ctx = self.app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()


class BaseTestCaseWithDatabase(BaseTestCase):
    def setUp(self):
        super().setUp()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        super().tearDown()

    def drop_all_tables(self, db):
        con = db.engine.connect()
        trans = con.begin()
        inspector = inspect(db.engine)

        meta = MetaData()
        tables = []
        all_fkeys = []

        for table_name in inspector.get_table_names():
            fkeys = []

            for fkey in inspector.get_foreign_keys(table_name):
                if not fkey["name"]:
                    continue

                fkeys.append(db.ForeignKeyConstraint((), (), name=fkey["name"]))

            tables.append(Table(table_name, meta, *fkeys))
            all_fkeys.extend(fkeys)

        for fkey in all_fkeys:
            con.execute(DropConstraint(fkey))

        for table in tables:
            con.execute(DropTable(table))

        trans.commit()


class BaseTestCaseWithClient(BaseTestCaseWithDatabase):
    def setUp(self):
        super().setUp()
        self.client = self.app.test_client()
