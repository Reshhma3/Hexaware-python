from entity.donation import Donation

class ItemDonation(Donation):
    def __init__(self, donor_name, amount, item_type):
        super().__init__(donor_name, amount)
        self.item_type = item_type

    def record_donation(self):
        return f"Item donation ({self.item_type}) worth ₹{self.amount} by {self.donor_name}"