"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Flammen Rides Unicycles
Developer: Brent T. Marnati
"""


def model_opts():
    # Frame size choice
    # Brakes Y/N choice (calls break_opts(brake_opts(yes) to brake_opts)
    # Frame color_options()
    #   - consider if multiple "color_options" lists will be needed or all colorized features can be made to work with a single list.
    # Returns frame_size, frame_color, brakes_yn, rotor_diameter {if brakes_yn(yes)}
    pass


def tire_opts():
    # Tire Brand
    # Tire Size (passes rim_opts(wheel_size) to restrict rim_size options)
    pass


def saddle_opts():
    # Saddle Model and Style (not a lot of variation, so each Brand/Model/Handle combo is an entry in this list)
    # Cushion Width
    # Cushion Color
    # Handle Leather Color (only enabled if certain saddle combo is chosen)
    pass


def seat_post_opts():
    # post size
    # clamp style
    # - Certain Clamp Styles enable Clamp Color Option
    pass


def rim_opts(wheel_size):
    # Rim Style Options
    # wheel_size sets rim_size
    # Rim Color
    pass


def crank_opts():
    # Crank Model/Length
    # Crank Color
    pass


def pedal_opts():
    # Pedal Make/Model
    pass


def brake_opts():
    # Only available if model_opts() selection makes it so.
    # Brake Make/Model
    # Rotor Diameter
    pass


def billing_info():
    # Collect Billing information
    pass


def shipping_info():
    # Collect shipping destination
    # Calculate shipping cost options based on destination, and weight
    # Present user with shipping options and the cost of each to
    # ==> Collect shipping method choice
    # Collect
    pass


def final_order():
    # Builds onscreen presentation of order with generated unique Order ID (invoice_num)
    # Offers 'Accept/Buy/Submit', 'Edit', 'Cancel' options.
    # Proceeds accordingly
    pass


def main():
    model_opts()
    wheel_size = tire_opts()
    saddle_opts()
    seat_post_opts()
    rim_opts(wheel_size)
    crank_opts()
    pedal_opts()
    brake_opts()
    billing_info()
    shipping_info()
    final_order()


main()
