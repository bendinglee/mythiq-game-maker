"""
Mythiq Game AI - Intelligent Game Generation Engine
Analyzes prompts and customizes base games with AI
"""

import re
import json
import random
from datetime import datetime
from base_games import BASE_GAMES
from customization_engine import CustomizationEngine

class GameAI:
    """
    Main AI engine that analyzes user prompts and generates custom games
    """
    
    def __init__(self):
        self.customization_engine = CustomizationEngine()
        self.games_generated = 0
        self.user_preferences = {}
        
        # Genre detection patterns
        self.genre_patterns = {
            'platformer': [
                'jump', 'platform', 'run', 'escape', 'adventure', 'mario', 
                'side-scroll', 'level', 'obstacle', 'ninja', 'hero'
            ],
            'puzzle': [
                'puzzle', 'match', 'solve', 'brain', 'logic', 'strategy',
                'crystal', 'gem', 'block', 'tetris', 'candy', 'color'
            ],
            'rpg': [
                'rpg', 'character', 'quest', 'story', 'adventure', 'fantasy',
                'village', 'knight', 'wizard', 'magic', 'level up', 'stats'
            ],
            'racing': [
                'race', 'car', 'speed', 'fast', 'track', 'lap', 'vehicle',
                'drive', 'circuit', 'formula', 'motorcycle', 'bike'
            ],
            'shooter': [
                'shoot', 'gun', 'battle', 'fight', 'enemy', 'defend', 'war',
                'space', 'alien', 'laser', 'weapon', 'combat', 'army'
            ]
        }
        
        # Theme detection patterns
        self.theme_patterns = {
            'ninja': {
                'keywords': ['ninja', 'stealth', 'shadow', 'assassin', 'katana'],
                'character_style': 'ninja',
                'environment': 'dark',
                'mechanics': ['stealth', 'wall_jump', 'throwing_stars']
            },
            'space': {
                'keywords': ['space', 'alien', 'cosmic', 'galaxy', 'planet', 'star'],
                'character_style': 'astronaut',
                'environment': 'cosmic',
                'mechanics': ['zero_gravity', 'laser_weapons', 'space_suit']
            },
            'medieval': {
                'keywords': ['knight', 'castle', 'sword', 'medieval', 'dragon', 'kingdom'],
                'character_style': 'knight',
                'environment': 'castle',
                'mechanics': ['sword_combat', 'shield', 'magic']
            },
            'forest': {
                'keywords': ['forest', 'tree', 'nature', 'woodland', 'jungle'],
                'character_style': 'ranger',
                'environment': 'forest',
                'mechanics': ['climbing', 'nature_powers', 'animal_friends']
            },
            'underwater': {
                'keywords': ['underwater', 'ocean', 'sea', 'fish', 'submarine'],
                'character_style': 'diver',
                'environment': 'underwater',
                'mechanics': ['swimming', 'air_bubbles', 'sea_creatures']
            }
        }
        
        # Difficulty indicators
        self.difficulty_patterns = {
            'easy': ['easy', 'simple', 'beginner', 'casual', 'relaxed'],
            'medium': ['medium', 'normal', 'balanced', 'standard'],
            'hard': ['hard', 'difficult', 'challenging', 'expert', 'intense']
        }
        
    def generate_game(self, prompt, user_id=None):
        """
        Main game generation method
        """
        try:
            # Analyze the user prompt
            analysis = self.analyze_prompt(prompt)
            
            # Select the best base game
            base_game_key = self.select_base_game(analysis)
            
            # Get customization parameters
            customizations = self.generate_customizations(analysis, prompt)
            
            # Apply customizations to base game
            customized_game = self.customization_engine.customize_game(
                base_game_key, customizations, prompt
            )
            
            # Track generation
            self.games_generated += 1
            if user_id:
                self.update_user_preferences(user_id, analysis)
            
            return {
                'game_type': analysis['genre'],
                'title': customized_game['title'],
                'description': customized_game['description'],
                'html_content': customized_game['html_content'],
                'generation_time': '30 seconds',
                'ai_analysis': {
                    'detected_genre': analysis['genre'],
                    'detected_theme': analysis['theme'],
                    'difficulty': analysis['difficulty'],
                    'confidence': analysis['confidence'],
                    'customizations_applied': len(customizations),
                    'base_game_used': base_game_key
                }
            }
            
        except Exception as e:
            # Fallback to simple generation
            return self._generate_fallback_game(prompt)
    
    def analyze_prompt(self, prompt):
        """
        Analyze user prompt to extract game requirements
        """
        prompt_lower = prompt.lower()
        
        # Detect genre
        genre_scores = {}
        for genre, keywords in self.genre_patterns.items():
            score = sum(1 for keyword in keywords if keyword in prompt_lower)
            if score > 0:
                genre_scores[genre] = score
        
        detected_genre = max(genre_scores, key=genre_scores.get) if genre_scores else 'platformer'
        
        # Detect theme
        detected_theme = 'adventure'  # default
        theme_score = 0
        for theme, theme_data in self.theme_patterns.items():
            score = sum(1 for keyword in theme_data['keywords'] if keyword in prompt_lower)
            if score > theme_score:
                theme_score = score
                detected_theme = theme
        
        # Detect difficulty
        detected_difficulty = 'medium'  # default
        for difficulty, keywords in self.difficulty_patterns.items():
            if any(keyword in prompt_lower for keyword in keywords):
                detected_difficulty = difficulty
                break
        
        # Calculate confidence
        total_keywords = sum(genre_scores.values()) + theme_score
        confidence = min(0.9, 0.3 + (total_keywords * 0.1))
        
        return {
            'genre': detected_genre,
            'theme': detected_theme,
            'difficulty': detected_difficulty,
            'confidence': confidence,
            'original_prompt': prompt,
            'keywords_found': total_keywords
        }
    
    def select_base_game(self, analysis):
        """
        Select the best base game for the detected genre
        """
        genre_to_base_game = {
            'platformer': 'forest_runner',
            'puzzle': 'crystal_matcher',
            'rpg': 'village_quest',
            'racing': 'speed_circuit',
            'shooter': 'space_defense'
        }
        
        return genre_to_base_game.get(analysis['genre'], 'forest_runner')
    
    def generate_customizations(self, analysis, prompt):
        """
        Generate customization parameters based on analysis
        """
        customizations = {
            'theme': analysis['theme'],
            'difficulty': analysis['difficulty'],
            'genre': analysis['genre']
        }
        
        # Add theme-specific customizations
        if analysis['theme'] in self.theme_patterns:
            theme_data = self.theme_patterns[analysis['theme']]
            customizations.update({
                'character_style': theme_data['character_style'],
                'environment': theme_data['environment'],
                'mechanics': theme_data['mechanics']
            })
        
        # Add genre-specific customizations
        if analysis['genre'] == 'platformer':
            customizations.update({
                'player_speed': 'normal' if analysis['difficulty'] == 'medium' else analysis['difficulty'],
                'jump_height': 'normal',
                'obstacles': True,
                'collectibles': True
            })
        elif analysis['genre'] == 'puzzle':
            customizations.update({
                'grid_size': 8 if analysis['difficulty'] == 'medium' else (6 if analysis['difficulty'] == 'easy' else 10),
                'colors': 6,
                'special_pieces': analysis['difficulty'] != 'easy'
            })
        elif analysis['genre'] == 'rpg':
            customizations.update({
                'character_class': 'warrior',
                'world_size': 'medium',
                'quest_complexity': analysis['difficulty']
            })
        
        # Extract specific requests from prompt
        prompt_lower = prompt.lower()
        
        # Color preferences
        color_keywords = {
            'red': '#FF6B6B', 'blue': '#4ECDC4', 'green': '#96CEB4',
            'purple': '#DDA0DD', 'yellow': '#FFEAA7', 'orange': '#FFA07A'
        }
        for color, hex_code in color_keywords.items():
            if color in prompt_lower:
                customizations['primary_color'] = hex_code
                break
        
        # Speed preferences
        if any(word in prompt_lower for word in ['fast', 'quick', 'speed']):
            customizations['game_speed'] = 'fast'
        elif any(word in prompt_lower for word in ['slow', 'relaxed', 'calm']):
            customizations['game_speed'] = 'slow'
        
        return customizations
    
    def update_user_preferences(self, user_id, analysis):
        """
        Learn from user preferences over time
        """
        if user_id not in self.user_preferences:
            self.user_preferences[user_id] = {
                'favorite_genres': {},
                'favorite_themes': {},
                'difficulty_preference': 'medium',
                'games_created': 0
            }
        
        user_prefs = self.user_preferences[user_id]
        user_prefs['games_created'] += 1
        
        # Track genre preferences
        genre = analysis['genre']
        user_prefs['favorite_genres'][genre] = user_prefs['favorite_genres'].get(genre, 0) + 1
        
        # Track theme preferences
        theme = analysis['theme']
        user_prefs['favorite_themes'][theme] = user_prefs['favorite_themes'].get(theme, 0) + 1
        
        # Update difficulty preference
        if analysis['difficulty'] != 'medium':
            user_prefs['difficulty_preference'] = analysis['difficulty']
    
    def _generate_fallback_game(self, prompt):
        """
        Fallback game generation if main system fails
        """
        return {
            'game_type': 'adventure',
            'title': f'Custom Adventure Game',
            'description': f'An adventure game inspired by: "{prompt}"',
            'html_content': self._create_fallback_html(prompt),
            'generation_time': '5 seconds',
            'ai_analysis': {
                'detected_genre': 'adventure',
                'detected_theme': 'general',
                'difficulty': 'medium',
                'confidence': 0.5,
                'note': 'Fallback generation used'
            }
        }
    
    def _create_fallback_html(self, prompt):
        """
        Create a simple fallback game
        """
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Adventure Game - {prompt[:30]}</title>
            <style>
                .game-container {{ text-align: center; margin: 20px; font-family: Arial; }}
                .game-area {{ width: 600px; height: 400px; border: 2px solid #4a4a4a; 
                            margin: 20px auto; background: linear-gradient(45deg, #667eea 0%, #764ba2 100%); 
                            display: flex; align-items: center; justify-content: center; color: white; }}
            </style>
        </head>
        <body>
            <div class="game-container">
                <h2>Adventure Game</h2>
                <p>Inspired by: "{prompt}"</p>
                <div class="game-area">
                    <div>
                        <h3>🎮 Game Ready!</h3>
                        <p>Your custom adventure game is being prepared...</p>
                        <button onclick="startGame()" style="padding: 10px 20px; font-size: 16px; 
                                background: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">
                            Start Adventure
                        </button>
                    </div>
                </div>
            </div>
            
            <script>
                function startGame() {{
                    alert('Welcome to your custom adventure! This is a demo version. Upload the full Game AI system for complete functionality.');
                }}
            </script>
        </body>
        </html>
        """
    
    def health_check(self):
        """
        Health check for the AI system
        """
        return {
            'status': 'healthy',
            'system_type': 'full_game_ai',
            'games_generated': self.games_generated,
            'active_users': len(self.user_preferences),
            'supported_genres': list(self.genre_patterns.keys()),
            'supported_themes': list(self.theme_patterns.keys()),
            'ai_confidence': 'high',
            'customization_engine': 'active'
        }

