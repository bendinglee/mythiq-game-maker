from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
import json
from datetime import datetime
import logging
import random

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Configuration
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
HUGGINGFACE_API_KEY = os.environ.get('HUGGINGFACE_API_KEY')

class GameMaker:
    def __init__(self):
        self.groq_available = bool(GROQ_API_KEY)
        self.hf_available = bool(HUGGINGFACE_API_KEY)
        
    def call_groq_for_game_concept(self, description):
        """Use Groq to generate game concept and mechanics"""
        if not self.groq_available:
            return None
            
        try:
            headers = {
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            }
            
            prompt = f"""Create a detailed game concept based on this description: "{description}"

Please provide:
1. Game Title
2. Core Mechanics (3-4 key gameplay elements)
3. Visual Style
4. Player Objective
5. Unique Features

Format as JSON with these keys: title, mechanics, visual_style, objective, features"""
            
            data = {
                "messages": [
                    {"role": "system", "content": "You are a creative game designer. Generate innovative, fun game concepts with clear mechanics."},
                    {"role": "user", "content": prompt}
                ],
                "model": "llama-3.1-70b-versatile",
                "temperature": 0.8,
                "max_tokens": 800
            }
            
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content']
            else:
                logger.error(f"Groq API error: {response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"Groq API exception: {str(e)}")
            return None
    
    def generate_html5_game(self, concept, description):
        """Generate playable HTML5 game based on concept"""
        try:
            # Extract game elements from concept
            game_title = "Mythiq Adventure"
            game_theme = "adventure"
            
            if concept and isinstance(concept, str):
                if "space" in concept.lower() or "sci-fi" in concept.lower():
                    game_theme = "space"
                elif "fantasy" in concept.lower() or "magic" in concept.lower():
                    game_theme = "fantasy"
                elif "puzzle" in concept.lower():
                    game_theme = "puzzle"
                elif "racing" in concept.lower() or "speed" in concept.lower():
                    game_theme = "racing"
            
            # Generate game based on theme
            if game_theme == "space":
                return self.generate_space_game(description)
            elif game_theme == "fantasy":
                return self.generate_fantasy_game(description)
            elif game_theme == "puzzle":
                return self.generate_puzzle_game(description)
            elif game_theme == "racing":
                return self.generate_racing_game(description)
            else:
                return self.generate_adventure_game(description)
                
        except Exception as e:
            logger.error(f"Game generation error: {str(e)}")
            return self.generate_default_game()
    
    def generate_space_game(self, description):
        """Generate space-themed game"""
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Space Explorer - {description[:30]}...</title>
    <style>
        body {{ margin: 0; padding: 20px; background: #000; color: #fff; font-family: Arial, sans-serif; }}
        canvas {{ border: 2px solid #00ffff; background: linear-gradient(to bottom, #000428, #004e92); }}
        .controls {{ margin-top: 10px; }}
        .score {{ font-size: 20px; margin-bottom: 10px; }}
    </style>
</head>
<body>
    <div class="score">Score: <span id="score">0</span> | Lives: <span id="lives">3</span></div>
    <canvas id="gameCanvas" width="800" height="600"></canvas>
    <div class="controls">
        <p>🚀 Use ARROW KEYS to move your spaceship | SPACEBAR to shoot | Avoid asteroids and shoot enemies!</p>
        <p>Game Concept: {description}</p>
    </div>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        
        let score = 0;
        let lives = 3;
        let gameRunning = true;
        
        // Player spaceship
        const player = {{
            x: canvas.width / 2,
            y: canvas.height - 50,
            width: 30,
            height: 30,
            speed: 5
        }};
        
        // Game objects
        let bullets = [];
        let enemies = [];
        let asteroids = [];
        
        // Input handling
        const keys = {{}};
        document.addEventListener('keydown', (e) => keys[e.code] = true);
        document.addEventListener('keyup', (e) => keys[e.code] = false);
        
        function spawnEnemy() {{
            enemies.push({{
                x: Math.random() * (canvas.width - 20),
                y: -20,
                width: 25,
                height: 25,
                speed: 2 + Math.random() * 2
            }});
        }}
        
        function spawnAsteroid() {{
            asteroids.push({{
                x: Math.random() * (canvas.width - 30),
                y: -30,
                width: 30,
                height: 30,
                speed: 1 + Math.random() * 3,
                rotation: 0
            }});
        }}
        
        function update() {{
            if (!gameRunning) return;
            
            // Player movement
            if (keys['ArrowLeft'] && player.x > 0) player.x -= player.speed;
            if (keys['ArrowRight'] && player.x < canvas.width - player.width) player.x += player.speed;
            if (keys['ArrowUp'] && player.y > 0) player.y -= player.speed;
            if (keys['ArrowDown'] && player.y < canvas.height - player.height) player.y += player.speed;
            
            // Shooting
            if (keys['Space']) {{
                bullets.push({{
                    x: player.x + player.width / 2,
                    y: player.y,
                    width: 3,
                    height: 10,
                    speed: 7
                }});
                keys['Space'] = false; // Prevent rapid fire
            }}
            
            // Update bullets
            bullets = bullets.filter(bullet => {{
                bullet.y -= bullet.speed;
                return bullet.y > 0;
            }});
            
            // Update enemies
            enemies.forEach(enemy => enemy.y += enemy.speed);
            enemies = enemies.filter(enemy => enemy.y < canvas.height);
            
            // Update asteroids
            asteroids.forEach(asteroid => {{
                asteroid.y += asteroid.speed;
                asteroid.rotation += 0.05;
            }});
            asteroids = asteroids.filter(asteroid => asteroid.y < canvas.height);
            
            // Collision detection
            checkCollisions();
            
            // Spawn new objects
            if (Math.random() < 0.02) spawnEnemy();
            if (Math.random() < 0.015) spawnAsteroid();
        }}
        
        function checkCollisions() {{
            // Bullet-enemy collisions
            bullets.forEach((bullet, bIndex) => {{
                enemies.forEach((enemy, eIndex) => {{
                    if (bullet.x < enemy.x + enemy.width &&
                        bullet.x + bullet.width > enemy.x &&
                        bullet.y < enemy.y + enemy.height &&
                        bullet.y + bullet.height > enemy.y) {{
                        bullets.splice(bIndex, 1);
                        enemies.splice(eIndex, 1);
                        score += 10;
                        document.getElementById('score').textContent = score;
                    }}
                }});
            }});
            
            // Player-enemy collisions
            enemies.forEach((enemy, index) => {{
                if (player.x < enemy.x + enemy.width &&
                    player.x + player.width > enemy.x &&
                    player.y < enemy.y + enemy.height &&
                    player.y + player.height > enemy.y) {{
                    enemies.splice(index, 1);
                    lives--;
                    document.getElementById('lives').textContent = lives;
                    if (lives <= 0) gameOver();
                }}
            }});
            
            // Player-asteroid collisions
            asteroids.forEach((asteroid, index) => {{
                if (player.x < asteroid.x + asteroid.width &&
                    player.x + player.width > asteroid.x &&
                    player.y < asteroid.y + asteroid.height &&
                    player.y + player.height > asteroid.y) {{
                    asteroids.splice(index, 1);
                    lives--;
                    document.getElementById('lives').textContent = lives;
                    if (lives <= 0) gameOver();
                }}
            }});
        }}
        
        function draw() {{
            // Clear canvas
            ctx.fillStyle = 'rgba(0, 4, 40, 0.1)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // Draw stars
            for (let i = 0; i < 50; i++) {{
                ctx.fillStyle = '#fff';
                ctx.fillRect(Math.random() * canvas.width, Math.random() * canvas.height, 1, 1);
            }}
            
            // Draw player
            ctx.fillStyle = '#00ffff';
            ctx.fillRect(player.x, player.y, player.width, player.height);
            
            // Draw bullets
            ctx.fillStyle = '#ffff00';
            bullets.forEach(bullet => {{
                ctx.fillRect(bullet.x, bullet.y, bullet.width, bullet.height);
            }});
            
            // Draw enemies
            ctx.fillStyle = '#ff0000';
            enemies.forEach(enemy => {{
                ctx.fillRect(enemy.x, enemy.y, enemy.width, enemy.height);
            }});
            
            // Draw asteroids
            ctx.fillStyle = '#888';
            asteroids.forEach(asteroid => {{
                ctx.save();
                ctx.translate(asteroid.x + asteroid.width/2, asteroid.y + asteroid.height/2);
                ctx.rotate(asteroid.rotation);
                ctx.fillRect(-asteroid.width/2, -asteroid.height/2, asteroid.width, asteroid.height);
                ctx.restore();
            }});
            
            if (!gameRunning) {{
                ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = '#fff';
                ctx.font = '48px Arial';
                ctx.textAlign = 'center';
                ctx.fillText('GAME OVER', canvas.width/2, canvas.height/2);
                ctx.font = '24px Arial';
                ctx.fillText(`Final Score: ${{score}}`, canvas.width/2, canvas.height/2 + 50);
            }}
        }}
        
        function gameOver() {{
            gameRunning = false;
        }}
        
        function gameLoop() {{
            update();
            draw();
            requestAnimationFrame(gameLoop);
        }}
        
        // Start game
        gameLoop();
    </script>
</body>
</html>"""
    
    def generate_adventure_game(self, description):
        """Generate adventure-themed game"""
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adventure Quest - {description[:30]}...</title>
    <style>
        body {{ margin: 0; padding: 20px; background: #2d5016; color: #fff; font-family: Arial, sans-serif; }}
        canvas {{ border: 2px solid #8B4513; background: linear-gradient(to bottom, #87CEEB, #228B22); }}
        .controls {{ margin-top: 10px; }}
        .score {{ font-size: 20px; margin-bottom: 10px; }}
    </style>
</head>
<body>
    <div class="score">Score: <span id="score">0</span> | Health: <span id="health">100</span></div>
    <canvas id="gameCanvas" width="800" height="600"></canvas>
    <div class="controls">
        <p>🏃 Use ARROW KEYS to move | Collect treasures and avoid obstacles!</p>
        <p>Game Concept: {description}</p>
    </div>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        
        let score = 0;
        let health = 100;
        let gameRunning = true;
        
        const player = {{
            x: 50,
            y: canvas.height / 2,
            width: 25,
            height: 25,
            speed: 4
        }};
        
        let treasures = [];
        let obstacles = [];
        
        const keys = {{}};
        document.addEventListener('keydown', (e) => keys[e.code] = true);
        document.addEventListener('keyup', (e) => keys[e.code] = false);
        
        function spawnTreasure() {{
            treasures.push({{
                x: canvas.width,
                y: Math.random() * (canvas.height - 50) + 25,
                width: 20,
                height: 20,
                speed: 3
            }});
        }}
        
        function spawnObstacle() {{
            obstacles.push({{
                x: canvas.width,
                y: Math.random() * (canvas.height - 40) + 20,
                width: 30,
                height: 40,
                speed: 2.5
            }});
        }}
        
        function update() {{
            if (!gameRunning) return;
            
            // Player movement
            if (keys['ArrowUp'] && player.y > 0) player.y -= player.speed;
            if (keys['ArrowDown'] && player.y < canvas.height - player.height) player.y += player.speed;
            if (keys['ArrowLeft'] && player.x > 0) player.x -= player.speed;
            if (keys['ArrowRight'] && player.x < canvas.width - player.width) player.x += player.speed;
            
            // Update treasures
            treasures.forEach(treasure => treasure.x -= treasure.speed);
            treasures = treasures.filter(treasure => treasure.x > -treasure.width);
            
            // Update obstacles
            obstacles.forEach(obstacle => obstacle.x -= obstacle.speed);
            obstacles = obstacles.filter(obstacle => obstacle.x > -obstacle.width);
            
            // Check collisions
            checkCollisions();
            
            // Spawn objects
            if (Math.random() < 0.02) spawnTreasure();
            if (Math.random() < 0.015) spawnObstacle();
        }}
        
        function checkCollisions() {{
            // Treasure collection
            treasures.forEach((treasure, index) => {{
                if (player.x < treasure.x + treasure.width &&
                    player.x + player.width > treasure.x &&
                    player.y < treasure.y + treasure.height &&
                    player.y + player.height > treasure.y) {{
                    treasures.splice(index, 1);
                    score += 20;
                    document.getElementById('score').textContent = score;
                }}
            }});
            
            // Obstacle damage
            obstacles.forEach((obstacle, index) => {{
                if (player.x < obstacle.x + obstacle.width &&
                    player.x + player.width > obstacle.x &&
                    player.y < obstacle.y + obstacle.height &&
                    player.y + player.height > obstacle.y) {{
                    obstacles.splice(index, 1);
                    health -= 25;
                    document.getElementById('health').textContent = health;
                    if (health <= 0) gameOver();
                }}
            }});
        }}
        
        function draw() {{
            // Clear canvas with gradient
            const gradient = ctx.createLinearGradient(0, 0, 0, canvas.height);
            gradient.addColorStop(0, '#87CEEB');
            gradient.addColorStop(1, '#228B22');
            ctx.fillStyle = gradient;
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // Draw player
            ctx.fillStyle = '#FFD700';
            ctx.fillRect(player.x, player.y, player.width, player.height);
            
            // Draw treasures
            ctx.fillStyle = '#FF6347';
            treasures.forEach(treasure => {{
                ctx.fillRect(treasure.x, treasure.y, treasure.width, treasure.height);
            }});
            
            // Draw obstacles
            ctx.fillStyle = '#8B4513';
            obstacles.forEach(obstacle => {{
                ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
            }});
            
            if (!gameRunning) {{
                ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = '#fff';
                ctx.font = '48px Arial';
                ctx.textAlign = 'center';
                ctx.fillText('GAME OVER', canvas.width/2, canvas.height/2);
                ctx.font = '24px Arial';
                ctx.fillText(`Final Score: ${{score}}`, canvas.width/2, canvas.height/2 + 50);
            }}
        }}
        
        function gameOver() {{
            gameRunning = false;
        }}
        
        function gameLoop() {{
            update();
            draw();
            requestAnimationFrame(gameLoop);
        }}
        
        gameLoop();
    </script>
</body>
</html>"""
    
    def generate_default_game(self):
        """Generate default game when all else fails"""
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mythiq Game</title>
    <style>
        body { margin: 0; padding: 20px; background: #1a1a2e; color: #fff; font-family: Arial, sans-serif; }
        canvas { border: 2px solid #16213e; background: #0f3460; }
        .controls { margin-top: 10px; }
    </style>
</head>
<body>
    <div>Score: <span id="score">0</span></div>
    <canvas id="gameCanvas" width="800" height="600"></canvas>
    <div class="controls">
        <p>Click anywhere to play! Collect the moving targets!</p>
    </div>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        let score = 0;
        let targets = [];
        
        function spawnTarget() {
            targets.push({
                x: Math.random() * (canvas.width - 30),
                y: Math.random() * (canvas.height - 30),
                width: 30,
                height: 30,
                vx: (Math.random() - 0.5) * 4,
                vy: (Math.random() - 0.5) * 4
            });
        }
        
        canvas.addEventListener('click', (e) => {
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            targets.forEach((target, index) => {
                if (x >= target.x && x <= target.x + target.width &&
                    y >= target.y && y <= target.y + target.height) {
                    targets.splice(index, 1);
                    score += 10;
                    document.getElementById('score').textContent = score;
                }
            });
        });
        
        function update() {
            targets.forEach(target => {
                target.x += target.vx;
                target.y += target.vy;
                
                if (target.x <= 0 || target.x >= canvas.width - target.width) target.vx *= -1;
                if (target.y <= 0 || target.y >= canvas.height - target.height) target.vy *= -1;
            });
            
            if (Math.random() < 0.02 && targets.length < 5) spawnTarget();
        }
        
        function draw() {
            ctx.fillStyle = '#0f3460';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            ctx.fillStyle = '#e94560';
            targets.forEach(target => {
                ctx.fillRect(target.x, target.y, target.width, target.height);
            });
        }
        
        function gameLoop() {
            update();
            draw();
            requestAnimationFrame(gameLoop);
        }
        
        spawnTarget();
        gameLoop();
    </script>
</body>
</html>"""

# Initialize game maker
game_maker = GameMaker()

@app.route('/')
def home():
    """Service status endpoint"""
    return jsonify({
        "service": "Mythiq Game Maker",
        "status": "online",
        "version": "2.0.0",
        "message": "AI-powered game generation with Groq integration",
        "features": [
            "AI game concept generation with Groq",
            "Playable HTML5 games",
            "Multiple game themes (space, adventure, puzzle, racing)",
            "Real-time game creation",
            "Interactive gameplay"
        ],
        "ai_status": {
            "groq_available": game_maker.groq_available,
            "huggingface_available": game_maker.hf_available
        },
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "service": "mythiq-game-maker",
        "status": "healthy",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route('/generate-game', methods=['POST'])
def generate_game():
    """Generate a playable game from description"""
    try:
        data = request.get_json()
        if not data or 'description' not in data:
            return jsonify({"error": "Game description is required"}), 400
        
        description = data['description'].strip()
        if not description:
            return jsonify({"error": "Game description cannot be empty"}), 400
        
        # Generate game concept with AI
        concept = game_maker.call_groq_for_game_concept(description)
        
        # Generate playable HTML5 game
        game_html = game_maker.generate_html5_game(concept, description)
        
        return jsonify({
            "game_html": game_html,
            "concept": concept,
            "description": description,
            "timestamp": datetime.now().isoformat(),
            "provider": "groq" if concept else "template"
        })
        
    except Exception as e:
        logger.error(f"Game generation error: {str(e)}")
        return jsonify({
            "error": "Could not generate game",
            "game_html": game_maker.generate_default_game()
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    logger.info(f"Starting Mythiq Game Maker on port {port}")
    logger.info(f"Groq API available: {game_maker.groq_available}")
    
    app.run(host='0.0.0.0', port=port, debug=False)
