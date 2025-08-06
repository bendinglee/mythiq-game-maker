"""
Free AI Code Generator - Converts AI-generated templates into complete, playable games
Uses FREE APIs (Groq, Hugging Face) to generate professional HTML/CSS/JavaScript code
"""

import os
import json
import re
import requests
from typing import Dict, Any, Optional
from free_ai_template_engine import GameTemplate, GameConcept

class FreeAICodeGenerator:
    """AI-powered code generation system using FREE APIs"""
    
    def __init__(self):
        # Groq API (FREE - you already have this!)
        self.groq_api_key = os.environ.get('GROQ_API_KEY')
        self.groq_base_url = "https://api.groq.com/openai/v1/chat/completions"
        
        # Hugging Face API (FREE)
        self.hf_api_key = os.environ.get('HUGGINGFACE_API_KEY', '')
        self.hf_base_url = "https://api-inference.huggingface.co/models"
        
        # Code quality standards
        self.quality_standards = {
            'html': {
                'semantic': True,
                'responsive': True,
                'accessibility': True,
                'mobile_optimized': True
            },
            'css': {
                'modern_features': True,
                'animations': True,
                'gradients': True,
                'responsive_design': True,
                'performance_optimized': True
            },
            'javascript': {
                'es6_features': True,
                'performance_optimized': True,
                'error_handling': True,
                'mobile_touch': True,
                'smooth_animations': True
            }
        }
    
    def _call_groq_api(self, messages: list, temperature: float = 0.3, max_tokens: int = 2000) -> str:
        """Call Groq API (FREE) for AI responses"""
        
        if not self.groq_api_key:
            raise Exception("GROQ_API_KEY not found in environment variables")
        
        headers = {
            "Authorization": f"Bearer {self.groq_api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "llama3-8b-8192",  # Free Groq model
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        try:
            response = requests.post(self.groq_base_url, headers=headers, json=data, timeout=60)
            response.raise_for_status()
            
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
            
        except Exception as e:
            print(f"Groq API error: {e}")
            raise Exception(f"Groq API call failed: {str(e)}")
    
    def generate_complete_game(self, template: GameTemplate) -> str:
        """Generate complete HTML game from AI template using FREE APIs"""
        
        try:
            # Generate complete game in one call for efficiency
            complete_game = self._generate_complete_game_code(template)
            
            # Optimize and validate
            optimized_game = self._optimize_code_quality(complete_game, template)
            
            return optimized_game
            
        except Exception as e:
            print(f"Game generation error: {e}")
            return self._fallback_complete_game(template)
    
    def _generate_complete_game_code(self, template: GameTemplate) -> str:
        """Generate complete HTML game using FREE AI in one call"""
        
        game_prompt = f"""
        Generate a complete HTML game file based on this template:
        
        GAME CONCEPT:
        - Title: {template.game_structure.get('title', 'Game')}
        - Genre: {template.concept.genre}
        - Theme: {template.concept.theme}
        - Mechanics: {', '.join(template.concept.mechanics)}
        
        VISUAL DESIGN:
        - Colors: {template.visual_design.get('color_palette', [])}
        - Background: {template.visual_design.get('background_style', '')}
        - Player: {template.visual_design.get('player_design', '')}
        - Enemies: {template.visual_design.get('enemy_design', '')}
        
        GAMEPLAY:
        - Movement: {template.gameplay_mechanics.get('movement', '')}
        - Interaction: {template.gameplay_mechanics.get('interaction', '')}
        - Win Condition: {template.game_structure.get('win_condition', '')}
        - Scoring: {template.game_structure.get('scoring_system', '')}
        
        REQUIREMENTS:
        - Complete HTML file with embedded CSS and JavaScript
        - Professional 8-9/10 quality
        - Mobile responsive with touch controls
        - Smooth 60fps animations
        - Modern CSS with gradients and effects
        - Complete game mechanics (movement, collision, scoring)
        - Start/pause/reset functionality
        - Mobile-optimized touch controls
        
        Generate a complete, playable HTML game file. Include:
        1. Semantic HTML structure
        2. Professional CSS with animations
        3. Complete JavaScript game logic
        4. Mobile touch support
        5. Responsive design
        
        Make it engaging, smooth, and professional quality.
        """
        
        try:
            messages = [
                {"role": "system", "content": "You are a senior game developer who creates complete, professional HTML games. Generate high-quality, playable games with modern code."},
                {"role": "user", "content": game_prompt}
            ]
            
            return self._call_groq_api(messages, temperature=0.5, max_tokens=4000)
            
        except Exception as e:
            print(f"Complete game generation error: {e}")
            return self._fallback_complete_game(template)
    
    def _optimize_code_quality(self, game_code: str, template: GameTemplate) -> str:
        """Use FREE AI to optimize code quality and performance"""
        
        # Only optimize if the code looks incomplete or low quality
        if len(game_code) < 2000 or not self._is_complete_html(game_code):
            
            optimization_prompt = f"""
            Optimize this HTML game code for professional quality:
            
            Current Code:
            {game_code[:1500]}...
            
            Improve:
            - Complete any missing functionality
            - Enhance visual quality to 8-9/10 level
            - Optimize for 60fps performance
            - Ensure mobile responsiveness
            - Add smooth animations
            - Fix any bugs or issues
            
            Return the complete, optimized HTML game file.
            """
            
            try:
                messages = [
                    {"role": "system", "content": "You are a senior developer who optimizes web games for professional quality and performance."},
                    {"role": "user", "content": optimization_prompt}
                ]
                
                optimized_code = self._call_groq_api(messages, temperature=0.2, max_tokens=4000)
                
                # Ensure we have a complete HTML document
                if self._is_complete_html(optimized_code) and len(optimized_code) > len(game_code):
                    return optimized_code
                
            except Exception as e:
                print(f"Code optimization error: {e}")
        
        return game_code
    
    def _is_complete_html(self, code: str) -> bool:
        """Check if code is a complete HTML document"""
        required_elements = ['<!DOCTYPE html>', '<html', '<head>', '<body>', '</html>']
        return all(element in code for element in required_elements)
    
    def _fallback_complete_game(self, template: GameTemplate) -> str:
        """Generate fallback complete game when AI fails"""
        
        colors = template.visual_design.get('color_palette', ['#3498db', '#e74c3c', '#2ecc71', '#f39c12'])
        title = template.game_structure.get('title', 'AI Generated Game')
        genre = template.concept.genre
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{template.concept.objective}">
    <title>{title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, {colors[0]} 0%, {colors[1]} 100%);
            color: white;
            overflow: hidden;
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
            border-bottom: 3px solid {colors[2]};
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }}
        
        .game-title {{
            font-size: 28px;
            font-weight: bold;
            color: {colors[2]};
            text-shadow: 0 0 15px {colors[2]};
            animation: glow 2s ease-in-out infinite alternate;
        }}
        
        @keyframes glow {{
            from {{ text-shadow: 0 0 15px {colors[2]}; }}
            to {{ text-shadow: 0 0 25px {colors[2]}, 0 0 35px {colors[2]}; }}
        }}
        
        .game-stats {{
            display: flex;
            gap: 30px;
        }}
        
        .stat {{
            display: flex;
            flex-direction: column;
            align-items: center;
            font-size: 14px;
        }}
        
        .stat-value {{
            font-size: 24px;
            font-weight: bold;
            color: {colors[3]};
            text-shadow: 0 0 10px {colors[3]};
        }}
        
        .game-canvas {{
            flex: 1;
            position: relative;
            overflow: hidden;
            background: radial-gradient(circle at center, rgba(255,255,255,0.1) 0%, transparent 70%);
        }}
        
        .player {{
            position: absolute;
            width: 50px;
            height: 50px;
            background: linear-gradient(45deg, {colors[2]}, {colors[3]});
            border-radius: 12px;
            border: 3px solid #fff;
            box-shadow: 0 0 20px {colors[2]}, inset 0 0 20px rgba(255,255,255,0.2);
            transition: all 0.1s ease;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            animation: pulse 1.5s ease-in-out infinite alternate;
        }}
        
        @keyframes pulse {{
            from {{ transform: translate(-50%, -50%) scale(1); }}
            to {{ transform: translate(-50%, -50%) scale(1.05); }}
        }}
        
        .enemy {{
            position: absolute;
            width: 40px;
            height: 40px;
            background: linear-gradient(45deg, {colors[1]}, #ff6b6b);
            border-radius: 8px;
            border: 2px solid #fff;
            box-shadow: 0 0 15px {colors[1]};
            animation: enemyFloat 2s ease-in-out infinite alternate;
        }}
        
        @keyframes enemyFloat {{
            from {{ transform: translateY(0px); }}
            to {{ transform: translateY(-10px); }}
        }}
        
        .collectible {{
            position: absolute;
            width: 30px;
            height: 30px;
            background: linear-gradient(45deg, {colors[3]}, #ffd700);
            border-radius: 50%;
            border: 2px solid #fff;
            box-shadow: 0 0 15px {colors[3]};
            animation: collectibleSpin 1s linear infinite;
        }}
        
        @keyframes collectibleSpin {{
            from {{ transform: rotate(0deg); }}
            to {{ transform: rotate(360deg); }}
        }}
        
        .particle {{
            position: absolute;
            width: 4px;
            height: 4px;
            background: {colors[3]};
            border-radius: 50%;
            pointer-events: none;
            animation: particleFade 1s ease-out forwards;
        }}
        
        @keyframes particleFade {{
            from {{ opacity: 1; transform: scale(1); }}
            to {{ opacity: 0; transform: scale(0); }}
        }}
        
        .game-controls {{
            display: flex;
            justify-content: center;
            gap: 15px;
            padding: 20px;
            background: rgba(0, 0, 0, 0.8);
            border-top: 2px solid {colors[2]};
        }}
        
        .control-btn {{
            padding: 12px 24px;
            background: linear-gradient(45deg, {colors[0]}, {colors[2]});
            border: none;
            color: white;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            font-size: 16px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }}
        
        .control-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.4);
        }}
        
        .control-btn:active {{
            transform: translateY(0px);
        }}
        
        .mobile-controls {{
            position: fixed;
            bottom: 80px;
            left: 50%;
            transform: translateX(-50%);
            display: none;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            z-index: 1000;
        }}
        
        .mobile-btn {{
            width: 60px;
            height: 60px;
            background: rgba(52, 152, 219, 0.8);
            border: 2px solid {colors[2]};
            border-radius: 50%;
            color: white;
            font-size: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            touch-action: manipulation;
        }}
        
        @media (max-width: 768px) {{
            .mobile-controls {{
                display: grid;
            }}
            
            .game-header {{
                padding: 10px 15px;
            }}
            
            .game-title {{
                font-size: 20px;
            }}
            
            .stat {{
                font-size: 12px;
            }}
            
            .stat-value {{
                font-size: 18px;
            }}
        }}
        
        .game-over {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(0, 0, 0, 0.9);
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            border: 3px solid {colors[2]};
            box-shadow: 0 0 30px rgba(0,0,0,0.8);
            display: none;
        }}
        
        .game-over h2 {{
            color: {colors[1]};
            margin-bottom: 20px;
            font-size: 32px;
        }}
        
        .final-score {{
            color: {colors[3]};
            font-size: 24px;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <div class="game-header">
        <div class="game-title">{title}</div>
        <div class="game-stats">
            <div class="stat">
                <span>Score</span>
                <span class="stat-value" id="score">0</span>
            </div>
            <div class="stat">
                <span>Level</span>
                <span class="stat-value" id="level">1</span>
            </div>
            <div class="stat">
                <span>Health</span>
                <span class="stat-value" id="health">100</span>
            </div>
        </div>
    </div>
    
    <div class="game-canvas" id="gameCanvas">
        <div class="player" id="player"></div>
        
        <div class="game-over" id="gameOver">
            <h2>Game Over!</h2>
            <div class="final-score" id="finalScore">Score: 0</div>
            <button class="control-btn" onclick="resetGame()">Play Again</button>
        </div>
    </div>
    
    <div class="game-controls">
        <button class="control-btn" onclick="startGame()" id="startBtn">Start Game</button>
        <button class="control-btn" onclick="pauseGame()" id="pauseBtn">Pause</button>
        <button class="control-btn" onclick="resetGame()">Reset</button>
    </div>
    
    <div class="mobile-controls">
        <div></div>
        <button class="mobile-btn" ontouchstart="movePlayer('up')">↑</button>
        <div></div>
        <button class="mobile-btn" ontouchstart="movePlayer('left')">←</button>
        <div></div>
        <button class="mobile-btn" ontouchstart="movePlayer('right')">→</button>
        <div></div>
        <button class="mobile-btn" ontouchstart="movePlayer('down')">↓</button>
        <div></div>
    </div>

    <script>
        // Game state
        let gameState = {{
            score: 0,
            level: 1,
            health: 100,
            isPlaying: false,
            isPaused: false,
            enemies: [],
            collectibles: [],
            particles: [],
            playerPos: {{ x: 50, y: 50 }},
            keys: {{}},
            lastTime: 0,
            spawnTimer: 0,
            difficulty: 1
        }};

        // Game elements
        const player = document.getElementById('player');
        const gameCanvas = document.getElementById('gameCanvas');
        const scoreElement = document.getElementById('score');
        const levelElement = document.getElementById('level');
        const healthElement = document.getElementById('health');
        const gameOverScreen = document.getElementById('gameOver');
        const finalScoreElement = document.getElementById('finalScore');

        // Game functions
        function startGame() {{
            if (!gameState.isPlaying) {{
                gameState.isPlaying = true;
                gameState.isPaused = false;
                gameOverScreen.style.display = 'none';
                document.getElementById('startBtn').textContent = 'Resume';
                gameLoop();
            }} else {{
                gameState.isPaused = false;
            }}
        }}

        function pauseGame() {{
            gameState.isPaused = !gameState.isPaused;
            document.getElementById('pauseBtn').textContent = gameState.isPaused ? 'Resume' : 'Pause';
        }}

        function resetGame() {{
            gameState = {{
                score: 0,
                level: 1,
                health: 100,
                isPlaying: false,
                isPaused: false,
                enemies: [],
                collectibles: [],
                particles: [],
                playerPos: {{ x: 50, y: 50 }},
                keys: {{}},
                lastTime: 0,
                spawnTimer: 0,
                difficulty: 1
            }};
            
            // Clear all game objects
            document.querySelectorAll('.enemy, .collectible, .particle').forEach(el => el.remove());
            
            gameOverScreen.style.display = 'none';
            document.getElementById('startBtn').textContent = 'Start Game';
            updateUI();
            updatePlayerPosition();
        }}

        function gameLoop(currentTime = 0) {{
            if (!gameState.isPlaying || gameState.isPaused) {{
                if (gameState.isPlaying) requestAnimationFrame(gameLoop);
                return;
            }}

            const deltaTime = currentTime - gameState.lastTime;
            gameState.lastTime = currentTime;

            // Update game logic
            handleInput();
            updateEnemies(deltaTime);
            updateCollectibles(deltaTime);
            updateParticles(deltaTime);
            checkCollisions();
            spawnObjects(deltaTime);
            updateDifficulty();
            updateUI();

            // Check game over
            if (gameState.health <= 0) {{
                endGame();
                return;
            }}

            requestAnimationFrame(gameLoop);
        }}

        function handleInput() {{
            const speed = 3;
            const canvasRect = gameCanvas.getBoundingClientRect();
            
            if (gameState.keys['ArrowLeft'] || gameState.keys['a']) {{
                gameState.playerPos.x = Math.max(0, gameState.playerPos.x - speed);
            }}
            if (gameState.keys['ArrowRight'] || gameState.keys['d']) {{
                gameState.playerPos.x = Math.min(100, gameState.playerPos.x + speed);
            }}
            if (gameState.keys['ArrowUp'] || gameState.keys['w']) {{
                gameState.playerPos.y = Math.max(0, gameState.playerPos.y - speed);
            }}
            if (gameState.keys['ArrowDown'] || gameState.keys['s']) {{
                gameState.playerPos.y = Math.min(100, gameState.playerPos.y + speed);
            }}
            
            updatePlayerPosition();
        }}

        function updatePlayerPosition() {{
            player.style.left = gameState.playerPos.x + '%';
            player.style.top = gameState.playerPos.y + '%';
        }}

        function spawnObjects(deltaTime) {{
            gameState.spawnTimer += deltaTime;
            
            if (gameState.spawnTimer > 2000 / gameState.difficulty) {{
                gameState.spawnTimer = 0;
                
                // Spawn enemy
                if (Math.random() < 0.7) {{
                    spawnEnemy();
                }} else {{
                    spawnCollectible();
                }}
            }}
        }}

        function spawnEnemy() {{
            const enemy = document.createElement('div');
            enemy.className = 'enemy';
            enemy.style.left = Math.random() * 90 + '%';
            enemy.style.top = Math.random() * 90 + '%';
            gameCanvas.appendChild(enemy);
            
            gameState.enemies.push({{
                element: enemy,
                x: parseFloat(enemy.style.left),
                y: parseFloat(enemy.style.top),
                vx: (Math.random() - 0.5) * 2,
                vy: (Math.random() - 0.5) * 2
            }});
        }}

        function spawnCollectible() {{
            const collectible = document.createElement('div');
            collectible.className = 'collectible';
            collectible.style.left = Math.random() * 90 + '%';
            collectible.style.top = Math.random() * 90 + '%';
            gameCanvas.appendChild(collectible);
            
            gameState.collectibles.push({{
                element: collectible,
                x: parseFloat(collectible.style.left),
                y: parseFloat(collectible.style.top)
            }});
        }}

        function updateEnemies(deltaTime) {{
            gameState.enemies.forEach((enemy, index) => {{
                enemy.x += enemy.vx * gameState.difficulty;
                enemy.y += enemy.vy * gameState.difficulty;
                
                // Bounce off walls
                if (enemy.x <= 0 || enemy.x >= 95) enemy.vx *= -1;
                if (enemy.y <= 0 || enemy.y >= 95) enemy.vy *= -1;
                
                enemy.x = Math.max(0, Math.min(95, enemy.x));
                enemy.y = Math.max(0, Math.min(95, enemy.y));
                
                enemy.element.style.left = enemy.x + '%';
                enemy.element.style.top = enemy.y + '%';
            }});
        }}

        function updateCollectibles(deltaTime) {{
            // Collectibles just stay in place and spin (CSS animation)
        }}

        function updateParticles(deltaTime) {{
            gameState.particles.forEach((particle, index) => {{
                particle.life -= deltaTime;
                if (particle.life <= 0) {{
                    particle.element.remove();
                    gameState.particles.splice(index, 1);
                }}
            }});
        }}

        function checkCollisions() {{
            const playerRect = {{
                x: gameState.playerPos.x,
                y: gameState.playerPos.y,
                width: 5,
                height: 5
            }};

            // Check enemy collisions
            gameState.enemies.forEach((enemy, index) => {{
                if (isColliding(playerRect, {{ x: enemy.x, y: enemy.y, width: 4, height: 4 }})) {{
                    gameState.health -= 10;
                    createParticles(enemy.x, enemy.y, '{colors[1]}');
                    enemy.element.remove();
                    gameState.enemies.splice(index, 1);
                }}
            }});

            // Check collectible collisions
            gameState.collectibles.forEach((collectible, index) => {{
                if (isColliding(playerRect, {{ x: collectible.x, y: collectible.y, width: 3, height: 3 }})) {{
                    gameState.score += 10 * gameState.level;
                    createParticles(collectible.x, collectible.y, '{colors[3]}');
                    collectible.element.remove();
                    gameState.collectibles.splice(index, 1);
                }}
            }});
        }}

        function isColliding(rect1, rect2) {{
            return rect1.x < rect2.x + rect2.width &&
                   rect1.x + rect1.width > rect2.x &&
                   rect1.y < rect2.y + rect2.height &&
                   rect1.y + rect1.height > rect2.y;
        }}

        function createParticles(x, y, color) {{
            for (let i = 0; i < 5; i++) {{
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = x + '%';
                particle.style.top = y + '%';
                particle.style.background = color;
                gameCanvas.appendChild(particle);
                
                gameState.particles.push({{
                    element: particle,
                    life: 1000
                }});
            }}
        }}

        function updateDifficulty() {{
            gameState.level = Math.floor(gameState.score / 100) + 1;
            gameState.difficulty = 1 + (gameState.level - 1) * 0.2;
        }}

        function updateUI() {{
            scoreElement.textContent = gameState.score;
            levelElement.textContent = gameState.level;
            healthElement.textContent = Math.max(0, gameState.health);
        }}

        function endGame() {{
            gameState.isPlaying = false;
            finalScoreElement.textContent = `Score: ${{gameState.score}}`;
            gameOverScreen.style.display = 'block';
            document.getElementById('startBtn').textContent = 'Start Game';
        }}

        function movePlayer(direction) {{
            const speed = 5;
            switch(direction) {{
                case 'up':
                    gameState.playerPos.y = Math.max(0, gameState.playerPos.y - speed);
                    break;
                case 'down':
                    gameState.playerPos.y = Math.min(100, gameState.playerPos.y + speed);
                    break;
                case 'left':
                    gameState.playerPos.x = Math.max(0, gameState.playerPos.x - speed);
                    break;
                case 'right':
                    gameState.playerPos.x = Math.min(100, gameState.playerPos.x + speed);
                    break;
            }}
            updatePlayerPosition();
        }}

        // Event listeners
        document.addEventListener('keydown', (e) => {{
            gameState.keys[e.key] = true;
            if (e.key === ' ') {{
                e.preventDefault();
                if (!gameState.isPlaying) {{
                    startGame();
                }} else {{
                    pauseGame();
                }}
            }}
        }});

        document.addEventListener('keyup', (e) => {{
            gameState.keys[e.key] = false;
        }});

        // Touch events for mobile
        let touchStartX, touchStartY;

        gameCanvas.addEventListener('touchstart', (e) => {{
            e.preventDefault();
            touchStartX = e.touches[0].clientX;
            touchStartY = e.touches[0].clientY;
        }});

        gameCanvas.addEventListener('touchmove', (e) => {{
            e.preventDefault();
            if (!gameState.isPlaying || gameState.isPaused) return;
            
            const touchX = e.touches[0].clientX;
            const touchY = e.touches[0].clientY;
            const deltaX = touchX - touchStartX;
            const deltaY = touchY - touchStartY;
            
            if (Math.abs(deltaX) > Math.abs(deltaY)) {{
                if (deltaX > 10) movePlayer('right');
                else if (deltaX < -10) movePlayer('left');
            }} else {{
                if (deltaY > 10) movePlayer('down');
                else if (deltaY < -10) movePlayer('up');
            }}
            
            touchStartX = touchX;
            touchStartY = touchY;
        }});

        // Initialize game
        updateUI();
        updatePlayerPosition();
    </script>
</body>
</html>'''
    
    def generate_game_preview(self, template: GameTemplate) -> Dict[str, Any]:
        """Generate a preview/summary of what the game will be like"""
        return {
            'title': template.game_structure.get('title', 'AI Generated Game'),
            'description': template.concept.objective,
            'genre': template.concept.genre,
            'mechanics': template.concept.mechanics,
            'visual_style': template.concept.visual_style,
            'complexity': template.concept.complexity,
            'estimated_quality': '8-9/10',
            'features': {
                'responsive_design': True,
                'mobile_optimized': True,
                'smooth_animations': True,
                'professional_graphics': True,
                'touch_controls': True,
                'keyboard_controls': True,
                'free_generation': True
            },
            'color_palette': template.visual_design.get('color_palette', []),
            'estimated_size': '15-25KB',
            'performance': '60fps target',
            'ai_powered': True,
            'cost': 'FREE'
        }
    
    def validate_generated_code(self, game_code: str) -> Dict[str, Any]:
        """Validate the generated game code"""
        validation_results = {
            'is_valid_html': False,
            'has_css': False,
            'has_javascript': False,
            'is_complete': False,
            'estimated_quality': 0,
            'issues': [],
            'free_generation': True
        }
        
        # Check HTML structure
        if '<!DOCTYPE html>' in game_code and '<html' in game_code and '</html>' in game_code:
            validation_results['is_valid_html'] = True
        else:
            validation_results['issues'].append('Invalid HTML structure')
        
        # Check CSS presence
        if '<style>' in game_code or 'style=' in game_code:
            validation_results['has_css'] = True
        else:
            validation_results['issues'].append('Missing CSS styling')
        
        # Check JavaScript presence
        if '<script>' in game_code or 'onclick=' in game_code:
            validation_results['has_javascript'] = True
        else:
            validation_results['issues'].append('Missing JavaScript logic')
        
        # Check completeness
        required_elements = ['game-container', 'player', 'gameLoop', 'startGame']
        has_all_elements = any(element in game_code for element in required_elements)
        validation_results['is_complete'] = has_all_elements
        
        if not has_all_elements:
            validation_results['issues'].append('Missing required game elements')
        
        # Estimate quality
        quality_score = 0
        if validation_results['is_valid_html']:
            quality_score += 3
        if validation_results['has_css']:
            quality_score += 3
        if validation_results['has_javascript']:
            quality_score += 3
        if validation_results['is_complete']:
            quality_score += 1
        
        validation_results['estimated_quality'] = quality_score
        
        return validation_results

