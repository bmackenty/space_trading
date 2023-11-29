class Events:
    event_name = ""
    description = ""
    trigger_conditions = {}
    probability = ""
    impact = {}
    duration = ""
    player_choices = []
    consequences = {}
    variability = ""
    story_tie_ins = ""
    notification_method = ""
    follow_up_events = []
    resource_demands = []
    npc_involvement = ""
    visual_and_audio_effects = ""
    rewards_and_penalties = {}
    feedback_mechanism = ""
    randomness_control = ""
    adaptability = ""
    cultural_and_environmental_influences = ""
    status = "Inactive"
    
    def __init__(self, event_name, description, trigger_conditions, probability, impact, duration, player_choices, consequences, variability, story_tie_ins, notification_method, follow_up_events, resource_demands, npc_involvement, visual_and_audio_effects, rewards_and_penalties, feedback_mechanism, randomness_control, adaptability, cultural_and_environmental_influences, status):
        self.event_name = event_name
        self.description = description
        self.trigger_conditions = trigger_conditions
        self.probability = probability
        self.impact = impact
        self.duration = duration
        self.player_choices = player_choices
        self.consequences = consequences
        self.variability = variability
        self.story_tie_ins = story_tie_ins
        self.notification_method = notification_method
        self.follow_up_events = follow_up_events
        self.resource_demands = resource_demands
        self.npc_involvement = npc_involvement
        self.visual_and_audio_effects = visual_and_audio_effects
        self.rewards_and_penalties = rewards_and_penalties
        self.feedback_mechanism = feedback_mechanism
        self.randomness_control = randomness_control
        self.adaptability = adaptability
        self.cultural_and_environmental_influences = cultural_and_environmental_influences
        self.status = status



# Description: Contains the event data for the game
random_events = {
    "Solar_Flare": {
        "Event Name": "Solar Flare",
        "Description": "A massive solar flare disrupts navigation and communication systems.",
        "Trigger Conditions": {"Location": "Near a star", "Time": "Random"},
        "Probability": "Low",
        "Impact": {"Navigation Difficulty": "Increased", "Communication": "Temporarily Disabled"},
        "Duration": "2 hours",
        "Player Choices": ["Seek shelter on nearest planet", "Activate emergency protocols", "Continue journey with risk"],
        "Consequences": {"Damage to Ship": "Possible", "Delay in Mission": "Likely"},
        "Variability": "Intensity of the flare",
        "Story Tie-ins": "None",
        "Notification Method": "In-game alert",
        "Follow-up Events": ["Aurora Spectacle", "Communication Blackout"],
        "Resource Demands": ["Extra Fuel", "Repair Kits"],
        "NPC Involvement": "None",
        "Visual and Audio Effects": "Bright flashes on screen, static noise",
        "Rewards and Penalties": {"Safe Navigation": "Experience Points", "Damage": "Repair Costs"},
        "Feedback Mechanism": "Status update post-event",
        "Randomness Control": "Occurs only once per game month",
        "Adaptability": "None",
        "Cultural and Environmental Influences": "None"
    },
    "Pirate_Ambush": {
        "Event Name": "Pirate Ambush",
        "Description": "Pirates ambush the player in a less-traveled sector.",
        "Trigger Conditions": {"Location": "Remote sectors", "Player Cargo Value": "High"},
        "Probability": "Medium",
        "Impact": {"Combat": "Initiated", "Cargo Risk": "High"},
        "Duration": "Varies (based on combat)",
        "Player Choices": ["Fight the pirates", "Attempt to flee", "Negotiate"],
        "Consequences": {"Loss of Cargo": "Possible", "Ship Damage": "Likely", "Gain Loot": "If victorious"},
        "Variability": "Pirate strength and numbers",
        "Story Tie-ins": "Potential to uncover pirate hideout location",
        "Notification Method": "Sudden attack alert",
        "Follow-up Events": ["Bounty Hunter Interest", "Revenge Encounter"],
        "Resource Demands": ["Ammunition", "Crew Stamina"],
        "NPC Involvement": "Pirate Leader",
        "Visual and Audio Effects": "Explosions, laser sounds",
        "Rewards and Penalties": {"Defeating Pirates": "Loot and Bounty Rewards", "Escape": "Fuel Loss", "Caught": "Lose Cargo"},
        "Feedback Mechanism": "Combat results screen",
        "Randomness Control": "Not in the same sector consecutively",
        "Adaptability": "Scales with player level",
        "Cultural and Environmental Influences": "Reflects local pirate activity"
    }
}


