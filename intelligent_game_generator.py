"""
🧠 INTELLIGENT GAME GENERATOR
Advanced prompt parsing and dynamic game generation system
"""

import random
import re
from datetime import datetime
from comprehensive_game_template_library import get_game_template, get_template_stats

class IntelligentGameGenerator:
    def __init__(self):
        self.generation_history = []
        self.success_rate = 0.0
        self.total_generations = 0
        
    def parse_prompt_advanced(self, prompt):
        """Advanced prompt parsing with context understanding"""
        prompt_lower = prompt.lower().strip()
        
        # Extract key information from prompt
        analysis = {
            'original_prompt': prompt,
            'keywords': [],
            'game_type': None,
            'specific_features': [],
            'difficulty': 'normal',
            'theme_preferences': [],
            'mechanics_requested': []
        }
        
        # Extract keywords
        words = re.findall(r'\b\w+\b', prompt_lower)
        analysis['keywords'] = words
        
        # Analyze for specific game requests
        game_indicators = {
            'darts': ['dart', 'darts', 'dartboard', 'bullseye', 'throw', 'target'],
            'basketball': ['basketball', 'hoop', 'court', 'shoot', 'slam', 'dunk'],
            'racing': ['race', 'racing', 'car', 'speed', 'fast', 'track', 'lap'],
            'soccer': ['soccer', 'football', 'goal', 'kick', 'field', 'penalty'],
            'tennis': ['tennis', 'racket', 'serve', 'court', 'net', 'match'],
            'golf': ['golf', 'putting', 'hole', 'club', 'green', 'par'],
            'chess': ['chess', 'king', 'queen', 'checkmate', 'strategy', 'board'],
            'poker': ['poker', 'cards', 'chips', 'bet', 'texas', 'holdem'],
            'tetris': ['tetris', 'blocks', 'lines', 'stack', 'falling'],
            'pinball': ['pinball', 'flipper', 'ball', 'arcade', 'bumper'],
            'shooting': ['shoot', 'gun', 'target', 'aim', 'bullet', 'sniper'],
            'fighting': ['fight', 'combat', 'martial', 'battle', 'fighter'],
            'puzzle': ['puzzle', 'brain', 'logic', 'solve', 'think'],
            'platformer': ['jump', 'platform', 'adventure', 'hero', 'level']
        }
        
        # Find best matching game type
        best_match = None
        best_score = 0
        
        for game_type, indicators in game_indicators.items():
            score = sum(1 for indicator in indicators if indicator in prompt_lower)
            if score > best_score:
                best_score = score
                best_match = game_type
        
        analysis['game_type'] = best_match or 'darts'  # Default fallback
        analysis['confidence'] = min(best_score / 3.0, 1.0)  # Confidence score
        
        # Extract specific features mentioned
        feature_patterns = {
            'multiplayer': ['multiplayer', 'vs', 'against', 'opponent', 'player'],
            'timed': ['time', 'timer', 'countdown', 'clock', 'seconds'],
            'scoring': ['score', 'points', 'high score', 'leaderboard'],
            'levels': ['level', 'stage', 'progression', 'advance'],
            'power_ups': ['power', 'bonus', 'special', 'upgrade'],
            'difficulty': ['easy', 'hard', 'difficult', 'challenge', 'expert']
        }
        
        for feature, patterns in feature_patterns.items():
            if any(pattern in prompt_lower for pattern in patterns):
                analysis['specific_features'].append(feature)
        
        # Determine difficulty
        if any(word in prompt_lower for word in ['easy', 'simple', 'beginner']):
            analysis['difficulty'] = 'easy'
        elif any(word in prompt_lower for word in ['hard', 'difficult', 'expert', 'pro']):
            analysis['difficulty'] = 'hard'
        elif any(word in prompt_lower for word in ['challenge', 'master', 'advanced']):
            analysis['difficulty'] = 'expert'
        
        return analysis
    
    def generate_game_html(self, template, analysis):
        """Generate complete HTML game based on template and analysis"""
        
        # Get template data
        title = template['title']
        theme = template['theme']
        character = template['character']
        mechanics = template['mechanics']
        ui_elements = template['ui_elements']
        colors = template['colors']
        description = template['description']
        
        # Customize based on analysis
        if analysis['difficulty'] == 'easy':
            difficulty_modifier = "Easy Mode - "
        elif analysis['difficulty'] == 'hard':
            difficulty_modifier = "Hard Mode - "
        elif analysis['difficulty'] == 'expert':
            difficulty_modifier = "Expert Mode - "
        else:
            difficulty_modifier = ""
        
        # Generate unique game mechanics based on game type
        game_mechanics = self.generate_game_mechanics(template['game_type'], analysis)
        
        # Create HTML game
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{difficulty_modifier}{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, {colors[0]}, {colors[1]});
            font-family: 'Arial', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: white;
        }}
        
        .game-container {{
            background: rgba(0, 0, 0, 0.8);
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            text-align: center;
            max-width: 800px;
            width: 90%;
        }}
        
        .game-header {{
            background: linear-gradient(45deg, {colors[2]}, {colors[3]});
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
        }}
        
        .game-title {{
            font-size: 2.5em;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }}
        
        .game-info {{
            font-size: 1.1em;
            margin: 10px 0;
            opacity: 0.9;
        }}
        
        .game-area {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 30px;
            margin: 20px 0;
            min-height: 300px;
            position: relative;
            overflow: hidden;
        }}
        
        .ui-panel {{
            display: flex;
            justify-content: space-around;
            background: rgba(0, 0, 0, 0.6);
            padding: 15px;
            border-radius: 10px;
            margin: 20px 0;
            flex-wrap: wrap;
        }}
        
        .ui-element {{
            background: linear-gradient(45deg, {colors[0]}, {colors[1]});
            padding: 10px 15px;
            border-radius: 8px;
            margin: 5px;
            font-weight: bold;
            min-width: 80px;
        }}
        
        .game-object {{
            position: absolute;
            border-radius: 50%;
            transition: all 0.3s ease;
        }}
        
        .controls {{
            margin: 20px 0;
        }}
        
        .control-btn {{
            background: linear-gradient(45deg, {colors[2]}, {colors[3]});
            color: white;
            border: none;
            padding: 12px 25px;
            margin: 5px;
            border-radius: 8px;
            font-size: 1.1em;
            cursor: pointer;
            transition: all 0.3s ease;
        }}
        
        .control-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }}
        
        .description {{
            background: rgba(255, 255, 255, 0.1);
            padding: 15px;
            border-radius: 10px;
            margin: 20px 0;
            font-style: italic;
        }}
        
        @media (max-width: 600px) {{
            .game-title {{ font-size: 2em; }}
            .ui-panel {{ flex-direction: column; }}
            .control-btn {{ width: 100%; margin: 5px 0; }}
        }}
    </style>
</head>
<body>
    <div class="game-container">
        <div class="game-header">
            <h1 class="game-title">{difficulty_modifier}{title}</h1>
            <div class="game-info">Theme: {theme} | Character: {character.replace('_', ' ')}</div>
        </div>
        
        <div class="ui-panel">
            {self.generate_ui_elements(ui_elements)}
        </div>
        
        <div class="game-area" id="gameArea">
            {game_mechanics['html']}
        </div>
        
        <div class="controls">
            {game_mechanics['controls']}
        </div>
        
        <div class="description">
            <strong>How to Play:</strong> {description}
        </div>
        
        <div class="description">
            <strong>Generated from prompt:</strong> "{analysis['original_prompt']}"<br>
            <strong>Game Type:</strong> {template['game_type'].title()}<br>
            <strong>Confidence:</strong> {analysis['confidence']:.1%}
        </div>
    </div>
    
    <script>
        {game_mechanics['javascript']}
    </script>
</body>
</html>"""
        
        return html_content
    
    def generate_ui_elements(self, ui_elements):
        """Generate UI elements HTML"""
        html = ""
        for element in ui_elements:
            initial_value = self.get_initial_value(element)
            html += f'<div class="ui-element" id="{element.lower()}">{element.replace("_", " ")}: <span id="{element.lower()}_value">{initial_value}</span></div>'
        return html
    
    def get_initial_value(self, element):
        """Get initial value for UI elements"""
        if 'score' in element.lower():
            return '0'
        elif 'lives' in element.lower() or 'health' in element.lower():
            return '3'
        elif 'level' in element.lower() or 'round' in element.lower():
            return '1'
        elif 'time' in element.lower():
            return '60'
        elif 'ammo' in element.lower() or 'darts' in element.lower():
            return '10'
        else:
            return '0'
    
    def generate_game_mechanics(self, game_type, analysis):
        """Generate specific game mechanics based on game type"""
        
        mechanics = {
            'darts': {
                'html': '''
                    <div style="position: relative; width: 300px; height: 300px; margin: 0 auto;">
                        <div id="dartboard" style="width: 300px; height: 300px; border-radius: 50%; background: radial-gradient(circle, #FFD700 10%, #FF0000 20%, #FFFFFF 30%, #00FF00 40%, #000000 50%); position: relative; cursor: crosshair;">
                            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 20px; height: 20px; background: #FFD700; border-radius: 50%; border: 2px solid #000;"></div>
                        </div>
                        <div id="dart" style="position: absolute; top: 50%; left: 10px; width: 30px; height: 5px; background: #8B4513; transform: translateY(-50%); display: none;"></div>
                    </div>
                ''',
                'controls': '''
                    <button class="control-btn" onclick="throwDart()">🎯 Throw Dart</button>
                    <button class="control-btn" onclick="resetGame()">🔄 New Game</button>
                ''',
                'javascript': '''
                    let score = 0;
                    let dartsLeft = 3;
                    let round = 1;
                    
                    function throwDart() {
                        if (dartsLeft <= 0) return;
                        
                        const dartboard = document.getElementById('dartboard');
                        const dart = document.getElementById('dart');
                        
                        // Simulate dart throw
                        const x = Math.random() * 300;
                        const y = Math.random() * 300;
                        const centerX = 150;
                        const centerY = 150;
                        const distance = Math.sqrt((x - centerX) ** 2 + (y - centerY) ** 2);
                        
                        // Calculate score based on distance from center
                        let points = 0;
                        if (distance < 15) points = 50; // Bullseye
                        else if (distance < 30) points = 25; // Inner ring
                        else if (distance < 60) points = 20; // Outer ring
                        else if (distance < 90) points = 15;
                        else if (distance < 120) points = 10;
                        else if (distance < 150) points = 5;
                        
                        score += points;
                        dartsLeft--;
                        
                        // Show dart on board
                        dart.style.display = 'block';
                        dart.style.left = x + 'px';
                        dart.style.top = y + 'px';
                        
                        // Update UI
                        document.getElementById('score_value').textContent = score;
                        document.getElementById('darts_left_value').textContent = dartsLeft;
                        document.getElementById('round_value').textContent = round;
                        
                        if (dartsLeft === 0) {
                            setTimeout(() => {
                                alert('Round complete! Score: ' + score);
                                round++;
                                dartsLeft = 3;
                                dart.style.display = 'none';
                                document.getElementById('round_value').textContent = round;
                                document.getElementById('darts_left_value').textContent = dartsLeft;
                            }, 1000);
                        }
                    }
                    
                    function resetGame() {
                        score = 0;
                        dartsLeft = 3;
                        round = 1;
                        document.getElementById('score_value').textContent = score;
                        document.getElementById('darts_left_value').textContent = dartsLeft;
                        document.getElementById('round_value').textContent = round;
                        document.getElementById('dart').style.display = 'none';
                    }
                    
                    // Click to throw dart
                    document.getElementById('dartboard').addEventListener('click', throwDart);
                '''
            },
            'basketball': {
                'html': '''
                    <div style="position: relative; width: 400px; height: 300px; margin: 0 auto; background: linear-gradient(to bottom, #87CEEB, #8B4513);">
                        <div id="hoop" style="position: absolute; top: 50px; right: 50px; width: 80px; height: 10px; background: #FF8C00; border-radius: 5px;"></div>
                        <div id="backboard" style="position: absolute; top: 30px; right: 30px; width: 10px; height: 100px; background: #FFFFFF;"></div>
                        <div id="ball" style="position: absolute; bottom: 50px; left: 50px; width: 30px; height: 30px; background: #FF8C00; border-radius: 50%; cursor: pointer;"></div>
                    </div>
                ''',
                'controls': '''
                    <button class="control-btn" onclick="shootBall()">🏀 Shoot Ball</button>
                    <button class="control-btn" onclick="resetGame()">🔄 New Game</button>
                ''',
                'javascript': '''
                    let score = 0;
                    let shots = 0;
                    let made = 0;
                    
                    function shootBall() {
                        const ball = document.getElementById('ball');
                        const success = Math.random() > 0.4; // 60% success rate
                        
                        shots++;
                        
                        // Animate ball
                        ball.style.transition = 'all 1s ease';
                        ball.style.transform = 'translate(300px, -200px)';
                        
                        setTimeout(() => {
                            if (success) {
                                score += 2;
                                made++;
                                alert('SCORE! 🏀');
                            } else {
                                alert('Miss! Try again!');
                            }
                            
                            // Reset ball position
                            ball.style.transition = 'none';
                            ball.style.transform = 'translate(0, 0)';
                            
                            // Update UI
                            document.getElementById('score_value').textContent = score;
                            document.getElementById('shots_made_value').textContent = made + '/' + shots;
                        }, 1000);
                    }
                    
                    function resetGame() {
                        score = 0;
                        shots = 0;
                        made = 0;
                        document.getElementById('score_value').textContent = score;
                        document.getElementById('shots_made_value').textContent = made + '/' + shots;
                    }
                '''
            }
        }
        
        # Default fallback mechanics for unsupported games
        if game_type not in mechanics:
            mechanics[game_type] = {
                'html': f'<div style="padding: 50px; font-size: 1.5em;">🎮 {game_type.title()} Game<br><br>Click the button below to play!</div>',
                'controls': '<button class="control-btn" onclick="playGame()">🎮 Play Game</button>',
                'javascript': '''
                    function playGame() {
                        alert('Game started! This is a ' + ''' + f'"{game_type}"' + ''' + ' game.');
                        let currentScore = parseInt(document.getElementById('score_value').textContent);
                        document.getElementById('score_value').textContent = currentScore + 10;
                    }
                '''
            }
        
        return mechanics[game_type]
    
    def generate_ultimate_game(self, prompt):
        """Main function to generate ultimate game from prompt"""
        try:
            # Parse the prompt
            analysis = self.parse_prompt_advanced(prompt)
            
            # Get appropriate template
            template = get_game_template(prompt)
            
            # Generate complete HTML game
            html_game = self.generate_game_html(template, analysis)
            
            # Track generation
            self.total_generations += 1
            generation_record = {
                'prompt': prompt,
                'game_type': analysis['game_type'],
                'confidence': analysis['confidence'],
                'timestamp': datetime.now().isoformat(),
                'success': True
            }
            self.generation_history.append(generation_record)
            
            # Calculate success rate
            successful_generations = sum(1 for record in self.generation_history if record['success'])
            self.success_rate = successful_generations / self.total_generations
            
            return {
                'success': True,
                'html': html_game,
                'analysis': analysis,
                'template': template,
                'generation_stats': {
                    'total_generations': self.total_generations,
                    'success_rate': self.success_rate,
                    'confidence': analysis['confidence']
                }
            }
            
        except Exception as e:
            # Track failed generation
            self.total_generations += 1
            generation_record = {
                'prompt': prompt,
                'error': str(e),
                'timestamp': datetime.now().isoformat(),
                'success': False
            }
            self.generation_history.append(generation_record)
            
            return {
                'success': False,
                'error': str(e),
                'fallback_html': self.generate_fallback_game(prompt)
            }
    
    def generate_fallback_game(self, prompt):
        """Generate a simple fallback game if main generation fails"""
        return f"""<!DOCTYPE html>
<html>
<head>
    <title>Game Generator</title>
    <style>
        body {{ font-family: Arial, sans-serif; text-align: center; padding: 50px; }}
        .game {{ background: #f0f0f0; padding: 30px; border-radius: 10px; }}
    </style>
</head>
<body>
    <div class="game">
        <h1>🎮 Game Generated</h1>
        <p>Based on your prompt: "{prompt}"</p>
        <button onclick="alert('Game started!')">Play Game</button>
    </div>
</body>
</html>"""

# Initialize the generator
game_generator = IntelligentGameGenerator()

def generate_ultimate_game(prompt):
    """Main function for external use"""
    return game_generator.generate_ultimate_game(prompt)

if __name__ == "__main__":
    # Test the system
    test_prompts = [
        "darts",
        "basketball game with scoring",
        "racing car game",
        "chess match",
        "simple puzzle game"
    ]
    
    print("🧠 TESTING INTELLIGENT GAME GENERATOR")
    print("=" * 60)
    
    for prompt in test_prompts:
        result = generate_ultimate_game(prompt)
        if result['success']:
            print(f"✅ '{prompt}' → {result['analysis']['game_type']} ({result['analysis']['confidence']:.1%} confidence)")
        else:
            print(f"❌ '{prompt}' → Failed: {result['error']}")
    
    print(f"\n📊 Success Rate: {game_generator.success_rate:.1%}")
    print(f"Total Generations: {game_generator.total_generations}")

