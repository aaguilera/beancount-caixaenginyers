from beancount.ingest.importers import csv


class Importer(csv.Importer):

    def __init__(self, account_name):
        super().__init__(config={
            csv.Col.PAYEE:    2,
            csv.Col.DATE:     3,
            csv.Col.AMOUNT:   4,
            csv.Col.BALANCE:  5
            },
            account=account_name,
            currency="EUR",
            dateutil_kwds={"dayfirst": True},
            skip_lines=8)

    def parse_amount(self, string):
        # cal transformar les comes a punts
        return super().parse_amount(string.replace(",", "."))

