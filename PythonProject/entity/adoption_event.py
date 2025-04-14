class AdoptionEvent:
    def __init__(self):
        self.participants = []

    def host_event(self):
        return f"Hosting adoption event with {len(self.participants)} participants."

    def register_participant(self, participant):
        self.participants.append(participant)