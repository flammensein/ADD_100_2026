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

## Project Status

This project is currently in an educational/prototype stage. It contains multiple iterative versions of the customization flow and archived backups, which is common in early-stage development. Some scripts are likely incomplete or transitional, and the codebase should be treated as a working learning project rather than a production e-commerce platform.

## Features

- Unicycle brand and model selection
- Wheel size and tire compatibility filtering
- Rim, saddle, seatpost, crank, and pedal selection
- Optional brake support logic
- Billing and shipping information collection
- Structured order data for final review
- JSON inventory export for menu generation
- Versioned development history in the backup folder

## Product Catalog

`product_catalog.json` is the current source of truth for product data.
`dictionaries.py` loads it and keeps the existing Python constants available to
the application. The app does not need a database connection in this mode.

Edit `product_catalog.json` when changing the catalog. The older `menu.json`
export and its menu utilities are archived in `backup003`.

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
├── pos_defaults.py            # POS constants
├── product_catalog.json       # Source-of-truth product catalog
└── README.md                  # Project documentation
```