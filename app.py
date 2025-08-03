from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from datetime import datetime
import requests
import random

app = Flask(__name__)

# Enable CORS for your frontend domain
CORS(app, origins=[
    'https://mythiq-ui-production.up.railway.app',
    'http://localhost:5173',
    'http://localhost:3000'
])

# Configuration
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
HUGGINGFACE_API_KEY = os.environ.get('HUGGINGFACE_API_KEY')
GAME_TEMPLATES_PATH = os.environ.get('GAME_TEMPLATES_PATH', '/tmp/games')

def check_groq_availability():
    """Check if Groq API is available"""
    try:
        if not GROQ_API_KEY:
            return False
        
        headers = {
            'Authorization': f'Bearer {GROQ_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        response = requests.post(
            'https://api.groq.com/openai/v1/chat/completions',
            headers=headers,
            json={
                'model': 'llama3-70b-8192',
                'messages': [{'role': 'user', 'content': 'test'}],
                'max_tokens': 1
            },
            timeout=5
        )
        return response.status_code == 200
    except:
        return False

def generate_game_with_groq(prompt):
    """Generate game using Groq API"""
    try:
        headers = {
            'Authorization': f'Bearer {GROQ_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        system_prompt = """You are a game developer AI. Create a complete, playable HTML5 game based on the user's request. 

IMPORTANT: Return ONLY valid HTML code that includes:
1. Complete HTML structure with <!DOCTYPE html>
2. Embedded CSS in <style> tags
3. Embedded JavaScript in <script> tags
4. A fully functional game that works immediately when opened in a browser

The game should be:
- Self-contained (no external dependencies)
- Playable immediately
- Include clear instructions
- Have proper game mechanics
- Be visually appealing

Do not include any explanations or markdown - just pure HTML code."""

        response = requests.post(
            'https://api.groq.com/openai/v1/chat/completions',
            headers=headers,
            json={
                'model': 'llama3-70b-8192',
                'messages': [
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': f"Create a {prompt} game"}
                ],
                'max_tokens': 4000,
                'temperature': 0.8
            },
            timeout=60
        )
        
        if response.status_code == 200:
            data = response.json()
            game_html = data['choices'][0]['message']['content']
            
            # Clean up the response to ensure it's valid HTML
            if '```html' in game_html:
                game_html = game_html.split('```html')[1].split('```')[0]
            elif '```' in game_html:
                game_html = game_html.split('```')[1]
            
            return game_html.strip()
    except Exception as e:
        print(f"Groq game generation error: {e}")
        return None

def generate_fallback_game(prompt):
    """Generate a simple fallback game"""
    game_templates = {
        'space': {
            'title': 'Space Adventure',
            'description': 'Navigate through space and avoid asteroids!',
            'color': '#000080'
        },
        'puzzle': {
            'title': 'Number Puzzle',
            'description': 'Solve the number sequence puzzle!',
            'color': '#4CAF50'
        },
        'adventure': {
            'title': 'Text Adventure',
            'description': 'Choose your path in this adventure!',
            'color': '#8B4513'
        }
    }
    
    # Determine game type from prompt
    game_type = 'adventure'
    if 'space' in prompt.lower():
        game_type = 'space'
    elif 'puzzle' in prompt.lower() or 'number' in prompt.lower():
        game_type = 'puzzle'
    
    template = game_templates.get(game_type, game_templates['adventure'])
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{template['title']}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, {template['color']}, #1a1a1a);
            color: white;
            margin: 0;
            padding: 20px;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}
        .game-container {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            max-width: 600px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }}
        h1 {{
            margin-bottom: 10px;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }}
        .description {{
            margin-bottom: 30px;
            font-size: 1.2em;
            opacity: 0.9;
        }}
        .game-area {{
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            min-height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        }}
        button {{
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            border: none;
            color: white;
            padding: 15px 30px;
            font-size: 1.1em;
            border-radius: 25px;
            cursor: pointer;
            margin: 10px;
            transition: transform 0.2s;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }}
        button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
        }}
        .score {{
            font-size: 1.5em;
            margin: 20px 0;
            font-weight: bold;
        }}
        .game-text {{
            font-size: 1.1em;
            line-height: 1.6;
            margin: 15px 0;
        }}
    </style>
</head>
<body>
    <div class="game-container">
        <h1>{template['title']}</h1>
        <div class="description">{template['description']}</div>
        
        <div class="game-area" id="gameArea">
            <div class="game-text" id="gameText">Welcome to your adventure! Click Start to begin.</div>
            <div class="score" id="score">Score: 0</div>
        </div>
        
        <button onclick="startGame()">Start Game</button>
        <button onclick="resetGame()">Reset</button>
    </div>

    <script>
        let score = 0;
        let gameState = 'start';
        
        function updateDisplay(text) {{
            document.getElementById('gameText').innerHTML = text;
            document.getElementById('score').innerHTML = 'Score: ' + score;
        }}
        
        function startGame() {{
            gameState = 'playing';
            score = 0;
            
            if ('{game_type}' === 'space') {{
                updateDisplay('🚀 You are flying through space!<br>Asteroids ahead! Quick, choose your action:<br><button onclick="dodgeLeft()">Dodge Left</button> <button onclick="dodgeRight()">Dodge Right</button>');
            }} else if ('{game_type}' === 'puzzle') {{
                let num1 = Math.floor(Math.random() * 10) + 1;
                let num2 = Math.floor(Math.random() * 10) + 1;
                let answer = num1 + num2;
                updateDisplay(`🧩 Solve this: ${{num1}} + ${{num2}} = ?<br><input type="number" id="answer" placeholder="Your answer"><br><button onclick="checkAnswer(${{answer}})">Submit</button>`);
            }} else {{
                updateDisplay('🏰 You stand before a mysterious castle.<br>What do you do?<br><button onclick="enterCastle()">Enter Castle</button> <button onclick="walkAround()">Walk Around</button>');
            }}
        }}
        
        function dodgeLeft() {{
            score += 10;
            updateDisplay('✅ Great dodge! You avoided the asteroid!<br><button onclick="continueSpace()">Continue Flying</button>');
        }}
        
        function dodgeRight() {{
            score += 15;
            updateDisplay('🌟 Perfect maneuver! Bonus points!<br><button onclick="continueSpace()">Continue Flying</button>');
        }}
        
        function continueSpace() {{
            updateDisplay('🚀 Flying deeper into space...<br>You found a space station! +50 points!<br><button onclick="startGame()">New Challenge</button>');
            score += 50;
            document.getElementById('score').innerHTML = 'Score: ' + score;
        }}
        
        function checkAnswer(correct) {{
            let userAnswer = parseInt(document.getElementById('answer').value);
            if (userAnswer === correct) {{
                score += 20;
                updateDisplay('🎉 Correct! Well done!<br><button onclick="startGame()">Next Puzzle</button>');
            }} else {{
                updateDisplay(`❌ Not quite! The answer was ${{correct}}<br><button onclick="startGame()">Try Another</button>`);
            }}
        }}
        
        function enterCastle() {{
            score += 25;
            updateDisplay('🏰 You bravely enter the castle and find treasure! +25 points!<br><button onclick="startGame()">New Adventure</button>');
        }}
        
        function walkAround() {{
            score += 10;
            updateDisplay('🌳 You discover a hidden garden with magical flowers! +10 points!<br><button onclick="startGame()">New Adventure</button>');
        }}
        
        function resetGame() {{
            score = 0;
            gameState = 'start';
            updateDisplay('Welcome to your adventure! Click Start to begin.');
        }}
    </script>
</body>
</html>"""

@app.route('/', methods=['GET'])
def home():
    """Health check and service info"""
    groq_available = check_groq_availability()
    
    return jsonify({
        'service': 'Mythiq Game Maker',
        'status': 'online',
        'version': '2.0.0',
        'timestamp': datetime.now().isoformat(),
        'ai_status': {
            'groq_available': groq_available,
            'huggingface_available': False
        },
        'features': [
            'AI game concept generation with Groq',
            'Playable HTML5 games',
            'Multiple game themes (space, adventure, puzzle, racing)',
            'Real-time game creation',
            'Interactive gameplay'
        ],
        'message': 'AI-powered game generation with Groq integration'
    })

@app.route('/generate-game', methods=['POST', 'OPTIONS'])
def generate_game():
    """Generate a game based on user prompt"""
    
    # Handle preflight OPTIONS request
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({'error': 'Game prompt is required'}), 400
        
        prompt = data['prompt']
        
        # Try to generate with Groq first
        if GROQ_API_KEY:
            game_html = generate_game_with_groq(prompt)
            if game_html:
                return jsonify({
                    'game_html': game_html,
                    'source': 'groq',
                    'prompt': prompt,
                    'timestamp': datetime.now().isoformat(),
                    'message': 'Game generated successfully with AI'
                })
        
        # Fallback to template-based generation
        game_html = generate_fallback_game(prompt)
        
        return jsonify({
            'game_html': game_html,
            'source': 'template',
            'prompt': prompt,
            'timestamp': datetime.now().isoformat(),
            'message': 'Game generated with template system'
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Game generation failed',
            'message': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'mythiq-game-maker',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)
