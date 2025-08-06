"""
🔥 ENHANCED AI GAME SCRAPER - MULTIPLE TEMPLATES & SMART PROMPT MATCHING
Fixes the prompt customization issue by providing diverse game templates
"""

import requests
from bs4 import BeautifulSoup
import random
import re
from typing import Dict, List, Optional

class EnhancedAIGameScraper:
    def __init__(self):
        self.scraped_library = {
            'underwater': [],
            'medieval': [],
            'space': [],
            'platformer': [],
            'puzzle': [],
            'racing': [],
            'adventure': [],
            'default': []
        }
        self.initialize_templates()
    
    def initialize_templates(self):
        """Initialize diverse game templates for different themes"""
        
        # UNDERWATER TEMPLATES
        self.scraped_library['underwater'] = [
            {
                'name': 'Mermaid Treasure Hunt',
                'theme': 'underwater',
                'character': 'mermaid',
                'mechanics': ['swimming', 'treasure_collection', 'avoid_creatures'],
                'enemies': ['jellyfish', 'sharks', 'sea_monsters'],
                'collectibles': ['pearls', 'treasures', 'shells'],
                'background': 'deep_ocean_blue',
                'controls': 'arrow_keys',
                'objective': 'collect_treasures_avoid_enemies'
            },
            {
                'name': 'Deep Sea Explorer',
                'theme': 'underwater',
                'character': 'diver',
                'mechanics': ['diving', 'oxygen_management', 'exploration'],
                'enemies': ['electric_eels', 'octopus', 'sea_urchins'],
                'collectibles': ['artifacts', 'coins', 'gems'],
                'background': 'coral_reef',
                'controls': 'wasd_keys',
                'objective': 'explore_depths_find_artifacts'
            }
        ]
        
        # MEDIEVAL TEMPLATES
        self.scraped_library['medieval'] = [
            {
                'name': 'Dragon Slayer Quest',
                'theme': 'medieval',
                'character': 'knight',
                'mechanics': ['sword_combat', 'shield_blocking', 'castle_exploration'],
                'enemies': ['dragons', 'goblins', 'skeletons'],
                'collectibles': ['gold_coins', 'magic_potions', 'armor_pieces'],
                'background': 'stone_castle',
                'controls': 'arrow_keys_space',
                'objective': 'defeat_dragon_save_kingdom'
            },
            {
                'name': 'Castle Defense',
                'theme': 'medieval',
                'character': 'archer',
                'mechanics': ['bow_shooting', 'tower_defense', 'resource_management'],
                'enemies': ['orcs', 'trolls', 'dark_knights'],
                'collectibles': ['arrows', 'gold', 'power_ups'],
                'background': 'castle_walls',
                'controls': 'mouse_click',
                'objective': 'defend_castle_from_invasion'
            }
        ]
        
        # SPACE TEMPLATES
        self.scraped_library['space'] = [
            {
                'name': 'Galactic Battle',
                'theme': 'space',
                'character': 'spaceship',
                'mechanics': ['laser_shooting', 'dodging', 'power_ups'],
                'enemies': ['alien_ships', 'asteroids', 'space_pirates'],
                'collectibles': ['energy_cells', 'weapon_upgrades', 'shields'],
                'background': 'star_field',
                'controls': 'arrow_keys_space',
                'objective': 'defeat_alien_fleet'
            },
            {
                'name': 'Asteroid Miner',
                'theme': 'space',
                'character': 'mining_ship',
                'mechanics': ['mining', 'navigation', 'cargo_management'],
                'enemies': ['space_worms', 'pirates', 'meteor_showers'],
                'collectibles': ['minerals', 'crystals', 'fuel'],
                'background': 'asteroid_field',
                'controls': 'wasd_keys',
                'objective': 'mine_resources_survive'
            }
        ]
        
        # PLATFORMER TEMPLATES
        self.scraped_library['platformer'] = [
            {
                'name': 'Jungle Adventure',
                'theme': 'jungle',
                'character': 'explorer',
                'mechanics': ['jumping', 'vine_swinging', 'climbing'],
                'enemies': ['monkeys', 'snakes', 'spiders'],
                'collectibles': ['bananas', 'gems', 'keys'],
                'background': 'tropical_jungle',
                'controls': 'arrow_keys',
                'objective': 'reach_temple_collect_treasure'
            },
            {
                'name': 'Sky Runner',
                'theme': 'clouds',
                'character': 'winged_hero',
                'mechanics': ['flying', 'gliding', 'wind_currents'],
                'enemies': ['storm_clouds', 'lightning', 'wind_spirits'],
                'collectibles': ['star_fragments', 'wind_crystals', 'feathers'],
                'background': 'cloudy_sky',
                'controls': 'arrow_keys_space',
                'objective': 'navigate_sky_realm'
            }
        ]
        
        # PUZZLE TEMPLATES
        self.scraped_library['puzzle'] = [
            {
                'name': 'Gem Matcher',
                'theme': 'colorful',
                'character': 'cursor',
                'mechanics': ['matching', 'chain_reactions', 'combo_scoring'],
                'enemies': ['time_limit', 'locked_gems', 'obstacles'],
                'collectibles': ['gems', 'bonus_points', 'multipliers'],
                'background': 'jeweled_grid',
                'controls': 'mouse_click',
                'objective': 'match_gems_high_score'
            },
            {
                'name': 'Block Puzzle',
                'theme': 'geometric',
                'character': 'blocks',
                'mechanics': ['tetris_style', 'line_clearing', 'rotation'],
                'enemies': ['rising_blocks', 'time_pressure', 'complex_shapes'],
                'collectibles': ['points', 'level_ups', 'special_blocks'],
                'background': 'grid_pattern',
                'controls': 'arrow_keys',
                'objective': 'clear_lines_survive'
            }
        ]
        
        # RACING TEMPLATES
        self.scraped_library['racing'] = [
            {
                'name': 'Speed Racer',
                'theme': 'racing',
                'character': 'race_car',
                'mechanics': ['acceleration', 'steering', 'nitro_boost'],
                'enemies': ['other_cars', 'obstacles', 'oil_spills'],
                'collectibles': ['nitro', 'coins', 'checkpoints'],
                'background': 'race_track',
                'controls': 'arrow_keys',
                'objective': 'finish_first_place'
            }
        ]
        
        # ADVENTURE TEMPLATES
        self.scraped_library['adventure'] = [
            {
                'name': 'Treasure Hunter',
                'theme': 'adventure',
                'character': 'adventurer',
                'mechanics': ['exploration', 'puzzle_solving', 'combat'],
                'enemies': ['traps', 'guardians', 'wild_animals'],
                'collectibles': ['treasures', 'maps', 'tools'],
                'background': 'ancient_ruins',
                'controls': 'arrow_keys_space',
                'objective': 'find_legendary_treasure'
            }
        ]
        
        # DEFAULT TEMPLATE (fallback)
        self.scraped_library['default'] = [
            {
                'name': 'Classic Adventure',
                'theme': 'generic',
                'character': 'hero',
                'mechanics': ['movement', 'collection', 'avoidance'],
                'enemies': ['obstacles', 'enemies', 'hazards'],
                'collectibles': ['items', 'points', 'power_ups'],
                'background': 'colorful',
                'controls': 'arrow_keys',
                'objective': 'survive_and_score'
            }
        ]
    
    def find_matching_template(self, prompt: str) -> Dict:
        """Find the best matching template based on prompt keywords"""
        prompt_lower = prompt.lower()
        
        # UNDERWATER KEYWORDS
        underwater_keywords = ['underwater', 'ocean', 'sea', 'mermaid', 'fish', 'diving', 'submarine', 'coral', 'whale', 'dolphin', 'treasure', 'deep', 'aquatic']
        if any(keyword in prompt_lower for keyword in underwater_keywords):
            return random.choice(self.scraped_library['underwater'])
        
        # MEDIEVAL KEYWORDS
        medieval_keywords = ['medieval', 'knight', 'dragon', 'castle', 'sword', 'armor', 'kingdom', 'quest', 'magic', 'wizard', 'dungeon', 'fantasy', 'royal']
        if any(keyword in prompt_lower for keyword in medieval_keywords):
            return random.choice(self.scraped_library['medieval'])
        
        # SPACE KEYWORDS
        space_keywords = ['space', 'alien', 'spaceship', 'laser', 'galaxy', 'planet', 'star', 'rocket', 'astronaut', 'cosmic', 'nebula', 'asteroid', 'sci-fi']
        if any(keyword in prompt_lower for keyword in space_keywords):
            return random.choice(self.scraped_library['space'])
        
        # PLATFORMER KEYWORDS
        platformer_keywords = ['platformer', 'jumping', 'jungle', 'vine', 'climbing', 'running', 'adventure', 'explorer', 'banana', 'monkey', 'temple']
        if any(keyword in prompt_lower for keyword in platformer_keywords):
            return random.choice(self.scraped_library['platformer'])
        
        # PUZZLE KEYWORDS
        puzzle_keywords = ['puzzle', 'matching', 'gems', 'blocks', 'tetris', 'brain', 'logic', 'strategy', 'thinking', 'solve', 'pattern']
        if any(keyword in prompt_lower for keyword in puzzle_keywords):
            return random.choice(self.scraped_library['puzzle'])
        
        # RACING KEYWORDS
        racing_keywords = ['racing', 'car', 'speed', 'track', 'driving', 'fast', 'race', 'vehicle', 'motor', 'championship']
        if any(keyword in prompt_lower for keyword in racing_keywords):
            return random.choice(self.scraped_library['racing'])
        
        # ADVENTURE KEYWORDS
        adventure_keywords = ['adventure', 'exploration', 'treasure', 'hunt', 'discover', 'journey', 'quest', 'ancient', 'ruins', 'mystery']
        if any(keyword in prompt_lower for keyword in adventure_keywords):
            return random.choice(self.scraped_library['adventure'])
        
        # DEFAULT FALLBACK
        return random.choice(self.scraped_library['default'])
    
    def customize_template_with_prompt(self, template: Dict, prompt: str) -> Dict:
        """Customize the template based on specific prompt details"""
        customized = template.copy()
        prompt_lower = prompt.lower()
        
        # Extract specific elements from prompt
        if 'mermaid' in prompt_lower:
            customized['character'] = 'mermaid'
        elif 'knight' in prompt_lower:
            customized['character'] = 'knight'
        elif 'spaceship' in prompt_lower or 'pilot' in prompt_lower:
            customized['character'] = 'spaceship'
        elif 'explorer' in prompt_lower:
            customized['character'] = 'explorer'
        
        # Customize enemies based on prompt
        if 'dragon' in prompt_lower:
            if 'dragons' not in customized['enemies']:
                customized['enemies'].append('dragons')
        elif 'alien' in prompt_lower:
            if 'aliens' not in customized['enemies']:
                customized['enemies'].append('aliens')
        elif 'shark' in prompt_lower:
            if 'sharks' not in customized['enemies']:
                customized['enemies'].append('sharks')
        
        # Customize collectibles
        if 'treasure' in prompt_lower:
            if 'treasures' not in customized['collectibles']:
                customized['collectibles'].append('treasures')
        elif 'gold' in prompt_lower:
            if 'gold' not in customized['collectibles']:
                customized['collectibles'].append('gold')
        elif 'gem' in prompt_lower:
            if 'gems' not in customized['collectibles']:
                customized['collectibles'].append('gems')
        
        return customized
    
    def get_template_stats(self) -> Dict:
        """Get statistics about available templates"""
        stats = {}
        for category, templates in self.scraped_library.items():
            stats[category] = len(templates)
        return stats
    
    def get_total_templates(self) -> int:
        """Get total number of available templates"""
        return sum(len(templates) for templates in self.scraped_library.values())

# Initialize the enhanced scraper
enhanced_scraper = EnhancedAIGameScraper()

def get_game_template(prompt: str) -> Dict:
    """Main function to get a customized game template based on prompt"""
    # Find matching template
    base_template = enhanced_scraper.find_matching_template(prompt)
    
    # Customize based on prompt specifics
    customized_template = enhanced_scraper.customize_template_with_prompt(base_template, prompt)
    
    return customized_template

def get_scraper_stats() -> Dict:
    """Get scraper statistics"""
    return {
        'total_templates': enhanced_scraper.get_total_templates(),
        'categories': enhanced_scraper.get_template_stats(),
        'version': '2.0.0 - Enhanced Multi-Template'
    }

# Test the system
if __name__ == "__main__":
    test_prompts = [
        "Create a magical underwater adventure with mermaids and treasure hunting",
        "Create a medieval fantasy game with knights fighting dragons in a castle",
        "Create an epic space battle with alien ships and laser weapons",
        "Create a jungle platformer with jumping and vine swinging",
        "Create a colorful puzzle game with matching gems"
    ]
    
    print("🔥 ENHANCED AI GAME SCRAPER - TESTING")
    print("=" * 50)
    
    for prompt in test_prompts:
        template = get_game_template(prompt)
        print(f"\n📝 PROMPT: {prompt}")
        print(f"🎮 TEMPLATE: {template['name']}")
        print(f"🎨 THEME: {template['theme']}")
        print(f"👤 CHARACTER: {template['character']}")
        print(f"⚔️ ENEMIES: {', '.join(template['enemies'][:3])}")
        print(f"💎 COLLECTIBLES: {', '.join(template['collectibles'][:3])}")
        print("-" * 50)
    
    stats = get_scraper_stats()
    print(f"\n📊 SCRAPER STATS:")
    print(f"Total Templates: {stats['total_templates']}")
    print(f"Categories: {stats['categories']}")

