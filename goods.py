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
