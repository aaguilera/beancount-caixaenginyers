#!/usr/bin/env python3
from beancount.ingest.importers import caixaenginyers


ACCOUNT_NAME = "Assets:CaixaEnginyers:CompteCorrent"

CONFIG = [
  caixaenginyers.Importer(ACCOUNT_NAME)
]

