# Flammen Rides Unicycles

A Python-based prototype for configuring and customizing a unicycle build from a catalog of parts, brands, sizes, and options. This project models the core workflow of a product configurator: selecting a model, matching compatible components, generating a customized order summary, and preparing the data needed for checkout and invoicing.

## Overview

Flammen Rides Unicycles is a learning-focused project designed to demonstrate:

- structured product data in a JSON catalog
- menu generation from inventory catalogs
- component compatibility rules
- interactive customization flow
- order data collection for billing and shipping
- JSON export of configuration data

The project is built as a prototype and is intended to reflect best practices for maintainable, readable code and clear product-data organization.

## Streamlit App

The web configurator is in `streamlit_app.py`. It reuses the product catalog,
pricing and validation constants, invoice formatting, and JSON order-storage
module from the command-line app.

Run it from the repository root:

```bash
python -m pip install -r flammen_rides_unicycles/requirements.txt
streamlit run flammen_rides_unicycles/streamlit_app.py
```

To deploy on Streamlit Community Cloud, connect this GitHub repository and set
the app file to `flammen_rides_unicycles/streamlit_app.py`. Community Cloud
accepts a `requirements.txt` alongside the app entrypoint.

Orders continue to use the existing structured `orders.json` format and
`order_storage.py` interface. This is suitable for the class prototype; move
the storage implementation behind that interface to MySQL before relying on
cloud storage for durable order history.

## Project Status

This project is currently in an educational/prototype stage. It contains multiple iterative versions of the customization flow and archived backups, which is common in early-stage development. Some scripts are likely incomplete or transitional, and the codebase should be treated as a working learning project rather than a production e-commerce platform.

## Features

- Unicycle brand and model selection
- Wheel size and tire compatibility filtering
- Rim, saddle, seatpost, crank, and pedal selection
- Optional brake support logic
- Billing and shipping information collection
- Structured order data for final review
- Persistent order history in `orders.json`
- Versioned development history in the backup folder

## Product Catalog

`product_catalog.json` is the current source of truth for product data.
`dictionaries.py` loads it and keeps the existing Python constants available to
the application. The app does not need a database connection in this mode.

Edit `product_catalog.json` when changing the catalog. The older `menu.json`
export and its menu utilities are archived in `backup003`.

## Order History

Submitted orders are appended to `orders.json` in this folder. Each order starts
with its invoice number, followed by the configuration, customer and shipping
details, and financial totals. The human-readable invoice, with the invoice
number at the top, is displayed before the customer confirms submission.
`order_storage.py` provides functions to read, create,
update, and delete saved orders; writes replace the JSON file atomically so an
interrupted save does not leave a partially written order history.

## Deferred MySQL Migration

The MySQL migration is paused. Its schema, seeder, optional driver requirements,
and related tests are archived in `backup003` for later. The application
currently reads from the JSON file.

## Directory Structure

```text
flammen_rides_unicycles/
├── backup001/                  # Archived project files
├── backup002/                  # Archived project files
├── backup003/                  # Deferred and unused files
├── dictionaries.py            # Loads the JSON catalog for Python callers
├── main.py                    # Current configurator
├── order_storage.py           # Persistent order history and CRUD operations
├── pos_defaults.py            # POS constants
├── product_catalog.json       # Source-of-truth product catalog
├── orders.json                # Created when the first order is submitted
└── README.md                  # Project documentation
```