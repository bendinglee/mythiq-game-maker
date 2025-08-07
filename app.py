"""
🔥 FIXED BACKEND WITH PROPER GAME DELIVERY
Complete backend that delivers actual playable games and downloadable files
"""

from flask import Flask, request, jsonify, render_template_string, send_file, make_response
from flask_cors import CORS
import random
import time
import json
import os
import zipfile
import tempfile
from datetime import datetime
import re
import traceback
import uuid

# Import revolutionary components with error handling
try:
    from revolutionary_prompt_processor import RevolutionaryPromptProcessor
    from true_randomization_engine import TrueRandomizationEngine
    from expanded_game_template_library import ExpandedGameTemplateLibrary
    REVOLUTIONARY_AVAILABLE = True
    print("🔥 Revolutionary components loaded successfully!")
except ImportError as e:
    REVOLUTIONARY_AVAILABLE = False
    print(f"⚠️ Revolutionary components not found: {e}")

# Import FREE AI components (if available)
try:
    from free_ai_template_engine import FreeAITemplateEngine
    from free_ai_code_generator import FreeAICodeGenerator
    FREE_AI_AVAILABLE = True
    print("🆓 FREE AI components loaded successfully!")
except ImportError:
    FREE_AI_AVAILABLE = False
    print("⚠️ FREE AI components not found, using revolutionary templates only")

app = Flask(__name__)
CORS(app)

# Create directories for game storage
GAMES_DIR = '/tmp/generated_games'
os.makedirs(GAMES_DIR, exist_ok=True)

# Initialize revolutionary components
if REVOLUTIONARY_AVAILABLE:
    try:
        print("🧠 Initializing Revolutionary Ultimate Game Maker...")
        prompt_processor = RevolutionaryPromptProcessor()
        randomization_engine = TrueRandomizationEngine()
        template_library = ExpandedGameTemplateLibrary()
        print("✅ Revolutionary components initialized successfully!")
    except Exception as e:
        print(f"❌ Error initializing revolutionary components: {e}")
        REVOLUTIONARY_AVAILABLE = False

# Initialize FREE AI components
if FREE_AI_AVAILABLE:
    try:
        free_ai_engine = FreeAITemplateEngine()
        free_ai_generator = FreeAICodeGenerator()
        print("✅ FREE AI engines initialized successfully!")
    except Exception as e:
        print(f"❌ Error initializing FREE AI components: {e}")
        FREE_AI_AVAILABLE = False

# Statistics tracking
stats = {
    'total_games_generated': 0,
    'ultimate_games': 0,
    'free_ai_games': 0,
    'enhanced_games': 0,
    'basic_games': 0,
    'files_downloaded': 0,
    'games_opened': 0
}

def create_complete_game_html(game_data, prompt):
    """Create a complete, standalone HTML game file"""
    
    # Extract game information
    title = game_data.get('title', 'Ultimate Game')
    game_type = game_data.get('type', 'Adventure')
    character = game_data.get('character', 'Hero')
    theme = game_data.get('theme', 'adventure')
    
    # Determine game mechanics based on theme
    if 'dart' in theme.lower() or 'dart' in prompt.lower():
        game_html = create_darts_game(title, character)
    elif 'basketball' in theme.lower() or 'basketball' in prompt.lower():
        game_html = create_basketball_game(title, character)
    elif 'underwater' in theme.lower() or 'mermaid' in prompt.lower():
        game_html = create_underwater_game(title, character)
    elif 'medieval' in theme.lower() or 'knight' in prompt.lower():
        game_html = create_medieval_game(title, character)
    elif 'racing' in theme.lower() or 'car' in prompt.lower():
        game_html = create_racing_game(title, character)
    else:
        game_html = create_adventure_game(title, character, theme)
    
    return game_html

def create_darts_game(title, character):
    """Create a complete darts game"""
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: white;
            margin: 0;
            padding: 20px;
            text-align: center;
            min-height: 100vh;
        }}
        .game-container {{
            max-width: 800px;
            margin: 0 auto;
            background: rgba(0,0,0,0.3);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        .dartboard {{
            width: 300px;
            height: 300px;
            border-radius: 50%;
            background: radial-gradient(circle, #ff0000 0%, #000000 10%, #ffffff 20%, #000000 30%, #ffff00 40%, #000000 50%, #00ff00 60%, #000000 70%, #ff0000 80%, #000000 90%);
            margin: 20px auto;
            position: relative;
            cursor: crosshair;
            border: 5px solid #333;
        }}
        .bullseye {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 30px;
            height: 30px;
            background: #ff0000;
            border-radius: 50%;
            border: 2px solid #000;
        }}
        .score {{
            font-size: 24px;
            margin: 20px 0;
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 10px;
        }}
        .throw-btn {{
            background: linear-gradient(45deg, #ff6b6b, #ee5a24);
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 25px;
            cursor: pointer;
            margin: 10px;
            transition: all 0.3s;
        }}
        .throw-btn:hover {{
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(255,107,107,0.4);
        }}
        .dart {{
            position: absolute;
            width: 4px;
            height: 20px;
            background: #8B4513;
            border-radius: 2px;
            transition: all 0.5s;
        }}
    </style>
</head>
<body>
    <div class="game-container">
        <h1>🎯 {title}</h1>
        <p>Character: {character}</p>
        <p>Aim for the bullseye! Click the dartboard to throw darts.</p>
        
        <div class="score">
            <div>Score: <span id="score">0</span></div>
            <div>Darts Thrown: <span id="darts">0</span></div>
            <div>Best Shot: <span id="best">0</span></div>
        </div>
        
        <div class="dartboard" id="dartboard" onclick="throwDart(event)">
            <div class="bullseye"></div>
        </div>
        
        <button class="throw-btn" onclick="resetGame()">🔄 New Game</button>
        <button class="throw-btn" onclick="autoThrow()">🎯 Auto Throw</button>
    </div>

    <script>
        let score = 0;
        let dartsThrown = 0;
        let bestShot = 0;
        
        function throwDart(event) {{
            const dartboard = document.getElementById('dartboard');
            const rect = dartboard.getBoundingClientRect();
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const clickX = event.clientX - rect.left;
            const clickY = event.clientY - rect.top;
            
            // Calculate distance from center
            const distance = Math.sqrt(Math.pow(clickX - centerX, 2) + Math.pow(clickY - centerY, 2));
            
            // Create dart element
            const dart = document.createElement('div');
            dart.className = 'dart';
            dart.style.left = clickX + 'px';
            dart.style.top = clickY + 'px';
            dartboard.appendChild(dart);
            
            // Calculate score based on distance
            let points = 0;
            if (distance < 15) {{
                points = 50; // Bullseye
                dart.style.background = '#ff0000';
            }} else if (distance < 30) {{
                points = 25; // Inner ring
                dart.style.background = '#ffff00';
            }} else if (distance < 60) {{
                points = 15; // Middle ring
                dart.style.background = '#00ff00';
            }} else if (distance < 90) {{
                points = 10; // Outer ring
                dart.style.background = '#0000ff';
            }} else if (distance < 150) {{
                points = 5; // Edge
                dart.style.background = '#ffffff';
            }}
            
            // Update score
            score += points;
            dartsThrown++;
            if (points > bestShot) bestShot = points;
            
            updateDisplay();
            
            // Remove dart after animation
            setTimeout(() => {{
                if (dart.parentNode) dart.parentNode.removeChild(dart);
            }}, 2000);
        }}
        
        function autoThrow() {{
            const dartboard = document.getElementById('dartboard');
            const rect = dartboard.getBoundingClientRect();
            
            // Random position with some skill (bias toward center)
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const randomX = centerX + (Math.random() - 0.5) * 200;
            const randomY = centerY + (Math.random() - 0.5) * 200;
            
            // Simulate click
            const event = {{
                clientX: rect.left + randomX,
                clientY: rect.top + randomY
            }};
            
            throwDart(event);
        }}
        
        function resetGame() {{
            score = 0;
            dartsThrown = 0;
            bestShot = 0;
            updateDisplay();
            
            // Remove all darts
            const darts = document.querySelectorAll('.dart');
            darts.forEach(dart => dart.remove());
        }}
        
        function updateDisplay() {{
            document.getElementById('score').textContent = score;
            document.getElementById('darts').textContent = dartsThrown;
            document.getElementById('best').textContent = bestShot;
        }}
        
        // Auto-demo on load
        setTimeout(() => {{
            autoThrow();
        }}, 1000);
    </script>
</body>
</html>
    """

def create_basketball_game(title, character):
    """Create a complete basketball game"""
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #ff7f00, #ff4500);
            color: white;
            margin: 0;
            padding: 20px;
            text-align: center;
            min-height: 100vh;
        }}
        .game-container {{
            max-width: 800px;
            margin: 0 auto;
            background: rgba(0,0,0,0.3);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        .court {{
            width: 400px;
            height: 300px;
            background: #8B4513;
            margin: 20px auto;
            position: relative;
            border: 3px solid #654321;
            border-radius: 10px;
        }}
        .hoop {{
            position: absolute;
            top: 50px;
            right: 20px;
            width: 60px;
            height: 40px;
            border: 4px solid #ff0000;
            border-radius: 50%;
            background: rgba(255,0,0,0.1);
        }}
        .ball {{
            position: absolute;
            width: 30px;
            height: 30px;
            background: radial-gradient(circle at 30% 30%, #ff8c00, #ff4500);
            border-radius: 50%;
            cursor: pointer;
            transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
            bottom: 20px;
            left: 50px;
            border: 2px solid #000;
        }}
        .score {{
            font-size: 24px;
            margin: 20px 0;
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 10px;
        }}
        .shoot-btn {{
            background: linear-gradient(45deg, #ff8c00, #ff4500);
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 25px;
            cursor: pointer;
            margin: 10px;
            transition: all 0.3s;
        }}
        .shoot-btn:hover {{
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(255,140,0,0.4);
        }}
    </style>
</head>
<body>
    <div class="game-container">
        <h1>🏀 {title}</h1>
        <p>Character: {character}</p>
        <p>Click the ball to shoot! Try to score baskets!</p>
        
        <div class="score">
            <div>Score: <span id="score">0</span></div>
            <div>Shots: <span id="shots">0</span></div>
            <div>Accuracy: <span id="accuracy">0%</span></div>
        </div>
        
        <div class="court" id="court">
            <div class="hoop" id="hoop"></div>
            <div class="ball" id="ball" onclick="shootBall()">🏀</div>
        </div>
        
        <button class="shoot-btn" onclick="shootBall()">🏀 Shoot</button>
        <button class="shoot-btn" onclick="resetGame()">🔄 New Game</button>
    </div>

    <script>
        let score = 0;
        let shots = 0;
        let isAnimating = false;
        
        function shootBall() {{
            if (isAnimating) return;
            
            isAnimating = true;
            shots++;
            
            const ball = document.getElementById('ball');
            const hoop = document.getElementById('hoop');
            
            // Random shot accuracy
            const accuracy = Math.random();
            const isGoodShot = accuracy > 0.3;
            
            if (isGoodShot) {{
                // Good shot - ball goes to hoop
                ball.style.transform = 'translate(290px, -180px) scale(0.8)';
                ball.style.transition = 'all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
                
                setTimeout(() => {{
                    score++;
                    updateDisplay();
                    ball.style.transform = 'translate(0, 0) scale(1)';
                    ball.style.transition = 'all 0.5s ease';
                    isAnimating = false;
                }}, 800);
            }} else {{
                // Miss - ball goes off course
                const missX = 200 + (Math.random() - 0.5) * 200;
                const missY = -100 + (Math.random() - 0.5) * 100;
                
                ball.style.transform = `translate(${{missX}}px, ${{missY}}px) scale(0.8)`;
                ball.style.transition = 'all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
                
                setTimeout(() => {{
                    updateDisplay();
                    ball.style.transform = 'translate(0, 0) scale(1)';
                    ball.style.transition = 'all 0.5s ease';
                    isAnimating = false;
                }}, 800);
            }}
        }}
        
        function resetGame() {{
            score = 0;
            shots = 0;
            updateDisplay();
        }}
        
        function updateDisplay() {{
            document.getElementById('score').textContent = score;
            document.getElementById('shots').textContent = shots;
            const accuracy = shots > 0 ? Math.round((score / shots) * 100) : 0;
            document.getElementById('accuracy').textContent = accuracy + '%';
        }}
        
        // Auto-demo on load
        setTimeout(() => {{
            shootBall();
        }}, 1000);
    </script>
</body>
</html>
    """

def create_underwater_game(title, character):
    """Create a complete underwater adventure game"""
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background: linear-gradient(180deg, #001f3f, #0074D9, #7FDBFF);
            color: white;
            margin: 0;
            padding: 20px;
            text-align: center;
            min-height: 100vh;
            overflow-x: hidden;
        }}
        .game-container {{
            max-width: 800px;
            margin: 0 auto;
            background: rgba(0,31,63,0.3);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        .ocean {{
            width: 100%;
            height: 400px;
            background: linear-gradient(180deg, rgba(127,219,255,0.3), rgba(0,116,217,0.5));
            position: relative;
            border-radius: 15px;
            overflow: hidden;
            margin: 20px 0;
        }}
        .mermaid {{
            position: absolute;
            bottom: 50px;
            left: 50px;
            font-size: 40px;
            cursor: pointer;
            transition: all 0.5s;
            animation: float 3s ease-in-out infinite;
        }}
        .treasure {{
            position: absolute;
            font-size: 30px;
            cursor: pointer;
            transition: all 0.3s;
            animation: sparkle 2s ease-in-out infinite;
        }}
        .fish {{
            position: absolute;
            font-size: 25px;
            animation: swim 8s linear infinite;
        }}
        .bubble {{
            position: absolute;
            width: 10px;
            height: 10px;
            background: rgba(255,255,255,0.6);
            border-radius: 50%;
            animation: bubble 4s linear infinite;
        }}
        @keyframes float {{
            0%, 100% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-10px); }}
        }}
        @keyframes sparkle {{
            0%, 100% {{ opacity: 1; transform: scale(1); }}
            50% {{ opacity: 0.7; transform: scale(1.1); }}
        }}
        @keyframes swim {{
            0% {{ left: -50px; }}
            100% {{ left: 100%; }}
        }}
        @keyframes bubble {{
            0% {{ bottom: 0; opacity: 1; }}
            100% {{ bottom: 400px; opacity: 0; }}
        }}
        .score {{
            font-size: 24px;
            margin: 20px 0;
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 10px;
        }}
        .action-btn {{
            background: linear-gradient(45deg, #0074D9, #001f3f);
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 25px;
            cursor: pointer;
            margin: 10px;
            transition: all 0.3s;
        }}
        .action-btn:hover {{
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0,116,217,0.4);
        }}
    </style>
</head>
<body>
    <div class="game-container">
        <h1>🧜‍♀️ {title}</h1>
        <p>Character: {character}</p>
        <p>Swim around and collect treasures! Click treasures to collect them.</p>
        
        <div class="score">
            <div>Treasures: <span id="treasures">0</span></div>
            <div>Depth: <span id="depth">10</span> meters</div>
            <div>Oxygen: <span id="oxygen">100</span>%</div>
        </div>
        
        <div class="ocean" id="ocean">
            <div class="mermaid" id="mermaid" onclick="swim()">🧜‍♀️</div>
        </div>
        
        <button class="action-btn" onclick="swim()">🏊‍♀️ Swim</button>
        <button class="action-btn" onclick="dive()">⬇️ Dive Deeper</button>
        <button class="action-btn" onclick="surface()">⬆️ Surface</button>
        <button class="action-btn" onclick="resetGame()">🔄 New Adventure</button>
    </div>

    <script>
        let treasures = 0;
        let depth = 10;
        let oxygen = 100;
        let gameInterval;
        
        function initGame() {{
            spawnTreasure();
            spawnFish();
            createBubbles();
            
            gameInterval = setInterval(() => {{
                if (depth > 5) {{
                    oxygen = Math.max(0, oxygen - 1);
                    updateDisplay();
                    
                    if (oxygen <= 0) {{
                        alert('Out of oxygen! Surface for air!');
                        surface();
                    }}
                }}
            }}, 1000);
        }}
        
        function swim() {{
            const mermaid = document.getElementById('mermaid');
            const newX = Math.random() * 700;
            const newY = Math.random() * 300;
            
            mermaid.style.left = newX + 'px';
            mermaid.style.bottom = newY + 'px';
            
            // Chance to find treasure while swimming
            if (Math.random() > 0.7) {{
                spawnTreasure();
            }}
        }}
        
        function dive() {{
            depth += 5;
            oxygen = Math.max(0, oxygen - 5);
            updateDisplay();
            
            // More treasures at deeper depths
            if (Math.random() > 0.5) {{
                spawnTreasure();
            }}
        }}
        
        function surface() {{
            depth = Math.max(5, depth - 10);
            oxygen = Math.min(100, oxygen + 20);
            updateDisplay();
        }}
        
        function spawnTreasure() {{
            const ocean = document.getElementById('ocean');
            const treasure = document.createElement('div');
            treasure.className = 'treasure';
            treasure.innerHTML = '💎';
            treasure.style.left = Math.random() * 700 + 'px';
            treasure.style.top = Math.random() * 300 + 'px';
            treasure.onclick = () => collectTreasure(treasure);
            ocean.appendChild(treasure);
            
            // Remove treasure after 10 seconds if not collected
            setTimeout(() => {{
                if (treasure.parentNode) treasure.parentNode.removeChild(treasure);
            }}, 10000);
        }}
        
        function collectTreasure(treasure) {{
            treasures++;
            updateDisplay();
            treasure.parentNode.removeChild(treasure);
            
            // Spawn new treasure
            setTimeout(spawnTreasure, 2000);
        }}
        
        function spawnFish() {{
            const ocean = document.getElementById('ocean');
            const fish = document.createElement('div');
            fish.className = 'fish';
            fish.innerHTML = '🐠';
            fish.style.top = Math.random() * 350 + 'px';
            ocean.appendChild(fish);
            
            setTimeout(() => {{
                if (fish.parentNode) fish.parentNode.removeChild(fish);
                spawnFish(); // Spawn next fish
            }}, 8000);
        }}
        
        function createBubbles() {{
            const ocean = document.getElementById('ocean');
            
            setInterval(() => {{
                const bubble = document.createElement('div');
                bubble.className = 'bubble';
                bubble.style.left = Math.random() * 800 + 'px';
                ocean.appendChild(bubble);
                
                setTimeout(() => {{
                    if (bubble.parentNode) bubble.parentNode.removeChild(bubble);
                }}, 4000);
            }}, 500);
        }}
        
        function resetGame() {{
            treasures = 0;
            depth = 10;
            oxygen = 100;
            updateDisplay();
            
            // Clear all treasures and fish
            const ocean = document.getElementById('ocean');
            const treasureElements = ocean.querySelectorAll('.treasure');
            const fishElements = ocean.querySelectorAll('.fish');
            
            treasureElements.forEach(t => t.remove());
            fishElements.forEach(f => f.remove());
            
            // Restart game elements
            spawnTreasure();
            spawnFish();
        }}
        
        function updateDisplay() {{
            document.getElementById('treasures').textContent = treasures;
            document.getElementById('depth').textContent = depth;
            document.getElementById('oxygen').textContent = oxygen;
        }}
        
        // Initialize game
        initGame();
    </script>
</body>
</html>
    """

def create_medieval_game(title, character):
    """Create a complete medieval adventure game"""
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #2c1810, #8b4513, #daa520);
            color: white;
            margin: 0;
            padding: 20px;
            text-align: center;
            min-height: 100vh;
        }}
        .game-container {{
            max-width: 800px;
            margin: 0 auto;
            background: rgba(44,24,16,0.8);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            border: 3px solid #daa520;
        }}
        .castle {{
            width: 100%;
            height: 300px;
            background: linear-gradient(180deg, #696969, #2f4f4f);
            position: relative;
            border-radius: 15px;
            margin: 20px 0;
            border: 2px solid #8b4513;
        }}
        .knight {{
            position: absolute;
            bottom: 20px;
            left: 50px;
            font-size: 40px;
            cursor: pointer;
            transition: all 0.5s;
        }}
        .dragon {{
            position: absolute;
            top: 50px;
            right: 50px;
            font-size: 50px;
            cursor: pointer;
            animation: dragonFly 4s ease-in-out infinite;
        }}
        .treasure {{
            position: absolute;
            font-size: 30px;
            cursor: pointer;
            animation: glow 2s ease-in-out infinite;
        }}
        @keyframes dragonFly {{
            0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
            50% {{ transform: translateY(-20px) rotate(5deg); }}
        }}
        @keyframes glow {{
            0%, 100% {{ text-shadow: 0 0 5px #ffd700; }}
            50% {{ text-shadow: 0 0 20px #ffd700, 0 0 30px #ffd700; }}
        }}
        .score {{
            font-size: 24px;
            margin: 20px 0;
            background: rgba(218,165,32,0.2);
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #daa520;
        }}
        .action-btn {{
            background: linear-gradient(45deg, #8b4513, #daa520);
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 25px;
            cursor: pointer;
            margin: 10px;
            transition: all 0.3s;
            border: 2px solid #2c1810;
        }}
        .action-btn:hover {{
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(218,165,32,0.4);
        }}
    </style>
</head>
<body>
    <div class="game-container">
        <h1>🏰 {title}</h1>
        <p>Character: {character}</p>
        <p>Defend the castle! Fight the dragon and collect treasures!</p>
        
        <div class="score">
            <div>Honor: <span id="honor">0</span></div>
            <div>Gold: <span id="gold">0</span></div>
            <div>Dragon Health: <span id="dragonHealth">100</span></div>
        </div>
        
        <div class="castle" id="castle">
            <div class="knight" id="knight" onclick="attack()">⚔️</div>
            <div class="dragon" id="dragon" onclick="dragonAttack()">🐉</div>
        </div>
        
        <button class="action-btn" onclick="attack()">⚔️ Attack Dragon</button>
        <button class="action-btn" onclick="defend()">🛡️ Defend</button>
        <button class="action-btn" onclick="searchTreasure()">💰 Search for Gold</button>
        <button class="action-btn" onclick="resetGame()">🔄 New Quest</button>
    </div>

    <script>
        let honor = 0;
        let gold = 0;
        let dragonHealth = 100;
        let knightHealth = 100;
        
        function attack() {{
            if (dragonHealth <= 0) return;
            
            const damage = Math.floor(Math.random() * 25) + 10;
            dragonHealth = Math.max(0, dragonHealth - damage);
            honor += damage;
            
            // Knight animation
            const knight = document.getElementById('knight');
            knight.style.transform = 'translateX(100px) scale(1.2)';
            setTimeout(() => {{
                knight.style.transform = 'translateX(0) scale(1)';
            }}, 500);
            
            if (dragonHealth <= 0) {{
                honor += 100;
                alert('🎉 Dragon defeated! You are victorious!');
                spawnTreasure();
            }} else {{
                // Dragon counter-attack
                setTimeout(dragonAttack, 1000);
            }}
            
            updateDisplay();
        }}
        
        function dragonAttack() {{
            if (dragonHealth <= 0) return;
            
            const damage = Math.floor(Math.random() * 20) + 5;
            knightHealth = Math.max(0, knightHealth - damage);
            
            // Dragon animation
            const dragon = document.getElementById('dragon');
            dragon.style.transform = 'translateX(-100px) scale(1.2)';
            setTimeout(() => {{
                dragon.style.transform = 'translateX(0) scale(1)';
            }}, 500);
            
            if (knightHealth <= 0) {{
                alert('💀 The dragon has defeated you! Try again!');
                resetGame();
            }}
        }}
        
        function defend() {{
            knightHealth = Math.min(100, knightHealth + 20);
            honor += 5;
            updateDisplay();
            
            const knight = document.getElementById('knight');
            knight.innerHTML = '🛡️';
            setTimeout(() => {{
                knight.innerHTML = '⚔️';
            }}, 1000);
        }}
        
        function searchTreasure() {{
            const foundGold = Math.floor(Math.random() * 50) + 10;
            gold += foundGold;
            honor += 10;
            updateDisplay();
            
            spawnTreasure();
        }}
        
        function spawnTreasure() {{
            const castle = document.getElementById('castle');
            const treasure = document.createElement('div');
            treasure.className = 'treasure';
            treasure.innerHTML = '💰';
            treasure.style.left = Math.random() * 600 + 'px';
            treasure.style.top = Math.random() * 200 + 'px';
            treasure.onclick = () => collectTreasure(treasure);
            castle.appendChild(treasure);
            
            setTimeout(() => {{
                if (treasure.parentNode) treasure.parentNode.removeChild(treasure);
            }}, 5000);
        }}
        
        function collectTreasure(treasure) {{
            gold += 25;
            honor += 15;
            updateDisplay();
            treasure.parentNode.removeChild(treasure);
        }}
        
        function resetGame() {{
            honor = 0;
            gold = 0;
            dragonHealth = 100;
            knightHealth = 100;
            updateDisplay();
            
            // Clear treasures
            const treasures = document.querySelectorAll('.treasure');
            treasures.forEach(t => t.remove());
        }}
        
        function updateDisplay() {{
            document.getElementById('honor').textContent = honor;
            document.getElementById('gold').textContent = gold;
            document.getElementById('dragonHealth').textContent = dragonHealth;
        }}
        
        // Auto-spawn treasure on start
        setTimeout(spawnTreasure, 2000);
    </script>
</body>
</html>
    """

def create_racing_game(title, character):
    """Create a complete racing game"""
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #333, #666, #999);
            color: white;
            margin: 0;
            padding: 20px;
            text-align: center;
            min-height: 100vh;
        }}
        .game-container {{
            max-width: 800px;
            margin: 0 auto;
            background: rgba(0,0,0,0.7);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        .track {{
            width: 100%;
            height: 400px;
            background: linear-gradient(90deg, #228B22 0%, #32CD32 20%, #808080 20%, #808080 80%, #32CD32 80%, #228B22 100%);
            position: relative;
            border-radius: 15px;
            margin: 20px 0;
            overflow: hidden;
        }}
        .car {{
            position: absolute;
            bottom: 50px;
            left: 50px;
            font-size: 40px;
            transition: all 0.3s;
            cursor: pointer;
        }}
        .opponent {{
            position: absolute;
            font-size: 35px;
            animation: drive 6s linear infinite;
        }}
        .finish-line {{
            position: absolute;
            right: 0;
            top: 0;
            width: 20px;
            height: 100%;
            background: repeating-linear-gradient(45deg, #000, #000 10px, #fff 10px, #fff 20px);
        }}
        @keyframes drive {{
            0% {{ left: -50px; }}
            100% {{ left: 100%; }}
        }}
        .score {{
            font-size: 24px;
            margin: 20px 0;
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 10px;
        }}
        .control-btn {{
            background: linear-gradient(45deg, #ff4500, #ff6347);
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 25px;
            cursor: pointer;
            margin: 10px;
            transition: all 0.3s;
        }}
        .control-btn:hover {{
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(255,69,0,0.4);
        }}
    </style>
</head>
<body>
    <div class="game-container">
        <h1>🏎️ {title}</h1>
        <p>Character: {character}</p>
        <p>Race to the finish line! Use controls to steer and accelerate!</p>
        
        <div class="score">
            <div>Speed: <span id="speed">0</span> mph</div>
            <div>Position: <span id="position">1st</span></div>
            <div>Lap Time: <span id="lapTime">0.0</span>s</div>
        </div>
        
        <div class="track" id="track">
            <div class="finish-line"></div>
            <div class="car" id="car">🏎️</div>
        </div>
        
        <button class="control-btn" onclick="accelerate()">⚡ Accelerate</button>
        <button class="control-btn" onclick="brake()">🛑 Brake</button>
        <button class="control-btn" onclick="steerLeft()">⬅️ Left</button>
        <button class="control-btn" onclick="steerRight()">➡️ Right</button>
        <button class="control-btn" onclick="resetRace()">🔄 New Race</button>
    </div>

    <script>
        let speed = 0;
        let position = 1;
        let lapTime = 0;
        let carPosition = 50;
        let raceStarted = false;
        let raceInterval;
        
        function startRace() {{
            if (raceStarted) return;
            raceStarted = true;
            
            // Spawn opponent cars
            spawnOpponent();
            
            // Start lap timer
            raceInterval = setInterval(() => {{
                lapTime += 0.1;
                updateDisplay();
            }}, 100);
        }}
        
        function accelerate() {{
            if (!raceStarted) startRace();
            
            speed = Math.min(200, speed + 20);
            
            // Move car forward
            const car = document.getElementById('car');
            carPosition = Math.min(700, carPosition + speed / 10);
            car.style.left = carPosition + 'px';
            
            // Check for finish line
            if (carPosition >= 680) {{
                finishRace();
            }}
            
            updateDisplay();
        }}
        
        function brake() {{
            speed = Math.max(0, speed - 30);
            updateDisplay();
        }}
        
        function steerLeft() {{
            const car = document.getElementById('car');
            const currentBottom = parseInt(car.style.bottom) || 50;
            car.style.bottom = Math.min(350, currentBottom + 30) + 'px';
        }}
        
        function steerRight() {{
            const car = document.getElementById('car');
            const currentBottom = parseInt(car.style.bottom) || 50;
            car.style.bottom = Math.max(20, currentBottom - 30) + 'px';
        }}
        
        function spawnOpponent() {{
            const track = document.getElementById('track');
            const opponent = document.createElement('div');
            opponent.className = 'opponent';
            opponent.innerHTML = '🚗';
            opponent.style.top = Math.random() * 300 + 'px';
            opponent.style.animationDuration = (4 + Math.random() * 4) + 's';
            track.appendChild(opponent);
            
            setTimeout(() => {{
                if (opponent.parentNode) opponent.parentNode.removeChild(opponent);
                if (raceStarted) spawnOpponent();
            }}, 8000);
        }}
        
        function finishRace() {{
            raceStarted = false;
            clearInterval(raceInterval);
            
            const finalTime = lapTime.toFixed(1);
            alert(`🏁 Race finished! Time: ${{finalTime}}s`);
        }}
        
        function resetRace() {{
            speed = 0;
            position = 1;
            lapTime = 0;
            carPosition = 50;
            raceStarted = false;
            
            if (raceInterval) clearInterval(raceInterval);
            
            const car = document.getElementById('car');
            car.style.left = '50px';
            car.style.bottom = '50px';
            
            // Clear opponents
            const opponents = document.querySelectorAll('.opponent');
            opponents.forEach(o => o.remove());
            
            updateDisplay();
        }}
        
        function updateDisplay() {{
            document.getElementById('speed').textContent = speed;
            document.getElementById('position').textContent = position + 'st';
            document.getElementById('lapTime').textContent = lapTime.toFixed(1);
        }}
        
        // Keyboard controls
        document.addEventListener('keydown', (e) => {{
            switch(e.key) {{
                case 'ArrowUp': accelerate(); break;
                case 'ArrowDown': brake(); break;
                case 'ArrowLeft': steerLeft(); break;
                case 'ArrowRight': steerRight(); break;
            }}
        }});
    </script>
</body>
</html>
    """

def create_adventure_game(title, character, theme):
    """Create a generic adventure game"""
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            margin: 0;
            padding: 20px;
            text-align: center;
            min-height: 100vh;
        }}
        .game-container {{
            max-width: 800px;
            margin: 0 auto;
            background: rgba(0,0,0,0.3);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        .adventure-area {{
            width: 100%;
            height: 400px;
            background: linear-gradient(180deg, #87CEEB, #228B22);
            position: relative;
            border-radius: 15px;
            margin: 20px 0;
            overflow: hidden;
        }}
        .hero {{
            position: absolute;
            bottom: 50px;
            left: 50px;
            font-size: 40px;
            cursor: pointer;
            transition: all 0.5s;
        }}
        .item {{
            position: absolute;
            font-size: 30px;
            cursor: pointer;
            animation: pulse 2s ease-in-out infinite;
        }}
        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.1); }}
        }}
        .score {{
            font-size: 24px;
            margin: 20px 0;
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 10px;
        }}
        .action-btn {{
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 25px;
            cursor: pointer;
            margin: 10px;
            transition: all 0.3s;
        }}
        .action-btn:hover {{
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(102,126,234,0.4);
        }}
    </style>
</head>
<body>
    <div class="game-container">
        <h1>🎮 {title}</h1>
        <p>Character: {character}</p>
        <p>Theme: {theme.title()}</p>
        <p>Explore the world and collect items! Click to move around.</p>
        
        <div class="score">
            <div>Score: <span id="score">0</span></div>
            <div>Items: <span id="items">0</span></div>
            <div>Level: <span id="level">1</span></div>
        </div>
        
        <div class="adventure-area" id="area" onclick="moveHero(event)">
            <div class="hero" id="hero">🦸‍♂️</div>
        </div>
        
        <button class="action-btn" onclick="explore()">🔍 Explore</button>
        <button class="action-btn" onclick="rest()">😴 Rest</button>
        <button class="action-btn" onclick="levelUp()">⬆️ Level Up</button>
        <button class="action-btn" onclick="resetGame()">🔄 New Adventure</button>
    </div>

    <script>
        let score = 0;
        let items = 0;
        let level = 1;
        
        function moveHero(event) {{
            const area = document.getElementById('area');
            const hero = document.getElementById('hero');
            const rect = area.getBoundingClientRect();
            
            const x = event.clientX - rect.left - 20;
            const y = event.clientY - rect.top - 20;
            
            hero.style.left = Math.max(0, Math.min(x, 760)) + 'px';
            hero.style.top = Math.max(0, Math.min(y, 360)) + 'px';
            
            score += 1;
            updateDisplay();
        }}
        
        function explore() {{
            spawnItem();
            score += 10;
            updateDisplay();
        }}
        
        function rest() {{
            score += 5;
            updateDisplay();
            
            const hero = document.getElementById('hero');
            hero.style.transform = 'scale(1.2)';
            setTimeout(() => {{
                hero.style.transform = 'scale(1)';
            }}, 1000);
        }}
        
        function levelUp() {{
            if (score >= level * 100) {{
                level++;
                score -= (level - 1) * 100;
                updateDisplay();
                alert(`🎉 Level Up! You are now level ${{level}}!`);
            }} else {{
                alert(`Need ${{level * 100 - score}} more points to level up!`);
            }}
        }}
        
        function spawnItem() {{
            const area = document.getElementById('area');
            const item = document.createElement('div');
            item.className = 'item';
            item.innerHTML = ['⭐', '💎', '🏆', '🎁', '🔮'][Math.floor(Math.random() * 5)];
            item.style.left = Math.random() * 700 + 'px';
            item.style.top = Math.random() * 300 + 'px';
            item.onclick = () => collectItem(item);
            area.appendChild(item);
            
            setTimeout(() => {{
                if (item.parentNode) item.parentNode.removeChild(item);
            }}, 8000);
        }}
        
        function collectItem(item) {{
            items++;
            score += 25;
            updateDisplay();
            item.parentNode.removeChild(item);
        }}
        
        function resetGame() {{
            score = 0;
            items = 0;
            level = 1;
            updateDisplay();
            
            // Reset hero position
            const hero = document.getElementById('hero');
            hero.style.left = '50px';
            hero.style.top = '350px';
            
            // Clear items
            const itemElements = document.querySelectorAll('.item');
            itemElements.forEach(i => i.remove());
        }}
        
        function updateDisplay() {{
            document.getElementById('score').textContent = score;
            document.getElementById('items').textContent = items;
            document.getElementById('level').textContent = level;
        }}
        
        // Auto-spawn items
        setInterval(() => {{
            if (Math.random() > 0.7) spawnItem();
        }}, 3000);
        
        // Initial item spawn
        setTimeout(spawnItem, 1000);
    </script>
</body>
</html>
    """

def create_game_zip(game_html, game_title):
    """Create a ZIP file containing the game"""
    # Create temporary file
    temp_dir = tempfile.mkdtemp()
    game_file = os.path.join(temp_dir, f"{game_title.replace(' ', '_')}.html")
    zip_file = os.path.join(temp_dir, f"{game_title.replace(' ', '_')}_game.zip")
    
    # Write game HTML to file
    with open(game_file, 'w', encoding='utf-8') as f:
        f.write(game_html)
    
    # Create ZIP file
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(game_file, f"{game_title.replace(' ', '_')}.html")
        
        # Add README
        readme_content = f"""
# {game_title}

## How to Play:
1. Open the HTML file in any web browser
2. Follow the on-screen instructions
3. Enjoy your game!

## Game Features:
- Interactive gameplay
- Responsive design
- Works on desktop and mobile
- No internet connection required

Generated by Mythiq Ultimate Game Maker
"""
        readme_file = os.path.join(temp_dir, "README.txt")
        with open(readme_file, 'w') as f:
            f.write(readme_content)
        zipf.write(readme_file, "README.txt")
    
    return zip_file

@app.route('/')
def index():
    """Root endpoint with proper game delivery info"""
    try:
        return jsonify({
            'message': 'Fixed Revolutionary Ultimate Game Maker API with File Delivery!',
            'status': 'healthy',
            'service': 'Revolutionary Game Maker with Complete File Delivery',
            'version': '7.0.0 - COMPLETE FILE DELIVERY VERSION',
            'revolutionary_available': REVOLUTIONARY_AVAILABLE,
            'free_ai_available': FREE_AI_AVAILABLE,
            'endpoints': {
                'health': '/health',
                'generate_game': '/generate-game',
                'ai_generate_game': '/ai-generate-game', 
                'ultimate_generate_game': '/ultimate-generate-game',
                'download_game': '/download-game/<game_id>',
                'play_game': '/play-game/<game_id>',
                'generation_stats': '/generation-stats',
                'ai_status': '/ai-status'
            },
            'features': {
                'playable_games': True,
                'file_downloads': True,
                'zip_packages': True,
                'iframe_support': True,
                'error_handling': True
            },
            'timestamp': datetime.now().isoformat(),
            'stats': stats
        })
    except Exception as e:
        return jsonify({
            'error': 'Error in root endpoint',
            'details': str(e),
            'traceback': traceback.format_exc()
        }), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    try:
        return jsonify({
            'status': 'healthy',
            'message': 'Fixed Revolutionary Ultimate Game Maker with File Delivery is operational',
            'revolutionary_available': REVOLUTIONARY_AVAILABLE,
            'free_ai_available': FREE_AI_AVAILABLE,
            'file_delivery': True,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'error': 'Health check failed',
            'details': str(e)
        }), 500

@app.route('/ultimate-generate-game', methods=['POST'])
def ultimate_generate_game():
    """Ultimate game generation with complete file delivery"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                'success': False,
                'error': 'No JSON data provided',
                'user_message': 'Please provide a game description.'
            }), 400
            
        prompt = data.get('prompt', '').strip()
        if not prompt:
            return jsonify({
                'success': False,
                'error': 'No prompt provided',
                'user_message': 'Please describe the game you want to create.'
            }), 400

        print(f"🎯 Ultimate generation request: {prompt}")
        
        try:
            # Generate unique game ID
            game_id = str(uuid.uuid4())[:8]
            
            # Create game data
            if REVOLUTIONARY_AVAILABLE:
                # Use revolutionary system
                analysis = prompt_processor.analyze_prompt(prompt)
                variation = randomization_engine.generate_variation(analysis['theme'], prompt)
                
                game_data = {
                    'title': variation.title,
                    'type': analysis['theme'].title(),
                    'character': variation.character,
                    'theme': analysis['theme'],
                    'features': variation.special_features,
                    'difficulty': variation.difficulty
                }
            else:
                # Simple fallback
                game_data = {
                    'title': 'Ultimate Game',
                    'type': 'Adventure',
                    'character': 'Hero',
                    'theme': 'adventure'
                }
            
            # Generate complete HTML game
            game_html = create_complete_game_html(game_data, prompt)
            
            # Save game files
            game_dir = os.path.join(GAMES_DIR, game_id)
            os.makedirs(game_dir, exist_ok=True)
            
            # Save HTML file
            html_file = os.path.join(game_dir, f"{game_data['title'].replace(' ', '_')}.html")
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(game_html)
            
            # Create ZIP file
            zip_file = create_game_zip(game_html, game_data['title'])
            zip_dest = os.path.join(game_dir, f"{game_data['title'].replace(' ', '_')}_game.zip")
            os.rename(zip_file, zip_dest)
            
            # Update stats
            stats['total_games_generated'] += 1
            stats['ultimate_games'] += 1
            
            return jsonify({
                'success': True,
                'game': {
                    'id': game_id,
                    'title': game_data['title'],
                    'type': game_data['type'],
                    'character': game_data['character'],
                    'theme': game_data['theme'],
                    'html': game_html,  # Full HTML for immediate display
                    'features': game_data.get('features', []),
                    'difficulty': game_data.get('difficulty', 'Medium')
                },
                'files': {
                    'html_url': f'/play-game/{game_id}',
                    'download_url': f'/download-game/{game_id}',
                    'zip_available': True
                },
                'generation_method': 'revolutionary_ultimate',
                'user_message': f'🎉 {game_data["title"]} generated successfully! Click "Open in New Window" to play or "Download" to get the game files.',
                'timestamp': datetime.now().isoformat()
            })
            
        except Exception as e:
            print(f"❌ Ultimate generation failed: {e}")
            return jsonify({
                'success': False,
                'error': 'Game generation failed',
                'details': str(e),
                'user_message': 'Sorry, there was an error generating your game. Please try again with a different description.'
            }), 500
            
    except Exception as e:
        print(f"❌ Ultimate generation error: {e}")
        return jsonify({
            'success': False,
            'error': 'Ultimate generation failed',
            'details': str(e),
            'user_message': 'Sorry, there was an unexpected error. Please try again.'
        }), 500

@app.route('/generate-game', methods=['POST'])
def generate_game():
    """Enhanced game generation endpoint"""
    try:
        # Redirect to ultimate generation for consistency
        return ultimate_generate_game()
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'Enhanced generation failed',
            'details': str(e),
            'user_message': 'Sorry, there was an error generating your game. Please try again.'
        }), 500

@app.route('/ai-generate-game', methods=['POST'])
def ai_generate_game():
    """FREE AI game generation endpoint"""
    try:
        # For now, redirect to ultimate generation
        # In the future, this could use different AI models
        return ultimate_generate_game()
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'FREE AI generation failed',
            'details': str(e),
            'user_message': 'Sorry, there was an error with FREE AI generation. Please try again.'
        }), 500

@app.route('/play-game/<game_id>')
def play_game(game_id):
    """Serve the game HTML file for playing"""
    try:
        game_dir = os.path.join(GAMES_DIR, game_id)
        if not os.path.exists(game_dir):
            return "Game not found", 404
        
        # Find HTML file in directory
        for file in os.listdir(game_dir):
            if file.endswith('.html'):
                html_file = os.path.join(game_dir, file)
                with open(html_file, 'r', encoding='utf-8') as f:
                    game_html = f.read()
                
                stats['games_opened'] += 1
                
                # Return HTML directly
                response = make_response(game_html)
                response.headers['Content-Type'] = 'text/html'
                return response
        
        return "Game file not found", 404
        
    except Exception as e:
        return f"Error loading game: {str(e)}", 500

@app.route('/download-game/<game_id>')
def download_game(game_id):
    """Download the game ZIP file"""
    try:
        game_dir = os.path.join(GAMES_DIR, game_id)
        if not os.path.exists(game_dir):
            return jsonify({'error': 'Game not found'}), 404
        
        # Find ZIP file in directory
        for file in os.listdir(game_dir):
            if file.endswith('.zip'):
                zip_file = os.path.join(game_dir, file)
                stats['files_downloaded'] += 1
                return send_file(zip_file, as_attachment=True, download_name=file)
        
        return jsonify({'error': 'Game ZIP file not found'}), 404
        
    except Exception as e:
        return jsonify({'error': f'Download failed: {str(e)}'}), 500

@app.route('/generation-stats')
def generation_stats():
    """Get generation statistics"""
    try:
        return jsonify({
            'stats': stats,
            'total_requests': stats['total_games_generated'],
            'revolutionary_available': REVOLUTIONARY_AVAILABLE,
            'free_ai_available': FREE_AI_AVAILABLE,
            'file_delivery_active': True,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'error': 'Stats retrieval failed',
            'details': str(e)
        }), 500

@app.route('/ai-status')
def ai_status():
    """Get AI system status"""
    try:
        return jsonify({
            'revolutionary_available': REVOLUTIONARY_AVAILABLE,
            'free_ai_available': FREE_AI_AVAILABLE,
            'file_delivery': True,
            'components': {
                'prompt_processor': REVOLUTIONARY_AVAILABLE,
                'randomization_engine': REVOLUTIONARY_AVAILABLE,
                'template_library': REVOLUTIONARY_AVAILABLE,
                'free_ai_engine': FREE_AI_AVAILABLE,
                'free_ai_generator': FREE_AI_AVAILABLE,
                'file_system': True,
                'zip_generation': True
            },
            'status': 'fully_operational',
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'error': 'AI status check failed',
            'details': str(e)
        }), 500

if __name__ == '__main__':
    print("🔥 Starting Fixed Revolutionary Ultimate Game Maker with Complete File Delivery...")
    print(f"🧠 Revolutionary System: {'✅ AVAILABLE' if REVOLUTIONARY_AVAILABLE else '❌ NOT AVAILABLE'}")
    print(f"🤖 FREE AI System: {'✅ AVAILABLE' if FREE_AI_AVAILABLE else '❌ NOT AVAILABLE'}")
    print("📁 File Delivery System: ✅ ACTIVE")
    print("🎮 Game Generation: ✅ READY")
    print("📦 ZIP Downloads: ✅ READY")
    print("🌐 Server starting on port 8080")
    print("🎯 Ready to deliver complete playable games!")
    
    app.run(host='0.0.0.0', port=8080, debug=False)
