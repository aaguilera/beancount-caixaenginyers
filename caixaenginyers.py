from beancount.core import data
from beancount.core.amount import Amount
from beangulp.importers import csv


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


class Importer(csv.CSVImporter):

    def __init__(self, account_name, categorizer=None):
        super().__init__(
            config={
                csv.Col.PAYEE:    2,
                csv.Col.DATE:     1,
                csv.Col.AMOUNT:   4,
                csv.Col.BALANCE:  5
            },
            account=account_name,
            currency="EUR",
            dateutil_kwds={"dayfirst": True},
            skip_lines=8,
            categorizer=categorizer)
        # CSVImporter uses composition (self.base = _CSVImporterBase),
        # so we must inject custom parse_amount into self.base directly
        base_parse = self.base.parse_amount
        self.base.parse_amount = lambda s: base_parse(s.replace(",", "."))
