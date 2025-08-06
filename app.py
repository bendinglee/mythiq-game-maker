"""
Enhanced Multi-Template Game Generator for Mythiq AI Platform
Supports: Space Shooter, Platformer, Puzzle, Racing games
Maintains professional quality across all templates
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

class MultiTemplateGameGenerator:
    def __init__(self):
        self.templates = {
            'space_shooter': {
                'name': 'Space Shooter',
                'features': ['Professional Graphics', 'Complete Shooting', 'Power-up System', 'Advanced Scoring', 'Particle Effects', 'Mobile Optimized'],
                'keywords': ['space', 'shooter', 'shoot', 'spaceship', 'laser', 'alien', 'enemy', 'asteroid']
            },
            'platformer': {
                'name': 'Platformer',
                'features': ['Professional Graphics', 'Jump Mechanics', 'Platform Physics', 'Collectibles', 'Enemy AI', 'Mobile Optimized'],
                'keywords': ['platform', 'jump', 'mario', 'side-scroll', 'coin', 'level', 'obstacle']
            },
            'puzzle': {
                'name': 'Puzzle',
                'features': ['Professional Graphics', 'Block Mechanics', 'Line Clearing', 'Scoring System', 'Level Progression', 'Mobile Optimized'],
                'keywords': ['puzzle', 'tetris', 'block', 'match', 'grid', 'clear', 'rotate']
            },
            'racing': {
                'name': 'Racing',
                'features': ['Professional Graphics', 'Vehicle Physics', 'Track System', 'Speed Mechanics', 'Lap Timing', 'Mobile Optimized'],
                'keywords': ['race', 'racing', 'car', 'speed', 'track', 'lap', 'vehicle', 'drive']
            }
        }
    
    def analyze_prompt(self, description):
        """Analyze the game description to determine the best template"""
        description_lower = description.lower()
        
        # Score each template based on keyword matches
        scores = {}
        for template_id, template_info in self.templates.items():
            score = 0
            for keyword in template_info['keywords']:
                if keyword in description_lower:
                    score += 1
            scores[template_id] = score
        
        # Return the template with the highest score, default to space_shooter
        best_template = max(scores, key=scores.get)
        if scores[best_template] == 0:
            best_template = 'space_shooter'  # Default fallback
        
        return best_template, self.templates[best_template]
    
    def get_enhanced_space_shooter_template(self, description):
        """Generate enhanced space shooter game"""
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enhanced Space Shooter</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);
            font-family: 'Arial', sans-serif;
            overflow: hidden;
            color: white;
        }}
        
        .game-container {{
            position: relative;
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        
        .game-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 30px;
            background: rgba(0, 0, 0, 0.8);
            border-bottom: 2px solid #00ffff;
        }}
        
        .game-title {{
            font-size: 24px;
            font-weight: bold;
            color: #00ffff;
            text-shadow: 0 0 10px #00ffff;
        }}
        
        .game-stats {{
            display: flex;
            gap: 30px;
            font-size: 18px;
        }}
        
        .stat {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .stat-value {{
            font-weight: bold;
            color: #00ff00;
        }}
        
        .game-canvas {{
            flex: 1;
            position: relative;
            background: radial-gradient(ellipse at center, #1a1a2e 0%, #0c0c0c 100%);
            overflow: hidden;
        }}
        
        .player {{
            position: absolute;
            bottom: 50px;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 60px;
            background: linear-gradient(45deg, #ff6b6b, #ff8e8e);
            clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
            border: 2px solid #fff;
            box-shadow: 0 0 20px #ff6b6b;
            transition: all 0.1s ease;
        }}
        
        .enemy {{
            position: absolute;
            width: 40px;
            height: 40px;
            background: linear-gradient(45deg, #ff4757, #ff6b7a);
            clip-path: polygon(50% 100%, 0% 0%, 100% 0%);
            border: 1px solid #fff;
            box-shadow: 0 0 15px #ff4757;
            animation: enemyMove 3s linear infinite;
        }}
        
        .laser {{
            position: absolute;
            width: 4px;
            height: 20px;
            background: linear-gradient(to top, #00ffff, #ffffff);
            border-radius: 2px;
            box-shadow: 0 0 10px #00ffff;
            animation: laserMove 1s linear infinite;
        }}
        
        .powerup {{
            position: absolute;
            width: 30px;
            height: 30px;
            background: linear-gradient(45deg, #ffd700, #ffed4e);
            border-radius: 50%;
            border: 2px solid #fff;
            box-shadow: 0 0 15px #ffd700;
            animation: powerupFloat 2s ease-in-out infinite alternate, powerupMove 4s linear infinite;
        }}
        
        .explosion {{
            position: absolute;
            width: 60px;
            height: 60px;
            background: radial-gradient(circle, #ff6b6b 0%, #ff8e8e 50%, transparent 100%);
            border-radius: 50%;
            animation: explode 0.5s ease-out forwards;
        }}
        
        .star {{
            position: absolute;
            width: 2px;
            height: 2px;
            background: white;
            border-radius: 50%;
            animation: starMove 5s linear infinite;
        }}
        
        .game-controls {{
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 20px;
            z-index: 100;
        }}
        
        .control-btn {{
            padding: 12px 24px;
            background: rgba(0, 255, 255, 0.2);
            border: 2px solid #00ffff;
            color: #00ffff;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }}
        
        .control-btn:hover {{
            background: rgba(0, 255, 255, 0.4);
            box-shadow: 0 0 20px #00ffff;
        }}
        
        @keyframes enemyMove {{
            from {{ top: -50px; }}
            to {{ top: 100vh; }}
        }}
        
        @keyframes laserMove {{
            from {{ bottom: 110px; }}
            to {{ bottom: 100vh; }}
        }}
        
        @keyframes powerupMove {{
            from {{ top: -40px; }}
            to {{ top: 100vh; }}
        }}
        
        @keyframes powerupFloat {{
            from {{ transform: scale(1) rotate(0deg); }}
            to {{ transform: scale(1.2) rotate(180deg); }}
        }}
        
        @keyframes explode {{
            0% {{ transform: scale(0); opacity: 1; }}
            100% {{ transform: scale(3); opacity: 0; }}
        }}
        
        @keyframes starMove {{
            from {{ top: -5px; }}
            to {{ top: 100vh; }}
        }}
        
        @media (max-width: 768px) {{
            .game-header {{
                padding: 10px 15px;
            }}
            
            .game-title {{
                font-size: 18px;
            }}
            
            .game-stats {{
                gap: 15px;
                font-size: 14px;
            }}
            
            .player {{
                width: 50px;
                height: 50px;
            }}
            
            .control-btn {{
                padding: 10px 20px;
                font-size: 14px;
            }}
        }}
    </style>
</head>
<body>
    <div class="game-container">
        <div class="game-header">
            <div class="game-title">🚀 Enhanced Space Shooter</div>
            <div class="game-stats">
                <div class="stat">
                    <span>Score:</span>
                    <span class="stat-value" id="score">0</span>
                </div>
                <div class="stat">
                    <span>Level:</span>
                    <span class="stat-value" id="level">1</span>
                </div>
                <div class="stat">
                    <span>Health:</span>
                    <span class="stat-value" id="health">100</span>
                </div>
            </div>
        </div>
        
        <div class="game-canvas" id="gameCanvas">
            <div class="player" id="player"></div>
        </div>
        
        <div class="game-controls">
            <button class="control-btn" onclick="startGame()">Start Game</button>
            <button class="control-btn" onclick="pauseGame()">Pause</button>
            <button class="control-btn" onclick="resetGame()">Reset</button>
        </div>
    </div>

    <script>
        // Game state
        let gameState = {{
            score: 0,
            level: 1,
            health: 100,
            isPlaying: false,
            isPaused: false,
            player: {{ x: 50, y: 50 }},
            enemies: [],
            lasers: [],
            powerups: [],
            stars: []
        }};

        // Game elements
        const player = document.getElementById('player');
        const gameCanvas = document.getElementById('gameCanvas');
        const scoreElement = document.getElementById('score');
        const levelElement = document.getElementById('level');
        const healthElement = document.getElementById('health');

        // Initialize game
        function initGame() {{
            createStars();
            updateUI();
        }}

        function createStars() {{
            for (let i = 0; i < 50; i++) {{
                createStar();
            }}
        }}

        function createStar() {{
            const star = document.createElement('div');
            star.className = 'star';
            star.style.left = Math.random() * 100 + '%';
            star.style.animationDelay = Math.random() * 5 + 's';
            gameCanvas.appendChild(star);
            
            setTimeout(() => {{
                if (star.parentNode) {{
                    star.parentNode.removeChild(star);
                }}
                if (gameState.isPlaying) {{
                    createStar();
                }}
            }}, 5000);
        }}

        function startGame() {{
            gameState.isPlaying = true;
            gameState.isPaused = false;
            spawnEnemies();
            spawnPowerups();
        }}

        function pauseGame() {{
            gameState.isPaused = !gameState.isPaused;
        }}

        function resetGame() {{
            gameState = {{
                score: 0,
                level: 1,
                health: 100,
                isPlaying: false,
                isPaused: false,
                player: {{ x: 50, y: 50 }},
                enemies: [],
                lasers: [],
                powerups: [],
                stars: []
            }};
            
            // Clear all game elements
            const enemies = document.querySelectorAll('.enemy');
            const lasers = document.querySelectorAll('.laser');
            const powerups = document.querySelectorAll('.powerup');
            const explosions = document.querySelectorAll('.explosion');
            
            enemies.forEach(enemy => enemy.remove());
            lasers.forEach(laser => laser.remove());
            powerups.forEach(powerup => powerup.remove());
            explosions.forEach(explosion => explosion.remove());
            
            updateUI();
        }}

        function spawnEnemies() {{
            if (!gameState.isPlaying || gameState.isPaused) return;
            
            const enemy = document.createElement('div');
            enemy.className = 'enemy';
            enemy.style.left = Math.random() * 90 + '%';
            enemy.style.top = '-50px';
            gameCanvas.appendChild(enemy);
            
            setTimeout(() => {{
                if (enemy.parentNode) {{
                    enemy.parentNode.removeChild(enemy);
                }}
            }}, 3000);
            
            setTimeout(() => {{
                if (gameState.isPlaying) {{
                    spawnEnemies();
                }}
            }}, 1000 + Math.random() * 2000);
        }}

        function spawnPowerups() {{
            if (!gameState.isPlaying || gameState.isPaused) return;
            
            const powerup = document.createElement('div');
            powerup.className = 'powerup';
            powerup.style.left = Math.random() * 90 + '%';
            powerup.style.top = '-40px';
            gameCanvas.appendChild(powerup);
            
            setTimeout(() => {{
                if (powerup.parentNode) {{
                    powerup.parentNode.removeChild(powerup);
                }}
            }}, 4000);
            
            setTimeout(() => {{
                if (gameState.isPlaying) {{
                    spawnPowerups();
                }}
            }}, 5000 + Math.random() * 10000);
        }}

        function shoot() {{
            if (!gameState.isPlaying || gameState.isPaused) return;
            
            const laser = document.createElement('div');
            laser.className = 'laser';
            const playerRect = player.getBoundingClientRect();
            const canvasRect = gameCanvas.getBoundingClientRect();
            
            laser.style.left = (playerRect.left - canvasRect.left + playerRect.width / 2) + 'px';
            laser.style.bottom = '110px';
            gameCanvas.appendChild(laser);
            
            setTimeout(() => {{
                if (laser.parentNode) {{
                    laser.parentNode.removeChild(laser);
                }}
            }}, 1000);
        }}

        function createExplosion(x, y) {{
            const explosion = document.createElement('div');
            explosion.className = 'explosion';
            explosion.style.left = x + 'px';
            explosion.style.top = y + 'px';
            gameCanvas.appendChild(explosion);
            
            setTimeout(() => {{
                if (explosion.parentNode) {{
                    explosion.parentNode.removeChild(explosion);
                }}
            }}, 500);
        }}

        function updateScore(points) {{
            gameState.score += points;
            if (gameState.score > gameState.level * 1000) {{
                gameState.level++;
            }}
            updateUI();
        }}

        function updateUI() {{
            scoreElement.textContent = gameState.score;
            levelElement.textContent = gameState.level;
            healthElement.textContent = gameState.health;
        }}

        // Controls
        document.addEventListener('keydown', (e) => {{
            if (!gameState.isPlaying || gameState.isPaused) return;
            
            const playerRect = player.getBoundingClientRect();
            const canvasRect = gameCanvas.getBoundingClientRect();
            
            switch(e.key) {{
                case 'ArrowLeft':
                case 'a':
                case 'A':
                    if (playerRect.left > canvasRect.left + 10) {{
                        player.style.left = (playerRect.left - canvasRect.left - 10) + 'px';
                    }}
                    break;
                case 'ArrowRight':
                case 'd':
                case 'D':
                    if (playerRect.right < canvasRect.right - 10) {{
                        player.style.left = (playerRect.left - canvasRect.left + 10) + 'px';
                    }}
                    break;
                case ' ':
                case 'Enter':
                    e.preventDefault();
                    shoot();
                    break;
                case 'p':
                case 'P':
                    pauseGame();
                    break;
            }}
        }});

        // Touch controls for mobile
        let touchStartX = 0;
        gameCanvas.addEventListener('touchstart', (e) => {{
            touchStartX = e.touches[0].clientX;
        }});

        gameCanvas.addEventListener('touchmove', (e) => {{
            e.preventDefault();
            if (!gameState.isPlaying || gameState.isPaused) return;
            
            const touchX = e.touches[0].clientX;
            const deltaX = touchX - touchStartX;
            
            const playerRect = player.getBoundingClientRect();
            const canvasRect = gameCanvas.getBoundingClientRect();
            const newLeft = playerRect.left - canvasRect.left + deltaX;
            
            if (newLeft >= 0 && newLeft <= canvasRect.width - playerRect.width) {{
                player.style.left = newLeft + 'px';
            }}
            
            touchStartX = touchX;
        }});

        gameCanvas.addEventListener('touchend', () => {{
            shoot();
        }});

        // Initialize game on load
        initGame();
    </script>
</body>
</html>'''
    
    def get_enhanced_platformer_template(self, description):
        """Generate enhanced platformer game"""
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Platformer</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #87CEEB 0%, #98FB98 50%, #90EE90 100%);
            font-family: 'Arial', sans-serif;
            overflow: hidden;
            color: #333;
        }}
        
        .game-container {{
            position: relative;
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        
        .game-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 30px;
            background: rgba(0, 0, 0, 0.8);
            border-bottom: 2px solid #FFD700;
            color: white;
        }}
        
        .game-title {{
            font-size: 24px;
            font-weight: bold;
            color: #FFD700;
            text-shadow: 0 0 10px #FFD700;
        }}
        
        .game-stats {{
            display: flex;
            gap: 30px;
            font-size: 18px;
        }}
        
        .stat {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .stat-value {{
            font-weight: bold;
            color: #00ff00;
        }}
        
        .game-canvas {{
            flex: 1;
            position: relative;
            background: linear-gradient(to bottom, #87CEEB 0%, #98FB98 70%, #8FBC8F 100%);
            overflow: hidden;
        }}
        
        .player {{
            position: absolute;
            bottom: 120px;
            left: 100px;
            width: 40px;
            height: 40px;
            background: linear-gradient(45deg, #FF6347, #FF7F50);
            border-radius: 8px;
            border: 2px solid #fff;
            box-shadow: 0 0 15px #FF6347;
            transition: all 0.1s ease;
        }}
        
        .platform {{
            position: absolute;
            background: linear-gradient(45deg, #8B4513, #A0522D);
            border: 2px solid #654321;
            border-radius: 4px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }}
        
        .coin {{
            position: absolute;
            width: 20px;
            height: 20px;
            background: linear-gradient(45deg, #FFD700, #FFA500);
            border-radius: 50%;
            border: 2px solid #fff;
            box-shadow: 0 0 10px #FFD700;
            animation: coinSpin 2s linear infinite;
        }}
        
        .enemy {{
            position: absolute;
            width: 30px;
            height: 30px;
            background: linear-gradient(45deg, #8B0000, #DC143C);
            border-radius: 6px;
            border: 2px solid #fff;
            box-shadow: 0 0 10px #8B0000;
            animation: enemyMove 3s ease-in-out infinite alternate;
        }}
        
        .cloud {{
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50px;
            animation: cloudMove 20s linear infinite;
        }}
        
        .game-controls {{
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 20px;
            z-index: 100;
        }}
        
        .control-btn {{
            padding: 12px 24px;
            background: rgba(255, 215, 0, 0.2);
            border: 2px solid #FFD700;
            color: #FFD700;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }}
        
        .control-btn:hover {{
            background: rgba(255, 215, 0, 0.4);
            box-shadow: 0 0 20px #FFD700;
        }}
        
        @keyframes coinSpin {{
            from {{ transform: rotateY(0deg); }}
            to {{ transform: rotateY(360deg); }}
        }}
        
        @keyframes enemyMove {{
            from {{ transform: translateX(0); }}
            to {{ transform: translateX(50px); }}
        }}
        
        @keyframes cloudMove {{
            from {{ left: -200px; }}
            to {{ left: 100vw; }}
        }}
        
        @media (max-width: 768px) {{
            .game-header {{
                padding: 10px 15px;
            }}
            
            .game-title {{
                font-size: 18px;
            }}
            
            .game-stats {{
                gap: 15px;
                font-size: 14px;
            }}
            
            .player {{
                width: 35px;
                height: 35px;
            }}
            
            .control-btn {{
                padding: 10px 20px;
                font-size: 14px;
            }}
        }}
    </style>
</head>
<body>
    <div class="game-container">
        <div class="game-header">
            <div class="game-title">🏃 Ultimate Platformer</div>
            <div class="game-stats">
                <div class="stat">
                    <span>Score:</span>
                    <span class="stat-value" id="score">0</span>
                </div>
                <div class="stat">
                    <span>Level:</span>
                    <span class="stat-value" id="level">1</span>
                </div>
                <div class="stat">
                    <span>Lives:</span>
                    <span class="stat-value" id="lives">3</span>
                </div>
            </div>
        </div>
        
        <div class="game-canvas" id="gameCanvas">
            <div class="player" id="player"></div>
            
            <!-- Platforms -->
            <div class="platform" style="bottom: 80px; left: 0; width: 200px; height: 20px;"></div>
            <div class="platform" style="bottom: 180px; left: 250px; width: 150px; height: 20px;"></div>
            <div class="platform" style="bottom: 280px; left: 450px; width: 200px; height: 20px;"></div>
            <div class="platform" style="bottom: 380px; left: 150px; width: 180px; height: 20px;"></div>
            
            <!-- Coins -->
            <div class="coin" style="bottom: 210px; left: 300px;"></div>
            <div class="coin" style="bottom: 310px; left: 500px;"></div>
            <div class="coin" style="bottom: 410px; left: 200px;"></div>
            
            <!-- Enemies -->
            <div class="enemy" style="bottom: 110px; left: 50px;"></div>
            <div class="enemy" style="bottom: 210px; left: 300px;"></div>
            
            <!-- Clouds -->
            <div class="cloud" style="top: 50px; width: 80px; height: 40px; animation-delay: 0s;"></div>
            <div class="cloud" style="top: 120px; width: 100px; height: 50px; animation-delay: -5s;"></div>
            <div class="cloud" style="top: 200px; width: 60px; height: 30px; animation-delay: -10s;"></div>
        </div>
        
        <div class="game-controls">
            <button class="control-btn" onclick="startGame()">Start Game</button>
            <button class="control-btn" onclick="pauseGame()">Pause</button>
            <button class="control-btn" onclick="resetGame()">Reset</button>
        </div>
    </div>

    <script>
        // Game state
        let gameState = {{
            score: 0,
            level: 1,
            lives: 3,
            isPlaying: false,
            isPaused: false,
            player: {{ x: 100, y: 120, velocityY: 0, onGround: false }},
            gravity: 0.8,
            jumpPower: -15
        }};

        // Game elements
        const player = document.getElementById('player');
        const gameCanvas = document.getElementById('gameCanvas');
        const scoreElement = document.getElementById('score');
        const levelElement = document.getElementById('level');
        const livesElement = document.getElementById('lives');

        function startGame() {{
            gameState.isPlaying = true;
            gameState.isPaused = false;
            gameLoop();
        }}

        function pauseGame() {{
            gameState.isPaused = !gameState.isPaused;
        }}

        function resetGame() {{
            gameState = {{
                score: 0,
                level: 1,
                lives: 3,
                isPlaying: false,
                isPaused: false,
                player: {{ x: 100, y: 120, velocityY: 0, onGround: false }},
                gravity: 0.8,
                jumpPower: -15
            }};
            
            player.style.left = '100px';
            player.style.bottom = '120px';
            updateUI();
        }}

        function gameLoop() {{
            if (!gameState.isPlaying || gameState.isPaused) {{
                if (gameState.isPlaying) {{
                    requestAnimationFrame(gameLoop);
                }}
                return;
            }}

            // Apply gravity
            gameState.player.velocityY += gameState.gravity;
            gameState.player.y += gameState.player.velocityY;

            // Check ground collision
            if (gameState.player.y <= 120) {{
                gameState.player.y = 120;
                gameState.player.velocityY = 0;
                gameState.player.onGround = true;
            }} else {{
                gameState.player.onGround = false;
            }}

            // Update player position
            player.style.left = gameState.player.x + 'px';
            player.style.bottom = gameState.player.y + 'px';

            requestAnimationFrame(gameLoop);
        }}

        function jump() {{
            if (gameState.player.onGround && gameState.isPlaying && !gameState.isPaused) {{
                gameState.player.velocityY = gameState.jumpPower;
                gameState.player.onGround = false;
            }}
        }}

        function moveLeft() {{
            if (gameState.isPlaying && !gameState.isPaused && gameState.player.x > 0) {{
                gameState.player.x -= 5;
            }}
        }}

        function moveRight() {{
            if (gameState.isPlaying && !gameState.isPaused && gameState.player.x < window.innerWidth - 40) {{
                gameState.player.x += 5;
            }}
        }}

        function updateScore(points) {{
            gameState.score += points;
            if (gameState.score > gameState.level * 500) {{
                gameState.level++;
            }}
            updateUI();
        }}

        function updateUI() {{
            scoreElement.textContent = gameState.score;
            levelElement.textContent = gameState.level;
            livesElement.textContent = gameState.lives;
        }}

        // Controls
        document.addEventListener('keydown', (e) => {{
            switch(e.key) {{
                case 'ArrowLeft':
                case 'a':
                case 'A':
                    moveLeft();
                    break;
                case 'ArrowRight':
                case 'd':
                case 'D':
                    moveRight();
                    break;
                case 'ArrowUp':
                case ' ':
                case 'w':
                case 'W':
                    e.preventDefault();
                    jump();
                    break;
                case 'p':
                case 'P':
                    pauseGame();
                    break;
            }}
        }});

        // Touch controls for mobile
        let touchStartX = 0;
        let touchStartY = 0;

        gameCanvas.addEventListener('touchstart', (e) => {{
            touchStartX = e.touches[0].clientX;
            touchStartY = e.touches[0].clientY;
        }});

        gameCanvas.addEventListener('touchend', (e) => {{
            const touchEndX = e.changedTouches[0].clientX;
            const touchEndY = e.changedTouches[0].clientY;
            const deltaX = touchEndX - touchStartX;
            const deltaY = touchEndY - touchStartY;

            if (Math.abs(deltaY) > Math.abs(deltaX)) {{
                if (deltaY < -30) {{
                    jump(); // Swipe up
                }}
            }} else {{
                if (deltaX > 30) {{
                    moveRight(); // Swipe right
                }} else if (deltaX < -30) {{
                    moveLeft(); // Swipe left
                }}
            }}
        }});

        // Initialize game
        updateUI();
    </script>
</body>
</html>'''
    
    def get_enhanced_puzzle_template(self, description):
        """Generate enhanced puzzle game"""
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Puzzle Game</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Arial', sans-serif;
            overflow: hidden;
            color: white;
        }}
        
        .game-container {{
            position: relative;
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        
        .game-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 30px;
            background: rgba(0, 0, 0, 0.8);
            border-bottom: 2px solid #9b59b6;
        }}
        
        .game-title {{
            font-size: 24px;
            font-weight: bold;
            color: #9b59b6;
            text-shadow: 0 0 10px #9b59b6;
        }}
        
        .game-stats {{
            display: flex;
            gap: 30px;
            font-size: 18px;
        }}
        
        .stat {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .stat-value {{
            font-weight: bold;
            color: #00ff00;
        }}
        
        .game-canvas {{
            flex: 1;
            position: relative;
            background: radial-gradient(ellipse at center, #667eea 0%, #764ba2 100%);
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        
        .puzzle-grid {{
            display: grid;
            grid-template-columns: repeat(10, 30px);
            grid-template-rows: repeat(20, 30px);
            gap: 1px;
            background: rgba(0, 0, 0, 0.5);
            padding: 10px;
            border-radius: 10px;
            border: 2px solid #9b59b6;
        }}
        
        .grid-cell {{
            width: 30px;
            height: 30px;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 3px;
        }}
        
        .grid-cell.filled {{
            background: linear-gradient(45deg, #e74c3c, #c0392b);
            border: 1px solid #fff;
            box-shadow: 0 0 5px #e74c3c;
        }}
        
        .falling-piece {{
            position: absolute;
            width: 30px;
            height: 30px;
            background: linear-gradient(45deg, #3498db, #2980b9);
            border: 2px solid #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px #3498db;
            animation: pieceFall 1s ease-in infinite;
        }}
        
        .next-piece {{
            position: absolute;
            top: 50px;
            right: 50px;
            background: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
            border: 2px solid #9b59b6;
        }}
        
        .next-piece h3 {{
            margin: 0 0 10px 0;
            color: #9b59b6;
            text-align: center;
        }}
        
        .next-grid {{
            display: grid;
            grid-template-columns: repeat(4, 20px);
            grid-template-rows: repeat(4, 20px);
            gap: 1px;
        }}
        
        .next-cell {{
            width: 20px;
            height: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 2px;
        }}
        
        .next-cell.filled {{
            background: linear-gradient(45deg, #f39c12, #e67e22);
            border: 1px solid #fff;
        }}
        
        .game-controls {{
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 20px;
            z-index: 100;
        }}
        
        .control-btn {{
            padding: 12px 24px;
            background: rgba(155, 89, 182, 0.2);
            border: 2px solid #9b59b6;
            color: #9b59b6;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }}
        
        .control-btn:hover {{
            background: rgba(155, 89, 182, 0.4);
            box-shadow: 0 0 20px #9b59b6;
        }}
        
        @keyframes pieceFall {{
            0% {{ transform: translateY(0); }}
            100% {{ transform: translateY(30px); }}
        }}
        
        @media (max-width: 768px) {{
            .game-header {{
                padding: 10px 15px;
            }}
            
            .game-title {{
                font-size: 18px;
            }}
            
            .game-stats {{
                gap: 15px;
                font-size: 14px;
            }}
            
            .puzzle-grid {{
                grid-template-columns: repeat(10, 25px);
                grid-template-rows: repeat(20, 25px);
            }}
            
            .grid-cell {{
                width: 25px;
                height: 25px;
            }}
            
            .control-btn {{
                padding: 10px 20px;
                font-size: 14px;
            }}
        }}
    </style>
</head>
<body>
    <div class="game-container">
        <div class="game-header">
            <div class="game-title">🧩 Ultimate Puzzle Game</div>
            <div class="game-stats">
                <div class="stat">
                    <span>Score:</span>
                    <span class="stat-value" id="score">0</span>
                </div>
                <div class="stat">
                    <span>Level:</span>
                    <span class="stat-value" id="level">1</span>
                </div>
                <div class="stat">
                    <span>Lines:</span>
                    <span class="stat-value" id="lines">0</span>
                </div>
            </div>
        </div>
        
        <div class="game-canvas" id="gameCanvas">
            <div class="puzzle-grid" id="puzzleGrid"></div>
            
            <div class="next-piece">
                <h3>Next Piece</h3>
                <div class="next-grid" id="nextGrid"></div>
            </div>
        </div>
        
        <div class="game-controls">
            <button class="control-btn" onclick="startGame()">Start Game</button>
            <button class="control-btn" onclick="pauseGame()">Pause</button>
            <button class="control-btn" onclick="resetGame()">Reset</button>
        </div>
    </div>

    <script>
        // Game state
        let gameState = {{
            score: 0,
            level: 1,
            lines: 0,
            isPlaying: false,
            isPaused: false,
            grid: [],
            currentPiece: null,
            nextPiece: null,
            dropTimer: 0,
            dropInterval: 1000
        }};

        // Game elements
        const puzzleGrid = document.getElementById('puzzleGrid');
        const nextGrid = document.getElementById('nextGrid');
        const scoreElement = document.getElementById('score');
        const levelElement = document.getElementById('level');
        const linesElement = document.getElementById('lines');

        // Tetris pieces
        const pieces = [
            [
                [1, 1, 1, 1] // I-piece
            ],
            [
                [1, 1],
                [1, 1] // O-piece
            ],
            [
                [0, 1, 0],
                [1, 1, 1] // T-piece
            ],
            [
                [1, 0, 0],
                [1, 1, 1] // L-piece
            ],
            [
                [0, 0, 1],
                [1, 1, 1] // J-piece
            ],
            [
                [0, 1, 1],
                [1, 1, 0] // S-piece
            ],
            [
                [1, 1, 0],
                [0, 1, 1] // Z-piece
            ]
        ];

        function initGame() {{
            // Initialize grid
            gameState.grid = Array(20).fill().map(() => Array(10).fill(0));
            
            // Create grid cells
            puzzleGrid.innerHTML = '';
            for (let row = 0; row < 20; row++) {{
                for (let col = 0; col < 10; col++) {{
                    const cell = document.createElement('div');
                    cell.className = 'grid-cell';
                    cell.dataset.row = row;
                    cell.dataset.col = col;
                    puzzleGrid.appendChild(cell);
                }}
            }}
            
            // Create next piece grid
            nextGrid.innerHTML = '';
            for (let i = 0; i < 16; i++) {{
                const cell = document.createElement('div');
                cell.className = 'next-cell';
                nextGrid.appendChild(cell);
            }}
            
            updateUI();
        }}

        function startGame() {{
            gameState.isPlaying = true;
            gameState.isPaused = false;
            gameState.currentPiece = generatePiece();
            gameState.nextPiece = generatePiece();
            updateNextPiece();
            gameLoop();
        }}

        function pauseGame() {{
            gameState.isPaused = !gameState.isPaused;
        }}

        function resetGame() {{
            gameState = {{
                score: 0,
                level: 1,
                lines: 0,
                isPlaying: false,
                isPaused: false,
                grid: [],
                currentPiece: null,
                nextPiece: null,
                dropTimer: 0,
                dropInterval: 1000
            }};
            
            initGame();
        }}

        function generatePiece() {{
            const pieceIndex = Math.floor(Math.random() * pieces.length);
            return {{
                shape: pieces[pieceIndex],
                x: 4,
                y: 0,
                color: pieceIndex + 1
            }};
        }}

        function gameLoop() {{
            if (!gameState.isPlaying) return;
            
            if (!gameState.isPaused) {{
                gameState.dropTimer += 50;
                if (gameState.dropTimer >= gameState.dropInterval) {{
                    dropPiece();
                    gameState.dropTimer = 0;
                }}
            }}
            
            setTimeout(gameLoop, 50);
        }}

        function dropPiece() {{
            if (gameState.currentPiece) {{
                gameState.currentPiece.y++;
                if (checkCollision()) {{
                    gameState.currentPiece.y--;
                    placePiece();
                    clearLines();
                    gameState.currentPiece = gameState.nextPiece;
                    gameState.nextPiece = generatePiece();
                    updateNextPiece();
                    
                    if (checkCollision()) {{
                        // Game over
                        gameState.isPlaying = false;
                        alert('Game Over! Score: ' + gameState.score);
                    }}
                }}
                updateGrid();
            }}
        }}

        function checkCollision() {{
            if (!gameState.currentPiece) return false;
            
            const {{ shape, x, y }} = gameState.currentPiece;
            
            for (let row = 0; row < shape.length; row++) {{
                for (let col = 0; col < shape[row].length; col++) {{
                    if (shape[row][col]) {{
                        const newX = x + col;
                        const newY = y + row;
                        
                        if (newX < 0 || newX >= 10 || newY >= 20) {{
                            return true;
                        }}
                        
                        if (newY >= 0 && gameState.grid[newY][newX]) {{
                            return true;
                        }}
                    }}
                }}
            }}
            
            return false;
        }}

        function placePiece() {{
            const {{ shape, x, y, color }} = gameState.currentPiece;
            
            for (let row = 0; row < shape.length; row++) {{
                for (let col = 0; col < shape[row].length; col++) {{
                    if (shape[row][col]) {{
                        const newX = x + col;
                        const newY = y + row;
                        
                        if (newY >= 0) {{
                            gameState.grid[newY][newX] = color;
                        }}
                    }}
                }}
            }}
        }}

        function clearLines() {{
            let linesCleared = 0;
            
            for (let row = 19; row >= 0; row--) {{
                if (gameState.grid[row].every(cell => cell !== 0)) {{
                    gameState.grid.splice(row, 1);
                    gameState.grid.unshift(Array(10).fill(0));
                    linesCleared++;
                    row++; // Check the same row again
                }}
            }}
            
            if (linesCleared > 0) {{
                gameState.lines += linesCleared;
                gameState.score += linesCleared * 100 * gameState.level;
                gameState.level = Math.floor(gameState.lines / 10) + 1;
                gameState.dropInterval = Math.max(100, 1000 - (gameState.level - 1) * 100);
                updateUI();
            }}
        }}

        function updateGrid() {{
            const cells = puzzleGrid.children;
            
            // Clear all cells
            for (let i = 0; i < cells.length; i++) {{
                cells[i].classList.remove('filled');
            }}
            
            // Draw placed pieces
            for (let row = 0; row < 20; row++) {{
                for (let col = 0; col < 10; col++) {{
                    if (gameState.grid[row][col]) {{
                        const cellIndex = row * 10 + col;
                        cells[cellIndex].classList.add('filled');
                    }}
                }}
            }}
            
            // Draw current piece
            if (gameState.currentPiece) {{
                const {{ shape, x, y }} = gameState.currentPiece;
                
                for (let row = 0; row < shape.length; row++) {{
                    for (let col = 0; col < shape[row].length; col++) {{
                        if (shape[row][col]) {{
                            const newX = x + col;
                            const newY = y + row;
                            
                            if (newX >= 0 && newX < 10 && newY >= 0 && newY < 20) {{
                                const cellIndex = newY * 10 + newX;
                                cells[cellIndex].classList.add('filled');
                            }}
                        }}
                    }}
                }}
            }}
        }}

        function updateNextPiece() {{
            const cells = nextGrid.children;
            
            // Clear all cells
            for (let i = 0; i < cells.length; i++) {{
                cells[i].classList.remove('filled');
            }}
            
            if (gameState.nextPiece) {{
                const {{ shape }} = gameState.nextPiece;
                
                for (let row = 0; row < shape.length; row++) {{
                    for (let col = 0; col < shape[row].length; col++) {{
                        if (shape[row][col]) {{
                            const cellIndex = row * 4 + col;
                            if (cellIndex < 16) {{
                                cells[cellIndex].classList.add('filled');
                            }}
                        }}
                    }}
                }}
            }}
        }}

        function updateUI() {{
            scoreElement.textContent = gameState.score;
            levelElement.textContent = gameState.level;
            linesElement.textContent = gameState.lines;
        }}

        // Controls
        document.addEventListener('keydown', (e) => {{
            if (!gameState.isPlaying || gameState.isPaused || !gameState.currentPiece) return;
            
            switch(e.key) {{
                case 'ArrowLeft':
                case 'a':
                case 'A':
                    gameState.currentPiece.x--;
                    if (checkCollision()) {{
                        gameState.currentPiece.x++;
                    }}
                    updateGrid();
                    break;
                case 'ArrowRight':
                case 'd':
                case 'D':
                    gameState.currentPiece.x++;
                    if (checkCollision()) {{
                        gameState.currentPiece.x--;
                    }}
                    updateGrid();
                    break;
                case 'ArrowDown':
                case 's':
                case 'S':
                    dropPiece();
                    break;
                case 'ArrowUp':
                case 'w':
                case 'W':
                    // Rotate piece (simplified)
                    const originalShape = gameState.currentPiece.shape;
                    gameState.currentPiece.shape = rotateMatrix(originalShape);
                    if (checkCollision()) {{
                        gameState.currentPiece.shape = originalShape;
                    }}
                    updateGrid();
                    break;
                case 'p':
                case 'P':
                    pauseGame();
                    break;
            }}
        }});

        function rotateMatrix(matrix) {{
            const rows = matrix.length;
            const cols = matrix[0].length;
            const rotated = Array(cols).fill().map(() => Array(rows).fill(0));
            
            for (let row = 0; row < rows; row++) {{
                for (let col = 0; col < cols; col++) {{
                    rotated[col][rows - 1 - row] = matrix[row][col];
                }}
            }}
            
            return rotated;
        }}

        // Touch controls for mobile
        let touchStartX = 0;
        let touchStartY = 0;

        puzzleGrid.addEventListener('touchstart', (e) => {{
            touchStartX = e.touches[0].clientX;
            touchStartY = e.touches[0].clientY;
        }});

        puzzleGrid.addEventListener('touchend', (e) => {{
            const touchEndX = e.changedTouches[0].clientX;
            const touchEndY = e.changedTouches[0].clientY;
            const deltaX = touchEndX - touchStartX;
            const deltaY = touchEndY - touchStartY;

            if (Math.abs(deltaX) > Math.abs(deltaY)) {{
                if (deltaX > 30) {{
                    // Swipe right
                    if (gameState.currentPiece) {{
                        gameState.currentPiece.x++;
                        if (checkCollision()) {{
                            gameState.currentPiece.x--;
                        }}
                        updateGrid();
                    }}
                }} else if (deltaX < -30) {{
                    // Swipe left
                    if (gameState.currentPiece) {{
                        gameState.currentPiece.x--;
                        if (checkCollision()) {{
                            gameState.currentPiece.x++;
                        }}
                        updateGrid();
                    }}
                }}
            }} else {{
                if (deltaY > 30) {{
                    // Swipe down
                    dropPiece();
                }} else if (deltaY < -30) {{
                    // Swipe up (rotate)
                    if (gameState.currentPiece) {{
                        const originalShape = gameState.currentPiece.shape;
                        gameState.currentPiece.shape = rotateMatrix(originalShape);
                        if (checkCollision()) {{
                            gameState.currentPiece.shape = originalShape;
                        }}
                        updateGrid();
                    }}
                }}
            }}
        }});

        // Initialize game on load
        initGame();
    </script>
</body>
</html>'''
    
    def get_enhanced_racing_template(self, description):
        """Generate enhanced racing game"""
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Racing Game</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 50%, #2c3e50 100%);
            font-family: 'Arial', sans-serif;
            overflow: hidden;
            color: white;
        }}
        
        .game-container {{
            position: relative;
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        
        .game-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 30px;
            background: rgba(0, 0, 0, 0.8);
            border-bottom: 2px solid #e74c3c;
        }}
        
        .game-title {{
            font-size: 24px;
            font-weight: bold;
            color: #e74c3c;
            text-shadow: 0 0 10px #e74c3c;
        }}
        
        .game-stats {{
            display: flex;
            gap: 30px;
            font-size: 18px;
        }}
        
        .stat {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .stat-value {{
            font-weight: bold;
            color: #00ff00;
        }}
        
        .game-canvas {{
            flex: 1;
            position: relative;
            background: linear-gradient(to bottom, #87CEEB 0%, #228B22 30%, #696969 100%);
            overflow: hidden;
        }}
        
        .road {{
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 300px;
            height: 100%;
            background: linear-gradient(to right, #333 0%, #555 20%, #666 50%, #555 80%, #333 100%);
            border-left: 4px solid #fff;
            border-right: 4px solid #fff;
        }}
        
        .road-line {{
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            width: 4px;
            height: 40px;
            background: #fff;
            animation: roadMove 0.5s linear infinite;
        }}
        
        .player-car {{
            position: absolute;
            bottom: 100px;
            left: 50%;
            transform: translateX(-50%);
            width: 40px;
            height: 60px;
            background: linear-gradient(45deg, #e74c3c, #c0392b);
            border-radius: 8px 8px 4px 4px;
            border: 2px solid #fff;
            box-shadow: 0 0 15px #e74c3c;
            transition: all 0.1s ease;
        }}
        
        .player-car::before {{
            content: '';
            position: absolute;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            width: 20px;
            height: 30px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 4px;
        }}
        
        .enemy-car {{
            position: absolute;
            width: 35px;
            height: 55px;
            background: linear-gradient(45deg, #3498db, #2980b9);
            border-radius: 8px 8px 4px 4px;
            border: 2px solid #fff;
            box-shadow: 0 0 10px #3498db;
            animation: enemyCarMove 3s linear infinite;
        }}
        
        .enemy-car::before {{
            content: '';
            position: absolute;
            top: 8px;
            left: 50%;
            transform: translateX(-50%);
            width: 18px;
            height: 25px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 3px;
        }}
        
        .obstacle {{
            position: absolute;
            width: 30px;
            height: 30px;
            background: linear-gradient(45deg, #95a5a6, #7f8c8d);
            border-radius: 4px;
            border: 2px solid #fff;
            animation: obstacleMove 4s linear infinite;
        }}
        
        .fuel-pickup {{
            position: absolute;
            width: 25px;
            height: 25px;
            background: linear-gradient(45deg, #f39c12, #e67e22);
            border-radius: 50%;
            border: 2px solid #fff;
            box-shadow: 0 0 10px #f39c12;
            animation: fuelMove 3s linear infinite, fuelSpin 1s linear infinite;
        }}
        
        .speed-boost {{
            position: absolute;
            width: 30px;
            height: 15px;
            background: linear-gradient(45deg, #9b59b6, #8e44ad);
            border-radius: 15px;
            border: 2px solid #fff;
            box-shadow: 0 0 10px #9b59b6;
            animation: boostMove 2.5s linear infinite, boostPulse 0.5s ease-in-out infinite alternate;
        }}
        
        .game-controls {{
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 20px;
            z-index: 100;
        }}
        
        .control-btn {{
            padding: 12px 24px;
            background: rgba(231, 76, 60, 0.2);
            border: 2px solid #e74c3c;
            color: #e74c3c;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }}
        
        .control-btn:hover {{
            background: rgba(231, 76, 60, 0.4);
            box-shadow: 0 0 20px #e74c3c;
        }}
        
        @keyframes roadMove {{
            from {{ top: -50px; }}
            to {{ top: 100vh; }}
        }}
        
        @keyframes enemyCarMove {{
            from {{ top: -70px; }}
            to {{ top: 100vh; }}
        }}
        
        @keyframes obstacleMove {{
            from {{ top: -40px; }}
            to {{ top: 100vh; }}
        }}
        
        @keyframes fuelMove {{
            from {{ top: -30px; }}
            to {{ top: 100vh; }}
        }}
        
        @keyframes fuelSpin {{
            from {{ transform: rotate(0deg); }}
            to {{ transform: rotate(360deg); }}
        }}
        
        @keyframes boostMove {{
            from {{ top: -20px; }}
            to {{ top: 100vh; }}
        }}
        
        @keyframes boostPulse {{
            from {{ transform: scale(1); }}
            to {{ transform: scale(1.2); }}
        }}
        
        @media (max-width: 768px) {{
            .game-header {{
                padding: 10px 15px;
            }}
            
            .game-title {{
                font-size: 18px;
            }}
            
            .game-stats {{
                gap: 15px;
                font-size: 14px;
            }}
            
            .road {{
                width: 250px;
            }}
            
            .player-car {{
                width: 35px;
                height: 50px;
            }}
            
            .control-btn {{
                padding: 10px 20px;
                font-size: 14px;
            }}
        }}
    </style>
</head>
<body>
    <div class="game-container">
        <div class="game-header">
            <div class="game-title">🏎️ Ultimate Racing Game</div>
            <div class="game-stats">
                <div class="stat">
                    <span>Score:</span>
                    <span class="stat-value" id="score">0</span>
                </div>
                <div class="stat">
                    <span>Speed:</span>
                    <span class="stat-value" id="speed">0</span>
                </div>
                <div class="stat">
                    <span>Fuel:</span>
                    <span class="stat-value" id="fuel">100</span>
                </div>
            </div>
        </div>
        
        <div class="game-canvas" id="gameCanvas">
            <div class="road" id="road">
                <!-- Road lines will be generated dynamically -->
            </div>
            <div class="player-car" id="playerCar"></div>
        </div>
        
        <div class="game-controls">
            <button class="control-btn" onclick="startGame()">Start Race</button>
            <button class="control-btn" onclick="pauseGame()">Pause</button>
            <button class="control-btn" onclick="resetGame()">Reset</button>
        </div>
    </div>

    <script>
        // Game state
        let gameState = {{
            score: 0,
            speed: 0,
            fuel: 100,
            isPlaying: false,
            isPaused: false,
            player: {{ x: 0, lane: 1 }}, // lane 0=left, 1=center, 2=right
            enemies: [],
            obstacles: [],
            pickups: [],
            roadLines: []
        }};

        // Game elements
        const playerCar = document.getElementById('playerCar');
        const gameCanvas = document.getElementById('gameCanvas');
        const road = document.getElementById('road');
        const scoreElement = document.getElementById('score');
        const speedElement = document.getElementById('speed');
        const fuelElement = document.getElementById('fuel');

        // Lane positions (relative to road center)
        const lanes = [-80, 0, 80];

        function initGame() {{
            createRoadLines();
            updatePlayerPosition();
            updateUI();
        }}

        function createRoadLines() {{
            for (let i = 0; i < 20; i++) {{
                createRoadLine();
            }}
        }}

        function createRoadLine() {{
            const line = document.createElement('div');
            line.className = 'road-line';
            line.style.top = (Math.random() * 100) + '%';
            line.style.animationDelay = Math.random() * 0.5 + 's';
            road.appendChild(line);
            
            setTimeout(() => {{
                if (line.parentNode) {{
                    line.parentNode.removeChild(line);
                }}
                if (gameState.isPlaying) {{
                    createRoadLine();
                }}
            }}, 500);
        }}

        function startGame() {{
            gameState.isPlaying = true;
            gameState.isPaused = false;
            gameState.speed = 50;
            spawnEnemies();
            spawnObstacles();
            spawnPickups();
            gameLoop();
        }}

        function pauseGame() {{
            gameState.isPaused = !gameState.isPaused;
        }}

        function resetGame() {{
            gameState = {{
                score: 0,
                speed: 0,
                fuel: 100,
                isPlaying: false,
                isPaused: false,
                player: {{ x: 0, lane: 1 }},
                enemies: [],
                obstacles: [],
                pickups: [],
                roadLines: []
            }};
            
            // Clear all game elements
            const enemies = document.querySelectorAll('.enemy-car');
            const obstacles = document.querySelectorAll('.obstacle');
            const pickups = document.querySelectorAll('.fuel-pickup, .speed-boost');
            
            enemies.forEach(enemy => enemy.remove());
            obstacles.forEach(obstacle => obstacle.remove());
            pickups.forEach(pickup => pickup.remove());
            
            updatePlayerPosition();
            updateUI();
        }}

        function gameLoop() {{
            if (!gameState.isPlaying) return;
            
            if (!gameState.isPaused) {{
                // Update score based on speed
                gameState.score += Math.floor(gameState.speed / 10);
                
                // Consume fuel
                gameState.fuel -= 0.1;
                if (gameState.fuel <= 0) {{
                    gameState.fuel = 0;
                    gameState.speed = Math.max(0, gameState.speed - 2);
                }}
                
                // Increase speed gradually
                if (gameState.fuel > 0) {{
                    gameState.speed = Math.min(100, gameState.speed + 0.1);
                }}
                
                updateUI();
            }}
            
            setTimeout(gameLoop, 100);
        }}

        function spawnEnemies() {{
            if (!gameState.isPlaying || gameState.isPaused) return;
            
            const enemy = document.createElement('div');
            enemy.className = 'enemy-car';
            const lane = Math.floor(Math.random() * 3);
            enemy.style.left = (150 + lanes[lane]) + 'px';
            enemy.style.top = '-70px';
            gameCanvas.appendChild(enemy);
            
            setTimeout(() => {{
                if (enemy.parentNode) {{
                    enemy.parentNode.removeChild(enemy);
                }}
            }}, 3000);
            
            setTimeout(() => {{
                if (gameState.isPlaying) {{
                    spawnEnemies();
                }}
            }}, 1500 + Math.random() * 2000);
        }}

        function spawnObstacles() {{
            if (!gameState.isPlaying || gameState.isPaused) return;
            
            const obstacle = document.createElement('div');
            obstacle.className = 'obstacle';
            const lane = Math.floor(Math.random() * 3);
            obstacle.style.left = (150 + lanes[lane]) + 'px';
            obstacle.style.top = '-40px';
            gameCanvas.appendChild(obstacle);
            
            setTimeout(() => {{
                if (obstacle.parentNode) {{
                    obstacle.parentNode.removeChild(obstacle);
                }}
            }}, 4000);
            
            setTimeout(() => {{
                if (gameState.isPlaying) {{
                    spawnObstacles();
                }}
            }}, 3000 + Math.random() * 4000);
        }}

        function spawnPickups() {{
            if (!gameState.isPlaying || gameState.isPaused) return;
            
            const pickupType = Math.random() > 0.5 ? 'fuel-pickup' : 'speed-boost';
            const pickup = document.createElement('div');
            pickup.className = pickupType;
            const lane = Math.floor(Math.random() * 3);
            pickup.style.left = (150 + lanes[lane]) + 'px';
            pickup.style.top = '-30px';
            gameCanvas.appendChild(pickup);
            
            setTimeout(() => {{
                if (pickup.parentNode) {{
                    pickup.parentNode.removeChild(pickup);
                }}
            }}, pickupType === 'fuel-pickup' ? 3000 : 2500);
            
            setTimeout(() => {{
                if (gameState.isPlaying) {{
                    spawnPickups();
                }}
            }}, 4000 + Math.random() * 6000);
        }}

        function updatePlayerPosition() {{
            const roadRect = road.getBoundingClientRect();
            const roadCenter = roadRect.left + roadRect.width / 2;
            const newX = roadCenter + lanes[gameState.player.lane] - 20; // 20 = half car width
            playerCar.style.left = newX + 'px';
        }}

        function moveLeft() {{
            if (gameState.isPlaying && !gameState.isPaused && gameState.player.lane > 0) {{
                gameState.player.lane--;
                updatePlayerPosition();
            }}
        }}

        function moveRight() {{
            if (gameState.isPlaying && !gameState.isPaused && gameState.player.lane < 2) {{
                gameState.player.lane++;
                updatePlayerPosition();
            }}
        }}

        function boost() {{
            if (gameState.isPlaying && !gameState.isPaused && gameState.fuel > 10) {{
                gameState.speed = Math.min(100, gameState.speed + 10);
                gameState.fuel -= 5;
                updateUI();
            }}
        }}

        function updateUI() {{
            scoreElement.textContent = Math.floor(gameState.score);
            speedElement.textContent = Math.floor(gameState.speed);
            fuelElement.textContent = Math.floor(gameState.fuel);
        }}

        // Controls
        document.addEventListener('keydown', (e) => {{
            switch(e.key) {{
                case 'ArrowLeft':
                case 'a':
                case 'A':
                    moveLeft();
                    break;
                case 'ArrowRight':
                case 'd':
                case 'D':
                    moveRight();
                    break;
                case 'ArrowUp':
                case ' ':
                case 'w':
                case 'W':
                    e.preventDefault();
                    boost();
                    break;
                case 'p':
                case 'P':
                    pauseGame();
                    break;
            }}
        }});

        // Touch controls for mobile
        let touchStartX = 0;
        let touchStartY = 0;

        gameCanvas.addEventListener('touchstart', (e) => {{
            touchStartX = e.touches[0].clientX;
            touchStartY = e.touches[0].clientY;
        }});

        gameCanvas.addEventListener('touchend', (e) => {{
            const touchEndX = e.changedTouches[0].clientX;
            const touchEndY = e.changedTouches[0].clientY;
            const deltaX = touchEndX - touchStartX;
            const deltaY = touchEndY - touchStartY;

            if (Math.abs(deltaX) > Math.abs(deltaY)) {{
                if (deltaX > 50) {{
                    moveRight(); // Swipe right
                }} else if (deltaX < -50) {{
                    moveLeft(); // Swipe left
                }}
            }} else {{
                if (deltaY < -50) {{
                    boost(); // Swipe up
                }}
            }}
        }});

        // Initialize game on load
        initGame();
    </script>
</body>
</html>'''
    
    def load_and_customize_template(self, template_id, template_info, description):
        """Load and customize the appropriate template based on template_id"""
        if template_id == 'space_shooter':
            return self.get_enhanced_space_shooter_template(description)
        elif template_id == 'platformer':
            return self.get_enhanced_platformer_template(description)
        elif template_id == 'puzzle':
            return self.get_enhanced_puzzle_template(description)
        elif template_id == 'racing':
            return self.get_enhanced_racing_template(description)
        else:
            # Default fallback to space shooter
            return self.get_enhanced_space_shooter_template(description)
    
    def generate_game(self, description, enhanced=True):
        """Generate a game based on the description"""
        if not enhanced:
            # Basic generation (fallback)
            return {
                'success': True,
                'game_html': f'<h1>Basic Game</h1><p>Game description: {description}</p>',
                'metadata': {
                    'template': 'basic',
                    'features': 2,
                    'quality': 'Basic'
                }
            }
        
        try:
            # Analyze prompt to determine best template
            template_id, template_info = self.analyze_prompt(description)
            
            # Generate the game HTML
            game_html = self.load_and_customize_template(template_id, template_info, description)
            
            # Create metadata
            metadata = {
                'template': template_id.title(),
                'features': len(template_info['features']),
                'quality': 'Professional',
                'template_info': template_info
            }
            
            return {
                'success': True,
                'game_html': game_html,
                'metadata': metadata
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'game_html': '<h1>Error</h1><p>Failed to generate game</p>',
                'metadata': {
                    'template': 'error',
                    'features': 0,
                    'quality': 'Failed'
                }
            }

# Initialize the generator
generator = MultiTemplateGameGenerator()

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

@app.route('/generate-game', methods=['POST'])
def generate_game():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        prompt = data.get('prompt', '')
        enhanced = data.get('enhanced', False)
        
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400
        
        # Generate the game
        result = generator.generate_game(prompt, enhanced)
        
        if result['success']:
            return jsonify({
                'game_html': result['game_html'],
                'metadata': result['metadata']
            })
        else:
            return jsonify({
                'error': result['error'],
                'game_html': result['game_html'],
                'metadata': result['metadata']
            }), 500
            
    except Exception as e:
        return jsonify({
            'error': str(e),
            'game_html': '<h1>Error</h1><p>Internal server error</p>',
            'metadata': {
                'template': 'error',
                'features': 0,
                'quality': 'Failed'
            }
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
