# Flammen Rides Unicycles

A Python-based prototype for configuring and customizing a unicycle build from a catalog of parts, brands, sizes, and options. This project models the core workflow of a product configurator: selecting a model, matching compatible components, generating a customized order summary, and preparing the data needed for checkout and invoicing.

## Overview

Flammen Rides Unicycles is a learning-focused project designed to demonstrate:

- structured product data using Python dictionaries
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

## Directory Structure

```text
flammen_rides_unicycles/
├── backup/                     # Archived/earlier versions of project files
├── create_menu.py             # Exports inventory data to menu.json
├── dictionaries.py            # Source-of-truth product dictionaries
├── menu.json                  # Generated inventory catalog
├── read_menu.py               # Legacy/experimental menu reader
├── rim_options.py             # Rim-related option logic
├── tire_options               # Tire option helper/data
├── uni_customizer_v0.1.py     # Initial prototype
├── uni_customizer_v0.2.py     # Early modular version
├── uni_customizer_v0.2.2.py   # Iteration with more complete flow
├── uni_customizer_v0.2.3.py   # Continued refactoring
├── uni_customizer_v0.2.4.py   # More advanced prototype
└── README.md                  # Project documentation