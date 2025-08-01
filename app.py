"""
Mythiq Game Maker - AI-Powered Game Generation
Railway-optimized Flask server with unique Game AI
"""

from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import logging
import os
import json
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Try to import game AI components with fallback
try:
    from game_ai import GameAI
    from base_games import BASE_GAMES
    from customization_engine import CustomizationEngine
    from game_templates import GameTemplateManager
    
    # Initialize Game AI system
    game_ai = GameAI()
    customization_engine = CustomizationEngine()
    template_manager = GameTemplateManager()
    
    AI_SYSTEM_LOADED = True
    logger.info("Full Game AI system loaded successfully!")
    
except ImportError as e:
    logger.warning(f"Game AI components not found: {e}")
    logger.info("Using fallback simple game generator")
    AI_SYSTEM_LOADED = False
    
    # Simple fallback game generator
    class SimpleGameGenerator:
        def __init__(self):
            self.game_count = 0
            
        def generate_game(self, prompt, user_id=None):
            self.game_count += 1
            
            # Simple game generation based on keywords
            prompt_lower = prompt.lower()
            
            if any(word in prompt_lower for word in ["platformer", "jump", "run", "escape"]):
                return self._generate_simple_platformer(prompt)
            elif any(word in prompt_lower for word in ["puzzle", "match", "brain", "solve"]):
                return self._generate_simple_puzzle(prompt)
            elif any(word in prompt_lower for word in ["rpg", "quest", "adventure", "character"]):
                return self._generate_simple_rpg(prompt)
            else:
                return self._generate_default_game(prompt)
        
        def _generate_simple_platformer(self, prompt):
            return {
                'game_type': 'platformer',
                'title': f'Custom Platformer Game',
                'description': f'A platformer game based on: "{prompt}"',
                'html_content': self._create_simple_platformer_html(prompt),
                'play_url': f'/play/platformer_{self.game_count}',
                'generation_time': '2 seconds',
                'ai_analysis': {
                    'detected_genre': 'platformer',
                    'theme': 'adventure',
                    'difficulty': 'medium'
                }
            }
        
        def _generate_simple_puzzle(self, prompt):
            return {
                'game_type': 'puzzle',
                'title': f'Custom Puzzle Game',
                'description': f'A puzzle game based on: "{prompt}"',
                'html_content': self._create_simple_puzzle_html(prompt),
                'play_url': f'/play/puzzle_{self.game_count}',
                'generation_time': '2 seconds',
                'ai_analysis': {
                    'detected_genre': 'puzzle',
                    'theme': 'logic',
                    'difficulty': 'medium'
                }
            }
        
        def _create_simple_platformer_html(self, prompt):
            return f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Custom Platformer - {prompt[:30]}</title>
                <style>
                    canvas {{ border: 2px solid #4a4a4a; background: linear-gradient(to bottom, #87CEEB, #228B22); }}
                    .game-container {{ text-align: center; margin: 20px; }}
                    .controls {{ margin: 10px; font-family: Arial; }}
                </style>
            </head>
            <body>
                <div class="game-container">
                    <h2>Custom Platformer Game</h2>
                    <p>Inspired by: "{prompt}"</p>
                    <canvas id="gameCanvas" width="800" height="400"></canvas>
                    <div class="controls">
                        <p>Use ARROW KEYS to move and jump! Collect coins!</p>
                        <p>Score: <span id="score">0</span> | Lives: <span id="lives">3</span></p>
                    </div>
                </div>
                
                <script>
                    const canvas = document.getElementById('gameCanvas');
                    const ctx = canvas.getContext('2d');
                    
                    let player = {{ x: 50, y: 300, width: 30, height: 30, velocityY: 0, onGround: false }};
                    let score = 0;
                    let lives = 3;
                    let coins = [];
                    let keys = {{}};
                    
                    function drawPlayer() {{
                        ctx.fillStyle = '#FF6B6B';
                        ctx.fillRect(player.x, player.y, player.width, player.height);
                    }}
                    
                    function drawCoins() {{
                        ctx.fillStyle = '#FFD700';
                        coins.forEach(coin => {{
                            ctx.beginPath();
                            ctx.arc(coin.x, coin.y, 10, 0, Math.PI * 2);
                            ctx.fill();
                        }});
                    }}
                    
                    function updateGame() {{
                        if (keys['ArrowLeft'] && player.x > 0) player.x -= 5;
                        if (keys['ArrowRight'] && player.x < canvas.width - player.width) player.x += 5;
                        if (keys['ArrowUp'] && player.onGround) {{
                            player.velocityY = -15;
                            player.onGround = false;
                        }}
                        
                        player.velocityY += 0.8;
                        player.y += player.velocityY;
                        
                        if (player.y > 300) {{
                            player.y = 300;
                            player.velocityY = 0;
                            player.onGround = true;
                        }}
                        
                        coins = coins.filter(coin => {{
                            if (Math.abs(player.x - coin.x) < 20 && Math.abs(player.y - coin.y) < 20) {{
                                score += 10;
                                document.getElementById('score').textContent = score;
                                return false;
                            }}
                            return true;
                        }});
                        
                        if (Math.random() < 0.02) {{
                            coins.push({{ x: canvas.width, y: Math.random() * 200 + 100 }});
                        }}
                        
                        coins.forEach(coin => coin.x -= 3);
                        coins = coins.filter(coin => coin.x > -20);
                    }}
                    
                    function gameLoop() {{
                        ctx.clearRect(0, 0, canvas.width, canvas.height);
                        updateGame();
                        drawPlayer();
                        drawCoins();
                        requestAnimationFrame(gameLoop);
                    }}
                    
                    document.addEventListener('keydown', (e) => keys[e.code] = true);
                    document.addEventListener('keyup', (e) => keys[e.code] = false);
                    
                    gameLoop();
                </script>
            </body>
            </html>
            """
        
        def _create_simple_puzzle_html(self, prompt):
            return f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Custom Puzzle - {prompt[:30]}</title>
                <style>
                    canvas {{ border: 2px solid #4a4a4a; background: #1a1a2e; }}
                    .game-container {{ text-align: center; margin: 20px; }}
                    .controls {{ margin: 10px; font-family: Arial; color: #fff; }}
                </style>
            </head>
            <body style="background: #0f0f23;">
                <div class="game-container">
                    <h2 style="color: #fff;">Custom Puzzle Game</h2>
                    <p style="color: #fff;">Inspired by: "{prompt}"</p>
                    <canvas id="puzzleCanvas" width="400" height="500"></canvas>
                    <div class="controls">
                        <p>Click to match colors!</p>
                        <p>Score: <span id="puzzleScore">0</span> | Moves: <span id="moves">30</span></p>
                    </div>
                </div>
                
                <script>
                    const canvas = document.getElementById('puzzleCanvas');
                    const ctx = canvas.getContext('2d');
                    
                    const GRID_SIZE = 8;
                    const CELL_SIZE = 45;
                    const COLORS = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD'];
                    
                    let grid = [];
                    let score = 0;
                    let moves = 30;
                    
                    function initGrid() {{
                        for (let row = 0; row < GRID_SIZE; row++) {{
                            grid[row] = [];
                            for (let col = 0; col < GRID_SIZE; col++) {{
                                grid[row][col] = Math.floor(Math.random() * COLORS.length);
                            }}
                        }}
                    }}
                    
                    function drawGrid() {{
                        ctx.clearRect(0, 0, canvas.width, canvas.height);
                        for (let row = 0; row < GRID_SIZE; row++) {{
                            for (let col = 0; col < GRID_SIZE; col++) {{
                                const x = col * CELL_SIZE + 10;
                                const y = row * CELL_SIZE + 10;
                                
                                ctx.fillStyle = COLORS[grid[row][col]];
                                ctx.fillRect(x, y, CELL_SIZE - 2, CELL_SIZE - 2);
                            }}
                        }}
                    }}
                    
                    canvas.addEventListener('click', (e) => {{
                        const rect = canvas.getBoundingClientRect();
                        const x = e.clientX - rect.left;
                        const y = e.clientY - rect.top;
                        
                        const col = Math.floor((x - 10) / CELL_SIZE);
                        const row = Math.floor((y - 10) / CELL_SIZE);
                        
                        if (row >= 0 && row < GRID_SIZE && col >= 0 && col < GRID_SIZE) {{
                            grid[row][col] = (grid[row][col] + 1) % COLORS.length;
                            score += 5;
                            moves--;
                            document.getElementById('puzzleScore').textContent = score;
                            document.getElementById('moves').textContent = moves;
                            drawGrid();
                        }}
                    }});
                    
                    initGrid();
                    drawGrid();
                </script>
            </body>
            </html>
            """
        
        def _generate_default_game(self, prompt):
            return {
                'game_type': 'adventure',
                'title': f'Custom Adventure Game',
                'description': f'An adventure game based on: "{prompt}"',
                'html_content': self._create_simple_platformer_html(prompt),
                'play_url': f'/play/adventure_{self.game_count}',
                'generation_time': '2 seconds',
                'ai_analysis': {
                    'detected_genre': 'adventure',
                    'theme': 'exploration',
                    'difficulty': 'medium'
                }
            }
        
        def health_check(self):
            return {
                'status': 'healthy',
                'system_type': 'simple_fallback',
                'games_generated': self.game_count,
                'note': 'Upload full Game AI files for advanced features'
            }
    
    # Initialize fallback system
    game_ai = SimpleGameGenerator()

# Store generated games
generated_games = {}

@app.route('/')
def home():
    """API information endpoint"""
    return jsonify({
        "message": "Mythiq Game Maker API - AI-Powered Game Generation",
        "version": "2.0.0",
        "system_type": "full_ai" if AI_SYSTEM_LOADED else "simple_fallback",
        "status": "running",
        "endpoints": {
            "generate": "/api/generate (POST)",
            "play": "/play/<game_id>",
            "health": "/health",
            "games": "/api/games"
        },
        "capabilities": {
            "ai_game_generation": True,
            "multiple_genres": True,
            "instant_playable_games": True,
            "customization_engine": AI_SYSTEM_LOADED,
            "base_game_library": AI_SYSTEM_LOADED
        },
        "note": "Upload full Game AI files for advanced features" if not AI_SYSTEM_LOADED else "Full Game AI system active!"
    })

@app.route('/api/generate', methods=['POST'])
def generate_game():
    """Generate a custom game based on user prompt"""
    try:
        data = request.get_json()
        
        if not data or 'prompt' not in data:
            return jsonify({
                'error': 'Prompt is required',
                'status': 'error'
            }), 400
        
        prompt = data.get('prompt', '').strip()
        user_id = data.get('user_id', 'default')
        
        if not prompt:
            return jsonify({
                'error': 'Prompt cannot be empty',
                'status': 'error'
            }), 400
        
        logger.info(f"Generating game for user {user_id}: {prompt[:50]}...")
        
        # Generate game using AI system
        start_time = datetime.now()
        game_result = game_ai.generate_game(prompt, user_id)
        generation_time = (datetime.now() - start_time).total_seconds()
        
        # Store the generated game
        game_id = f"game_{len(generated_games) + 1}_{int(datetime.now().timestamp())}"
        generated_games[game_id] = {
            'game_data': game_result,
            'prompt': prompt,
            'user_id': user_id,
            'created_at': datetime.now().isoformat(),
            'generation_time': generation_time
        }
        
        logger.info(f"Game generated successfully: {game_result['game_type']} in {generation_time:.2f}s")
        
        return jsonify({
            'game_id': game_id,
            'game_type': game_result['game_type'],
            'title': game_result['title'],
            'description': game_result['description'],
            'play_url': f'/play/{game_id}',
            'generation_time': f'{generation_time:.2f} seconds',
            'ai_analysis': game_result.get('ai_analysis', {}),
            'system_type': 'full_ai' if AI_SYSTEM_LOADED else 'simple_fallback',
            'status': 'success'
        })
        
    except Exception as e:
        logger.error(f"Error generating game: {e}")
        return jsonify({
            'error': 'Game generation failed',
            'message': str(e),
            'status': 'error'
        }), 500

@app.route('/play/<game_id>')
def play_game(game_id):
    """Serve the generated game for playing"""
    try:
        if game_id not in generated_games:
            return jsonify({
                'error': 'Game not found',
                'message': 'The requested game does not exist or has expired',
                'status': 'error'
            }), 404
        
        game_data = generated_games[game_id]['game_data']
        return game_data['html_content'], 200, {'Content-Type': 'text/html'}
        
    except Exception as e:
        logger.error(f"Error serving game {game_id}: {e}")
        return jsonify({
            'error': 'Failed to load game',
            'message': str(e),
            'status': 'error'
        }), 500

@app.route('/api/games')
def list_games():
    """List all generated games"""
    try:
        games_list = []
        for game_id, game_info in generated_games.items():
            games_list.append({
                'game_id': game_id,
                'title': game_info['game_data']['title'],
                'game_type': game_info['game_data']['game_type'],
                'prompt': game_info['prompt'],
                'created_at': game_info['created_at'],
                'play_url': f'/play/{game_id}'
            })
        
        return jsonify({
            'games': games_list,
            'total_games': len(games_list),
            'system_type': 'full_ai' if AI_SYSTEM_LOADED else 'simple_fallback',
            'status': 'success'
        })
        
    except Exception as e:
        logger.error(f"Error listing games: {e}")
        return jsonify({
            'error': 'Failed to list games',
            'message': str(e),
            'status': 'error'
        }), 500

@app.route('/health')
def health():
    """Health check endpoint for Railway"""
    try:
        health_status = game_ai.health_check()
        health_status.update({
            'service': 'mythiq-game-maker',
            'system_loaded': AI_SYSTEM_LOADED,
            'generated_games': len(generated_games),
            'timestamp': datetime.now().isoformat()
        })
        return jsonify(health_status)
    except Exception as e:
        logger.error(f"Health check error: {e}")
        return jsonify({
            'status': 'unhealthy',
            'service': 'mythiq-game-maker',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found',
        'message': 'The requested endpoint does not exist',
        'available_endpoints': [
            '/',
            '/api/generate',
            '/play/<game_id>',
            '/api/games',
            '/health'
        ],
        'status': 'error'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {error}")
    return jsonify({
        'error': 'Internal server error',
        'message': 'Something went wrong on our end',
        'status': 'error'
    }), 500

if __name__ == '__main__':
    # Get port from environment (Railway sets this)
    port = int(os.environ.get('PORT', 5002))
    
    logger.info(f"Starting Mythiq Game Maker on port {port}")
    logger.info(f"System type: {'Full AI' if AI_SYSTEM_LOADED else 'Simple Fallback'}")
    logger.info("Game generation: AI-powered custom games from user prompts")
    logger.info("Deployment: Railway-optimized, Professional-grade")
    
    # Run the app
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False  # Set to False for production
    )

