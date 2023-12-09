# this file should contain a list of goods, their base price, and a description
# the goods should be science fiction goods

good_categories = {
    "Raw_Materials": {
        "Examples": ["Iron Ore", "Hydrogen Fuel", "Titanium"],
        "Common Uses": ["Manufacturing", "Fuel", "Construction"],
        "Special Notes": "Widely available but low profit margins."
    },
    "Manufactured_Goods": {
        "Examples": ["Spacecraft Parts", "Electronics", "Machinery"],
        "Common Uses": ["Repairs", "Upgrades", "Industrial"],
        "Special Notes": "Requires industrial facilities to produce."
    },
    "Luxury_Items": {
        "Examples": ["Fine Art", "Rare Wines", "Jewelry"],
        "Common Uses": ["Trade with affluent clients", "Gifts"],
        "Special Notes": "High value but market volatility is common."
    },
    "Technological_Items": {
        "Examples": ["Quantum Chips", "AI Cores", "Advanced Sensors"],
        "Common Uses": ["Tech upgrades", "Research"],
        "Special Notes": "High demand in technologically advanced regions."
    },
    "Foodstuffs": {
        "Examples": ["Synthetic Meat", "Hydroponic Vegetables", "Nutrient Packs"],
        "Common Uses": ["Consumption", "Agriculture"]
    },
        "Medicinal_Products": {
        "Examples": ["Pharmaceuticals", "Medical Equipment", "Biotech Implants"],
        "Common Uses": ["Healthcare", "Life Support", "Enhancements"],
        "Special Notes": "Steady demand, but regulations vary significantly by region."
    },
    "Energy_Sources": {
        "Examples": ["Fusion Cells", "Antimatter Containers", "Solar Panels"],
        "Common Uses": ["Power Generation", "Ship Fuel", "Industrial Energy"],
        "Special Notes": "Essential for all space activities, constant demand."
    },
    "Cultural_Artifacts": {
        "Examples": ["Ancient Relics", "Artistic Works", "Historical Documents"],
        "Common Uses": ["Museums", "Collectors", "Academic Study"],
        "Special Notes": "Niche market, potentially high value but with legal complexities."
    },
    "Research_Materials": {
        "Examples": ["Exotic Matter", "Genetic Samples", "Archaeological Finds"],
        "Common Uses": ["Scientific Research", "Experimental Tech"],
        "Special Notes": "Highly specialized and often subject to strict regulations."
    },
    "Illegal_Goods": {
        "Examples": ["Narcotics", "Contraband Tech", "Smuggled Artifacts"],
        "Common Uses": ["Black Market", "Underworld Deals"],
        "Special Notes": "High risk and reward, illegal in many jurisdictions."
    },
    "Military_Equipment": {
        "Examples": ["Laser Cannons", "Shield Generators", "Combat Drones"],
        "Common Uses": ["Arming Ships", "Planetary Defense", "Mercenary Activities"],
        "Special Notes": "High demand in conflict zones, but sale may be restricted."
    },
    "Construction_Materials": {
        "Examples": ["Composite Alloys", "Nano-Cement", "Self-Assembling Scaffoldings"],
        "Common Uses": ["Building Space Stations", "Habitat Construction", "Infrastructure Projects"],
        "Special Notes": "Steady demand in expanding colonies or reconstruction areas."
    },
    "Data_Resources": {
        "Examples": ["Star Maps", "Encrypted Databases", "Scientific Research"],
        "Common Uses": ["Navigation", "Information Trading", "Academic Study"],
        "Special Notes": "Intangible but can be highly valuable; piracy risk."
    },
    "Organic_Materials": {
        "Examples": ["Seeds", "Microbial Cultures", "Genetic Templates"],
        "Common Uses": ["Terraforming", "Agriculture", "Biotech"],
        "Special Notes": "Special storage conditions often required."
    },
    "Hazardous_Materials": {
        "Examples": ["Radioactive Isotopes", "Toxic Waste", "Corrosive Chemicals"],
        "Common Uses": ["Industrial Processes", "Weaponry", "Waste Disposal"],
        "Special Notes": "Transportation and handling are risky and heavily regulated."
    },
    "Communication_Devices": {
        "Examples": ["Quantum Transceivers", "Holo-Projectors", "Signal Jammers"],
        "Common Uses": ["Communication", "Media", "Espionage"],
        "Special Notes": "Varying legality and technical complexity."
    },
    "Personal_Items": {
        "Examples": ["Clothing", "Jewelry", "Entertainment Devices"],
        "Common Uses": ["Daily Use", "Fashion", "Leisure Activities"],
        "Special Notes": "Broad market appeal, trends can fluctuate rapidly."
    },
    "Transport_Vehicles": {
        "Examples": ["Shuttlecraft", "Cargo Haulers", "Hoverbikes"],
        "Common Uses": ["Transportation", "Cargo Movement", "Personal Travel"],
        "Special Notes": "Requires servicing facilities; registration may be needed."
    },
    "Survival_Gear": {
        "Examples": ["Space Suits", "Oxygen Generators", "Emergency Rations"],
        "Common Uses": ["Exploration", "Disaster Preparedness", "Colonization"],
        "Special Notes": "Essential for high-risk environments."
    },
    "Artificial_Intelligence": {
        "Examples": ["Navigational AIs", "Personal Assistants", "Tactical Simulators"],
        "Common Uses": ["Automation", "Efficiency Improvement", "Training"],
        "Special Notes": "Ethical and legal considerations in certain jurisdictions."
    },
    "Exploration_Equipment": {
        "Examples": ["Deep Space Probes", "Planetary Rovers", "Astronomical Telescopes"],
        "Common Uses": ["Space Exploration", "Scientific Research", "Astrobiology Studies"],
        "Special Notes": "Highly advanced technology, often requires collaboration with research institutions."
    },
    "Virtual_Realities": {
        "Examples": ["Immersive Simulations", "Virtual Worlds", "Augmented Reality Devices"],
        "Common Uses": ["Entertainment", "Training", "Therapeutic Applications"],
        "Special Notes": "Rapidly evolving field with diverse applications, from leisure to professional training."
    },
    "Environmental_Technology": {
        "Examples": ["Climate Control Systems", "Eco-Friendly Materials", "Sustainable Energy Solutions"],
        "Common Uses": ["Habitat Management", "Eco-Preservation", "Energy Efficiency"],
        "Special Notes": "Growing demand in light of environmental concerns and sustainability goals."
    },
    "Security_Systems": {
        "Examples": ["Surveillance Drones", "Encryption Software", "Automated Defense Platforms"],
        "Common Uses": ["Asset Protection", "Information Security", "Public Safety"],
        "Special Notes": "Highly sensitive market, often requires clearance and compliance with legal standards."
    },
    "Recreational_Goods": {
        "Examples": ["Holographic Games", "Zero-G Sports Equipment", "Leisure Craft"],
        "Common Uses": ["Leisure", "Sport", "Recreation"],
        "Special Notes": "Trends can be highly variable, influenced by cultural shifts and technological innovations."
    },
    "Bioengineering_Products": {
        "Examples": ["Custom Organisms", "Genetic Modification Kits", "Ecosystem Simulators"],
        "Common Uses": ["Biological Research", "Agriculture", "Medical Applications"],
        "Special Notes": "Ethical considerations and regulatory compliance are significant factors."
    },
    "Dimensional_Artifacts": {
        "Examples": ["Time-Folded Crystals", "Interdimensional Gateways", "Quantum Entanglement Devices"],
        "Common Uses": ["Experimental Physics", "Advanced Communication", "Space-Time Research"],
        "Special Notes": "Extremely rare and often poorly understood; handle with utmost caution."
    },
    "Crypto_Biological_Samples": {
        "Examples": ["Alien Flora Seeds", "Mythical Creature DNA", "Sentient Fungi Spores"],
        "Common Uses": ["Xenobiology", "Genetic Engineering", "Pharmaceutical Development"],
        "Special Notes": "Potential for unknown effects; strict containment protocols advised."
    },
    "Psionic_Technology": {
        "Examples": ["Telepathy Amplifiers", "Mind-Control Helmets", "Emotion Detectors"],
        "Common Uses": ["Mental Health", "Interrogation", "Espionage"],
        "Special Notes": "Ethical and moral implications; regulated in most advanced civilizations."
    },
    "Cosmic_Rarities": {
        "Examples": ["Star Core Fragments", "Nebula Gas Samples", "Black Hole Photons"],
        "Common Uses": ["Astrophysics Research", "High-Energy Experiments", "Cosmological Studies"],
        "Special Notes": "Incredibly scarce and difficult to acquire; often priceless."
    },
    "Mythos_Artifacts": {
        "Examples": ["Ancient Runestones", "Cursed Relics", "Lost Civilization Technology"],
        "Common Uses": ["Archeology", "Occult Studies", "Cultural Preservation"],
        "Special Notes": "May carry historical significance and unexplained powers; handle with reverence."
    },
    "Quantum_Constructs": {
        "Examples": ["Holographic Memory Orbs", "Quantum State Manipulators", "Dimensional Bridges"],
        "Common Uses": ["Data Storage", "Reality Engineering", "Transdimensional Travel"],
        "Special Notes": "Highly advanced and often requires quantum computing resources to operate."
    },
    "Nano_Engineered_Materials": {
        "Examples": ["Self-Repairing Metals", "Programmable Liquid Alloys", "Nano-Assemblers"],
        "Common Uses": ["Construction", "Manufacturing", "Medical Applications"],
        "Special Notes": "Versatile and adaptive, but requires sophisticated control systems."
    },
    "Galactic_Mapping_Tools": {
        "Examples": ["Wormhole Navigators", "Star Cluster Mappers", "Cosmic Anomaly Detectors"],
        "Common Uses": ["Exploration", "Astrogation", "Research"],
        "Special Notes": "Essential for safe and efficient interstellar travel."
    },
    "Synthetic_Life_Forms": {
        "Examples": ["Artificial Intelligence Beings", "Bioengineered Companions", "Customized Avatars"],
        "Common Uses": ["Assistance", "Companionship", "Role Fulfillment"],
        "Special Notes": "Ethical considerations are paramount; some jurisdictions have strict regulations."
    },
    "Temporal_Manipulation_Devices": {
        "Examples": ["Time Dilation Modules", "Chronal Stabilizers", "Temporal Communicators"],
        "Common Uses": ["Experimental Physics", "Time-Shifted Operations", "Historical Research"],
        "Special Notes": "Use is controversial and potentially dangerous; often restricted by temporal accords."
    }
}

communication_devices = {
    "Quantum Transceivers": {
        "Common Uses": "Communication",
        "Special Notes": "Allows for instant communication over vast distances, using quantum entanglement."
    },
    "Holo-Projectors": {
        "Common Uses": "Media",
        "Special Notes": "Projects high-resolution holograms for entertainment and presentations."
    },
    "Signal Jammers": {
        "Common Uses": "Espionage",
        "Special Notes": "Used to disrupt communications, often for covert operations."
    },
    "Subspace Radios": {
        "Common Uses": "Long-Distance Communication",
        "Special Notes": "Bypasses normal space to allow faster-than-light transmissions."
    },
    "Neural Communicators": {
        "Common Uses": "Silent Communication",
        "Special Notes": "Interfaces directly with neural implants for private and secure messages."
    },
    "Interstellar Broadcast Arrays": {
        "Common Uses": "Wide-Area Media",
        "Special Notes": "Capable of sending signals across entire star systems."
    },
    "Cryptographic Coders": {
        "Common Uses": "Secure Communication",
        "Special Notes": "Encrypts messages to prevent unauthorized access."
    },
    "Telepathy Amplifiers": {
        "Common Uses": "Enhanced Interaction",
        "Special Notes": "Boosts mental communication abilities, often used in diplomatic negotiations."
    },
    "Stealth Comms Units": {
        "Common Uses": "Covert Operations",
        "Special Notes": "Designed for undetectable communication, avoiding interception."
    },
    "Galactic Relay Stations": {
        "Common Uses": "Communication Infrastructure",
        "Special Notes": "Amplifies and redirects communication signals across vast interstellar distances."
    },
    "Universal Translators": {
        "Common Uses": "Multicultural Communication",
        "Special Notes": "Automatically translates between different languages and dialects."
    },
    "Emergency Beacon Transmitters": {
        "Common Uses": "Distress Signals",
        "Special Notes": "Used for signaling emergencies in space, a must-have for explorers."
    },
    "Virtual Reality Conferencing Systems": {
        "Common Uses": "Virtual Meetings",
        "Special Notes": "Enables immersive and interactive virtual meetings."
    },
    "Sonic Messaging Devices": {
        "Common Uses": "Underwater Communication",
        "Special Notes": "Uses sound waves for communication in aquatic environments."
    },
    "Frequency Hoppers": {
        "Common Uses": "Evasion",
        "Special Notes": "Rapidly changes transmission frequencies to avoid detection and jamming."
    },

    "Quantum Entanglement Communicators": {
        "Common Uses": "Instantaneous Communication",
        "Special Notes": "Operates on quantum entanglement principles for real-time communication across any distance."
    },
    "Neural Interface Messengers": {
        "Common Uses": "Direct Neural Communication",
        "Special Notes": "Transmits thoughts and ideas directly between users via neural implants."
    },
    "Holo-Telepresence Pods": {
        "Common Uses": "Virtual Meetings",
        "Special Notes": "Creates a lifelike holographic presence of individuals in remote locations."
    },
    "Dimensional Wave Transmitters": {
        "Common Uses": "Multidimensional Communication",
        "Special Notes": "Capable of sending signals through alternate dimensions, bypassing conventional barriers."
    },
    "Galactic Echo Relays": {
        "Common Uses": "Deep Space Broadcasting",
        "Special Notes": "Amplifies signals across galaxies, utilizing natural cosmic phenomena."
    },
    "Temporal Signal Devices": {
        "Common Uses": "Time-Shifted Communication",
        "Special Notes": "Allows messages to be sent backwards or forwards in time over short intervals."
    },
    "Subspace Whisper Networks": {
        "Common Uses": "Covert Espionage",
        "Special Notes": "Undetectable communication channels using subspace frequencies."
    },
    "Gravitational Comm Arrays": {
        "Common Uses": "Long-Range Communication",
        "Special Notes": "Utilizes gravitational waves for transmitting data over vast cosmic distances."
    },
    "Dark Matter Transceivers": {
        "Common Uses": "High-Density Data Transmission",
        "Special Notes": "Employs dark matter properties to handle massive amounts of data."
    },
    "Photon Burst Messengers": {
        "Common Uses": "Rapid Information Transfer",
        "Special Notes": "Uses photon bursts to transmit data at the speed of light."
    },
    "Bio-Synthetic Signalers": {
        "Common Uses": "Organic Communication",
        "Special Notes": "Integrates organic components for a natural form of signal transmission."
    },
    "Interdimensional Beacons": {
        "Common Uses": "Cross-Reality Messages",
        "Special Notes": "Capable of sending signals to and from different dimensions or realities."
    },
    "Quantum Foam Transponders": {
        "Common Uses": "Ultra-Secure Communication",
        "Special Notes": "Operates on the principles of quantum foam for unbreakable encryption."
    },
    "Cosmic String Receivers": {
        "Common Uses": "Fundamental Force Communication",
        "Special Notes": "Taps into cosmic strings for a novel method of data transmission."
    },
    "Etheric Wave Modulators": {
        "Common Uses": "Ether-Based Transmission",
        "Special Notes": "Utilizes the theoretical concept of ether for communication across space-time fabric."
    }
}














hazardous_materials = {
    "Radioactive Isotopes": {
        "Common Uses": "Industrial Processes",
        "Special Notes": "Used in power generation and medical applications, but highly dangerous."
    },
    "Toxic Waste": {
        "Common Uses": "Waste Disposal",
        "Special Notes": "Byproduct of various industrial activities, requires careful handling."
    },
    "Corrosive Chemicals": {
        "Common Uses": "Weaponry",
        "Special Notes": "Used in manufacturing and military applications, poses serious safety risks."
    },
    "Neurotoxins": {
        "Common Uses": "Chemical Warfare",
        "Special Notes": "Extremely lethal, used in illegal weaponry and assassination tools."
    },
    "Unstable Plasma": {
        "Common Uses": "Experimental Tech",
        "Special Notes": "Highly volatile, used in advanced energy research."
    },
    "Nanobot Swarms": {
        "Common Uses": "Industrial Sabotage",
        "Special Notes": "Capable of dismantling structures at the molecular level, illegal in many jurisdictions."
    },
    "Acidic Compounds": {
        "Common Uses": "Material Processing",
        "Special Notes": "Used in mining and refining, but can cause severe burns and environmental damage."
    },
    "Biological Agents": {
        "Common Uses": "Biological Warfare",
        "Special Notes": "Contains pathogens, restricted under intergalactic biohazard protocols."
    },
    "Electromagnetic Pulse Bombs": {
        "Common Uses": "Electronic Disruption",
        "Special Notes": "Can disable all electronic devices in their blast radius, highly regulated."
    },
    "Quantum Destabilizers": {
        "Common Uses": "Advanced Weaponry",
        "Special Notes": "Disrupts quantum fields, extremely dangerous and forbidden in many systems."
    },
    "Thermite Charges": {
        "Common Uses": "Demolition",
        "Special Notes": "Used for controlled demolitions but can be repurposed for destructive uses."
    },
    "Singularity Grenades": {
        "Common Uses": "Tactical Warfare",
        "Special Notes": "Creates temporary micro-black holes, use is controversial and heavily regulated."
    },
    "Radiation Emitters": {
        "Common Uses": "Industrial",
        "Special Notes": "Used in various applications, but prolonged exposure is harmful."
    },
    "Hyperacidic Solvents": {
        "Common Uses": "Material Decomposition",
        "Special Notes": "Capable of dissolving almost any material, extremely hazardous."
    },
    "Psychotropic Aerosols": {
        "Common Uses": "Crowd Control",
        "Special Notes": "Used for incapacitating individuals, legality varies by region."
    }
}


organic_materials = {
    "Seeds": {
        "Common Uses": "Terraforming",
        "Special Notes": "Diverse varieties adapted for different planetary ecosystems."
    },
    "Microbial Cultures": {
        "Common Uses": "Agriculture",
        "Special Notes": "Used for soil enrichment and biodegradation processes."
    },
    "Genetic Templates": {
        "Common Uses": "Biotech",
        "Special Notes": "Blueprints for creating or modifying organic life forms."
    },
    "Algal Strains": {
        "Common Uses": "Biofuel Production",
        "Special Notes": "Efficiently convert sunlight and CO2 into biofuels."
    },
    "Bioengineered Fertilizers": {
        "Common Uses": "Enhanced Agriculture",
        "Special Notes": "Customized for specific crops, improve yield and resilience."
    },
    "Splicing Enzymes": {
        "Common Uses": "Genetic Engineering",
        "Special Notes": "Key components in cutting-edge genetic modification techniques."
    },
    "Stem Cell Cultures": {
        "Common Uses": "Regenerative Medicine",
        "Special Notes": "Capable of differentiating into a variety of cell types for medical treatments."
    },
    "Symbiotic Bacteria": {
        "Common Uses": "Waste Recycling",
        "Special Notes": "Break down organic waste, useful in closed-loop life support systems."
    },
    "Xenoflora Samples": {
        "Common Uses": "Exotic Agriculture",
        "Special Notes": "Plant species from different planets, offering unique agricultural properties."
    },
    "Pollinator Drones": {
        "Common Uses": "Automated Agriculture",
        "Special Notes": "Robotic insects designed to pollinate crops in controlled environments."
    },
    "Tissue Regeneration Gels": {
        "Common Uses": "Medical Treatment",
        "Special Notes": "Accelerate healing processes and tissue regeneration."
    },
    "Mycorrhizal Networks": {
        "Common Uses": "Soil Health",
        "Special Notes": "Fungi that form symbiotic relationships with plants, enhancing nutrient uptake."
    },
    "Photosynthetic Bacterium": {
        "Common Uses": "Oxygen Production",
        "Special Notes": "Utilized in life support systems for oxygen generation."
    },
    "Bioluminescent Algae": {
        "Common Uses": "Natural Lighting",
        "Special Notes": "Used for sustainable, low-energy illumination."
    },
    "Adaptive Coral Polyps": {
        "Common Uses": "Marine Ecosystems",
        "Special Notes": "Engineered to build reefs and support marine life in diverse water conditions."
    }
}


data_resources = {
    "Star Maps": {
        "Common Uses": "Navigation",
        "Special Notes": "Detailed charts of star systems, essential for space travel."
    },
    "Encrypted Databases": {
        "Common Uses": "Information Trading",
        "Special Notes": "Contains sensitive information, highly secure and sought after."
    },
    "Scientific Research": {
        "Common Uses": "Academic Study",
        "Special Notes": "Valuable findings from various fields of study."
    },
    "Historical Archives": {
        "Common Uses": "Education",
        "Special Notes": "Comprehensive records of historical events and civilizations."
    },
    "Galactic Trade Records": {
        "Common Uses": "Market Analysis",
        "Special Notes": "Data on trade flows and economic trends across the galaxy."
    },
    "Biological Data Banks": {
        "Common Uses": "Medical Research",
        "Special Notes": "Genetic and medical information from countless species."
    },
    "Astronomical Observations": {
        "Common Uses": "Research",
        "Special Notes": "Data from space telescopes and observatories, crucial for understanding the cosmos."
    },
    "Quantum Encryption Keys": {
        "Common Uses": "Security",
        "Special Notes": "Advanced cryptography tools, nearly impossible to crack."
    },
    "Military Intelligence": {
        "Common Uses": "Strategic Planning",
        "Special Notes": "Sensitive information on military capabilities and plans."
    },
    "Artificial Intelligence Models": {
        "Common Uses": "AI Development",
        "Special Notes": "Complex algorithms and AI training data."
    },
    "Exoplanet Survey Data": {
        "Common Uses": "Exploration",
        "Special Notes": "Information on potentially habitable planets and resources."
    },
    "Cultural Anthologies": {
        "Common Uses": "Sociological Study",
        "Special Notes": "Comprehensive studies of different cultures and societies."
    },
    "Subspace Communication Logs": {
        "Common Uses": "Research",
        "Special Notes": "Data from communications using advanced subspace technology."
    },
    "Technological Blueprints": {
        "Common Uses": "Engineering",
        "Special Notes": "Designs for advanced technology, highly coveted in tech sectors."
    },
    "Dark Web Networks": {
        "Common Uses": "Underground Information",
        "Special Notes": "Access to the hidden parts of the galactic network, a hub for illicit activities."
    },

    "Multidimensional Physics Studies": {
        "Common Uses": "Theoretical Research",
        "Special Notes": "Cutting-edge research exploring the properties of multiple dimensions beyond our own."
    },
    "Quantum Consciousness Theory": {
        "Common Uses": "Neuroscience and AI Development",
        "Special Notes": "Exploration of consciousness from a quantum perspective, with applications in AI."
    },
    "Exotic Matter Analysis": {
        "Common Uses": "Material Science",
        "Special Notes": "Research into rare forms of matter, potentially altering the understanding of physics."
    },
    "Dark Energy Research Papers": {
        "Common Uses": "Astrophysics",
        "Special Notes": "Studies on the mysterious dark energy, aiming to uncover its role in cosmic expansion."
    },
    "Transpecies Genetics Reports": {
        "Common Uses": "Genetic Engineering",
        "Special Notes": "Research on genetic material from diverse alien species for advanced genetic modifications."
    },
    "Nanotechnology Development Data": {
        "Common Uses": "Manufacturing and Medicine",
        "Special Notes": "Detailed studies on the use of nanobots for medical and industrial purposes."
    },
    "Temporal Mechanics Research": {
        "Common Uses": "Time Travel Studies",
        "Special Notes": "Theoretical research into the possibility and implications of time manipulation."
    },
    "Interstellar Ecology Surveys": {
        "Common Uses": "Environmental Science",
        "Special Notes": "Studies of ecosystems on various planets, vital for understanding alien biomes."
    },
    "Subquantum Anomaly Analysis": {
        "Common Uses": "Quantum Physics",
        "Special Notes": "Investigation of phenomena at scales smaller than quantum particles."
    },
    "Hyperspace Navigation Techniques": {
        "Common Uses": "Astrogation",
        "Special Notes": "Advanced research into navigating through hyperspace, crucial for interstellar travel."
    }
}



construction_materials = {
    "Composite Alloys": {
        "Common Uses": "Building Space Stations",
        "Special Notes": "Strong yet lightweight, ideal for space structures."
    },
    "Nano-Cement": {
        "Common Uses": "Habitat Construction",
        "Special Notes": "Self-hardening and adaptable for various planetary conditions."
    },
    "Self-Assembling Scaffoldings": {
        "Common Uses": "Infrastructure Projects",
        "Special Notes": "Automated construction, reduces labor and time significantly."
    },
    "Smart Glass": {
        "Common Uses": "Building Envelopes",
        "Special Notes": "Transparency adjustable, energy-efficient, and insulating."
    },
    "Carbon Nanotubes": {
        "Common Uses": "Reinforcement",
        "Special Notes": "Incredibly strong, used in high-stress structural applications."
    },
    "Aerogel Insulation": {
        "Common Uses": "Thermal Insulation",
        "Special Notes": "Lightweight and highly effective, suitable for extreme environments."
    },
    "Polymer Composites": {
        "Common Uses": "Versatile Construction",
        "Special Notes": "Durable and resistant to various environmental factors."
    },
    "Shape-Memory Alloys": {
        "Common Uses": "Adaptive Structures",
        "Special Notes": "Metals that revert to their original shape, useful in dynamic designs."
    },
    "Quantum Dots": {
        "Common Uses": "Energy Systems",
        "Special Notes": "Tiny semiconductors that enhance solar panel efficiency."
    },
    "Magnetic Levitation Blocks": {
        "Common Uses": "Infrastructure Projects",
        "Special Notes": "Used in creating frictionless, efficient transportation systems."
    },
    "Radiation Shielding Tiles": {
        "Common Uses": "Space Habitats",
        "Special Notes": "Provides protection against cosmic and solar radiation."
    },
    "3D Printed Modules": {
        "Common Uses": "Rapid Construction",
        "Special Notes": "Enables quick assembly of complex structures on-site."
    },
    "Self-Healing Concrete": {
        "Common Uses": "Infrastructure Longevity",
        "Special Notes": "Concrete that repairs its own cracks, increasing durability."
    },
    "Liquid Metal": {
        "Common Uses": "Dynamic Structures",
        "Special Notes": "Metal that can be reshaped and solidified on command."
    },
    "Bioreactive Bricks": {
        "Common Uses": "Eco-Friendly Construction",
        "Special Notes": "Living bricks that can self-repair and adapt to environmental changes."
    },

    "Organometallic Frameworks": {
        "Common Uses": "Adaptive Construction",
        "Special Notes": "Hybrid materials combining metal ions and organic ligands, versatile in various building applications."
    },
    "Living Metal Alloys": {
        "Common Uses": "Self-Repairing Structures",
        "Special Notes": "Metallic compounds with organic properties, capable of self-repair and environmental adaptation."
    },
    "Bio-Responsive Steel": {
        "Common Uses": "Responsive Architecture",
        "Special Notes": "Steel infused with organic sensors, reacts to environmental changes for optimal stability."
    },
    "Mycelium Composites": {
        "Common Uses": "Eco-Friendly Building",
        "Special Notes": "Sustainable material made from fungal mycelium, strong and biodegradable."
    },
    "Photosynthetic Panels": {
        "Common Uses": "Energy Efficient Buildings",
        "Special Notes": "Incorporates organic photosynthetic elements, harnessing solar energy for power and air purification."
    },
    "Algae-Infused Concrete": {
        "Common Uses": "Eco-Building Projects",
        "Special Notes": "Concrete blended with algae, captures carbon dioxide and releases oxygen."
    },
    "Symbiotic Bricks": {
        "Common Uses": "Living Buildings",
        "Special Notes": "Bricks that house micro-ecosystems, contributing to local biodiversity and building health."
    },
    "Chloroplast-Embedded Glass": {
        "Common Uses": "Bio-Active Windows",
        "Special Notes": "Glass embedded with chloroplasts for oxygen production and light regulation."
    },
    "Bioluminescent Lighting Fixtures": {
        "Common Uses": "Natural Illumination",
        "Special Notes": "Use organic light sources for low-energy, ambient lighting."
    },
    "Adaptive Bio-Facades": {
        "Common Uses": "Dynamic Exteriors",
        "Special Notes": "Exterior surfaces that adapt to weather and light conditions, improving energy efficiency."
    }
}



illegal_goods = {
    "Narcotics": {
        "Common Uses": "Black Market",
        "Special Notes": "Highly addictive substances, illegal in most sectors."
    },
    "Contraband Tech": {
        "Common Uses": "Underworld Deals",
        "Special Notes": "Technological items banned due to their potential misuse."
    },
    "Smuggled Artifacts": {
        "Common Uses": "Black Market",
        "Special Notes": "Historical or cultural items illegally taken from their origins."
    },
    "Unlicensed Weapons": {
        "Common Uses": "Underworld Deals",
        "Special Notes": "Highly powerful weaponry, restricted in many systems."
    },
    "Hacked AI Cores": {
        "Common Uses": "Black Market",
        "Special Notes": "AI systems with removed safety protocols, highly illegal."
    },
    "Stolen Data": {
        "Common Uses": "Espionage",
        "Special Notes": "Confidential information, ranging from corporate secrets to government intelligence."
    },
    "Illegal Cybernetics": {
        "Common Uses": "Underground Clinics",
        "Special Notes": "Augmentations that enhance human capabilities beyond legal limits."
    },
    "Banned Chemicals": {
        "Common Uses": "Illegal Manufacturing",
        "Special Notes": "Substances used for creating dangerous drugs or weapons."
    },
    "Forged Documents": {
        "Common Uses": "Identity Fraud",
        "Special Notes": "Fake passports, licenses, and other official papers."
    },
    "Exotic Animals": {
        "Common Uses": "Illegal Pet Trade",
        "Special Notes": "Endangered species smuggled for private collectors."
    },
    "Black Market Software": {
        "Common Uses": "Hacking",
        "Special Notes": "Programs used for illicit activities like hacking or digital theft."
    },
    "Counterfeit Currency": {
        "Common Uses": "Financial Fraud",
        "Special Notes": "Fake money, a direct threat to economic stability."
    },
    "Clone Identification Chips": {
        "Common Uses": "Identity Theft",
        "Special Notes": "Used to replicate or steal digital identities."
    },
    "Restricted Pharmaceuticals": {
        "Common Uses": "Unlicensed Medicine",
        "Special Notes": "Medicines not approved for public use, potentially dangerous."
    },
    "Warp Drive Disruptors": {
        "Common Uses": "Sabotage",
        "Special Notes": "Illegal devices used to interfere with FTL travel."
    }
}

military_equipment = {
    "Laser Cannons": {
        "Common Uses": "Arming Ships",
        "Special Notes": "Standard offensive weaponry for most spacecraft."
    },
    "Shield Generators": {
        "Common Uses": "Planetary Defense",
        "Special Notes": "Provides a protective barrier against various attacks."
    },
    "Combat Drones": {
        "Common Uses": "Mercenary Activities",
        "Special Notes": "Unmanned units for reconnaissance and combat operations."
    },
    "Plasma Rifles": {
        "Common Uses": "Ground Combat",
        "Special Notes": "High-powered infantry weapon, effective against armored targets."
    },
    "EMP Disruptors": {
        "Common Uses": "Electronic Warfare",
        "Special Notes": "Used to disable enemy electronics and shield systems."
    },
    "Tactical Exosuits": {
        "Common Uses": "Special Operations",
        "Special Notes": "Enhances soldiers' physical abilities and provides additional protection."
    },
    "Ion Blasters": {
        "Common Uses": "Ship-to-Ship Combat",
        "Special Notes": "Effective at disabling enemy ship systems without causing hull damage."
    },
    "Stealth Field Generators": {
        "Common Uses": "Covert Operations",
        "Special Notes": "Renders a ship nearly invisible to most detection methods."
    },
    "Orbital Strike Weapons": {
        "Common Uses": "Planetary Assault",
        "Special Notes": "Capable of delivering devastating attacks from orbit."
    },
    "Automated Turrets": {
        "Common Uses": "Base Defense",
        "Special Notes": "Self-operating defense systems for stationary installations."
    },
    "Quantum Torpedoes": {
        "Common Uses": "Heavy Assault",
        "Special Notes": "Advanced torpedoes with massive destructive power."
    },
    "Cyberwarfare Kits": {
        "Common Uses": "Intelligence Gathering",
        "Special Notes": "Tools for hacking into enemy systems and gathering intel."
    },
    "Anti-Air Missiles": {
        "Common Uses": "Aerial Defense",
        "Special Notes": "Designed to target and destroy incoming airborne threats."
    },
    "Mobile Command Units": {
        "Common Uses": "Field Operations",
        "Special Notes": "Portable units equipped with communication and strategy tools."
    },
    "Infiltration Drones": {
        "Common Uses": "Espionage",
        "Special Notes": "Small, discreet drones used for spying and information gathering."
    }
}


research_materials = {
    "Exotic Matter": {
        "Common Uses": "Scientific Research",
        "Special Notes": "Rare and used in cutting-edge physics experiments."
    },
    "Genetic Samples": {
        "Common Uses": "Biological Research",
        "Special Notes": "Includes DNA from diverse species, used in genetics and medicine."
    },
    "Archaeological Finds": {
        "Common Uses": "Historical Study",
        "Special Notes": "Relics from ancient civilizations, valuable for historical research."
    },
    "Astrophysical Data": {
        "Common Uses": "Cosmology Research",
        "Special Notes": "Data from deep space observations, crucial for understanding the universe."
    },
    "Quantum Particles": {
        "Common Uses": "Quantum Physics",
        "Special Notes": "Used in experiments to explore quantum mechanics."
    },
    "Alien Flora Samples": {
        "Common Uses": "Exobiology",
        "Special Notes": "Plants from other worlds, studied for their unique properties."
    },
    "Meteorite Fragments": {
        "Common Uses": "Geological Research",
        "Special Notes": "Provides insights into the composition of other celestial bodies."
    },
    "Microbial Cultures": {
        "Common Uses": "Medical Research",
        "Special Notes": "Studied for developing new medicines and understanding diseases."
    },
    "Dark Energy Readings": {
        "Common Uses": "Theoretical Physics",
        "Special Notes": "Measurements of one of the universe's greatest mysteries."
    },
    "Nebula Gas Samples": {
        "Common Uses": "Astrochemistry",
        "Special Notes": "Collected from nebulae for chemical analysis."
    },
    "Cryogenically Preserved Specimens": {
        "Common Uses": "Biological Study",
        "Special Notes": "Species preserved at low temperatures for future research."
    },
    "Artificial Intelligence Algorithms": {
        "Common Uses": "AI Development",
        "Special Notes": "Advanced algorithms used to enhance AI capabilities."
    },
    "Subspace Anomaly Data": {
        "Common Uses": "Wormhole Research",
        "Special Notes": "Information on phenomena that could enable faster-than-light travel."
    },
    "Gravitational Wave Recordings": {
        "Common Uses": "Space-Time Research",
        "Special Notes": "Used to study massive cosmic events like black hole mergers."
    },
    "Synthetic Bio-Materials": {
        "Common Uses": "Regenerative Medicine",
        "Special Notes": "Engineered tissues and organs for medical research and transplants."
    }
}


cultural_artifacts = {
    "Ancient Relics": {
        "Common Uses": "Museums",
        "Special Notes": "Artifacts from extinct civilizations, highly prized by historians."
    },
    "Artistic Works": {
        "Common Uses": "Collectors",
        "Special Notes": "Includes paintings, sculptures, and other forms of art from various cultures."
    },
    "Historical Documents": {
        "Common Uses": "Academic Study",
        "Special Notes": "Rare manuscripts and scrolls containing valuable historical information."
    },
    "Alien Sculptures": {
        "Common Uses": "Museums",
        "Special Notes": "Artistic creations from alien species, unique and enigmatic."
    },
    "Time-Capsules": {
        "Common Uses": "Academic Study",
        "Special Notes": "Preserved containers with items from specific eras, offering insights into past cultures."
    },
    "Galactic Maps": {
        "Common Uses": "Collectors",
        "Special Notes": "Ancient star charts showing historical astro-navigation routes."
    },
    "Ceremonial Attires": {
        "Common Uses": "Exhibitions",
        "Special Notes": "Traditional clothing from various cultures, rich in history."
    },
    "Mythological Artifacts": {
        "Common Uses": "Museums",
        "Special Notes": "Objects believed to have mythical powers or significance."
    },
    "Ancient Weaponry": {
        "Common Uses": "Collectors",
        "Special Notes": "Historical weapons, often seen as symbols of power."
    },
    "Lost Language Tablets": {
        "Common Uses": "Linguistic Research",
        "Special Notes": "Contain inscriptions in languages no longer spoken."
    },
    "Holographic Histories": {
        "Common Uses": "Educational",
        "Special Notes": "Interactive holograms depicting significant historical events."
    },
    "Interstellar Diplomatic Gifts": {
        "Common Uses": "Cultural Study",
        "Special Notes": "Gifts exchanged between different species, representing peace or alliance."
    },
    "Cultural Music Instruments": {
        "Common Uses": "Musical Study",
        "Special Notes": "Instruments that are integral to the musical traditions of various civilizations."
    },
    "Sacred Texts": {
        "Common Uses": "Religious Study",
        "Special Notes": "Holy scriptures and texts from different belief systems across the galaxy."
    },
    "Architectural Blueprints": {
        "Common Uses": "Academic Study",
        "Special Notes": "Designs of historically significant buildings or structures."
    },
    "Virtual Reality Archives": {
        "Common Uses": "Interactive Learning",
        "Special Notes": "VR experiences that recreate historical or cultural events."
    },
    "Cosmic Art Installations": {
        "Common Uses": "Public Displays",
        "Special Notes": "Large-scale art pieces, often displayed in space for public viewing."
    },
    "Historic Spacecraft Models": {
        "Common Uses": "Collectors",
        "Special Notes": "Scale models of famous spacecraft used in historic missions."
    },
    "Intergalactic Heritage Sites": {
        "Common Uses": "Tourism",
        "Special Notes": "Locations of significant cultural or historical importance."
    }
}


energy_sources = {
    "Fusion Cells": {
        "Common Uses": "Power Generation",
        "Special Notes": "Widely used for clean and efficient energy production."
    },
    "Antimatter Containers": {
        "Common Uses": "Ship Fuel",
        "Special Notes": "Highly efficient, but requires extreme caution in handling."
    },
    "Solar Panels": {
        "Common Uses": "Industrial Energy",
        "Special Notes": "Renewable energy source, commonly used on planets and space stations."
    },
    "Zero-Point Energy Modules": {
        "Common Uses": "Power Generation",
        "Special Notes": "Harvests energy from quantum vacuum fluctuations, cutting-edge technology."
    },
    "Quantum Batteries": {
        "Common Uses": "Portable Power",
        "Special Notes": "Extremely high-capacity energy storage in a compact form."
    },
    "Dark Energy Extractors": {
        "Common Uses": "Power Generation",
        "Special Notes": "Experimental technology harnessing the energy of dark energy."
    },
    "Gravitational Power Generators": {
        "Common Uses": "Industrial Energy",
        "Special Notes": "Utilizes gravitational forces to generate large amounts of energy."
    },
    "Plasma Reactors": {
        "Common Uses": "Ship Fuel",
        "Special Notes": "Provides high thrust and efficiency, used in advanced spacecraft."
    },
    "Thermal Converters": {
        "Common Uses": "Power Generation",
        "Special Notes": "Converts heat from planetary cores or stars into usable energy."
    },
    "Tachyon Accelerators": {
        "Common Uses": "Research and Power",
        "Special Notes": "Advanced concept for harnessing energy from faster-than-light particles."
    },
    "Neutrino Harvesters": {
        "Common Uses": "Ambient Energy Collection",
        "Special Notes": "Captures and converts neutrinos into a usable form of energy."
    },
    "Magnetic Field Inducers": {
        "Common Uses": "Power Generation",
        "Special Notes": "Generates energy through the manipulation of planetary magnetic fields."
    },
    "Nuclear Pulse Units": {
        "Common Uses": "Ship Fuel",
        "Special Notes": "Older technology, provides substantial thrust for interstellar travel."
    },
    "Ion Drives": {
        "Common Uses": "Ship Propulsion",
        "Special Notes": "Efficient for long-distance space travel, with moderate energy requirements."
    },
    "Dyson Sphere Segments": {
        "Common Uses": "Megastructure Power",
        "Special Notes": "Part of a hypothetical megastructure to harness the energy of a star."
    },

    "Mycelial Network Drive": {
        "Common Uses": "Advanced Space Travel",
        "Special Notes": "Utilizes an interdimensional mycelial network for instantaneous travel across vast distances."
    },
    "Quantum Singularity Reactors": {
        "Common Uses": "Power Generation",
        "Special Notes": "Harnesses energy from artificially created micro black holes, extremely efficient."
    },
    "Subspace Energy Extractors": {
        "Common Uses": "Power Generation",
        "Special Notes": "Extracts energy from subspace anomalies, a relatively new and evolving technology."
    },
    "Dark Matter Converters": {
        "Common Uses": "High-Efficiency Fuel",
        "Special Notes": "Converts dark matter into immense energy, theoretical and highly sought after."
    },
    "Galactic Core Batteries": {
        "Common Uses": "Massive Power Reserves",
        "Special Notes": "Capable of storing and utilizing energy drawn directly from galactic cores."
    },
    "Chrono-Energetic Cells": {
        "Common Uses": "Temporal Manipulation and Power",
        "Special Notes": "Advanced cells that can store energy derived from time fluctuations, highly experimental."
    },
    "Wormhole Power Generators": {
        "Common Uses": "Interstellar Energy Transfer",
        "Special Notes": "Generates power by stabilizing and harnessing energy from natural wormholes."
    },
    "Cosmic Ray Collectors": {
        "Common Uses": "Space-Based Energy Harvesting",
        "Special Notes": "Collects and converts high-energy cosmic rays into usable power."
    },
    "Stellar Wind Harvesters": {
        "Common Uses": "Renewable Energy",
        "Special Notes": "Captures and utilizes stellar winds from stars, efficient for space stations in close orbits."
    },
    "Interdimensional Rift Tappers": {
        "Common Uses": "Exotic Power Generation",
        "Special Notes": "Draws power from interdimensional rifts, a highly advanced and risky technology."
    }
}



medicinal_products = {
    "Pharmaceuticals": {
        "Common Uses": "Healthcare",
        "Special Notes": "Wide range of medicines for various ailments, subject to strict regulations."
    },
    "Medical Equipment": {
        "Common Uses": "Healthcare",
        "Special Notes": "Includes advanced diagnostic and surgical tools."
    },
    "Biotech Implants": {
        "Common Uses": "Enhancements",
        "Special Notes": "Used for augmenting human capabilities or treating injuries."
    },
    "Regenerative Serums": {
        "Common Uses": "Healing",
        "Special Notes": "Promotes rapid healing of wounds and regeneration of tissues."
    },
    "Nanomedical Robots": {
        "Common Uses": "Healthcare",
        "Special Notes": "Tiny robots for precise surgical procedures and internal repairs."
    },
    "Genetic Modification Kits": {
        "Common Uses": "Enhancements",
        "Special Notes": "Customizable kits for genetic enhancements, highly regulated."
    },
    "Cybernetic Prosthetics": {
        "Common Uses": "Life Support",
        "Special Notes": "Advanced prosthetics that restore or enhance physical functions."
    },
    "Neural Stimulators": {
        "Common Uses": "Healthcare",
        "Special Notes": "Devices that help in recovering from neural injuries or disorders."
    },
    "Anti-Radiation Medication": {
        "Common Uses": "Healthcare",
        "Special Notes": "Essential for treatment and protection in high-radiation environments."
    },
    "Bionic Organs": {
        "Common Uses": "Life Support",
        "Special Notes": "Synthetic organs that mimic the function of natural ones."
    },
    "Vaccination Drones": {
        "Common Uses": "Healthcare",
        "Special Notes": "Automated drones for mass immunization, especially in outbreak areas."
    },
    "Telemedicine Kits": {
        "Common Uses": "Remote Healthcare",
        "Special Notes": "Enables medical consultations and basic treatment in remote locations."
    },
    "Cryogenic Medical Pods": {
        "Common Uses": "Life Support",
        "Special Notes": "Used for preserving life during critical medical conditions or deep space travel."
    },
    "Molecular Scanners": {
        "Common Uses": "Diagnostics",
        "Special Notes": "Advanced devices for detailed molecular analysis of diseases."
    },
    "Psychoactive Compounds": {
        "Common Uses": "Therapeutic",
        "Special Notes": "Regulated substances used for treating various mental health conditions."
    },
    "Neural Harmonizers": {
        "Common Uses": "Mental Health",
        "Special Notes": "Devices that synchronize brain waves to alleviate stress and anxiety disorders."
    },
    "Quantum Consciousness Expanders": {
        "Common Uses": "Cognitive Enhancement",
        "Special Notes": "Uses quantum algorithms to enhance perception and cognitive abilities."
    },
    "Emotion Regulators": {
        "Common Uses": "Emotional Balance",
        "Special Notes": "Implants that help regulate and stabilize emotional states."
    },
    "Mindfulness Nanobots": {
        "Common Uses": "Mental Wellness",
        "Special Notes": "Nanobots that stimulate neural pathways to promote mindfulness and mental clarity."
    },
    "Psychoactive Synthesizers": {
        "Common Uses": "Therapeutic Treatment",
        "Special Notes": "Customizes psychoactive compounds specific to patient's neural profile."
    },
    "Hyperspace Dream Inducers": {
        "Common Uses": "Sleep Therapy",
        "Special Notes": "Induces deep, restorative sleep with vivid, controlled dreamscapes."
    },
    "Cognitive Rejuvenation Pods": {
        "Common Uses": "Memory Care",
        "Special Notes": "Advanced chambers designed to rejuvenate and enhance memory retention."
    },
    "Empathy Amplifiers": {
        "Common Uses": "Social Therapy",
        "Special Notes": "Enhances empathy and understanding in interpersonal therapy."
    },
    "Virtual Reality Therapy Suites": {
        "Common Uses": "Holistic Treatment",
        "Special Notes": "Immersive environments for comprehensive mental health therapy."
    },
    "Transcendental Meditation Interfaces": {
        "Common Uses": "Stress Relief",
        "Special Notes": "Direct neural interfaces that guide users into deep meditative states."
    }
}


foodstuffs = {
    "Synthetic Meat": {
        "Common Uses": "Consumption",
        "Special Notes": "Protein-rich alternative to traditional meat, environmentally friendly."
    },
    "Hydroponic Vegetables": {
        "Common Uses": "Consumption",
        "Special Notes": "Grown in nutrient solutions, suitable for space agriculture."
    },
    "Nutrient Packs": {
        "Common Uses": "Consumption",
        "Special Notes": "Compact and efficient source of essential nutrients."
    },
    "Algae-Based Foods": {
        "Common Uses": "Consumption",
        "Special Notes": "Sustainable and versatile, available in various flavors."
    },
    "Space Honey": {
        "Common Uses": "Consumption",
        "Special Notes": "Produced by genetically engineered space bees, known for its unique taste."
    },
    "Lab-Grown Fruits": {
        "Common Uses": "Consumption",
        "Special Notes": "Cultivated in controlled environments, offering a variety of flavors."
    },
    "Protein Bars": {
        "Common Uses": "Consumption",
        "Special Notes": "Energy-rich and convenient for travelers and explorers."
    },
    "Vitamin Supplements": {
        "Common Uses": "Consumption",
        "Special Notes": "Essential for maintaining health in low-gravity environments."
    },
    "Cultured Dairy Products": {
        "Common Uses": "Consumption",
        "Special Notes": "Includes cheeses and yogurts made from synthetic milk."
    },
    "Exotic Spices": {
        "Common Uses": "Culinary",
        "Special Notes": "Rare spices from distant planets, highly sought after for gourmet cooking."
    },
    "Aeroponic Grains": {
        "Common Uses": "Consumption",
        "Special Notes": "Efficiently grown in air or mist environments, staple food source."
    },
    "Emergency Rations": {
        "Common Uses": "Survival",
        "Special Notes": "Long-lasting and nutrient-dense, used in emergency situations."
    },
    "GMO Superfoods": {
        "Common Uses": "Consumption",
        "Special Notes": "Genetically modified for enhanced nutritional value."
    },
    "Zero-G Coffee Beans": {
        "Common Uses": "Consumption",
        "Special Notes": "Grown in microgravity, known for its rich and smooth flavor."
    },
    "Synthetic Flavorings": {
        "Common Uses": "Culinary",
        "Special Notes": "Artificial flavors used to enhance the taste of space food."
    }
}



raw_materials_goods = {
    "Iron Ore": {
        "Common Uses": "Manufacturing",
        "Special Notes": "Essential for steel production, widely available."
    },
    "Hydrogen Fuel": {
        "Common Uses": "Fuel",
        "Special Notes": "Primary fuel source for many spacecraft, high demand."
    },
    "Titanium": {
        "Common Uses": "Construction",
        "Special Notes": "Strong and lightweight, used in advanced building projects."
    },
    "Copper": {
        "Common Uses": "Electronics",
        "Special Notes": "Critical in electrical equipment, moderately abundant."
    },
    "Silica": {
        "Common Uses": "Manufacturing",
        "Special Notes": "Used in producing glass and silicon chips."
    },
    "Helium-3": {
        "Common Uses": "Fuel",
        "Special Notes": "Rare, used in fusion reactors, high profit margins."
    },
    "Aluminum": {
        "Common Uses": "Manufacturing",
        "Special Notes": "Used in a wide range of industries, easily recyclable."
    },
    "Platinum": {
        "Common Uses": "Catalysts",
        "Special Notes": "Rare and valuable, used in various high-tech applications."
    },
    "Lithium": {
        "Common Uses": "Batteries",
        "Special Notes": "Key component in rechargeable batteries, increasing demand."
    },
    "Uranium": {
        "Common Uses": "Energy",
        "Special Notes": "Used in nuclear reactors, highly regulated."
    },
    "Quantum Crystals": {
        "Common Uses": "Quantum Computing",
        "Special Notes": "Extremely rare, used in advanced quantum processors."
    },
    "Neutronium": {
        "Common Uses": "Starship Hulls",
        "Special Notes": "Incredibly dense material, ideal for constructing spacecraft hulls."
    },
    "Dark Matter": {
        "Common Uses": "Energy",
        "Special Notes": "Highly speculative and valuable, used in experimental energy systems."
    },
    "Exotic Matter": {
        "Common Uses": "Warp Drives",
        "Special Notes": "Required for FTL travel, only obtainable in certain regions of space."
    },
    "Nanotubes": {
        "Common Uses": "Construction",
        "Special Notes": "Stronger than steel and lighter than air, used in cutting-edge architecture."
    },
    "Antimatter": {
        "Common Uses": "Power Generation",
        "Special Notes": "Extremely powerful and efficient energy source, dangerous to handle."
    },
    "Bio-Gel": {
        "Common Uses": "Medical",
        "Special Notes": "Revolutionary healing compound, accelerates cellular regeneration."
    },
    "Photonic Fibers": {
        "Common Uses": "Electronics",
        "Special Notes": "Used in ultrafast data transmission cables, more efficient than traditional materials."
    },
    "Zero-Point Modules": {
        "Common Uses": "Power Generation",
        "Special Notes": "Extracts energy from quantum vacuum fluctuations, very advanced technology."
    },
    "Nanite Clusters": {
        "Common Uses": "Manufacturing",
        "Special Notes": "Self-replicating nanobots used in automated production lines."
    }
}


technological_items = {
    "Quantum Chips": {
        "Common Uses": "Tech upgrades",
        "Special Notes": "Essential for high-speed computing."
    },
    "AI Cores": {
        "Common Uses": "Tech upgrades",
        "Special Notes": "Used in advanced robotics and AI systems."
    },
    "Advanced Sensors": {
        "Common Uses": "Research",
        "Special Notes": "Crucial for exploration and scientific data gathering."
    },
    "Holographic Interfaces": {
        "Common Uses": "Tech upgrades",
        "Special Notes": "Provides immersive interaction with technology."
    },
    "Neural Interfaces": {
        "Common Uses": "Research",
        "Special Notes": "Connects technology directly with the brain."
    },
    "Fusion Power Cells": {
        "Common Uses": "Tech upgrades",
        "Special Notes": "Highly efficient and clean energy source."
    },
    "FTL Drive Components": {
        "Common Uses": "Tech upgrades",
        "Special Notes": "Necessary for faster-than-light travel systems."
    },
    "Nanobot Assemblers": {
        "Common Uses": "Manufacturing",
        "Special Notes": "Enables precise construction at a molecular level."
    },
    "Cybersecurity Suites": {
        "Common Uses": "Tech upgrades",
        "Special Notes": "Critical for protection against hacking and cyber attacks."
    },
    "Photon Processors": {
        "Common Uses": "Tech upgrades",
        "Special Notes": "Ultrafast processors for complex computations."
    },
    "Virtual Reality Pods": {
        "Common Uses": "Entertainment",
        "Special Notes": "Offers fully immersive virtual experiences."
    },
    "Bio-Enhancement Kits": {
        "Common Uses": "Medical",
        "Special Notes": "Used for augmenting human capabilities."
    },
    "Anti-Gravity Generators": {
        "Common Uses": "Tech upgrades",
        "Special Notes": "Allows for creation of gravity-free environments."
    },
    "Teleportation Arrays": {
        "Common Uses": "Transport",
        "Special Notes": "Facilitates instant travel over short distances."
    },
    "Energy Shields": {
        "Common Uses": "Defense",
        "Special Notes": "Provides a protective barrier against various threats."
    },
    "Space-Time Modulators": {
        "Common Uses": "Research",
        "Special Notes": "Experimental tech for studying and manipulating space-time."
    },
    "Subspace Communicators": {
        "Common Uses": "Communication",
        "Special Notes": "Enables faster-than-light communication across galaxies."
    },
    "Quantum Encoders": {
        "Common Uses": "Security",
        "Special Notes": "Utilized for unbreakable data encryption."
    },
    "Exoplanetary Mappers": {
        "Common Uses": "Exploration",
        "Special Notes": "Advanced systems for charting new planets and star systems."
    },
    "Temporal Sensors": {
        "Common Uses": "Research",
        "Special Notes": "Used for detecting and analyzing temporal anomalies."
    }
}


manufactured_goods = {
    "Spacecraft Parts": {
        "Common Uses": "Repairs",
        "Special Notes": "Essential for maintenance and upgrading of various spacecraft."
    },
    "Electronics": {
        "Common Uses": "Upgrades",
        "Special Notes": "Used in a wide range of tech applications, from computers to advanced sensors."
    },
    "Machinery": {
        "Common Uses": "Industrial",
        "Special Notes": "Vital for construction and industrial production."
    },
    "Quantum Computers": {
        "Common Uses": "Data Processing",
        "Special Notes": "Used for advanced computing tasks, crucial for research and navigation systems."
    },
    "Fusion Reactors": {
        "Common Uses": "Energy",
        "Special Notes": "Provides clean and efficient power for various applications."
    },
    "Nanorobotics": {
        "Common Uses": "Manufacturing",
        "Special Notes": "Enables precision manufacturing at microscopic levels."
    },
    "Holographic Displays": {
        "Common Uses": "Communication",
        "Special Notes": "Offers advanced interactive visual communication solutions."
    },
    "Force Field Generators": {
        "Common Uses": "Defense",
        "Special Notes": "Provides protective barriers for spacecraft and installations."
    },
    "Teleportation Devices": {
        "Common Uses": "Transport",
        "Special Notes": "Enables instant transportation of goods and personnel."
    },
    "Neural Implants": {
        "Common Uses": "Medical",
        "Special Notes": "Enhances cognitive abilities and treats various neurological disorders."
    },
    "Anti-Gravity Modules": {
        "Common Uses": "Construction",
        "Special Notes": "Utilized in building advanced structures and vehicles."
    },
    "Photon Cannons": {
        "Common Uses": "Weaponry",
        "Special Notes": "High-energy weapons used for both offense and defense in space battles."
    },
    "Warp Drive Engines": {
        "Common Uses": "Space Travel",
        "Special Notes": "Allows faster-than-light travel, essential for interstellar journeys."
    },
    "Artificial Intelligence Cores": {
        "Common Uses": "Automation",
        "Special Notes": "Forms the brain of automated systems and robots."
    },
    "Bionic Prosthetics": {
        "Common Uses": "Medical",
        "Special Notes": "High-tech replacements for lost limbs, enhancing physical capabilities."
    },
    "Cloaking Devices": {
        "Common Uses": "Stealth",
        "Special Notes": "Advanced technology that renders spacecraft invisible to most sensors."
    },
    "Interstellar Comms Arrays": {
        "Common Uses": "Communication",
        "Special Notes": "Enables real-time communication across vast interstellar distances."
    },
    "Graviton Beam Projectors": {
        "Common Uses": "Industrial",
        "Special Notes": "Utilized in space construction, capable of moving large objects with precision."
    },
    "Cybernetic AI Enhancements": {
        "Common Uses": "Upgrades",
        "Special Notes": "Augments AI capabilities, leading to smarter and more autonomous systems."
    },
    "Temporal Navigators": {
        "Common Uses": "Time Travel",
        "Special Notes": "Experimental devices allowing for limited manipulation of time."
    },
    "Energy Shield Emitter": {
        "Common Uses": "Defense",
        "Special Notes": "Creates a protective energy barrier around objects, highly effective against various attacks."
    },
    "Synthetic Atmosphere Processors": {
        "Common Uses": "Terraforming",
        "Special Notes": "Critical for creating habitable environments on otherwise uninhabitable planets."
    },
    "Quantum Encryption Modules": {
        "Common Uses": "Security",
        "Special Notes": "Provides unbreakable encryption for communications and data storage."
    },
    "Multi-Dimensional Scanners": {
        "Common Uses": "Exploration",
        "Special Notes": "Capable of scanning across various dimensions, revealing hidden or cloaked objects."
    },
    "Bio-Synthetic Organ Fabricators": {
        "Common Uses": "Medical",
        "Special Notes": "Used in medical facilities to create organic replacements for damaged organs."
    }
}

luxury_items = {
    "Fine Art": {
        "Common Uses": "Trade with affluent clients",
        "Special Notes": "Includes rare paintings and sculptures, highly prized by collectors."
    },
    "Rare Wines": {
        "Common Uses": "Gifts",
        "Special Notes": "Aged wines from renowned planets, valued for their exquisite taste."
    },
    "Jewelry": {
        "Common Uses": "Trade with affluent clients",
        "Special Notes": "Crafted using precious metals and gemstones, popular among the elite."
    },
    "Designer Clothing": {
        "Common Uses": "Fashion",
        "Special Notes": "High-fashion apparel from famous designers, a symbol of status."
    },
    "Exotic Pets": {
        "Common Uses": "Companionship",
        "Special Notes": "Rare and unique creatures from across the galaxy, sought after by exotic pet enthusiasts."
    },
    "Luxury Yachts": {
        "Common Uses": "Leisure",
        "Special Notes": "State-of-the-art spacecraft designed for comfort and style, favored by the wealthy."
    },
    "Gourmet Foods": {
        "Common Uses": "Culinary Delights",
        "Special Notes": "Includes delicacies from across the universe, highly sought after by epicureans."
    },
    "Holographic Art": {
        "Common Uses": "Decor",
        "Special Notes": "Futuristic art form that uses holograms to create stunning visual displays."
    },
    "Antique Relics": {
        "Common Uses": "Collectibles",
        "Special Notes": "Ancient artifacts from extinct civilizations, valuable to historians and collectors."
    },
    "Synthetic Diamonds": {
        "Common Uses": "Jewelry",
        "Special Notes": "Lab-grown diamonds that are indistinguishable from natural ones, eco-friendly and conflict-free."
    },
    "Virtual Reality Experiences": {
        "Common Uses": "Entertainment",
        "Special Notes": "Immersive and interactive virtual adventures, tailored for high-end clients."
    },
    "Custom Androids": {
        "Common Uses": "Personal Assistance",
        "Special Notes": "Bespoke androids designed for companionship and assistance, equipped with advanced AI."
    },
    "Nano-Jewelry": {
        "Common Uses": "Fashion",
        "Special Notes": "Jewelry embedded with nanotechnology, changing appearance on command."
    },
    "Intergalactic Cruise Tickets": {
        "Common Uses": "Travel",
        "Special Notes": "Passage aboard luxury space cruises, offering extraordinary cosmic tours."
    },
    "Astral Perfumes": {
        "Common Uses": "Personal Use",
        "Special Notes": "Rare and exquisite scents crafted from the essences of distant worlds."
    }
}




# goods = {
#     "HydrogenFuel": {"Type": "Raw Material", "Value": 10, "Weight": 1, "Quality": "Standard", "Durability": "Stable", "Rarity": "Common", "Legal Status": "Legal", "Production Requirements": "Simple", "Technological Level": "Low", "Cultural Value": "Low", "Expiration": "None"},
#     "QuantumChips": {"Type": "Technology", "Value": 500, "Weight": 0.5, "Quality": "High", "Durability": "Fragile", "Rarity": "Rare", "Legal Status": "Restricted", "Production Requirements": "Complex", "Technological Level": "High", "Cultural Value": "Low", "Expiration": "None"},
#     "LuxuryFoods": {"Type": "Foodstuffs", "Value": 100, "Weight": 2, "Quality": "Luxury", "Durability": "Perishable", "Rarity": "Uncommon", "Legal Status": "Legal", "Production Requirements": "Moderate", "Technological Level": "Medium", "Cultural Value": "High", "Expiration": "Short"},
#     "AlienArtifacts": {"Type": "Cultural", "Value": 1000, "Weight": 3, "Quality": "Varied", "Durability": "Durable", "Rarity": "Rare", "Legal Status": "Illegal", "Production Requirements": "N/A", "Technological Level": "Unknown", "Cultural Value": "Very High", "Expiration": "None"},
#     "MedicalSupplies": {"Type": "Medicinal", "Value": 200, "Weight": 1.5, "Quality": "High", "Durability": "Stable", "Rarity": "Common", "Legal Status": "Legal", "Production Requirements": "Complex", "Technological Level": "High", "Cultural Value": "Medium", "Expiration": "Moderate"},
#     "MilitaryHardware": {"Type": "Technology", "Value": 1000, "Weight": 5, "Quality": "High", "Durability": "Stable", "Rarity": "Rare", "Legal Status": "Restricted", "Production Requirements": "Complex", "Technological Level": "High", "Cultural Value": "Low", "Expiration": "None"},
#     "StellarMaps": {"Type": "Information", "Value": 300, "Weight": 0, "Quality": "High", "Durability": "N/A", "Rarity": "Uncommon", "Legal Status": "Legal", "Production Requirements": "Specialized", "Technological Level": "Medium", "Cultural Value": "Medium", "Expiration": "None"},
#     "RobotParts": {"Type": "Manufactured Goods", "Value": 150, "Weight": 5, "Quality": "Standard", "Durability": "Durable", "Rarity": "Common", "Legal Status": "Legal", "Production Requirements": "Moderate", "Technological Level": "High", "Cultural Value": "Low", "Expiration": "None"},
#     "BioGel": {"Type": "Medicinal", "Value": 250, "Weight": 2, "Quality": "High", "Durability": "Stable", "Rarity": "Uncommon", "Legal Status": "Restricted", "Production Requirements": "Complex", "Technological Level": "Advanced", "Cultural Value": "Low", "Expiration": "Long"},
#     "ExoticSpices": {"Type": "Luxury Items", "Value": 400, "Weight": 1, "Quality": "Luxury", "Durability": "Perishable", "Rarity": "Rare", "Legal Status": "Legal", "Production Requirements": "Simple", "Technological Level": "Low", "Cultural Value": "High", "Expiration": "Moderate"},
#     "NanoFibers": {"Type": "Technology", "Value": 600, "Weight": 0.2, "Quality": "High", "Durability": "Fragile", "Rarity": "Rare", "Legal Status": "Legal", "Production Requirements": "High-tech", "Technological Level": "Advanced", "Cultural Value": "Low", "Expiration": "None"},
#     "AncientManuscripts": {"Type": "Cultural", "Value": 800, "Weight": 3, "Quality": "Varied", "Durability": "Fragile", "Rarity": "Very Rare", "Legal Status": "Legal", "Production Requirements": "N/A", "Technological Level": "N/A", "Cultural Value": "Very High", "Expiration": "None"},
#     "RareMetals": {"Type": "Raw Material", "Value": 200, "Weight": 5, "Quality": "Standard", "Durability": "Stable", "Rarity": "Uncommon", "Legal Status": "Legal", "Production Requirements": "Simple", "Technological Level": "Low", "Cultural Value": "Low", "Expiration": "None"},
#     "PreciousMetals": {"Type": "Raw Material", "Value": 300, "Weight": 5, "Quality": "Standard", "Durability": "Stable", "Rarity": "Rare", "Legal Status": "Legal", "Production Requirements": "Simple", "Technological Level": "Low", "Cultural Value": "Low", "Expiration": "None"},
#     "DarkMatterSamples": {"Type": "Research Material", "Value": 1000, "Weight": 0.1, "Quality": "High", "Durability": "Stable", "Rarity": "Extremely Rare", "Legal Status": "Restricted", "Production Requirements": "Advanced", "Technological Level": "Very High", "Cultural Value": "Low", "Expiration": "None"},
#     "CyberneticImplants": {"Type": "Technology", "Value": 450, "Weight": 2, "Quality": "High", "Durability": "Durable", "Rarity": "Uncommon", "Legal Status": "Restricted", "Production Requirements": "Complex", "Technological Level": "High", "Cultural Value": "Medium", "Expiration": "None"},
#     "PlasmaCoils": {"Type": "Technology", "Value": 350, "Weight": 4, "Quality": "Standard", "Durability": "Durable", "Rarity": "Common", "Legal Status": "Legal", "Production Requirements": "Moderate", "Technological Level": "Medium", "Cultural Value": "Low", "Expiration": "None"},
#     "CryogenicContainers": {"Type": "Manufactured Goods", "Value": 200, "Weight": 6, "Quality": "Standard", "Durability": "Durable", "Rarity": "Common", "Legal Status": "Legal", "Production Requirements": "Simple", "Technological Level": "Medium", "Cultural Value": "Low", "Expiration": "None"},
#     "StarSteel": {"Type": "Manufactured Goods", "Value": 150, "Weight": 5, "Quality": "High", "Durability": "Durable", "Rarity": "Uncommon", "Legal Status": "Legal", "Production Requirements": "Advanced", "Technological Level": "Medium", "Cultural Value": "Low", "Expiration": "None"},
#     "CryoHerbs": {"Type": "Medicinal", "Value": 300, "Weight": 0.2, "Quality": "Premium", "Durability": "Perishable", "Rarity": "Rare", "Legal Status": "Legal", "Production Requirements": "Specific", "Technological Level": "High", "Cultural Value": "Medium", "Expiration": "Short"},
#     "HoloProjectors": {"Type": "Technology", "Value": 450, "Weight": 1.2, "Quality": "Standard", "Durability": "Moderate", "Rarity": "Common", "Legal Status": "Legal", "Production Requirements": "Moderate", "Technological Level": "High", "Cultural Value": "Medium", "Expiration": "None"},
#     "NeutroniumOre": {"Type": "Raw Material", "Value": 800, "Weight": 10, "Quality": "Raw", "Durability": "Stable", "Rarity": "Very Rare", "Legal Status": "Restricted", "Production Requirements": "Extreme", "Technological Level": "Advanced", "Cultural Value": "Low", "Expiration": "None"}
# }
