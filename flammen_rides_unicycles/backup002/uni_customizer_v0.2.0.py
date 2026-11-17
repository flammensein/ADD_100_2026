"""
-----------------------------------------------------------------------
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Flammen Rides Unicycles v0.2
-----------------------------------------------------------------------

SYSTEM DICTIONARIES
# TODO: Populate the following dictionaries with inventory data:
# - UNICYCLE_BRANDS
# - TIRE_OPTIONS
# - SADDLE_OPTIONS
# - SEAT_POST_OPTIONS
# - CLAMP_STYLES
# - RIM_OPTIONS
# - CRANK_OPTIONS
# - PEDAL_OPTIONS
# - BRAKE_OPTIONS
# - SHIPPING_METHODS
"""


def load_inventory(filepath):
    # TODO: Read inventory data from the external CSV file.
    # TODO: Return a nested dictionary of parts, options, and pricing to supply the menus.
    pass


def build_frame_assembly():
    # TODO: Prompt the user for unicycle brand and model selection.
    # TODO: Determine if the selected frame supports disc brakes.
    # TODO: Return a dictionary containing frame specs and brake compatibility.
    pass


def build_wheel_assembly(brakes_supported):
    # TODO: Prompt for tire brand and size, extracting the core wheel size.
    # TODO: Filter and prompt for rim options based on the extracted wheel size.
    # TODO: If brakes_supported is True, prompt for brake system and rotor size.
    # TODO: Return a dictionary of all wheel and brake components.
    pass


def build_seating_assembly(frame_brand):
    # TODO: Prompt for saddle model, cushion width, and color.
    # TODO: Filter seatpost options based on the frame_brand and saddle mount style.
    # TODO: Prompt for seatpost length and clamp style/color.
    # TODO: Return a dictionary of the complete seating setup.
    pass


def build_drivetrain_assembly():
    # TODO: Prompt for crank arm model, interface, length, and color.
    # TODO: Prompt for pedal make, material, and color.
    # TODO: Return a dictionary of the drivetrain components.
    pass


def checkout_process():
    # TODO: Collect user billing details (name, email, address, payment method).
    # TODO: Prompt for shipping destination (or default to billing address).
    # TODO: Calculate and prompt for shipping speed/cost.
    # TODO: Return dictionaries for both billing and shipping information.
    pass


def build_customization():
    # TODO: Act as the single coordinator function for the unicycle build.
    # TODO: Call build_frame_assembly() and store the frame specs.
    # TODO: Pass dependent variables (like frame_brand or brakes_supported) into the other assembly functions.
    # TODO: Compile and return a single, massive order_data dictionary containing all sub-assemblies.
    pass


def review_order(order_data):
    # TODO: Generate a unique invoice_num.
    # TODO: Display a formatted, onscreen summary of the compiled order_data.
    # TODO: Prompt the user to 'Accept', 'Edit', or 'Cancel'.
    # TODO: Return the invoice_num and the user's status choice.
    pass


def write_invoice(order_data, invoice_num):
    # TODO: Calculate final totals, taxes, and shipping.
    # TODO: Write a cleanly formatted, human-readable receipt to a unique text file based on the invoice_num.
    pass


def log_order_history(order_data, invoice_num):
    # TODO: Flatten the order attributes into a computer-readable format.
    # TODO: Append a structured, comma-separated record to order_history.csv.
    pass


def main():
    # TODO: Establish a Structured State Flag (program_running = True) to control the main loop.
    # TODO: Load inventory data.
    # TODO: Call build_customization() to coordinate the parts selection.
    # TODO: Call checkout_process() to gather user details.
    # TODO: Call review_order() to confirm the build.
    # TODO: If confirmed, trigger write_invoice() and log_order_history(), then exit the loop.
    pass


main()
