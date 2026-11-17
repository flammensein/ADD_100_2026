"""Streamlit web interface for the Flammen Rides unicycle configurator."""

import streamlit as st

from dictionaries import (
    AVAILABLE_RIM_COLORS,
    BRAKE_OPTIONS,
    CLAMP_COLORS,
    CLAMP_STYLES,
    CRANK_OPTIONS,
    PEDAL_OPTIONS,
    RIM_OPTIONS,
    SADDLE_CUSHION_COLORS,
    SADDLE_LEATHER_COLORS,
    SADDLE_OPTIONS,
    SEAT_POST_OPTIONS,
    TIRE_OPTIONS,
    UNICYCLE_BRANDS,
)
from main import format_invoice
from order_storage import create_order, generate_invoice_number
from pos_defaults import (
    BASE_PRICE,
    EMAIL_PATTERN,
    SHIPPING_METHODS,
    US_STATE_CODES,
    ZIP_CODE_PATTERN,
)

st.set_page_config(page_title="Flammen Rides Unicycles", page_icon="🚲", layout="wide")

st.title("Flammen Rides Unicycles")
st.caption("Build a custom unicycle, review your invoice, and submit your order.")

st.header("1. Choose your frame and tire")
frame_brand = st.selectbox("Frame brand", list(UNICYCLE_BRANDS), key="frame_brand")
models = UNICYCLE_BRANDS[frame_brand]
selected_model = st.selectbox(
    "Model",
    list(models),
    format_func=lambda model: (f"{model} ({models[model]['wheel_size']} wheel)"),
    key=f"model_{frame_brand}",
)
model_specs = models[selected_model]
wheel_size = model_specs["wheel_size"]

compatible_tires = {
    brand: [size for size in sizes if f'{size.split()[0]}"' == wheel_size]
    for brand, sizes in TIRE_OPTIONS.items()
}
compatible_tires = {brand: sizes for brand, sizes in compatible_tires.items() if sizes}
if not compatible_tires:
    st.error(f"No tires are available for wheel size {wheel_size}.")
    st.stop()

col1, col2 = st.columns(2)
with col1:
    tire_brand = st.selectbox(
        "Tire brand",
        list(compatible_tires),
        key=f"tire_brand_{wheel_size}",
    )
with col2:
    tire_size = st.selectbox(
        "Tire size",
        compatible_tires[tire_brand],
        key=f"tire_size_{wheel_size}_{tire_brand}",
    )
selected_tire = f"{tire_brand} {tire_size}"

st.header("2. Customize your components")
col1, col2 = st.columns(2)
with col1:
    saddle_name = st.selectbox("Saddle", list(SADDLE_OPTIONS))
    saddle_specs = SADDLE_OPTIONS[saddle_name]
    saddle_width = st.selectbox("Cushion width", saddle_specs["cushion_widths"])
    cushion_color = st.selectbox("Cushion color", SADDLE_CUSHION_COLORS)
    leather_color = "N/A"
    if saddle_specs.get("handle_leather_option", False):
        customize_leather = st.checkbox("Add custom handle leather")
        if customize_leather:
            leather_color = st.selectbox("Handle leather color", SADDLE_LEATHER_COLORS)

    compatible_posts = [
        name
        for name, specs in SEAT_POST_OPTIONS.items()
        if frame_brand in specs.get("compatible_brands", [])
        or specs.get("type", "Standard") == saddle_specs.get("mount_style", "Standard")
    ]
    if not compatible_posts:
        st.error(f"No compatible seatposts are available for {frame_brand}.")
        st.stop()

    post_name = st.selectbox("Seatpost", compatible_posts)
    post_specs = SEAT_POST_OPTIONS[post_name]
    post_length = st.selectbox(
        "Seatpost length (mm)",
        post_specs.get("lengths_mm", [300]),
    )
    clamp_name = st.selectbox("Seatpost clamp", list(CLAMP_STYLES))
    clamp_color = "Standard Black"
    if CLAMP_STYLES[clamp_name].get("color_customizable", False):
        clamp_color = st.selectbox("Clamp color", CLAMP_COLORS)

with col2:
    compatible_rims = [
        name
        for name, specs in RIM_OPTIONS.items()
        if wheel_size in specs.get("compatible_wheel_sizes", [])
    ]
    if not compatible_rims:
        st.error(f"No rims are available for wheel size {wheel_size}.")
        st.stop()

    rim_name = st.selectbox("Rim", compatible_rims)
    rim_color = st.selectbox("Rim color", AVAILABLE_RIM_COLORS)
    rim_specs = RIM_OPTIONS[rim_name]

    crank_name = st.selectbox("Crank model", list(CRANK_OPTIONS))
    crank_specs = CRANK_OPTIONS[crank_name]
    crank_length = st.selectbox("Crank length", crank_specs.get("lengths", ["125mm"]))
    crank_color = st.selectbox(
        "Crank color", crank_specs.get("available_colors", ["Black"])
    )

    pedal_brand = st.selectbox("Pedal brand", list(PEDAL_OPTIONS))
    pedal_specs = PEDAL_OPTIONS[pedal_brand]
    pedal_color = st.selectbox(
        "Pedal color", pedal_specs.get("available_colors", ["Black"])
    )

    brakes_installed = False
    brake_data = {
        "brakes_installed": False,
        "brake_model": "None",
        "type": "N/A",
        "rotor_diameter_mm": "N/A",
    }
    if model_specs.get("disc_brakes_supported", True):
        brakes_installed = st.checkbox("Install brakes", value=True)
    else:
        st.info("This frame does not support disc brakes.")

    if brakes_installed:
        brake_name = st.selectbox("Brake system", list(BRAKE_OPTIONS))
        brake_specs = BRAKE_OPTIONS[brake_name]
        supported_rotors = brake_specs.get("supported_rotors_mm", [])
        rotor_size = "N/A"
        if supported_rotors:
            default_rotor = brake_specs.get("default_rotor_mm")
            default_index = (
                supported_rotors.index(default_rotor)
                if default_rotor in supported_rotors
                else 0
            )
            rotor_size = st.selectbox(
                "Rotor size (mm)",
                supported_rotors,
                index=default_index,
            )
        brake_data = {
            "brakes_installed": True,
            "brake_model": brake_name,
            "type": brake_specs.get("type", "Hydraulic Disc"),
            "rotor_diameter_mm": rotor_size,
        }

saddle_data = {
    "saddle_name": saddle_name,
    "mount_style": saddle_specs.get("mount_style", "Standard"),
    "width": saddle_width,
    "cushion_color": cushion_color,
    "leather_color": leather_color,
}
seat_post_data = {
    "post_model": post_name,
    "diameter_mm": post_specs.get("diameter_mm"),
    "length_mm": post_length,
    "clamp_style": clamp_name,
    "clamp_color": clamp_color,
}
rim_data = {
    "rim_model": rim_name,
    "rim_color": rim_color,
    "width_mm": rim_specs.get("width_mm", "Standard"),
    "construction": rim_specs.get("construction", "double-wall"),
}
crank_data = {
    "crank_model": crank_name,
    "interface": crank_specs.get("interface", "Standard"),
    "length": crank_length,
    "color": crank_color,
}
pedal_data = {
    "pedal_brand": pedal_brand,
    "material": pedal_specs.get("material", "Plastic platform"),
    "pins": pedal_specs.get("pins", "Molded studs"),
    "color": pedal_color,
}

st.header("3. Billing and shipping")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Billing information")
    billing_name = st.text_input("Full name", key="billing_name")
    billing_email = st.text_input("Email", key="billing_email")
    billing_address = st.text_input("Street address", key="billing_address")
    billing_city = st.text_input("City", key="billing_city")
    billing_state = st.text_input(
        "State (2-letter code)", max_chars=2, key="billing_state"
    )
    billing_zip = st.text_input("ZIP code", key="billing_zip")
    payment_method = st.selectbox(
        "Payment method",
        ["Credit Card", "PayPal", "Apple Pay"],
        help="This prototype records your selection but does not process payments.",
    )

with col2:
    st.subheader("Shipping information")
    same_as_billing = st.checkbox("Use billing address for shipping", value=True)
    if same_as_billing:
        shipping_destination = {
            "full_name": billing_name,
            "address": billing_address,
            "city": billing_city,
            "state": billing_state.upper(),
            "zip_code": billing_zip,
        }
    else:
        shipping_destination = {
            "full_name": st.text_input("Recipient full name", key="shipping_name"),
            "address": st.text_input("Shipping street address", key="shipping_address"),
            "city": st.text_input("Shipping city", key="shipping_city"),
            "state": st.text_input(
                "Shipping state (2-letter code)",
                max_chars=2,
                key="shipping_state",
            ).upper(),
            "zip_code": st.text_input("Shipping ZIP code", key="shipping_zip"),
        }

    shipping_choices = list(SHIPPING_METHODS)
    shipping_choice = st.selectbox(
        "Shipping method",
        shipping_choices,
        format_func=lambda choice: (
            f"{SHIPPING_METHODS[choice]['name']} — "
            f"${SHIPPING_METHODS[choice]['cost']:.2f} "
            f"({SHIPPING_METHODS[choice]['days']})"
        ),
    )
shipping_specs = SHIPPING_METHODS[shipping_choice]

billing_data = {
    "full_name": billing_name.strip(),
    "email": billing_email.strip(),
    "address": billing_address.strip(),
    "city": billing_city.strip(),
    "state": billing_state.strip().upper(),
    "zip_code": billing_zip.strip(),
    "payment_method": payment_method,
}
shipping_data = {
    "destination": {key: value.strip() for key, value in shipping_destination.items()},
    "method_name": shipping_specs["name"],
    "shipping_cost": shipping_specs["cost"],
    "delivery_estimate": shipping_specs["days"],
}
order_data = {
    "frame_brand": frame_brand,
    "selected_model": selected_model,
    "wheel_size": wheel_size,
    "tire": selected_tire,
    "rim": rim_data,
    "saddle": saddle_data,
    "seat_post": seat_post_data,
    "cranks": crank_data,
    "pedals": pedal_data,
    "brakes": brake_data,
    "billing": billing_data,
    "shipping": shipping_data,
}

shipping_cost = shipping_specs["cost"]
tax_amount = BASE_PRICE * 0.08
total_cost = BASE_PRICE + tax_amount + shipping_cost

st.header("4. Review your order")
price_col1, price_col2, price_col3 = st.columns(3)
price_col1.metric("Build subtotal", f"${BASE_PRICE:.2f}")
price_col2.metric("Estimated tax (8%)", f"${tax_amount:.2f}")
price_col3.metric("Total with shipping", f"${total_cost:.2f}")

preview_invoice = format_invoice(
    order_data,
    "PREVIEW",
    BASE_PRICE,
    tax_amount,
    total_cost,
)
st.code(preview_invoice, language=None)

confirmed = st.checkbox("I have reviewed the order and want to submit it.")
if st.button("Submit order", type="primary"):
    errors = []
    if not billing_data["full_name"]:
        errors.append("Enter the billing name.")
    if not EMAIL_PATTERN.fullmatch(billing_data["email"]):
        errors.append("Enter a valid email address.")
    if not billing_data["address"] or not billing_data["city"]:
        errors.append("Enter the billing street address and city.")
    if billing_data["state"] not in US_STATE_CODES:
        errors.append("Enter a valid two-letter billing state code.")
    if not ZIP_CODE_PATTERN.fullmatch(billing_data["zip_code"]):
        errors.append("Enter a valid billing ZIP code.")
    if any(not value for value in shipping_data["destination"].values()):
        errors.append("Complete all shipping address fields.")
    if shipping_data["destination"]["state"] not in US_STATE_CODES:
        errors.append("Enter a valid two-letter shipping state code.")
    if not ZIP_CODE_PATTERN.fullmatch(shipping_data["destination"]["zip_code"]):
        errors.append("Enter a valid shipping ZIP code.")

    if errors:
        st.error(
            "Please fix the following before submitting:\n\n- " + "\n- ".join(errors)
        )
    elif not confirmed:
        st.warning("Review the invoice and confirm the order before submitting.")
    else:
        try:
            invoice_num = generate_invoice_number()
            saved_order = {"invoice_num": invoice_num}
            saved_order.update(order_data)
            saved_order["financials"] = {
                "subtotal": BASE_PRICE,
                "tax_amount": tax_amount,
                "shipping_cost": shipping_cost,
                "total_cost": total_cost,
            }
            create_order(saved_order)
        except (OSError, ValueError) as error:
            st.error(f"Could not save the order: {error}")
        else:
            st.session_state["submitted_invoice"] = format_invoice(
                order_data,
                invoice_num,
                BASE_PRICE,
                tax_amount,
                total_cost,
            )
            st.session_state["submitted_invoice_num"] = invoice_num

if "submitted_invoice" in st.session_state:
    st.success(f"Order {st.session_state['submitted_invoice_num']} was submitted.")
    st.code(st.session_state["submitted_invoice"], language=None)
