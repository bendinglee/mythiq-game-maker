"""
🔥 REVOLUTIONARY PROMPT PROCESSOR
Advanced AI-powered prompt analysis with complex keyword recognition and theme mapping
"""

import re
import random
from typing import Dict, List, Tuple, Optional

class RevolutionaryPromptProcessor:
    """
    Advanced prompt processing engine that understands complex descriptions
    and maps them to appropriate game templates with high accuracy
    """
    
    def __init__(self):
        self.theme_keywords = {
            # Sports & Games
            'darts': ['dart', 'darts', 'bullseye', 'dartboard', 'throwing', 'target practice'],
            'basketball': ['basketball', 'hoop', 'court', 'dribble', 'shoot', 'slam dunk', 'nba'],
            'soccer': ['soccer', 'football', 'goal', 'kick', 'field', 'fifa', 'penalty'],
            'tennis': ['tennis', 'racket', 'court', 'serve', 'volley', 'wimbledon'],
            'golf': ['golf', 'hole', 'club', 'swing', 'green', 'putt', 'tee'],
            'baseball': ['baseball', 'bat', 'pitch', 'home run', 'diamond', 'mlb'],
            
            # Racing & Vehicles
            'racing': ['racing', 'race', 'car', 'speed', 'track', 'formula', 'nascar', 'drift'],
            'motorcycle': ['motorcycle', 'bike', 'motorbike', 'rider', 'highway'],
            'boat': ['boat', 'sailing', 'yacht', 'speedboat', 'water racing'],
            
            # Adventure & Fantasy
            'underwater': ['underwater', 'ocean', 'sea', 'diving', 'submarine', 'aquatic', 'marine'],
            'mermaid': ['mermaid', 'merman', 'siren', 'sea creature', 'underwater princess'],
            'treasure': ['treasure', 'gold', 'coins', 'chest', 'jewels', 'gems', 'riches'],
            'pirate': ['pirate', 'ship', 'captain', 'sword', 'parrot', 'island'],
            'medieval': ['medieval', 'knight', 'castle', 'sword', 'armor', 'kingdom', 'royal'],
            'dragon': ['dragon', 'fire', 'wings', 'scales', 'breath', 'mythical'],
            'fantasy': ['fantasy', 'magic', 'wizard', 'spell', 'enchanted', 'mystical'],
            'space': ['space', 'alien', 'rocket', 'planet', 'galaxy', 'astronaut', 'cosmic'],
            'jungle': ['jungle', 'forest', 'trees', 'vines', 'animals', 'adventure'],
            
            # Action & Combat
            'shooting': ['shooting', 'gun', 'bullet', 'target', 'sniper', 'weapon'],
            'fighting': ['fighting', 'combat', 'martial arts', 'boxing', 'karate', 'battle'],
            'war': ['war', 'army', 'soldier', 'military', 'tank', 'battlefield'],
            
            # Puzzle & Strategy
            'puzzle': ['puzzle', 'brain', 'logic', 'solve', 'riddle', 'challenge'],
            'tetris': ['tetris', 'blocks', 'falling', 'lines', 'shapes', 'stack'],
            'match3': ['match', 'candy', 'gems', 'swap', 'crush', 'connect'],
            'chess': ['chess', 'king', 'queen', 'bishop', 'knight', 'pawn', 'checkmate'],
            'cards': ['cards', 'poker', 'blackjack', 'solitaire', 'deck', 'ace'],
            
            # Arcade & Classic
            'pinball': ['pinball', 'flipper', 'ball', 'bumper', 'arcade'],
            'pacman': ['pacman', 'ghost', 'dots', 'maze', 'chomp'],
            'asteroids': ['asteroids', 'rocks', 'space', 'ship', 'debris'],
            'platformer': ['platform', 'jump', 'run', 'climb', 'side-scroll'],
        }
        
        self.complexity_indicators = {
            'simple': ['simple', 'basic', 'easy', 'casual'],
            'complex': ['complex', 'advanced', 'challenging', 'hardcore'],
            'adventure': ['adventure', 'quest', 'journey', 'explore', 'discover'],
            'action': ['action', 'fast', 'intense', 'exciting', 'thrilling'],
            'strategy': ['strategy', 'tactical', 'planning', 'thinking', 'smart'],
        }
        
        self.character_keywords = {
            'hero': ['hero', 'protagonist', 'champion', 'warrior'],
            'knight': ['knight', 'paladin', 'crusader', 'armor'],
            'mermaid': ['mermaid', 'merman', 'sea princess', 'aquatic being'],
            'pirate': ['pirate', 'buccaneer', 'captain', 'sailor'],
            'wizard': ['wizard', 'mage', 'sorcerer', 'magician'],
            'alien': ['alien', 'extraterrestrial', 'martian', 'space being'],
            'robot': ['robot', 'android', 'cyborg', 'machine'],
            'animal': ['animal', 'creature', 'beast', 'wildlife'],
        }
        
        self.environment_keywords = {
            'castle': ['castle', 'fortress', 'palace', 'tower', 'dungeon'],
            'ocean': ['ocean', 'sea', 'water', 'waves', 'deep'],
            'space': ['space', 'cosmos', 'galaxy', 'stars', 'void'],
            'forest': ['forest', 'woods', 'trees', 'jungle', 'wilderness'],
            'city': ['city', 'urban', 'buildings', 'streets', 'metropolis'],
            'desert': ['desert', 'sand', 'dunes', 'oasis', 'hot'],
            'ice': ['ice', 'snow', 'frozen', 'arctic', 'cold'],
            'volcano': ['volcano', 'lava', 'fire', 'eruption', 'molten'],
        }

    def analyze_prompt(self, prompt: str) -> Dict:
        """
        Advanced prompt analysis that extracts themes, complexity, characters, and environments
        """
        prompt_lower = prompt.lower()
        
        # Extract primary themes
        themes = self._extract_themes(prompt_lower)
        
        # Extract complexity level
        complexity = self._extract_complexity(prompt_lower)
        
        # Extract character types
        characters = self._extract_characters(prompt_lower)
        
        # Extract environment
        environment = self._extract_environment(prompt_lower)
        
        # Determine primary game type
        primary_type = self._determine_primary_type(themes, prompt_lower)
        
        # Extract descriptive elements
        descriptors = self._extract_descriptors(prompt_lower)
        
        return {
            'primary_type': primary_type,
            'themes': themes,
            'complexity': complexity,
            'characters': characters,
            'environment': environment,
            'descriptors': descriptors,
            'confidence': self._calculate_confidence(themes, primary_type),
            'original_prompt': prompt
        }
    
    def _extract_themes(self, prompt: str) -> List[str]:
        """Extract all matching themes from the prompt"""
        found_themes = []
        
        for theme, keywords in self.theme_keywords.items():
            for keyword in keywords:
                if keyword in prompt:
                    found_themes.append(theme)
                    break
        
        return list(set(found_themes))  # Remove duplicates
    
    def _extract_complexity(self, prompt: str) -> str:
        """Determine complexity level from prompt"""
        for complexity, keywords in self.complexity_indicators.items():
            for keyword in keywords:
                if keyword in prompt:
                    return complexity
        return 'medium'  # Default
    
    def _extract_characters(self, prompt: str) -> List[str]:
        """Extract character types mentioned in prompt"""
        found_characters = []
        
        for character, keywords in self.character_keywords.items():
            for keyword in keywords:
                if keyword in prompt:
                    found_characters.append(character)
                    break
        
        return found_characters
    
    def _extract_environment(self, prompt: str) -> Optional[str]:
        """Extract primary environment from prompt"""
        for environment, keywords in self.environment_keywords.items():
            for keyword in keywords:
                if keyword in prompt:
                    return environment
        return None
    
    def _determine_primary_type(self, themes: List[str], prompt: str) -> str:
        """Determine the primary game type based on themes and context"""
        if not themes:
            # Fallback analysis for unrecognized prompts
            if any(word in prompt for word in ['adventure', 'explore', 'quest']):
                return 'adventure'
            elif any(word in prompt for word in ['underwater', 'ocean', 'sea']):
                return 'underwater'
            elif any(word in prompt for word in ['medieval', 'knight', 'castle']):
                return 'medieval'
            elif any(word in prompt for word in ['space', 'alien', 'galaxy']):
                return 'space'
            else:
                return 'darts'  # Safe fallback
        
        # Priority-based selection
        priority_order = [
            'underwater', 'medieval', 'space', 'fantasy',  # Adventure themes
            'darts', 'basketball', 'soccer', 'tennis',     # Sports themes
            'racing', 'motorcycle',                        # Racing themes
            'puzzle', 'tetris', 'chess',                   # Puzzle themes
            'shooting', 'fighting',                        # Action themes
        ]
        
        for theme in priority_order:
            if theme in themes:
                return theme
        
        return themes[0] if themes else 'darts'
    
    def _extract_descriptors(self, prompt: str) -> List[str]:
        """Extract descriptive adjectives and modifiers"""
        descriptors = []
        
        descriptor_patterns = [
            r'\b(magical?|mystical?|enchanted?)\b',
            r'\b(epic|legendary|heroic)\b',
            r'\b(dark|bright|colorful)\b',
            r'\b(fast|slow|intense)\b',
            r'\b(challenging|easy|difficult)\b',
            r'\b(retro|modern|futuristic)\b',
        ]
        
        for pattern in descriptor_patterns:
            matches = re.findall(pattern, prompt, re.IGNORECASE)
            descriptors.extend(matches)
        
        return descriptors
    
    def _calculate_confidence(self, themes: List[str], primary_type: str) -> float:
        """Calculate confidence score for the analysis"""
        if not themes:
            return 0.3  # Low confidence for unrecognized prompts
        
        if len(themes) == 1:
            return 0.9  # High confidence for clear single theme
        
        if primary_type in themes:
            return 0.8  # Good confidence when primary type is in themes
        
        return 0.6  # Medium confidence for multiple themes

    def get_game_suggestions(self, analysis: Dict) -> List[str]:
        """Get multiple game suggestions based on analysis"""
        primary = analysis['primary_type']
        themes = analysis['themes']
        
        suggestions = [primary]
        
        # Add related themes
        for theme in themes:
            if theme != primary and theme not in suggestions:
                suggestions.append(theme)
        
        # Add fallback options
        fallbacks = ['darts', 'basketball', 'platformer']
        for fallback in fallbacks:
            if fallback not in suggestions:
                suggestions.append(fallback)
        
        return suggestions[:5]  # Return top 5 suggestions

# Example usage and testing
if __name__ == "__main__":
    processor = RevolutionaryPromptProcessor()
    
    test_prompts = [
        "Create a magical underwater adventure game with mermaids, treasure hunting, and sea creatures",
        "darts",
        "basketball game with NBA players",
        "medieval fantasy game with knights fighting dragons in a castle",
        "space battle with aliens and laser weapons",
        "racing game with fast cars on a track",
        "puzzle game with falling blocks like tetris",
        "asdfghjkl random nonsense xyz123"
    ]
    
    print("🔥 REVOLUTIONARY PROMPT PROCESSOR TESTING")
    print("=" * 60)
    
    for prompt in test_prompts:
        print(f"\nPrompt: '{prompt}'")
        analysis = processor.analyze_prompt(prompt)
        suggestions = processor.get_game_suggestions(analysis)
        
        print(f"Primary Type: {analysis['primary_type']}")
        print(f"Themes: {analysis['themes']}")
        print(f"Characters: {analysis['characters']}")
        print(f"Environment: {analysis['environment']}")
        print(f"Confidence: {analysis['confidence']:.1%}")
        print(f"Suggestions: {suggestions}")
        print("-" * 40)

