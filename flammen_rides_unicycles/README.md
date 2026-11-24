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
- Persistent order history in `orders.json`
- Versioned development history in the backup folder

Seatposts must match the selected frame model's `seatpost_diameter_mm` and the
saddle's mount style; seatpost `compatible_brands` entries are not used for
matching. Frames without an available compatible seatpost and saddle are
excluded from the frame menu, and saddles without a matching seatpost are
excluded from the saddle menu. Missing or invalid frame diameters are reported
as catalog errors rather than guessed. The QX RGB 29 currently has only a
Pivotal seatpost in the catalog.
After a configuration edit, existing components are checked for compatibility.
If another section must change, the customer can update it or cancel the edit.
Editing billing also prompts the customer to review shipping.
The configurator displays the selections made so far before each build section
and when editing sections.

Frame seatpost-diameter references:

- Nimbus [Hatchet 27.5](https://www.unicycle.co.uk/product/27-nimbus-hatchet-muni-unicycle-grey/)
  and [Oracle frames](https://www.unicycle.co.uk/product/nimbus-oracle-disc-unicycle-frame/):
  25.4 mm.
- [Kris Holm frames](https://www.krisholm.com/en/gear/component/frames):
  27.2 mm.
- QU-AX Muni [24](https://jwseurope.com/muni-mountain-unicycles/261-qu-ax-muni-24-unicycle.html)
  and [27.5](https://qu-ax.de/catalog/QU-AX-Muni-584-mm-275-black): 25.4 mm;
  [QX RGB 29](https://www.circus-expert.com/qx-rgb-muni-29-inch-with-disc-brake-red.html):
  31.6 mm.
- [Mad4One URC frames](https://www.mad4one.com/gb/frames/520-mad4one-frame-muni-m.html):
  25.4 mm.
- Club [20](https://www.unicycle.co.uk/product/20-club-freestyle-unicycle-with-white-tyre/)
  and [24](https://www.clubunicycles.com/24-club-freestyle-unicycle/):
  25.4 mm.
- The [QU-AX Pivotal seatpost](https://qu-ax.de/catalog/QU-AX-Pivotal-Seatpost-aluminum-316-mm)
  is 31.6 mm in diameter and 500 mm long.

The configurator checks the listed diameter and mount specifications, not every
physical fit or safety requirement. Verify parts and clamp compatibility against
the exact frame and component versions before assembly.

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