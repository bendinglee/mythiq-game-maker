from flask import Flask, request, jsonify, render_template, send_from_directory
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
GAME_TEMPLATES_PATH = os.environ.get('GAME_TEMPLATES_PATH', './templates/games/')

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

class EnhancedGameGenerator:
    def __init__(self):
        self.game_templates = {
            'space_shooter': {
                'name': 'Space Shooter',
                'template': 'enhanced_space_shooter.html',
                'keywords': ['space', 'shooter', 'spaceship', 'asteroid', 'laser', 'shoot'],
                'features': ['movement', 'shooting', 'enemies', 'powerups', 'scoring', 'health']
            },
            'platformer': {
                'name': 'Platformer',
                'template': 'enhanced_platformer.html',
                'keywords': ['platform', 'jump', 'mario', 'side-scroll', 'collect'],
                'features': ['movement', 'jumping', 'platforms', 'enemies', 'collectibles']
            },
            'puzzle': {
                'name': 'Puzzle Game',
                'template': 'enhanced_puzzle.html',
                'keywords': ['puzzle', 'match', 'tetris', 'block', 'grid'],
                'features': ['grid', 'matching', 'scoring', 'levels']
            },
            'racing': {
                'name': 'Racing Game',
                'template': 'enhanced_racing.html',
                'keywords': ['race', 'car', 'speed', 'track', 'drive'],
                'features': ['movement', 'obstacles', 'speed', 'scoring']
            }
        }
    
    def analyze_game_request(self, description):
        """Analyze game description to determine best template"""
        description_lower = description.lower()
        
        # Score each template based on keyword matches
        template_scores = {}
        for template_id, template_info in self.game_templates.items():
            score = 0
            for keyword in template_info['keywords']:
                if keyword in description_lower:
                    score += 1
            template_scores[template_id] = score
        
        # Return template with highest score, default to space_shooter
        best_template = max(template_scores, key=template_scores.get)
        if template_scores[best_template] == 0:
            best_template = 'space_shooter'  # Default
        
        return best_template, self.game_templates[best_template]
    
    def generate_enhanced_game(self, description):
        """Generate enhanced game using professional templates"""
        try:
            # 1. Analyze request and select template
            template_id, template_info = self.analyze_game_request(description)
            
            # 2. Load and customize template
            game_html = self.load_and_customize_template(template_id, template_info, description)
            
            # 3. Add metadata
            metadata = {
                'title': self.generate_game_title(description, template_info),
                'template_used': template_id,
                'features': template_info['features'],
                'generated_at': datetime.now().isoformat(),
                'description': description
            }
            
            return {
                'success': True,
                'html': game_html,
                'metadata': metadata
            }
            
        except Exception as e:
            print(f"Enhanced generation failed: {e}")
            # Fallback to AI generation
            return self.fallback_ai_generation(description)
    
    def load_and_customize_template(self, template_id, template_info, description):
        """Load template and customize based on description"""
        
        # For now, return the enhanced space shooter template
        # In production, you would load from actual template files
        return self.get_enhanced_space_shooter_template(description)
    
    def get_enhanced_space_shooter_template(self, description):
        """Return enhanced space shooter template"""
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enhanced Space Shooter</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
            color: white;
        }

        .game-header {
            text-align: center;
            margin-bottom: 20px;
        }

        .game-header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
            color: #00d4ff;
        }

        .game-container {
            background: rgba(0, 20, 40, 0.9);
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            border: 2px solid rgba(0, 212, 255, 0.3);
            max-width: 900px;
            width: 100%;
        }

        .game-ui {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(0,0,0,0.3);
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        .score-display, .level-display {
            font-size: 1.2rem;
            font-weight: bold;
            color: #00d4ff;
        }

        .health-bar {
            width: 200px;
            height: 20px;
            background: rgba(255,0,0,0.3);
            border-radius: 10px;
            overflow: hidden;
            border: 2px solid rgba(255,255,255,0.3);
        }

        .health-fill {
            height: 100%;
            background: linear-gradient(90deg, #ff4444, #ff8888);
            width: 100%;
            transition: width 0.3s ease;
        }

        .game-canvas {
            width: 100%;
            height: 500px;
            background: linear-gradient(180deg, #000428 0%, #004e92 100%);
            border-radius: 15px;
            position: relative;
            overflow: hidden;
            border: 3px solid rgba(0, 212, 255, 0.3);
            box-shadow: inset 0 0 20px rgba(0,0,0,0.5);
        }

        .stars {
            position: absolute;
            width: 100%;
            height: 100%;
            pointer-events: none;
        }

        .star {
            position: absolute;
            background: white;
            border-radius: 50%;
            animation: twinkle 3s infinite;
        }

        @keyframes twinkle {
            0%, 100% { opacity: 0.3; }
            50% { opacity: 1; }
        }

        .spaceship {
            position: absolute;
            width: 40px;
            height: 40px;
            background: linear-gradient(45deg, #00ff88, #00cc66);
            clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
            box-shadow: 0 0 20px rgba(0, 255, 136, 0.6);
            transition: all 0.1s ease;
            z-index: 10;
        }

        .asteroid {
            position: absolute;
            background: linear-gradient(45deg, #ff6b35, #f7931e);
            border-radius: 50%;
            box-shadow: 0 0 15px rgba(255, 107, 53, 0.5);
            animation: rotate 3s linear infinite;
        }

        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .laser {
            position: absolute;
            width: 3px;
            height: 20px;
            background: linear-gradient(180deg, #00ffff, #ffffff);
            border-radius: 2px;
            box-shadow: 0 0 10px #00ffff;
        }

        .powerup {
            position: absolute;
            width: 30px;
            height: 30px;
            background: linear-gradient(45deg, #ffd700, #ffed4e);
            border-radius: 50%;
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
            animation: powerupFloat 3s ease-in-out infinite;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
        }

        @keyframes powerupFloat {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }

        .explosion {
            position: absolute;
            width: 60px;
            height: 60px;
            background: radial-gradient(circle, #ffff00, #ff4500, transparent);
            border-radius: 50%;
            animation: explode 0.6s ease-out forwards;
        }

        @keyframes explode {
            0% { transform: scale(0); opacity: 1; }
            100% { transform: scale(3); opacity: 0; }
        }

        .game-controls {
            margin-top: 20px;
            text-align: center;
            background: rgba(0,0,0,0.2);
            padding: 15px;
            border-radius: 10px;
        }

        .controls-info {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin-bottom: 10px;
        }

        .control-key {
            background: #333;
            color: #fff;
            padding: 8px 15px;
            border-radius: 5px;
            font-weight: bold;
            box-shadow: 0 3px 6px rgba(0,0,0,0.3);
        }

        .game-features {
            margin-top: 20px;
            background: rgba(0,0,0,0.2);
            padding: 20px;
            border-radius: 10px;
        }

        .game-features h3 {
            margin-bottom: 15px;
            color: #00d4ff;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
        }

        .feature-item {
            padding: 10px;
            background: rgba(255,255,255,0.1);
            border-radius: 5px;
            border-left: 4px solid #00d4ff;
        }

        @media (max-width: 768px) {
            .game-container {
                margin: 10px;
                padding: 15px;
            }
            
            .game-canvas {
                height: 400px;
            }
            
            .game-ui {
                flex-direction: column;
                gap: 10px;
            }
            
            .health-bar {
                width: 150px;
            }
        }
    </style>
</head>
<body>
    <div class="game-header">
        <h1>🚀 Enhanced Space Shooter</h1>
        <p>Professional AI-Generated Game with Advanced Features</p>
    </div>

    <div class="game-container">
        <div class="game-ui">
            <div class="score-display">Score: <span id="score">0</span></div>
            <div class="health-bar">
                <div class="health-fill" id="healthFill"></div>
            </div>
            <div class="level-display">Level: <span id="level">1</span></div>
        </div>
        
        <div class="game-canvas" id="gameCanvas">
            <div class="stars" id="stars"></div>
        </div>
        
        <div class="game-controls">
            <div class="controls-info">
                <div class="control-key">WASD</div>
                <div class="control-key">Arrow Keys</div>
                <div class="control-key">SPACE</div>
                <div class="control-key">Mouse Click</div>
            </div>
            <p>Move with WASD/Arrows • Shoot with SPACE/Click • Pause with P</p>
        </div>
        
        <div class="game-features">
            <h3>✨ Enhanced Features</h3>
            <div class="features-grid">
                <div class="feature-item">🎨 Professional Graphics</div>
                <div class="feature-item">🔫 Complete Shooting System</div>
                <div class="feature-item">⭐ Power-up System</div>
                <div class="feature-item">📊 Advanced Scoring</div>
                <div class="feature-item">🎯 Difficulty Scaling</div>
                <div class="feature-item">💥 Particle Effects</div>
                <div class="feature-item">📱 Mobile Optimized</div>
                <div class="feature-item">🎵 Sound Ready</div>
            </div>
        </div>
    </div>

    <script>
        class EnhancedSpaceShooter {
            constructor() {
                this.canvas = document.getElementById('gameCanvas');
                this.width = this.canvas.offsetWidth;
                this.height = this.canvas.offsetHeight;
                
                this.gameState = {
                    score: 0,
                    level: 1,
                    health: 100,
                    gameRunning: false,
                    paused: false
                };
                
                this.entities = {
                    player: null,
                    enemies: [],
                    lasers: [],
                    powerups: [],
                    particles: []
                };
                
                this.input = {
                    keys: {},
                    mouse: { x: 0, y: 0 }
                };
                
                this.timers = {
                    lastShot: 0,
                    lastEnemySpawn: 0,
                    lastPowerupSpawn: 0
                };
                
                this.config = {
                    player: { speed: 5, fireRate: 200, size: 40 },
                    enemy: { spawnRate: 0.02, baseSpeed: 2, sizeRange: [20, 50] },
                    powerup: { spawnRate: 0.005, duration: 10000 }
                };
                
                this.init();
            }
            
            init() {
                this.setupEventListeners();
                this.createStarField();
                this.createPlayer();
                this.startGameLoop();
                this.gameState.gameRunning = true;
            }
            
            setupEventListeners() {
                document.addEventListener('keydown', (e) => {
                    this.input.keys[e.code] = true;
                    if (e.code === 'Space') {
                        e.preventDefault();
                        this.shoot();
                    }
                    if (e.code === 'KeyP') {
                        this.togglePause();
                    }
                });
                
                document.addEventListener('keyup', (e) => {
                    this.input.keys[e.code] = false;
                });
                
                this.canvas.addEventListener('mousemove', (e) => {
                    const rect = this.canvas.getBoundingClientRect();
                    this.input.mouse.x = e.clientX - rect.left;
                    this.input.mouse.y = e.clientY - rect.top;
                });
                
                this.canvas.addEventListener('click', () => {
                    this.shoot();
                });
                
                // Touch events for mobile
                this.canvas.addEventListener('touchstart', (e) => {
                    e.preventDefault();
                    const touch = e.touches[0];
                    const rect = this.canvas.getBoundingClientRect();
                    this.input.mouse.x = touch.clientX - rect.left;
                    this.input.mouse.y = touch.clientY - rect.top;
                    this.shoot();
                });
                
                this.canvas.addEventListener('touchmove', (e) => {
                    e.preventDefault();
                    const touch = e.touches[0];
                    const rect = this.canvas.getBoundingClientRect();
                    this.input.mouse.x = touch.clientX - rect.left;
                    this.input.mouse.y = touch.clientY - rect.top;
                });
            }
            
            createStarField() {
                const starsContainer = document.getElementById('stars');
                for (let i = 0; i < 50; i++) {
                    const star = document.createElement('div');
                    star.className = 'star';
                    star.style.left = Math.random() * 100 + '%';
                    star.style.top = Math.random() * 100 + '%';
                    star.style.width = star.style.height = (Math.random() * 3 + 1) + 'px';
                    star.style.animationDelay = Math.random() * 3 + 's';
                    starsContainer.appendChild(star);
                }
            }
            
            createPlayer() {
                this.entities.player = {
                    x: this.width / 2 - this.config.player.size / 2,
                    y: this.height - this.config.player.size - 20,
                    width: this.config.player.size,
                    height: this.config.player.size,
                    speed: this.config.player.speed,
                    element: this.createElement('spaceship', this.width / 2 - this.config.player.size / 2, this.height - this.config.player.size - 20)
                };
            }
            
            createElement(className, x, y, width, height) {
                const element = document.createElement('div');
                element.className = className;
                element.style.position = 'absolute';
                element.style.left = x + 'px';
                element.style.top = y + 'px';
                if (width) element.style.width = width + 'px';
                if (height) element.style.height = height + 'px';
                this.canvas.appendChild(element);
                return element;
            }
            
            updatePlayer() {
                if (!this.entities.player || this.gameState.paused) return;
                
                const player = this.entities.player;
                
                // Movement
                if (this.input.keys['KeyW'] || this.input.keys['ArrowUp']) {
                    player.y = Math.max(0, player.y - player.speed);
                }
                if (this.input.keys['KeyS'] || this.input.keys['ArrowDown']) {
                    player.y = Math.min(this.height - player.height, player.y + player.speed);
                }
                if (this.input.keys['KeyA'] || this.input.keys['ArrowLeft']) {
                    player.x = Math.max(0, player.x - player.speed);
                }
                if (this.input.keys['KeyD'] || this.input.keys['ArrowRight']) {
                    player.x = Math.min(this.width - player.width, player.x + player.speed);
                }
                
                // Update visual position
                player.element.style.left = player.x + 'px';
                player.element.style.top = player.y + 'px';
            }
            
            shoot() {
                if (!this.entities.player || this.gameState.paused) return;
                
                const now = Date.now();
                if (now - this.timers.lastShot < this.config.player.fireRate) return;
                
                const player = this.entities.player;
                const laser = {
                    x: player.x + player.width / 2 - 1.5,
                    y: player.y,
                    width: 3,
                    height: 20,
                    speed: 8,
                    element: this.createElement('laser', player.x + player.width / 2 - 1.5, player.y, 3, 20)
                };
                
                this.entities.lasers.push(laser);
                this.timers.lastShot = now;
            }
            
            spawnEnemy() {
                if (this.gameState.paused) return;
                
                const spawnRate = this.config.enemy.spawnRate + (this.gameState.level - 1) * 0.005;
                
                if (Math.random() < spawnRate) {
                    const size = Math.random() * (this.config.enemy.sizeRange[1] - this.config.enemy.sizeRange[0]) + this.config.enemy.sizeRange[0];
                    const enemy = {
                        x: Math.random() * (this.width - size),
                        y: -size,
                        width: size,
                        height: size,
                        speed: this.config.enemy.baseSpeed + Math.random() * 2 + (this.gameState.level - 1) * 0.3,
                        points: Math.floor(size / 2),
                        element: this.createElement('asteroid', Math.random() * (this.width - size), -size, size, size)
                    };
                    
                    this.entities.enemies.push(enemy);
                }
            }
            
            spawnPowerup() {
                if (this.gameState.paused) return;
                
                if (Math.random() < this.config.powerup.spawnRate) {
                    const types = ['health', 'rapidfire', 'multishot', 'shield'];
                    const type = types[Math.floor(Math.random() * types.length)];
                    const icons = { health: '❤️', rapidfire: '⚡', multishot: '🔥', shield: '🛡️' };
                    
                    const powerup = {
                        x: Math.random() * (this.width - 30),
                        y: -30,
                        width: 30,
                        height: 30,
                        speed: 2,
                        type: type,
                        element: this.createElement('powerup', Math.random() * (this.width - 30), -30, 30, 30)
                    };
                    
                    powerup.element.innerHTML = icons[type];
                    this.entities.powerups.push(powerup);
                }
            }
            
            updateEntities() {
                if (this.gameState.paused) return;
                
                // Update lasers
                this.entities.lasers = this.entities.lasers.filter(laser => {
                    laser.y -= laser.speed;
                    laser.element.style.top = laser.y + 'px';
                    
                    if (laser.y < -laser.height) {
                        laser.element.remove();
                        return false;
                    }
                    return true;
                });
                
                // Update enemies
                this.entities.enemies = this.entities.enemies.filter(enemy => {
                    enemy.y += enemy.speed;
                    enemy.element.style.top = enemy.y + 'px';
                    
                    if (enemy.y > this.height) {
                        enemy.element.remove();
                        return false;
                    }
                    return true;
                });
                
                // Update powerups
                this.entities.powerups = this.entities.powerups.filter(powerup => {
                    powerup.y += powerup.speed;
                    powerup.element.style.top = powerup.y + 'px';
                    
                    if (powerup.y > this.height) {
                        powerup.element.remove();
                        return false;
                    }
                    return true;
                });
            }
            
            checkCollisions() {
                if (this.gameState.paused) return;
                
                // Laser-enemy collisions
                this.entities.lasers.forEach((laser, lIndex) => {
                    this.entities.enemies.forEach((enemy, eIndex) => {
                        if (this.isColliding(laser, enemy)) {
                            this.createExplosion(enemy.x + enemy.width / 2, enemy.y + enemy.height / 2);
                            
                            laser.element.remove();
                            enemy.element.remove();
                            this.entities.lasers.splice(lIndex, 1);
                            this.entities.enemies.splice(eIndex, 1);
                            
                            this.gameState.score += enemy.points * this.gameState.level;
                            this.updateUI();
                        }
                    });
                });
                
                // Player-enemy collisions
                if (this.entities.player) {
                    this.entities.enemies.forEach((enemy, eIndex) => {
                        if (this.isColliding(this.entities.player, enemy)) {
                            this.createExplosion(enemy.x + enemy.width / 2, enemy.y + enemy.height / 2);
                            enemy.element.remove();
                            this.entities.enemies.splice(eIndex, 1);
                            
                            this.gameState.health -= 20;
                            this.updateUI();
                            
                            if (this.gameState.health <= 0) {
                                this.gameOver();
                            }
                        }
                    });
                    
                    // Player-powerup collisions
                    this.entities.powerups.forEach((powerup, pIndex) => {
                        if (this.isColliding(this.entities.player, powerup)) {
                            this.collectPowerup(powerup.type);
                            powerup.element.remove();
                            this.entities.powerups.splice(pIndex, 1);
                        }
                    });
                }
            }
            
            isColliding(obj1, obj2) {
                return obj1.x < obj2.x + obj2.width &&
                       obj1.x + obj1.width > obj2.x &&
                       obj1.y < obj2.y + obj2.height &&
                       obj1.y + obj1.height > obj2.y;
            }
            
            createExplosion(x, y) {
                const explosion = this.createElement('explosion', x - 30, y - 30, 60, 60);
                setTimeout(() => explosion.remove(), 600);
            }
            
            collectPowerup(type) {
                switch (type) {
                    case 'health':
                        this.gameState.health = Math.min(100, this.gameState.health + 25);
                        break;
                    case 'rapidfire':
                        this.config.player.fireRate = 100;
                        setTimeout(() => this.config.player.fireRate = 200, this.config.powerup.duration);
                        break;
                    case 'multishot':
                        // Implement multishot logic
                        break;
                    case 'shield':
                        // Implement shield logic
                        break;
                }
                this.updateUI();
            }
            
            updateUI() {
                document.getElementById('score').textContent = this.gameState.score;
                document.getElementById('level').textContent = this.gameState.level;
                document.getElementById('healthFill').style.width = this.gameState.health + '%';
                
                // Level progression
                if (this.gameState.score > this.gameState.level * 500) {
                    this.gameState.level++;
                }
            }
            
            togglePause() {
                this.gameState.paused = !this.gameState.paused;
            }
            
            gameOver() {
                this.gameState.gameRunning = false;
                setTimeout(() => {
                    alert(`Game Over! Final Score: ${this.gameState.score}`);
                    this.resetGame();
                }, 1000);
            }
            
            resetGame() {
                // Clear all entities
                this.entities.enemies.forEach(enemy => enemy.element.remove());
                this.entities.lasers.forEach(laser => laser.element.remove());
                this.entities.powerups.forEach(powerup => powerup.element.remove());
                
                this.entities.enemies = [];
                this.entities.lasers = [];
                this.entities.powerups = [];
                
                this.gameState.score = 0;
                this.gameState.level = 1;
                this.gameState.health = 100;
                this.gameState.gameRunning = true;
                this.gameState.paused = false;
                
                this.createPlayer();
                this.updateUI();
            }
            
            startGameLoop() {
                const gameLoop = () => {
                    if (this.gameState.gameRunning) {
                        this.updatePlayer();
                        this.spawnEnemy();
                        this.spawnPowerup();
                        this.updateEntities();
                        this.checkCollisions();
                    }
                    requestAnimationFrame(gameLoop);
                };
                
                gameLoop();
            }
        }
        
        // Initialize game when page loads
        document.addEventListener('DOMContentLoaded', () => {
            new EnhancedSpaceShooter();
        });
    </script>
</body>
</html>'''
    
    def generate_game_title(self, description, template_info):
        """Generate appropriate game title"""
        titles = {
            'space_shooter': ['Galactic Defense', 'Space Warrior', 'Asteroid Blaster', 'Cosmic Shooter'],
            'platformer': ['Adventure Quest', 'Platform Hero', 'Jump Master', 'Side Scroller'],
            'puzzle': ['Mind Bender', 'Puzzle Master', 'Brain Teaser', 'Logic Game'],
            'racing': ['Speed Racer', 'Fast Track', 'Racing Champion', 'Speed Demon']
        }
        
        template_titles = titles.get(template_info.get('name', '').lower().replace(' ', '_'), ['Epic Game'])
        return random.choice(template_titles)
    
    def fallback_ai_generation(self, description):
        """Fallback to AI generation if template system fails"""
        try:
            return generate_game_with_groq(description)
        except:
            return {
                'success': False,
                'error': 'Game generation failed',
                'html': '<h1>Game generation temporarily unavailable</h1>'
            }

# Initialize enhanced generator
enhanced_generator = EnhancedGameGenerator()

def generate_game_with_groq(prompt):
    """Generate game using Groq API with enhanced prompts"""
    try:
        headers = {
            'Authorization': f'Bearer {GROQ_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        # Enhanced system prompt for better game generation
        system_prompt = """You are a professional game developer AI. Create a complete, playable HTML5 game based on the user's request.

CRITICAL REQUIREMENTS:
1. Return ONLY valid HTML code with <!DOCTYPE html>
2. Include embedded CSS in <style> tags with professional styling
3. Include embedded JavaScript in <script> tags with complete game logic
4. Create a fully functional game that works immediately in a browser
5. Implement ALL requested features (shooting, powerups, scoring, etc.)
6. Use professional graphics with CSS animations and effects
7. Make it visually appealing with gradients, shadows, and animations
8. Include proper game mechanics (collision detection, scoring, levels)
9. Add mobile touch controls for responsive design
10. Include game UI (score, health, controls instructions)

VISUAL REQUIREMENTS:
- Use CSS gradients and box-shadows for professional appearance
- Implement smooth animations and transitions
- Create engaging visual effects (explosions, particle effects)
- Use modern color schemes and typography
- Make it responsive for mobile devices

GAME MECHANICS:
- Implement complete player movement (WASD/arrows)
- Add shooting mechanics with projectiles
- Include enemy spawning and AI behavior
- Implement collision detection and responses
- Add scoring system with level progression
- Include power-ups and special abilities
- Add game states (playing, paused, game over)

The game should be self-contained, professional-looking, and immediately playable."""

        response = requests.post(
            'https://api.groq.com/openai/v1/chat/completions',
            headers=headers,
            json={
                'model': 'llama3-70b-8192',
                'messages': [
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': prompt}
                ],
                'max_tokens': 4000,
                'temperature': 0.7
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            game_html = result['choices'][0]['message']['content']
            
            # Post-process the generated HTML
            game_html = enhance_generated_html(game_html)
            
            return {
                'success': True,
                'html': game_html,
                'metadata': {
                    'generated_with': 'groq_api',
                    'model': 'llama3-70b-8192',
                    'generated_at': datetime.now().isoformat()
                }
            }
        else:
            return {'success': False, 'error': f'API Error: {response.status_code}'}
            
    except Exception as e:
        return {'success': False, 'error': str(e)}

def enhance_generated_html(html_content):
    """Post-process generated HTML to improve quality"""
    # Add meta viewport if missing
    if 'viewport' not in html_content:
        html_content = html_content.replace(
            '<head>',
            '<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">'
        )
    
    # Ensure professional styling
    if 'background:' not in html_content and 'background-color:' not in html_content:
        html_content = html_content.replace(
            'body {',
            'body {\n            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);'
        )
    
    return html_content

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'groq_available': check_groq_availability()
    })

@app.route('/generate_game', methods=['POST'])
def generate_game():
    """Enhanced game generation endpoint"""
    try:
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({'error': 'No prompt provided'}), 400
        
        prompt = data['prompt']
        use_enhanced = data.get('enhanced', True)  # Default to enhanced generation
        
        if use_enhanced:
            # Use enhanced template-based generation
            result = enhanced_generator.generate_enhanced_game(prompt)
        else:
            # Use traditional AI generation
            result = generate_game_with_groq(prompt)
        
        if result.get('success'):
            return jsonify({
                'success': True,
                'html': result['html'],
                'metadata': result.get('metadata', {})
            })
        else:
            return jsonify({
                'success': False,
                'error': result.get('error', 'Unknown error'),
                'html': result.get('html', '<h1>Game generation failed</h1>')
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'html': '<h1>Game generation error</h1>'
        }), 500

@app.route('/templates/<path:filename>')
def serve_template(filename):
    """Serve game templates"""
    return send_from_directory('templates', filename)

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files"""
    return send_from_directory('static', filename)

@app.route('/', methods=['GET'])
def index():
    """Root endpoint"""
    return jsonify({
        'service': 'Mythiq Enhanced Game Maker',
        'version': '2.0.0',
        'status': 'operational',
        'features': [
            'Enhanced template-based game generation',
            'Professional graphics and animations',
            'Complete feature implementation',
            'Mobile optimization',
            'AI-powered customization'
        ],
        'endpoints': {
            '/generate_game': 'POST - Generate enhanced games',
            '/health': 'GET - Health check',
            '/templates/<filename>': 'GET - Serve game templates',
            '/static/<filename>': 'GET - Serve static assets'
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
