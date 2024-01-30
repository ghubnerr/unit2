class ProductPricingService:
    def __init__(self, pricing_data_provider, tax_calculator, discount_calculator):
        self.pricing_data_provider = pricing_data_provider
        self.tax_calculator = tax_calculator
        self.discount_calculator = discount_calculator

    def calculate_final_price(self, product_id, user_id=None):
        # Get base price from data provider
        base_price = self.pricing_data_provider.get_base_price(product_id)

        # Calculate applicable taxes
        taxes = self.tax_calculator.calculate_taxes(base_price, user_id)

        # Apply any applicable discounts
        discounts = self.discount_calculator.calculate_discounts(base_price, user_id)

        # Calculate final price
        final_price = base_price + taxes - discounts

        return final_price
