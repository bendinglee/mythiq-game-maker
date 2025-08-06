"""
Game Template Manager - Handles Templates and Assets
Manages HTML templates, CSS styles, and game assets
"""

import os
import json
from datetime import datetime

class GameTemplateManager:
    """
    Manages game templates, assets, and HTML generation
    """
    
    def __init__(self):
        self.templates_loaded = 0
        self.assets_managed = 0
        
        # CSS style templates for different themes
        self.css_templates = {
            'ninja': {
                'body_style': 'background: linear-gradient(135deg, #2C3E50, #34495E); color: #ECF0F1; font-family: "Courier New", monospace;',
                'canvas_style': 'border: 3px solid #E74C3C; box-shadow: 0 0 20px rgba(231, 76, 60, 0.5);',
                'ui_style': 'background: rgba(44, 62, 80, 0.9); border: 1px solid #E74C3C; border-radius: 8px;',
                'button_style': 'background: #E74C3C; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-weight: bold;'
            },
            'space': {
                'body_style': 'background: linear-gradient(135deg, #0F0F23, #1A1A2E); color: #E94560; font-family: "Arial", sans-serif;',
                'canvas_style': 'border: 3px solid #0F3460; box-shadow: 0 0 30px rgba(15, 52, 96, 0.8);',
                'ui_style': 'background: rgba(26, 26, 46, 0.9); border: 1px solid #0F3460; border-radius: 10px;',
                'button_style': 'background: #0F3460; color: #E94560; border: none; padding: 12px 24px; border-radius: 6px; cursor: pointer;'
            },
            'medieval': {
                'body_style': 'background: linear-gradient(135deg, #8B4513, #A0522D); color: #F5DEB3; font-family: "Times New Roman", serif;',
                'canvas_style': 'border: 4px solid #DAA520; box-shadow: 0 0 25px rgba(218, 165, 32, 0.6);',
                'ui_style': 'background: rgba(139, 69, 19, 0.9); border: 2px solid #DAA520; border-radius: 12px;',
                'button_style': 'background: #DAA520; color: #8B4513; border: none; padding: 12px 20px; border-radius: 4px; cursor: pointer; font-weight: bold;'
            },
            'forest': {
                'body_style': 'background: linear-gradient(135deg, #228B22, #32CD32); color: #FFFFFF; font-family: "Verdana", sans-serif;',
                'canvas_style': 'border: 3px solid #FFD700; box-shadow: 0 0 20px rgba(255, 215, 0, 0.7);',
                'ui_style': 'background: rgba(34, 139, 34, 0.9); border: 1px solid #FFD700; border-radius: 8px;',
                'button_style': 'background: #FFD700; color: #228B22; border: none; padding: 10px 18px; border-radius: 5px; cursor: pointer;'
            },
            'underwater': {
                'body_style': 'background: linear-gradient(135deg, #006994, #0099CC); color: #F0F8FF; font-family: "Arial", sans-serif;',
                'canvas_style': 'border: 3px solid #00CED1; box-shadow: 0 0 25px rgba(0, 206, 209, 0.8);',
                'ui_style': 'background: rgba(0, 105, 148, 0.9); border: 1px solid #00CED1; border-radius: 10px;',
                'button_style': 'background: #00CED1; color: #006994; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer;'
            }
        }
        
        # JavaScript code snippets for different features
        self.js_snippets = {
            'particle_system': '''
                function createParticleSystem(x, y, color, count = 5) {
                    for (let i = 0; i < count; i++) {
                        particles.push({
                            x: x + Math.random() * 20 - 10,
                            y: y + Math.random() * 20 - 10,
                            vx: (Math.random() - 0.5) * 8,
                            vy: (Math.random() - 0.5) * 8,
                            color: color,
                            alpha: 1,
                            size: Math.random() * 4 + 2,
                            life: 60
                        });
                    }
                }
                
                function updateParticles() {
                    particles.forEach((particle, index) => {
                        particle.x += particle.vx;
                        particle.y += particle.vy;
                        particle.alpha -= 0.02;
                        particle.life--;
                        
                        if (particle.alpha <= 0 || particle.life <= 0) {
                            particles.splice(index, 1);
                        }
                    });
                }
                
                function drawParticles() {
                    particles.forEach(particle => {
                        ctx.save();
                        ctx.globalAlpha = particle.alpha;
                        ctx.fillStyle = particle.color;
                        ctx.fillRect(particle.x, particle.y, particle.size, particle.size);
                        ctx.restore();
                    });
                }
            ''',
            
            'sound_effects': '''
                const audioContext = new (window.AudioContext || window.webkitAudioContext)();
                
                function playSound(frequency, duration, type = 'sine') {
                    const oscillator = audioContext.createOscillator();
                    const gainNode = audioContext.createGain();
                    
                    oscillator.connect(gainNode);
                    gainNode.connect(audioContext.destination);
                    
                    oscillator.frequency.value = frequency;
                    oscillator.type = type;
                    
                    gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
                    gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + duration);
                    
                    oscillator.start(audioContext.currentTime);
                    oscillator.stop(audioContext.currentTime + duration);
                }
                
                function playCoinSound() { playSound(800, 0.1); }
                function playJumpSound() { playSound(400, 0.2); }
                function playHitSound() { playSound(200, 0.3, 'sawtooth'); }
                function playLevelUpSound() { playSound(600, 0.5); }
            ''',
            
            'collision_detection': '''
                function checkCollision(rect1, rect2) {
                    return rect1.x < rect2.x + rect2.width &&
                           rect1.x + rect1.width > rect2.x &&
                           rect1.y < rect2.y + rect2.height &&
                           rect1.y + rect1.height > rect2.y;
                }
                
                function checkCircleCollision(circle1, circle2) {
                    const dx = circle1.x - circle2.x;
                    const dy = circle1.y - circle2.y;
                    const distance = Math.sqrt(dx * dx + dy * dy);
                    return distance < circle1.radius + circle2.radius;
                }
                
                function checkPointInRect(point, rect) {
                    return point.x >= rect.x && point.x <= rect.x + rect.width &&
                           point.y >= rect.y && point.y <= rect.y + rect.height;
                }
            ''',
            
            'animation_system': '''
                function createAnimation(startValue, endValue, duration, easing = 'linear') {
                    return {
                        startValue,
                        endValue,
                        duration,
                        currentTime: 0,
                        easing,
                        getValue() {
                            const progress = Math.min(this.currentTime / this.duration, 1);
                            const easedProgress = this.applyEasing(progress);
                            return this.startValue + (this.endValue - this.startValue) * easedProgress;
                        },
                        update(deltaTime) {
                            this.currentTime += deltaTime;
                            return this.currentTime >= this.duration;
                        },
                        applyEasing(t) {
                            switch(this.easing) {
                                case 'easeIn': return t * t;
                                case 'easeOut': return 1 - (1 - t) * (1 - t);
                                case 'easeInOut': return t < 0.5 ? 2 * t * t : 1 - 2 * (1 - t) * (1 - t);
                                default: return t;
                            }
                        }
                    };
                }
            ''',
            
            'input_handler': '''
                class InputHandler {
                    constructor() {
                        this.keys = {};
                        this.mouse = { x: 0, y: 0, clicked: false };
                        this.setupEventListeners();
                    }
                    
                    setupEventListeners() {
                        document.addEventListener('keydown', (e) => {
                            this.keys[e.code] = true;
                            e.preventDefault();
                        });
                        
                        document.addEventListener('keyup', (e) => {
                            this.keys[e.code] = false;
                            e.preventDefault();
                        });
                        
                        canvas.addEventListener('mousemove', (e) => {
                            const rect = canvas.getBoundingClientRect();
                            this.mouse.x = e.clientX - rect.left;
                            this.mouse.y = e.clientY - rect.top;
                        });
                        
                        canvas.addEventListener('click', (e) => {
                            this.mouse.clicked = true;
                            setTimeout(() => this.mouse.clicked = false, 100);
                        });
                    }
                    
                    isKeyPressed(key) {
                        return this.keys[key] || false;
                    }
                    
                    getMousePosition() {
                        return { x: this.mouse.x, y: this.mouse.y };
                    }
                    
                    isMouseClicked() {
                        return this.mouse.clicked;
                    }
                }
            '''
        }
        
        # HTML template components
        self.html_components = {
            'game_header': '''
                <div class="game-header" style="{header_style}">
                    <h1>{game_title}</h1>
                    <p class="game-description">{game_description}</p>
                </div>
            ''',
            
            'game_canvas': '''
                <canvas id="{canvas_id}" width="{width}" height="{height}" style="{canvas_style}">
                    Your browser does not support the HTML5 canvas element.
                </canvas>
            ''',
            
            'game_controls': '''
                <div class="game-controls" style="{controls_style}">
                    <div class="control-instructions">
                        <h3>Controls:</h3>
                        <p>{control_instructions}</p>
                    </div>
                    <div class="game-stats">
                        {game_stats}
                    </div>
                </div>
            ''',
            
            'game_ui': '''
                <div class="game-ui" style="{ui_style}">
                    <div class="ui-left">
                        {left_ui_elements}
                    </div>
                    <div class="ui-center">
                        {center_ui_elements}
                    </div>
                    <div class="ui-right">
                        {right_ui_elements}
                    </div>
                </div>
            ''',
            
            'modal_dialog': '''
                <div id="gameModal" class="modal" style="display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.8);">
                    <div class="modal-content" style="background-color: #fefefe; margin: 15% auto; padding: 20px; border: 1px solid #888; width: 300px; border-radius: 10px; text-align: center;">
                        <span class="close" style="color: #aaa; float: right; font-size: 28px; font-weight: bold; cursor: pointer;">&times;</span>
                        <div id="modalContent">
                            {modal_content}
                        </div>
                    </div>
                </div>
            '''
        }
        
        # Game state management templates
        self.state_management = {
            'game_state': '''
                class GameState {
                    constructor() {
                        this.currentState = 'menu';
                        this.states = {
                            menu: new MenuState(),
                            playing: new PlayingState(),
                            paused: new PausedState(),
                            gameOver: new GameOverState()
                        };
                    }
                    
                    update(deltaTime) {
                        this.states[this.currentState].update(deltaTime);
                    }
                    
                    render(ctx) {
                        this.states[this.currentState].render(ctx);
                    }
                    
                    changeState(newState) {
                        this.states[this.currentState].exit();
                        this.currentState = newState;
                        this.states[this.currentState].enter();
                    }
                    
                    handleInput(input) {
                        this.states[this.currentState].handleInput(input);
                    }
                }
            ''',
            
            'save_system': '''
                class SaveSystem {
                    constructor() {
                        this.saveKey = 'mythiq_game_save';
                    }
                    
                    saveGame(gameData) {
                        try {
                            const saveData = {
                                ...gameData,
                                timestamp: Date.now(),
                                version: '1.0'
                            };
                            localStorage.setItem(this.saveKey, JSON.stringify(saveData));
                            return true;
                        } catch (error) {
                            console.error('Failed to save game:', error);
                            return false;
                        }
                    }
                    
                    loadGame() {
                        try {
                            const saveData = localStorage.getItem(this.saveKey);
                            if (saveData) {
                                return JSON.parse(saveData);
                            }
                            return null;
                        } catch (error) {
                            console.error('Failed to load game:', error);
                            return null;
                        }
                    }
                    
                    deleteSave() {
                        localStorage.removeItem(this.saveKey);
                    }
                    
                    hasSave() {
                        return localStorage.getItem(this.saveKey) !== null;
                    }
                }
            '''
        }
    
    def generate_complete_html(self, game_config):
        """
        Generate complete HTML for a customized game
        """
        try:
            theme = game_config.get('theme', 'adventure')
            title = game_config.get('title', 'Custom Game')
            description = game_config.get('description', 'A custom game experience')
            
            # Get theme styles
            styles = self.css_templates.get(theme, self.css_templates['forest'])
            
            # Build the complete HTML
            html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            {styles['body_style']}
            margin: 0;
            padding: 20px;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        
        .game-container {{
            max-width: 1000px;
            width: 100%;
            text-align: center;
        }}
        
        .game-header {{
            margin-bottom: 20px;
        }}
        
        .game-header h1 {{
            font-size: 2.5em;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }}
        
        .game-description {{
            font-size: 1.2em;
            margin: 10px 0;
            opacity: 0.9;
        }}
        
        #gameCanvas {{
            {styles['canvas_style']}
            display: block;
            margin: 20px auto;
        }}
        
        .game-controls {{
            {styles['ui_style']}
            padding: 15px;
            margin: 20px auto;
            max-width: 800px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
        }}
        
        .control-instructions {{
            flex: 1;
            text-align: left;
            min-width: 300px;
        }}
        
        .game-stats {{
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }}
        
        .stat-item {{
            {styles['ui_style']}
            padding: 8px 12px;
            border-radius: 5px;
            font-weight: bold;
            min-width: 80px;
        }}
        
        .game-button {{
            {styles['button_style']}
            margin: 5px;
            transition: transform 0.2s;
        }}
        
        .game-button:hover {{
            transform: scale(1.05);
        }}
        
        .modal {{
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.8);
        }}
        
        .modal-content {{
            background-color: #fefefe;
            margin: 15% auto;
            padding: 20px;
            border: 1px solid #888;
            width: 300px;
            border-radius: 10px;
            text-align: center;
            color: #333;
        }}
        
        .close {{
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
        }}
        
        .close:hover {{
            color: #000;
        }}
        
        @media (max-width: 768px) {{
            body {{ padding: 10px; }}
            .game-header h1 {{ font-size: 2em; }}
            .game-controls {{ flex-direction: column; gap: 15px; }}
            .control-instructions {{ text-align: center; }}
        }}
    </style>
</head>
<body>
    <div class="game-container">
        <div class="game-header">
            <h1>{title}</h1>
            <p class="game-description">{description}</p>
        </div>
        
        <canvas id="gameCanvas" width="{game_config.get('canvas_width', 800)}" height="{game_config.get('canvas_height', 600)}">
            Your browser does not support the HTML5 canvas element.
        </canvas>
        
        <div class="game-controls">
            <div class="control-instructions">
                <h3>How to Play:</h3>
                <p>{game_config.get('instructions', 'Use controls to play the game!')}</p>
                <p><strong>Objective:</strong> {game_config.get('objective', 'Complete the challenge!')}</p>
            </div>
            <div class="game-stats">
                {self._generate_stat_elements(game_config)}
            </div>
        </div>
        
        <div class="game-actions">
            <button class="game-button" onclick="startGame()">Start Game</button>
            <button class="game-button" onclick="pauseGame()">Pause</button>
            <button class="game-button" onclick="resetGame()">Reset</button>
            <button class="game-button" onclick="showHelp()">Help</button>
        </div>
    </div>
    
    <!-- Modal for dialogs -->
    <div id="gameModal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="closeModal()">&times;</span>
            <div id="modalContent"></div>
        </div>
    </div>
    
    <script>
        // Game initialization
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        
        // Game configuration
        const GAME_CONFIG = {json.dumps(game_config, indent=8)};
        
        // Game variables
        let gameRunning = false;
        let gamePaused = false;
        let gameStartTime = Date.now();
        let lastFrameTime = 0;
        
        // Include utility functions
        {self.js_snippets['particle_system']}
        {self.js_snippets['sound_effects']}
        {self.js_snippets['collision_detection']}
        {self.js_snippets['animation_system']}
        {self.js_snippets['input_handler']}
        
        // Initialize input handler
        const input = new InputHandler();
        
        // Game state management
        {self.state_management['game_state']}
        {self.state_management['save_system']}
        
        // Initialize save system
        const saveSystem = new SaveSystem();
        
        // Main game functions
        function startGame() {{
            if (!gameRunning) {{
                gameRunning = true;
                gamePaused = false;
                gameStartTime = Date.now();
                showMessage('Game Started!', 'success');
                gameLoop();
            }}
        }}
        
        function pauseGame() {{
            gamePaused = !gamePaused;
            showMessage(gamePaused ? 'Game Paused' : 'Game Resumed', 'info');
        }}
        
        function resetGame() {{
            gameRunning = false;
            gamePaused = false;
            // Reset game state here
            showMessage('Game Reset!', 'info');
            initializeGame();
        }}
        
        function showHelp() {{
            const helpContent = `
                <h3>Game Help</h3>
                <p><strong>Controls:</strong> {game_config.get('instructions', 'Use controls to play!')}</p>
                <p><strong>Objective:</strong> {game_config.get('objective', 'Complete the challenge!')}</p>
                <p><strong>Tips:</strong> Practice makes perfect!</p>
                <button class="game-button" onclick="closeModal()">Got it!</button>
            `;
            showModal(helpContent);
        }}
        
        function showMessage(message, type = 'info') {{
            console.log(`[{title}] ${{message}}`);
            // You can add visual message display here
        }}
        
        function showModal(content) {{
            document.getElementById('modalContent').innerHTML = content;
            document.getElementById('gameModal').style.display = 'block';
        }}
        
        function closeModal() {{
            document.getElementById('gameModal').style.display = 'none';
        }}
        
        function initializeGame() {{
            // Game-specific initialization
            console.log('🎮 {title} - Powered by Mythiq Game AI');
            console.log('Theme: {theme}');
            console.log('Ready to play!');
        }}
        
        function gameLoop(currentTime = 0) {{
            if (!gameRunning || gamePaused) {{
                if (gameRunning) {{
                    requestAnimationFrame(gameLoop);
                }}
                return;
            }}
            
            const deltaTime = currentTime - lastFrameTime;
            lastFrameTime = currentTime;
            
            // Clear canvas
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Update game logic
            updateGame(deltaTime);
            
            // Render game
            renderGame(ctx);
            
            // Continue loop
            requestAnimationFrame(gameLoop);
        }}
        
        function updateGame(deltaTime) {{
            // Game-specific update logic will be inserted here
            updateParticles();
        }}
        
        function renderGame(ctx) {{
            // Game-specific rendering logic will be inserted here
            drawParticles();
            
            // Draw UI
            drawUI(ctx);
        }}
        
        function drawUI(ctx) {{
            // Draw game time
            const gameTime = Math.floor((Date.now() - gameStartTime) / 1000);
            ctx.fillStyle = 'white';
            ctx.font = '16px Arial';
            ctx.fillText(`Time: ${{gameTime}}s`, 10, 25);
        }}
        
        // Initialize particles array
        let particles = [];
        
        // Initialize the game
        initializeGame();
        
        // Auto-save functionality
        setInterval(() => {{
            if (gameRunning) {{
                const gameData = {{
                    // Add game state data here
                    time: Date.now() - gameStartTime,
                    theme: GAME_CONFIG.theme
                }};
                saveSystem.saveGame(gameData);
            }}
        }}, 30000); // Save every 30 seconds
        
        // Load saved game on startup
        window.addEventListener('load', () => {{
            const savedGame = saveSystem.loadGame();
            if (savedGame) {{
                console.log('Saved game found:', savedGame);
                // Load saved state here
            }}
        }});
        
        console.log('🎮 {title} - Fully Loaded and Ready!');
        console.log('🤖 Powered by Mythiq Game AI');
        console.log('🎨 Theme: {theme}');
        console.log('⚡ All systems operational!');
    </script>
</body>
</html>
            '''
            
            self.templates_loaded += 1
            return html
            
        except Exception as e:
            return self._generate_fallback_html(game_config, str(e))
    
    def _generate_stat_elements(self, game_config):
        """Generate HTML for game statistics display"""
        genre = game_config.get('genre', 'platformer')
        
        if genre == 'platformer':
            return '''
                <div class="stat-item">Score: <span id="score">0</span></div>
                <div class="stat-item">Lives: <span id="lives">3</span></div>
                <div class="stat-item">Level: <span id="level">1</span></div>
            '''
        elif genre == 'puzzle':
            return '''
                <div class="stat-item">Score: <span id="puzzleScore">0</span></div>
                <div class="stat-item">Moves: <span id="moves">30</span></div>
                <div class="stat-item">Level: <span id="puzzleLevel">1</span></div>
            '''
        elif genre == 'rpg':
            return '''
                <div class="stat-item">HP: <span id="hp">100</span></div>
                <div class="stat-item">MP: <span id="mp">50</span></div>
                <div class="stat-item">Gold: <span id="gold">0</span></div>
                <div class="stat-item">Level: <span id="rpgLevel">1</span></div>
            '''
        else:
            return '''
                <div class="stat-item">Score: <span id="gameScore">0</span></div>
                <div class="stat-item">Time: <span id="gameTime">0:00</span></div>
            '''
    
    def _generate_fallback_html(self, game_config, error):
        """Generate fallback HTML if template generation fails"""
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Game Template Error</title>
            <style>
                body {{ font-family: Arial; text-align: center; margin: 50px; }}
                .error {{ color: #ff4444; background: #ffe6e6; padding: 20px; border-radius: 10px; }}
            </style>
        </head>
        <body>
            <h2>Game Template Generation Error</h2>
            <div class="error">
                <p>Error: {error}</p>
                <p>Game Config: {json.dumps(game_config, indent=2)}</p>
            </div>
            <p>Please check the game configuration and try again.</p>
        </body>
        </html>
        '''
    
    def get_css_for_theme(self, theme):
        """Get CSS styles for a specific theme"""
        return self.css_templates.get(theme, self.css_templates['forest'])
    
    def get_js_snippet(self, snippet_name):
        """Get JavaScript code snippet by name"""
        return self.js_snippets.get(snippet_name, '')
    
    def get_html_component(self, component_name):
        """Get HTML component template by name"""
        return self.html_components.get(component_name, '')
    
    def list_available_themes(self):
        """List all available themes"""
        return list(self.css_templates.keys())
    
    def list_available_snippets(self):
        """List all available JavaScript snippets"""
        return list(self.js_snippets.keys())
    
    def health_check(self):
        """Health check for template manager"""
        return {
            'status': 'healthy',
            'templates_loaded': self.templates_loaded,
            'assets_managed': self.assets_managed,
            'available_themes': len(self.css_templates),
            'available_snippets': len(self.js_snippets),
            'available_components': len(self.html_components)
        }

print("🎨 Game Template Manager Loaded:")
print(f"  {len(GameTemplateManager().css_templates)} CSS theme templates")
print(f"  {len(GameTemplateManager().js_snippets)} JavaScript code snippets")
print(f"  {len(GameTemplateManager().html_components)} HTML components")
print("✅ Ready to generate complete game templates!")
