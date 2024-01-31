class Pricing:
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



class MockPricingDataProvider:
    def get_base_price(self, (*args):
        return 100

class MockTaxCalculator:
    def calculate_taxes(self, *args):
        return 200

class MockDiscountCalculator():
    def calculate_discounts(self, *args):
        return 200


import unittest

class UnitTests(unittest.TestCase):
    def test_calculate_final_price(self):
        data_provider = MockPricingDataProvider()
        tax_calculator = MockTaxCalculator()
        discount_calculator = MockDiscountCalculator()
        
        my_pricing = Pricing(pricing_data_provider=data_provider, tax_calculator=tax_calculator, discount_calculator=discount_calculator)
        result = my_pricing.calculate_final_price(0)
        self.assertEquals(100, result)

if __name__ == "__main__":
    unittest.main()
    
