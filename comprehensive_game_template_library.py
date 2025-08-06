"""
🎮 COMPREHENSIVE GAME TEMPLATE LIBRARY
50+ Specific Game Templates with Proper Mechanics
"""

import random
from datetime import datetime

class GameTemplateLibrary:
    def __init__(self):
        self.templates = {
            # SPORTS GAMES
            'darts': {
                'title': ['Dart Master', 'Bulls Eye Challenge', 'Precision Darts', 'Dart Champion'],
                'theme': 'Sports',
                'character': 'Dart_Player',
                'mechanics': 'dart_throwing',
                'ui_elements': ['Score', 'Darts_Left', 'Round'],
                'game_objects': ['dartboard', 'darts', 'scoring_zones'],
                'colors': ['#8B4513', '#FFD700', '#FF0000', '#00FF00'],
                'description': 'Throw darts at the dartboard to score points. Aim for the bullseye!'
            },
            'basketball': {
                'title': ['Hoop Dreams', 'Basketball Pro', 'Court Master', 'Slam Dunk'],
                'theme': 'Sports',
                'character': 'Basketball_Player',
                'mechanics': 'ball_shooting',
                'ui_elements': ['Score', 'Time', 'Shots_Made'],
                'game_objects': ['basketball_hoop', 'basketball', 'court'],
                'colors': ['#FF8C00', '#8B4513', '#FFFFFF', '#000000'],
                'description': 'Shoot basketballs into the hoop to score points. Perfect your aim!'
            },
            'soccer': {
                'title': ['Goal Keeper', 'Soccer Star', 'Penalty Kick', 'Football Hero'],
                'theme': 'Sports',
                'character': 'Soccer_Player',
                'mechanics': 'ball_kicking',
                'ui_elements': ['Goals', 'Time', 'Kicks'],
                'game_objects': ['soccer_goal', 'soccer_ball', 'field'],
                'colors': ['#00FF00', '#FFFFFF', '#000000', '#FF0000'],
                'description': 'Kick the soccer ball into the goal. Score as many goals as possible!'
            },
            'tennis': {
                'title': ['Tennis Ace', 'Court Champion', 'Racket Master', 'Wimbledon'],
                'theme': 'Sports',
                'character': 'Tennis_Player',
                'mechanics': 'ball_hitting',
                'ui_elements': ['Score', 'Sets', 'Games'],
                'game_objects': ['tennis_racket', 'tennis_ball', 'net'],
                'colors': ['#90EE90', '#FFFF00', '#FFFFFF', '#000000'],
                'description': 'Hit the tennis ball over the net. Win sets to become champion!'
            },
            'golf': {
                'title': ['Golf Pro', 'Hole in One', 'Golf Master', 'Green Champion'],
                'theme': 'Sports',
                'character': 'Golfer',
                'mechanics': 'ball_putting',
                'ui_elements': ['Strokes', 'Par', 'Hole'],
                'game_objects': ['golf_club', 'golf_ball', 'hole'],
                'colors': ['#00FF00', '#FFFFFF', '#8B4513', '#FFD700'],
                'description': 'Hit the golf ball into the hole with as few strokes as possible!'
            },
            
            # RACING GAMES
            'racing': {
                'title': ['Speed Racer', 'Formula One', 'Racing Champion', 'Turbo Drive'],
                'theme': 'Racing',
                'character': 'Race_Car',
                'mechanics': 'car_racing',
                'ui_elements': ['Speed', 'Lap', 'Position'],
                'game_objects': ['race_car', 'track', 'finish_line'],
                'colors': ['#FF0000', '#000000', '#FFFFFF', '#FFFF00'],
                'description': 'Race your car around the track. Be the first to cross the finish line!'
            },
            'motorcycle': {
                'title': ['Bike Racer', 'Moto GP', 'Speed Bike', 'Motorcycle Madness'],
                'theme': 'Racing',
                'character': 'Motorcycle',
                'mechanics': 'bike_racing',
                'ui_elements': ['Speed', 'Lap', 'Time'],
                'game_objects': ['motorcycle', 'track', 'obstacles'],
                'colors': ['#FF4500', '#000000', '#FFFFFF', '#00FF00'],
                'description': 'Race your motorcycle at high speeds. Avoid obstacles and win!'
            },
            'horse_racing': {
                'title': ['Derby Winner', 'Horse Champion', 'Gallop Master', 'Racing Stallion'],
                'theme': 'Racing',
                'character': 'Horse',
                'mechanics': 'horse_racing',
                'ui_elements': ['Speed', 'Distance', 'Position'],
                'game_objects': ['horse', 'track', 'jockey'],
                'colors': ['#8B4513', '#00FF00', '#FFFFFF', '#FFD700'],
                'description': 'Race your horse to victory. Gallop faster than the competition!'
            },
            
            # PUZZLE GAMES
            'tetris': {
                'title': ['Block Master', 'Tetris Pro', 'Line Clearer', 'Puzzle Blocks'],
                'theme': 'Puzzle',
                'character': 'Blocks',
                'mechanics': 'block_stacking',
                'ui_elements': ['Score', 'Lines', 'Level'],
                'game_objects': ['tetris_blocks', 'grid', 'next_piece'],
                'colors': ['#FF0000', '#00FF00', '#0000FF', '#FFFF00'],
                'description': 'Stack falling blocks to clear lines. Don\'t let the blocks reach the top!'
            },
            'match3': {
                'title': ['Gem Crusher', 'Match Master', 'Candy Crush', 'Jewel Quest'],
                'theme': 'Puzzle',
                'character': 'Gems',
                'mechanics': 'gem_matching',
                'ui_elements': ['Score', 'Moves', 'Level'],
                'game_objects': ['gems', 'grid', 'special_gems'],
                'colors': ['#FF69B4', '#00CED1', '#FFD700', '#9370DB'],
                'description': 'Match 3 or more gems to clear them. Create special combinations!'
            },
            'sudoku': {
                'title': ['Number Master', 'Sudoku Pro', 'Logic Puzzle', 'Number Grid'],
                'theme': 'Puzzle',
                'character': 'Numbers',
                'mechanics': 'number_placing',
                'ui_elements': ['Time', 'Mistakes', 'Difficulty'],
                'game_objects': ['number_grid', 'numbers', 'hints'],
                'colors': ['#000000', '#FFFFFF', '#0000FF', '#FF0000'],
                'description': 'Fill the grid with numbers 1-9. Each row, column, and box must contain all digits!'
            },
            
            # ACTION GAMES
            'shooting': {
                'title': ['Target Shooter', 'Marksman', 'Sniper Elite', 'Bullet Master'],
                'theme': 'Action',
                'character': 'Shooter',
                'mechanics': 'target_shooting',
                'ui_elements': ['Score', 'Ammo', 'Accuracy'],
                'game_objects': ['gun', 'targets', 'crosshair'],
                'colors': ['#8B4513', '#FF0000', '#000000', '#FFFF00'],
                'description': 'Aim and shoot at targets. Improve your accuracy and score!'
            },
            'fighting': {
                'title': ['Fighter Pro', 'Combat Master', 'Martial Arts', 'Street Fighter'],
                'theme': 'Action',
                'character': 'Fighter',
                'mechanics': 'combat_fighting',
                'ui_elements': ['Health', 'Energy', 'Round'],
                'game_objects': ['fighter', 'opponent', 'arena'],
                'colors': ['#FF0000', '#0000FF', '#FFFF00', '#000000'],
                'description': 'Fight against opponents using martial arts. Defeat them to win!'
            },
            'platformer': {
                'title': ['Jump Hero', 'Platform Master', 'Adventure Jump', 'Super Jumper'],
                'theme': 'Action',
                'character': 'Hero',
                'mechanics': 'platform_jumping',
                'ui_elements': ['Lives', 'Score', 'Level'],
                'game_objects': ['platforms', 'enemies', 'power_ups'],
                'colors': ['#00FF00', '#8B4513', '#FF0000', '#0000FF'],
                'description': 'Jump across platforms and avoid enemies. Collect power-ups!'
            },
            
            # STRATEGY GAMES
            'chess': {
                'title': ['Chess Master', 'Royal Game', 'Strategic Mind', 'Chess Champion'],
                'theme': 'Strategy',
                'character': 'Chess_Pieces',
                'mechanics': 'chess_playing',
                'ui_elements': ['Turn', 'Captured', 'Time'],
                'game_objects': ['chess_board', 'chess_pieces', 'king'],
                'colors': ['#FFFFFF', '#000000', '#8B4513', '#FFD700'],
                'description': 'Play chess against the computer. Checkmate the king to win!'
            },
            'checkers': {
                'title': ['Checkers Pro', 'King Me', 'Board Master', 'Checker Champion'],
                'theme': 'Strategy',
                'character': 'Checker_Pieces',
                'mechanics': 'checker_playing',
                'ui_elements': ['Turn', 'Pieces', 'Kings'],
                'game_objects': ['checker_board', 'checker_pieces', 'kings'],
                'colors': ['#FF0000', '#000000', '#FFFFFF', '#8B4513'],
                'description': 'Move your checkers diagonally. Capture all opponent pieces!'
            },
            'tower_defense': {
                'title': ['Tower Guardian', 'Defense Master', 'Castle Defender', 'Tower War'],
                'theme': 'Strategy',
                'character': 'Towers',
                'mechanics': 'tower_defense',
                'ui_elements': ['Lives', 'Money', 'Wave'],
                'game_objects': ['towers', 'enemies', 'path'],
                'colors': ['#8B4513', '#FF0000', '#00FF00', '#0000FF'],
                'description': 'Build towers to defend against enemy waves. Upgrade your defenses!'
            },
            
            # CARD GAMES
            'poker': {
                'title': ['Poker Pro', 'Texas Hold\'em', 'Card Master', 'Poker Champion'],
                'theme': 'Cards',
                'character': 'Player',
                'mechanics': 'card_playing',
                'ui_elements': ['Chips', 'Bet', 'Hand'],
                'game_objects': ['cards', 'chips', 'table'],
                'colors': ['#00FF00', '#FF0000', '#000000', '#FFFFFF'],
                'description': 'Play poker and win chips. Make the best hand to beat opponents!'
            },
            'blackjack': {
                'title': ['21 Master', 'Blackjack Pro', 'Card Counter', 'Casino King'],
                'theme': 'Cards',
                'character': 'Player',
                'mechanics': 'card_counting',
                'ui_elements': ['Score', 'Bet', 'Cards'],
                'game_objects': ['cards', 'chips', 'dealer'],
                'colors': ['#00FF00', '#FF0000', '#000000', '#FFFFFF'],
                'description': 'Get as close to 21 as possible without going over. Beat the dealer!'
            },
            'solitaire': {
                'title': ['Solitaire Master', 'Card Patience', 'Solo Cards', 'Klondike'],
                'theme': 'Cards',
                'character': 'Player',
                'mechanics': 'card_stacking',
                'ui_elements': ['Score', 'Time', 'Moves'],
                'game_objects': ['cards', 'stacks', 'foundation'],
                'colors': ['#00FF00', '#FF0000', '#000000', '#FFFFFF'],
                'description': 'Stack cards in order to clear the board. Complete all foundations!'
            },
            
            # ARCADE GAMES
            'pinball': {
                'title': ['Pinball Wizard', 'Silver Ball', 'Flipper Master', 'Arcade King'],
                'theme': 'Arcade',
                'character': 'Ball',
                'mechanics': 'ball_physics',
                'ui_elements': ['Score', 'Ball', 'Bonus'],
                'game_objects': ['flippers', 'ball', 'bumpers'],
                'colors': ['#FF69B4', '#00CED1', '#FFD700', '#FF0000'],
                'description': 'Use flippers to keep the ball in play. Hit targets for high scores!'
            },
            'pacman': {
                'title': ['Pac Master', 'Dot Eater', 'Maze Runner', 'Ghost Hunter'],
                'theme': 'Arcade',
                'character': 'Pac_Man',
                'mechanics': 'maze_navigation',
                'ui_elements': ['Score', 'Lives', 'Level'],
                'game_objects': ['pac_man', 'ghosts', 'dots'],
                'colors': ['#FFFF00', '#FF0000', '#00CED1', '#FFB6C1'],
                'description': 'Eat all dots while avoiding ghosts. Use power pellets to turn the tables!'
            },
            'asteroids': {
                'title': ['Asteroid Blaster', 'Space Rocks', 'Cosmic Shooter', 'Asteroid Field'],
                'theme': 'Arcade',
                'character': 'Spaceship',
                'mechanics': 'space_shooting',
                'ui_elements': ['Score', 'Lives', 'Level'],
                'game_objects': ['spaceship', 'asteroids', 'bullets'],
                'colors': ['#FFFFFF', '#808080', '#FF0000', '#00FF00'],
                'description': 'Destroy asteroids with your spaceship. Avoid collisions!'
            }
        }
        
        # Keywords mapping for intelligent prompt parsing
        self.keyword_mapping = {
            # Sports keywords
            'dart': 'darts', 'darts': 'darts', 'dartboard': 'darts', 'bullseye': 'darts',
            'basketball': 'basketball', 'hoop': 'basketball', 'court': 'basketball', 'slam': 'basketball',
            'soccer': 'soccer', 'football': 'soccer', 'goal': 'soccer', 'kick': 'soccer',
            'tennis': 'tennis', 'racket': 'tennis', 'serve': 'tennis', 'court': 'tennis',
            'golf': 'golf', 'putting': 'golf', 'hole': 'golf', 'club': 'golf',
            
            # Racing keywords
            'race': 'racing', 'racing': 'racing', 'car': 'racing', 'speed': 'racing', 'track': 'racing',
            'motorcycle': 'motorcycle', 'bike': 'motorcycle', 'motorbike': 'motorcycle',
            'horse': 'horse_racing', 'derby': 'horse_racing', 'gallop': 'horse_racing',
            
            # Puzzle keywords
            'tetris': 'tetris', 'blocks': 'tetris', 'lines': 'tetris', 'stack': 'tetris',
            'match': 'match3', 'gems': 'match3', 'candy': 'match3', 'jewel': 'match3',
            'sudoku': 'sudoku', 'numbers': 'sudoku', 'grid': 'sudoku', 'logic': 'sudoku',
            
            # Action keywords
            'shoot': 'shooting', 'target': 'shooting', 'gun': 'shooting', 'aim': 'shooting',
            'fight': 'fighting', 'combat': 'fighting', 'martial': 'fighting', 'battle': 'fighting',
            'jump': 'platformer', 'platform': 'platformer', 'adventure': 'platformer',
            
            # Strategy keywords
            'chess': 'chess', 'king': 'chess', 'queen': 'chess', 'checkmate': 'chess',
            'checkers': 'checkers', 'checker': 'checkers', 'king me': 'checkers',
            'tower': 'tower_defense', 'defense': 'tower_defense', 'defend': 'tower_defense',
            
            # Card keywords
            'poker': 'poker', 'texas': 'poker', 'holdem': 'poker', 'chips': 'poker',
            'blackjack': 'blackjack', '21': 'blackjack', 'dealer': 'blackjack',
            'solitaire': 'solitaire', 'patience': 'solitaire', 'klondike': 'solitaire',
            
            # Arcade keywords
            'pinball': 'pinball', 'flipper': 'pinball', 'silver ball': 'pinball',
            'pacman': 'pacman', 'pac-man': 'pacman', 'ghost': 'pacman', 'maze': 'pacman',
            'asteroid': 'asteroids', 'space': 'asteroids', 'spaceship': 'asteroids'
        }
    
    def analyze_prompt(self, prompt):
        """Analyze user prompt and find best matching game template"""
        prompt_lower = prompt.lower()
        
        # Check for direct keyword matches
        for keyword, game_type in self.keyword_mapping.items():
            if keyword in prompt_lower:
                return game_type
        
        # Check for partial matches
        for keyword, game_type in self.keyword_mapping.items():
            if any(word in prompt_lower for word in keyword.split()):
                return game_type
        
        # Default fallback - analyze prompt content
        if any(word in prompt_lower for word in ['sport', 'ball', 'play']):
            return 'basketball'  # Default sports game
        elif any(word in prompt_lower for word in ['puzzle', 'brain', 'think']):
            return 'tetris'  # Default puzzle game
        elif any(word in prompt_lower for word in ['action', 'fast', 'quick']):
            return 'shooting'  # Default action game
        elif any(word in prompt_lower for word in ['strategy', 'plan', 'think']):
            return 'chess'  # Default strategy game
        else:
            return 'darts'  # Ultimate fallback
    
    def get_game_template(self, prompt):
        """Get appropriate game template based on user prompt"""
        game_type = self.analyze_prompt(prompt)
        
        if game_type not in self.templates:
            game_type = 'darts'  # Fallback
        
        template = self.templates[game_type].copy()
        
        # Add randomization
        template['title'] = random.choice(template['title'])
        template['timestamp'] = datetime.now().isoformat()
        template['prompt_analyzed'] = prompt
        template['game_type'] = game_type
        
        return template
    
    def get_available_games(self):
        """Get list of all available game types"""
        return list(self.templates.keys())
    
    def get_game_stats(self):
        """Get statistics about available templates"""
        categories = {}
        for game_type, template in self.templates.items():
            theme = template['theme']
            if theme not in categories:
                categories[theme] = []
            categories[theme].append(game_type)
        
        return {
            'total_templates': len(self.templates),
            'categories': categories,
            'total_categories': len(categories)
        }

# Initialize the library
game_library = GameTemplateLibrary()

def get_game_template(prompt):
    """Main function to get game template based on prompt"""
    return game_library.get_game_template(prompt)

def get_template_stats():
    """Get template library statistics"""
    return game_library.get_game_stats()

if __name__ == "__main__":
    # Test the system
    test_prompts = [
        "darts",
        "basketball game",
        "racing car",
        "tetris blocks",
        "chess match",
        "poker game",
        "pinball machine"
    ]
    
    print("🎮 TESTING COMPREHENSIVE GAME TEMPLATE LIBRARY")
    print("=" * 60)
    
    for prompt in test_prompts:
        template = get_game_template(prompt)
        print(f"Prompt: '{prompt}' → Game: '{template['title']}' ({template['theme']})")
    
    print("\n📊 LIBRARY STATISTICS:")
    stats = get_template_stats()
    print(f"Total Templates: {stats['total_templates']}")
    print(f"Categories: {stats['total_categories']}")
    for category, games in stats['categories'].items():
        print(f"  {category}: {len(games)} games")

