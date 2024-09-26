import numpy as np

class WeatherSimulation:
    def __init__(self, transition_probabilities, holding_times):
        self.transition_probabilities = transition_probabilities
        self.holding_times = holding_times
        self.states = list(transition_probabilities.keys())
        self.current_state_name = self.states[0]
        self.state_duration = holding_times[self.current_state_name]
        self.time_elapsed_in_state = 0

        # Check transition probabilities sum to 1 for each state
        for state, transitions in self.transition_probabilities.items():
            total_prob = sum(transitions.values())
            if not np.isclose(total_prob, 1.0):
                raise RuntimeError(f"Transition probabilities for '{state}' do not sum to 1. Found: {total_prob}")

    def get_states(self):
        """Returns a list of all states."""
        return self.states

    def current_state(self):
        """Returns the current state."""
        return self.current_state_name

    def next_state(self):
        """Advance to the next state based on transition probabilities."""
        if self.time_elapsed_in_state < self.state_duration:
            self.time_elapsed_in_state += 1
        else:
            self.time_elapsed_in_state = 1  # Reset time for new state
            next_state_probs = self.transition_probabilities[self.current_state_name]
            next_state = np.random.choice(self.states, p=[next_state_probs[s] for s in self.states])
            self.current_state_name = next_state
            self.state_duration = self.holding_times[next_state]

    def set_state(self, new_state):
        """Manually set the current state."""
        if new_state in self.states:
            self.current_state_name = new_state
            self.state_duration = self.holding_times[new_state]
            self.time_elapsed_in_state = 0
        else:
            raise ValueError(f"State '{new_state}' does not exist in states list.")

    def current_state_remaining_hours(self):
        """Returns the remaining hours in the current state."""
        return self.state_duration - self.time_elapsed_in_state

    def iterable(self):
        """A generator to iterate through states."""
        while True:
            yield self.current_state()
            self.next_state()

    def simulate(self, hours):
        """Run the simulation for a number of hours and return the state distribution."""
        state_counts = {state: 0 for state in self.states}

        for _ in range(hours):
            state_counts[self.current_state()] += 1
            self.next_state()

        total_counts = sum(state_counts.values())
        return [(state_counts[state] / total_counts) * 100 for state in self.states]
