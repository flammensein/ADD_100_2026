CREATE TABLE IF NOT EXISTS brands (
    brand_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    seed_key VARCHAR(100) NOT NULL,
    canonical_name VARCHAR(120) NOT NULL,
    PRIMARY KEY (brand_id),
    UNIQUE KEY uq_brands_seed_key (seed_key),
    UNIQUE KEY uq_brands_canonical_name (canonical_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS brand_aliases (
    brand_alias_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    brand_id BIGINT UNSIGNED NOT NULL,
    seed_key VARCHAR(160) NOT NULL,
    context_code VARCHAR(40) NOT NULL,
    alias_label VARCHAR(160) NOT NULL,
    PRIMARY KEY (brand_alias_id),
    UNIQUE KEY uq_brand_alias_seed_key (seed_key),
    UNIQUE KEY uq_brand_alias_context_label (context_code, alias_label),
    UNIQUE KEY uq_brand_alias_id_brand (brand_alias_id, brand_id),
    CONSTRAINT fk_brand_aliases_brand
        FOREIGN KEY (brand_id) REFERENCES brands (brand_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS product_categories (
    category_code VARCHAR(40) NOT NULL,
    category_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (category_code),
    UNIQUE KEY uq_product_categories_name (category_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS products (
    product_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    seed_key VARCHAR(200) NOT NULL,
    category_code VARCHAR(40) NOT NULL,
    brand_id BIGINT UNSIGNED NOT NULL,
    brand_alias_id BIGINT UNSIGNED NOT NULL,
    product_name VARCHAR(200) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    PRIMARY KEY (product_id),
    UNIQUE KEY uq_products_seed_key (seed_key),
    UNIQUE KEY uq_products_category_brand_name
        (category_code, brand_id, product_name),
    CONSTRAINT fk_products_category
        FOREIGN KEY (category_code) REFERENCES product_categories (category_code),
    CONSTRAINT fk_products_brand
        FOREIGN KEY (brand_id) REFERENCES brands (brand_id),
    CONSTRAINT fk_products_brand_alias
        FOREIGN KEY (brand_alias_id, brand_id)
        REFERENCES brand_aliases (brand_alias_id, brand_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS product_variants (
    variant_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    product_id BIGINT UNSIGNED NOT NULL,
    seed_key VARCHAR(240) NOT NULL,
    display_label VARCHAR(160) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    PRIMARY KEY (variant_id),
    UNIQUE KEY uq_product_variants_seed_key (seed_key),
    UNIQUE KEY uq_product_variants_product_label (product_id, display_label),
    CONSTRAINT fk_product_variants_product
        FOREIGN KEY (product_id) REFERENCES products (product_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS variant_measurements (
    variant_id BIGINT UNSIGNED NOT NULL,
    measurement_code VARCHAR(40) NOT NULL,
    sequence_no SMALLINT UNSIGNED NOT NULL DEFAULT 1,
    numeric_value DECIMAL(9,3) NOT NULL,
    unit_code VARCHAR(12) NOT NULL,
    PRIMARY KEY (variant_id, measurement_code, sequence_no),
    CONSTRAINT fk_variant_measurements_variant
        FOREIGN KEY (variant_id) REFERENCES product_variants (variant_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS wheel_sizes (
    wheel_size_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    nominal_diameter_in DECIMAL(5,2) NOT NULL,
    display_label VARCHAR(32) NOT NULL,
    PRIMARY KEY (wheel_size_id),
    UNIQUE KEY uq_wheel_sizes_diameter (nominal_diameter_in),
    UNIQUE KEY uq_wheel_sizes_label (display_label)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS mount_standards (
    mount_standard_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    standard_code VARCHAR(40) NOT NULL,
    display_label VARCHAR(80) NOT NULL,
    PRIMARY KEY (mount_standard_id),
    UNIQUE KEY uq_mount_standards_code (standard_code),
    UNIQUE KEY uq_mount_standards_label (display_label)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS unicycle_model_specs (
    product_id BIGINT UNSIGNED NOT NULL,
    wheel_size_id BIGINT UNSIGNED NOT NULL,
    disc_brakes_supported BOOLEAN NOT NULL,
    PRIMARY KEY (product_id),
    CONSTRAINT fk_unicycle_model_specs_product
        FOREIGN KEY (product_id) REFERENCES products (product_id),
    CONSTRAINT fk_unicycle_model_specs_wheel_size
        FOREIGN KEY (wheel_size_id) REFERENCES wheel_sizes (wheel_size_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS tire_specs (
    product_id BIGINT UNSIGNED NOT NULL,
    size_label VARCHAR(80) NOT NULL,
    width_in DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (product_id),
    CONSTRAINT fk_tire_specs_product
        FOREIGN KEY (product_id) REFERENCES products (product_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS saddle_specs (
    product_id BIGINT UNSIGNED NOT NULL,
    mount_standard_id BIGINT UNSIGNED NOT NULL,
    handle_leather_option BOOLEAN NOT NULL,
    PRIMARY KEY (product_id),
    CONSTRAINT fk_saddle_specs_product
        FOREIGN KEY (product_id) REFERENCES products (product_id),
    CONSTRAINT fk_saddle_specs_mount_standard
        FOREIGN KEY (mount_standard_id) REFERENCES mount_standards (mount_standard_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS seat_post_specs (
    product_id BIGINT UNSIGNED NOT NULL,
    mount_standard_id BIGINT UNSIGNED NOT NULL,
    diameter_mm DECIMAL(6,2) NOT NULL,
    PRIMARY KEY (product_id),
    CONSTRAINT fk_seat_post_specs_product
        FOREIGN KEY (product_id) REFERENCES products (product_id),
    CONSTRAINT fk_seat_post_specs_mount_standard
        FOREIGN KEY (mount_standard_id) REFERENCES mount_standards (mount_standard_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS rim_specs (
    product_id BIGINT UNSIGNED NOT NULL,
    diameter_in DECIMAL(5,2) NOT NULL,
    construction VARCHAR(80) NOT NULL,
    width_mm DECIMAL(6,2) NULL,
    PRIMARY KEY (product_id),
    CONSTRAINT fk_rim_specs_product
        FOREIGN KEY (product_id) REFERENCES products (product_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS crank_specs (
    product_id BIGINT UNSIGNED NOT NULL,
    interface_label VARCHAR(160) NOT NULL,
    PRIMARY KEY (product_id),
    CONSTRAINT fk_crank_specs_product
        FOREIGN KEY (product_id) REFERENCES products (product_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS pedal_specs (
    product_id BIGINT UNSIGNED NOT NULL,
    material VARCHAR(160) NOT NULL,
    pins VARCHAR(160) NOT NULL,
    PRIMARY KEY (product_id),
    CONSTRAINT fk_pedal_specs_product
        FOREIGN KEY (product_id) REFERENCES products (product_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS brake_specs (
    product_id BIGINT UNSIGNED NOT NULL,
    brake_type VARCHAR(80) NOT NULL,
    PRIMARY KEY (product_id),
    CONSTRAINT fk_brake_specs_product
        FOREIGN KEY (product_id) REFERENCES products (product_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS option_groups (
    option_group_code VARCHAR(50) NOT NULL,
    group_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (option_group_code),
    UNIQUE KEY uq_option_groups_name (group_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS option_values (
    option_value_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    option_group_code VARCHAR(50) NOT NULL,
    seed_key VARCHAR(160) NOT NULL,
    value_label VARCHAR(100) NOT NULL,
    PRIMARY KEY (option_value_id),
    UNIQUE KEY uq_option_values_seed_key (seed_key),
    UNIQUE KEY uq_option_values_group_label (option_group_code, value_label),
    CONSTRAINT fk_option_values_group
        FOREIGN KEY (option_group_code)
        REFERENCES option_groups (option_group_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS product_option_values (
    product_id BIGINT UNSIGNED NOT NULL,
    option_value_id BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (product_id, option_value_id),
    CONSTRAINT fk_product_option_values_product
        FOREIGN KEY (product_id) REFERENCES products (product_id),
    CONSTRAINT fk_product_option_values_value
        FOREIGN KEY (option_value_id) REFERENCES option_values (option_value_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS clamp_style_settings (
    option_value_id BIGINT UNSIGNED NOT NULL,
    color_customizable BOOLEAN NOT NULL,
    PRIMARY KEY (option_value_id),
    CONSTRAINT fk_clamp_style_settings_option
        FOREIGN KEY (option_value_id) REFERENCES option_values (option_value_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS clamp_style_color_options (
    clamp_style_option_value_id BIGINT UNSIGNED NOT NULL,
    color_option_value_id BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (clamp_style_option_value_id, color_option_value_id),
    CONSTRAINT fk_clamp_style_colors_style
        FOREIGN KEY (clamp_style_option_value_id)
        REFERENCES clamp_style_settings (option_value_id),
    CONSTRAINT fk_clamp_style_colors_color
        FOREIGN KEY (color_option_value_id) REFERENCES option_values (option_value_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS product_wheel_size_compatibility (
    product_id BIGINT UNSIGNED NOT NULL,
    wheel_size_id BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (product_id, wheel_size_id),
    CONSTRAINT fk_product_wheel_compatibility_product
        FOREIGN KEY (product_id) REFERENCES products (product_id),
    CONSTRAINT fk_product_wheel_compatibility_size
        FOREIGN KEY (wheel_size_id) REFERENCES wheel_sizes (wheel_size_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS seat_post_frame_brand_compatibility (
    seat_post_product_id BIGINT UNSIGNED NOT NULL,
    frame_brand_id BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (seat_post_product_id, frame_brand_id),
    CONSTRAINT fk_seat_post_frame_compatibility_post
        FOREIGN KEY (seat_post_product_id) REFERENCES seat_post_specs (product_id),
    CONSTRAINT fk_seat_post_frame_compatibility_brand
        FOREIGN KEY (frame_brand_id) REFERENCES brands (brand_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS brake_rotor_compatibility (
    brake_product_id BIGINT UNSIGNED NOT NULL,
    rotor_diameter_mm SMALLINT UNSIGNED NOT NULL,
    is_default BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (brake_product_id, rotor_diameter_mm),
    CONSTRAINT fk_brake_rotor_compatibility_brake
        FOREIGN KEY (brake_product_id) REFERENCES brake_specs (product_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
