# beancount-caixaenginyers

Beancount importer per a fitxers CSV de moviments de Caixa d'Enginyers.

## Project Structure

- `caixaenginyers.py` — Importer principal. Hereda de `beancount.ingest.importers.csv.Importer`. Configura les columnes del CSV (PAYEE=2, DATE=1, AMOUNT=4, BALANCE=5), salta 8 línies de capçalera, i sobreescriu `parse_amount` per convertir comes decimals a punts.
- `import.py` — Punt d'entrada per `beangulp`. Defineix `ACCOUNT_NAME` i la llista `CONFIG` amb una instància de `caixaenginyers.Importer`.
- `MovimientosCuenta-2023.csv` — Fitxer de mostra amb moviments reals (anonymitzats).
- `README.md` — Documentació d'ús en català.
- `LICENSE` — Llicència del projecte.

## Tech Stack

- Python 3
- [Beancount](https://github.com/beancount/beancount/) (double-entry bookkeeping)

## Usage

```bash
python import.py extract MovimientosCuenta.csv
```

## CSV Format

Columnes: DATA D'OPERACIÓ, CONCEPTE, DATA VALOR, IMPORT, SALDO

Particularitats:
- Separador decimal: `,` (coma)
- 8 línies de capçalera (informació del compte, titular, saldo, dates)
- Codificació: UTF-8

## Code Conventions

- Seguir PEP8 (pycodestyle)
- Mantenir l'estil existent: classes senzilles, herència dels importers de Beancount, sense dependencies
- Docstrings i comentaris en català (seguint el patró del README)
