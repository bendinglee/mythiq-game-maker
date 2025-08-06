"""
Fixed Mythiq Game Maker with AI-Powered Template Customization
- Proper Railway deployment configuration
- AI-powered prompt analysis and template customization
- Professional graphics maintained across all game types
- Unique game generation while preserving quality
"""

import os
import json
import random
import re
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class AIGameCustomizer:
    def __init__(self):
        self.templates = {
            'space_shooter': {
                'name': 'Space Shooter',
                'keywords': ['space', 'shooter', 'shoot', 'spaceship', 'laser', 'alien', 'enemy', 'asteroid', 'galaxy', 'cosmic'],
                'themes': ['cosmic', 'alien_invasion', 'space_patrol', 'asteroid_field', 'galactic_war'],
                'colors': ['#00ffff', '#ff6b6b', '#9b59b6', '#f39c12', '#e74c3c'],
                'enemies': ['alien', 'asteroid', 'drone', 'mothership', 'fighter'],
                'powerups': ['laser_upgrade', 'shield', 'rapid_fire', 'multi_shot', 'health']
            },
            'platformer': {
                'name': 'Platformer',
                'keywords': ['platform', 'jump', 'mario', 'side-scroll', 'coin', 'level', 'obstacle', 'adventure'],
                'themes': ['forest', 'castle', 'underground', 'sky', 'desert'],
                'colors': ['#FFD700', '#FF6347', '#32CD32', '#87CEEB', '#DDA0DD'],
                'enemies': ['goomba', 'spike', 'guard', 'monster', 'robot'],
                'powerups': ['coin', 'gem', 'key', 'star', 'mushroom']
            },
            'puzzle': {
                'name': 'Puzzle',
                'keywords': ['puzzle', 'tetris', 'block', 'match', 'grid', 'clear', 'rotate', 'logic'],
                'themes': ['classic', 'neon', 'crystal', 'digital', 'retro'],
                'colors': ['#9b59b6', '#3498db', '#e74c3c', '#f39c12', '#2ecc71'],
                'pieces': ['I_piece', 'O_piece', 'T_piece', 'L_piece', 'J_piece', 'S_piece', 'Z_piece'],
                'effects': ['line_clear', 'combo', 'cascade', 'flash', 'particle']
            },
            'racing': {
                'name': 'Racing',
                'keywords': ['race', 'racing', 'car', 'speed', 'track', 'lap', 'vehicle', 'drive', 'formula'],
                'themes': ['city', 'desert', 'mountain', 'highway', 'circuit'],
                'colors': ['#e74c3c', '#3498db', '#f39c12', '#2ecc71', '#9b59b6'],
                'vehicles': ['sports_car', 'formula', 'truck', 'motorcycle', 'hover_car'],
                'obstacles': ['oil_spill', 'barrier', 'other_car', 'debris', 'pothole']
            }
        }
    
    def analyze_prompt(self, description):
        """AI-powered prompt analysis to determine template and customizations"""
        description_lower = description.lower()
        
        # Score each template based on keyword matches
        scores = {}
        for template_id, template_info in self.templates.items():
            score = 0
            for keyword in template_info['keywords']:
                if keyword in description_lower:
                    score += 1
            scores[template_id] = score
        
        # Get the best template
        best_template = max(scores, key=scores.get)
        if scores[best_template] == 0:
            best_template = 'space_shooter'  # Default fallback
        
        return best_template, self.templates[best_template]
    
    def extract_customizations(self, description, template_info):
        """Extract specific customizations from the prompt"""
        description_lower = description.lower()
        customizations = {}
        
        # Extract theme preferences
        if 'themes' in template_info:
            for theme in template_info['themes']:
                if theme in description_lower:
                    customizations['theme'] = theme
                    break
            if 'theme' not in customizations:
                customizations['theme'] = random.choice(template_info['themes'])
        
        # Extract color preferences
        color_words = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan']
        color_map = {
            'red': '#e74c3c', 'blue': '#3498db', 'green': '#2ecc71',
            'yellow': '#f39c12', 'purple': '#9b59b6', 'orange': '#e67e22',
            'pink': '#e91e63', 'cyan': '#00ffff'
        }
        
        for color_word in color_words:
            if color_word in description_lower:
                customizations['primary_color'] = color_map[color_word]
                break
        
        if 'primary_color' not in customizations:
            customizations['primary_color'] = random.choice(template_info['colors'])
        
        # Extract difficulty preferences
        if any(word in description_lower for word in ['easy', 'simple', 'beginner']):
            customizations['difficulty'] = 'easy'
        elif any(word in description_lower for word in ['hard', 'difficult', 'challenging', 'expert']):
            customizations['difficulty'] = 'hard'
        else:
            customizations['difficulty'] = 'medium'
        
        # Extract specific game elements mentioned
        customizations['elements'] = []
        if 'enemies' in template_info:
            for enemy in template_info['enemies']:
                if enemy in description_lower:
                    customizations['elements'].append(enemy)
        
        if 'powerups' in template_info:
            for powerup in template_info['powerups']:
                if powerup in description_lower:
                    customizations['elements'].append(powerup)
        
        return customizations
    
    def customize_template(self, template_id, template_info, customizations, description):
        """Generate customized game based on template and AI analysis"""
        
        if template_id == 'space_shooter':
            return self.generate_custom_space_shooter(customizations, description)
        elif template_id == 'platformer':
            return self.generate_custom_platformer(customizations, description)
        elif template_id == 'puzzle':
            return self.generate_custom_puzzle(customizations, description)
        elif template_id == 'racing':
            return self.generate_custom_racing(customizations, description)
        else:
            return self.generate_custom_space_shooter(customizations, description)
    
    def generate_custom_space_shooter(self, customizations, description):
        """Generate customized space shooter with AI-driven variations"""
        
        theme = customizations.get('theme', 'cosmic')
        primary_color = customizations.get('primary_color', '#00ffff')
        difficulty = customizations.get('difficulty', 'medium')
        
        # Customize based on theme
        if theme == 'alien_invasion':
            title = "👽 Alien Invasion Defense"
            background = "linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%)"
            enemy_color = "#ff4757"
        elif theme == 'space_patrol':
            title = "🚀 Space Patrol Mission"
            background = "linear-gradient(135deg, #2c3e50 0%, #34495e 50%, #2c3e50 100%)"
            enemy_color = "#e74c3c"
        elif theme == 'asteroid_field':
            title = "☄️ Asteroid Field Navigator"
            background = "linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)"
            enemy_color = "#95a5a6"
        else:
            title = "🌌 Cosmic Adventure"
            background = "linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%)"
            enemy_color = "#ff6b6b"
        
        # Adjust difficulty
        if difficulty == 'easy':
            enemy_spawn_rate = "3000 + Math.random() * 4000"
            player_health = "150"
            enemy_speed = "4s"
        elif difficulty == 'hard':
            enemy_spawn_rate = "800 + Math.random() * 1200"
            player_health = "75"
            enemy_speed = "2s"
        else:
            enemy_spawn_rate = "1500 + Math.random() * 2500"
            player_health = "100"
            enemy_speed = "3s"
        
        # Generate unique game title based on description
        game_title = self.generate_unique_title(description, "Space Shooter")
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{game_title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: {background};
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
            border-bottom: 2px solid {primary_color};
        }}
        
        .game-title {{
            font-size: 24px;
            font-weight: bold;
            color: {primary_color};
            text-shadow: 0 0 10px {primary_color};
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
            background: linear-gradient(45deg, {primary_color}, {primary_color}aa);
            clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
            border: 2px solid #fff;
            box-shadow: 0 0 20px {primary_color};
            transition: all 0.1s ease;
        }}
        
        .enemy {{
            position: absolute;
            width: 40px;
            height: 40px;
            background: linear-gradient(45deg, {enemy_color}, {enemy_color}aa);
            clip-path: polygon(50% 100%, 0% 0%, 100% 0%);
            border: 1px solid #fff;
            box-shadow: 0 0 15px {enemy_color};
            animation: enemyMove {enemy_speed} linear infinite;
        }}
        
        .laser {{
            position: absolute;
            width: 4px;
            height: 20px;
            background: linear-gradient(to top, {primary_color}, #ffffff);
            border-radius: 2px;
            box-shadow: 0 0 10px {primary_color};
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
            background: radial-gradient(circle, {primary_color} 0%, {primary_color}aa 50%, transparent 100%);
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
            border: 2px solid {primary_color};
            color: {primary_color};
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }}
        
        .control-btn:hover {{
            background: rgba(0, 255, 255, 0.4);
            box-shadow: 0 0 20px {primary_color};
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
            <div class="game-title">{title}</div>
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
                    <span class="stat-value" id="health">{player_health}</span>
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
        // Game state with customized parameters
        let gameState = {{
            score: 0,
            level: 1,
            health: {player_health},
            isPlaying: false,
            isPaused: false,
            player: {{ x: 50, y: 50 }},
            enemies: [],
            lasers: [],
            powerups: [],
            stars: [],
            difficulty: '{difficulty}',
            theme: '{theme}'
        }};

        // Game elements
        const player = document.getElementById('player');
        const gameCanvas = document.getElementById('gameCanvas');
        const scoreElement = document.getElementById('score');
        const levelElement = document.getElementById('level');
        const healthElement = document.getElementById('health');

        // Initialize game with customizations
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
                health: {player_health},
                isPlaying: false,
                isPaused: false,
                player: {{ x: 50, y: 50 }},
                enemies: [],
                lasers: [],
                powerups: [],
                stars: [],
                difficulty: '{difficulty}',
                theme: '{theme}'
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
            }}, {enemy_speed.replace('s', '000')});
            
            setTimeout(() => {{
                if (gameState.isPlaying) {{
                    spawnEnemies();
                }}
            }}, {enemy_spawn_rate});
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
    
    def generate_custom_platformer(self, customizations, description):
        """Generate customized platformer with AI-driven variations"""
        
        theme = customizations.get('theme', 'forest')
        primary_color = customizations.get('primary_color', '#FFD700')
        difficulty = customizations.get('difficulty', 'medium')
        
        # Customize based on theme
        if theme == 'castle':
            title = "🏰 Castle Adventure"
            background = "linear-gradient(135deg, #8B4513 0%, #A0522D 50%, #CD853F 100%)"
        elif theme == 'underground':
            title = "⛏️ Underground Explorer"
            background = "linear-gradient(135deg, #2F4F4F 0%, #696969 50%, #808080 100%)"
        elif theme == 'sky':
            title = "☁️ Sky Kingdom"
            background = "linear-gradient(135deg, #87CEEB 0%, #98FB98 50%, #90EE90 100%)"
        else:
            title = "🌲 Forest Adventure"
            background = "linear-gradient(135deg, #87CEEB 0%, #98FB98 50%, #90EE90 100%)"
        
        # Generate unique game title
        game_title = self.generate_unique_title(description, "Platformer")
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{game_title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: {background};
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
            border-bottom: 2px solid {primary_color};
            color: white;
        }}
        
        .game-title {{
            font-size: 24px;
            font-weight: bold;
            color: {primary_color};
            text-shadow: 0 0 10px {primary_color};
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
            background: {background};
            overflow: hidden;
        }}
        
        .player {{
            position: absolute;
            bottom: 120px;
            left: 100px;
            width: 40px;
            height: 40px;
            background: linear-gradient(45deg, {primary_color}, {primary_color}aa);
            border-radius: 8px;
            border: 2px solid #fff;
            box-shadow: 0 0 15px {primary_color};
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
            background: linear-gradient(45deg, {primary_color}, {primary_color}aa);
            border-radius: 50%;
            border: 2px solid #fff;
            box-shadow: 0 0 10px {primary_color};
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
            border: 2px solid {primary_color};
            color: {primary_color};
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }}
        
        .control-btn:hover {{
            background: rgba(255, 215, 0, 0.4);
            box-shadow: 0 0 20px {primary_color};
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
            <div class="game-title">{title}</div>
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
        // Game state with customizations
        let gameState = {{
            score: 0,
            level: 1,
            lives: 3,
            isPlaying: false,
            isPaused: false,
            player: {{ x: 100, y: 120, velocityY: 0, onGround: false }},
            gravity: 0.8,
            jumpPower: -15,
            theme: '{theme}',
            difficulty: '{difficulty}'
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
                jumpPower: -15,
                theme: '{theme}',
                difficulty: '{difficulty}'
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
    
    def generate_custom_puzzle(self, customizations, description):
        """Generate customized puzzle game with AI-driven variations"""
        
        theme = customizations.get('theme', 'classic')
        primary_color = customizations.get('primary_color', '#9b59b6')
        difficulty = customizations.get('difficulty', 'medium')
        
        # Customize based on theme
        if theme == 'neon':
            title = "💫 Neon Puzzle"
            background = "linear-gradient(135deg, #000000 0%, #1a1a2e 50%, #16213e 100%)"
        elif theme == 'crystal':
            title = "💎 Crystal Blocks"
            background = "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
        elif theme == 'digital':
            title = "🔲 Digital Matrix"
            background = "linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%)"
        else:
            title = "🧩 Classic Puzzle"
            background = "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
        
        # Generate unique game title
        game_title = self.generate_unique_title(description, "Puzzle")
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{game_title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: {background};
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
            border-bottom: 2px solid {primary_color};
        }}
        
        .game-title {{
            font-size: 24px;
            font-weight: bold;
            color: {primary_color};
            text-shadow: 0 0 10px {primary_color};
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
            border: 2px solid {primary_color};
        }}
        
        .grid-cell {{
            width: 30px;
            height: 30px;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 3px;
        }}
        
        .grid-cell.filled {{
            background: linear-gradient(45deg, {primary_color}, {primary_color}aa);
            border: 1px solid #fff;
            box-shadow: 0 0 5px {primary_color};
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
            border: 2px solid {primary_color};
        }}
        
        .next-piece h3 {{
            margin: 0 0 10px 0;
            color: {primary_color};
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
            border: 2px solid {primary_color};
            color: {primary_color};
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }}
        
        .control-btn:hover {{
            background: rgba(155, 89, 182, 0.4);
            box-shadow: 0 0 20px {primary_color};
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
            <div class="game-title">{title}</div>
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
        // Game state with customizations
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
            dropInterval: 1000,
            theme: '{theme}',
            difficulty: '{difficulty}'
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
                dropInterval: 1000,
                theme: '{theme}',
                difficulty: '{difficulty}'
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
    
    def generate_custom_racing(self, customizations, description):
        """Generate customized racing game with AI-driven variations"""
        
        theme = customizations.get('theme', 'city')
        primary_color = customizations.get('primary_color', '#e74c3c')
        difficulty = customizations.get('difficulty', 'medium')
        
        # Customize based on theme
        if theme == 'desert':
            title = "🏜️ Desert Rally"
            background = "linear-gradient(to bottom, #FFD700 0%, #DEB887 30%, #D2691E 100%)"
        elif theme == 'mountain':
            title = "🏔️ Mountain Circuit"
            background = "linear-gradient(to bottom, #87CEEB 0%, #228B22 30%, #696969 100%)"
        elif theme == 'highway':
            title = "🛣️ Highway Speed"
            background = "linear-gradient(to bottom, #87CEEB 0%, #32CD32 30%, #696969 100%)"
        else:
            title = "🏙️ City Racing"
            background = "linear-gradient(to bottom, #87CEEB 0%, #228B22 30%, #696969 100%)"
        
        # Generate unique game title
        game_title = self.generate_unique_title(description, "Racing")
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{game_title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: {background};
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
            border-bottom: 2px solid {primary_color};
        }}
        
        .game-title {{
            font-size: 24px;
            font-weight: bold;
            color: {primary_color};
            text-shadow: 0 0 10px {primary_color};
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
            background: {background};
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
            background: linear-gradient(45deg, {primary_color}, {primary_color}aa);
            border-radius: 8px 8px 4px 4px;
            border: 2px solid #fff;
            box-shadow: 0 0 15px {primary_color};
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
            background: linear-gradient(45deg, {primary_color}, {primary_color}aa);
            border-radius: 15px;
            border: 2px solid #fff;
            box-shadow: 0 0 10px {primary_color};
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
            border: 2px solid {primary_color};
            color: {primary_color};
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }}
        
        .control-btn:hover {{
            background: rgba(231, 76, 60, 0.4);
            box-shadow: 0 0 20px {primary_color};
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
            <div class="game-title">{title}</div>
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
        // Game state with customizations
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
            roadLines: [],
            theme: '{theme}',
            difficulty: '{difficulty}'
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
                roadLines: [],
                theme: '{theme}',
                difficulty: '{difficulty}'
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
    
    def generate_unique_title(self, description, game_type):
        """Generate a unique game title based on the description"""
        # Extract key words from description
        words = re.findall(r'\b\w+\b', description.lower())
        
        # Filter out common words
        common_words = {'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'create', 'make', 'game'}
        key_words = [word for word in words if word not in common_words and len(word) > 2]
        
        # Take first 2-3 meaningful words
        if len(key_words) >= 2:
            title_words = key_words[:2]
            title = ' '.join(word.capitalize() for word in title_words) + f' {game_type}'
        elif len(key_words) == 1:
            title = key_words[0].capitalize() + f' {game_type}'
        else:
            title = f'Epic {game_type}'
        
        return title

# Initialize the AI customizer
ai_customizer = AIGameCustomizer()

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
        
        if not enhanced:
            # Basic generation (fallback)
            return jsonify({
                'game_html': f'<h1>Basic Game</h1><p>Game description: {prompt}</p>',
                'metadata': {
                    'template': 'basic',
                    'features': 2,
                    'quality': 'Basic'
                }
            })
        
        # AI-powered enhanced generation
        template_id, template_info = ai_customizer.analyze_prompt(prompt)
        customizations = ai_customizer.extract_customizations(prompt, template_info)
        game_html = ai_customizer.customize_template(template_id, template_info, customizations, prompt)
        
        # Create metadata
        metadata = {
            'template': template_id.replace('_', ' ').title(),
            'features': len(template_info.get('keywords', [])),
            'quality': 'Professional',
            'theme': customizations.get('theme', 'default'),
            'difficulty': customizations.get('difficulty', 'medium'),
            'customizations': customizations
        }
        
        return jsonify({
            'game_html': game_html,
            'metadata': metadata
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'game_html': '<h1>Error</h1><p>Failed to generate game</p>',
            'metadata': {
                'template': 'error',
                'features': 0,
                'quality': 'Failed'
            }
        }), 500

if __name__ == '__main__':
    # Get port from environment variable (Railway provides this)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
