#!/usr/bin/env python3
from caixaenginyers import Importer, Categorizer
from beangulp import Ingest


ACCOUNT_NAME = "Assets:CaixaEnginyers:CompteCorrent"

CONFIG = [
  Importer(ACCOUNT_NAME, categorizer=Categorizer()),
]

if __name__ == "__main__":
    Ingest(CONFIG)()
