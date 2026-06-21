from beancount.core import data
from beancount.core.amount import Amount
from beangulp.importers import csvbase


class Categorizer:

    def __call__(self, txn, row):
        concepte = (row[2] or "").upper()
        if "DEL MOLINO" in concepte:
            return self._categorize_molino(txn)
        return txn

    @staticmethod
    def _categorize_molino(txn):
        # Example: add a tag to the transaction
        # txn = txn._replace(tags=frozenset(set(txn.tags) | {"Dinar"}))
        txn = txn._replace(narration="Dinar")
        amount = txn.postings[0].units
        txn.postings.append(
            data.Posting(
                "Expenses:Restaurants",
                Amount(-amount.number, amount.currency),
                None, None, None, None,
            )
        )
        return txn


class Importer(csvbase.Importer):

    encoding = "utf8"
    skiplines = 7
    names = True
    order = csvbase.Order.DESCENDING

    date = csvbase.Date("DATA D'OPERACIÓ", frmt="%d/%m/%Y")
    payee = csvbase.Column("CONCEPTE")
    narration = csvbase.Column(0)
    amount = csvbase.Amount("IMPORT", subs={",": "."})
    balance = csvbase.Amount("SALDO", subs={",": "."})

    def __init__(self, account, categorizer=None):
        super().__init__(account, "EUR")
        self.categorizer = categorizer

    def identify(self, filepath):
        return filepath.lower().endswith(".csv")

    def finalize(self, txn, row):
        if self.categorizer:
            return self.categorizer(txn, row)
        return txn
