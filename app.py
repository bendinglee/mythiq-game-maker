"""
🔥 FIXED REVOLUTIONARY ULTIMATE GAME MAKER BACKEND
Complete backend with proper error handling and Flask routes
"""

from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import random
import time
import json
from datetime import datetime
import re
import traceback

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
    'prompt_accuracy_rate': 0.0,
    'user_satisfaction_rate': 0.0,
    'average_generation_time': 0.0,
    'unique_games_generated': 0,
    'complex_prompts_handled': 0,
    'randomization_success_rate': 0.0
}

# Game generation history for uniqueness tracking
generation_history = []

def log_generation(prompt, game_type, generation_method, success=True):
    """Log game generation for statistics and uniqueness tracking"""
    global stats
    
    stats['total_games_generated'] += 1
    
    if generation_method == 'ultimate':
        stats['ultimate_games'] += 1
    elif generation_method == 'free_ai':
        stats['free_ai_games'] += 1
    elif generation_method == 'enhanced':
        stats['enhanced_games'] += 1
    else:
        stats['basic_games'] += 1

@app.route('/')
def index():
    """Root endpoint - FIXES THE 404 ISSUE"""
    try:
        return jsonify({
            'message': 'Fixed Revolutionary Ultimate Game Maker API is running!',
            'status': 'healthy',
            'service': 'Revolutionary Game Maker with Advanced Prompt Processing',
            'version': '6.0.0 - FIXED REVOLUTIONARY VERSION',
            'revolutionary_available': REVOLUTIONARY_AVAILABLE,
            'free_ai_available': FREE_AI_AVAILABLE,
            'endpoints': {
                'health': '/health',
                'generate_game': '/generate-game',
                'ai_generate_game': '/ai-generate-game',
                'ultimate_generate_game': '/ultimate-generate-game',
                'generation_stats': '/generation-stats',
                'ai_status': '/ai-status'
            },
            'revolutionary_features': {
                'advanced_prompt_processing': REVOLUTIONARY_AVAILABLE,
                'true_randomization': REVOLUTIONARY_AVAILABLE,
                'expanded_templates': REVOLUTIONARY_AVAILABLE,
                'complex_prompt_handling': REVOLUTIONARY_AVAILABLE
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
            'message': 'Fixed Revolutionary Ultimate Game Maker is operational',
            'revolutionary_available': REVOLUTIONARY_AVAILABLE,
            'free_ai_available': FREE_AI_AVAILABLE,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'error': 'Health check failed',
            'details': str(e)
        }), 500

@app.route('/ultimate-generate-game', methods=['POST'])
def ultimate_generate_game():
    """Ultimate game generation with revolutionary prompt processing"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        prompt = data.get('prompt', '').strip()
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        print(f"🎯 Ultimate generation request: {prompt}")
        
        if REVOLUTIONARY_AVAILABLE:
            # Use revolutionary system
            try:
                # Process prompt with revolutionary processor
                analysis = prompt_processor.analyze_prompt(prompt)
                print(f"🧠 Prompt analysis: {analysis}")
                
                # Generate unique variation
                variation = randomization_engine.generate_variation(analysis['theme'], prompt)
                print(f"🎲 Generated variation: {variation.title}")
                
                # Get appropriate template
                template = template_library.get_template(analysis['theme'], variation)
                print(f"🎮 Selected template: {analysis['theme']}")
                
                # Generate the game
                game_html = template['html']
                
                # Log successful generation
                log_generation(prompt, analysis['theme'], 'ultimate', True)
                
                return jsonify({
                    'success': True,
                    'game': {
                        'title': variation.title,
                        'type': analysis['theme'].title(),
                        'character': variation.character,
                        'theme': analysis['theme'],
                        'html': game_html,
                        'features': variation.special_features,
                        'difficulty': variation.difficulty,
                        'ui_elements': variation.ui_elements,
                        'color_scheme': variation.color_scheme
                    },
                    'analysis': analysis,
                    'generation_method': 'revolutionary_ultimate',
                    'timestamp': datetime.now().isoformat()
                })
                
            except Exception as e:
                print(f"❌ Revolutionary generation failed: {e}")
                # Fall back to simple generation
                return generate_simple_game(prompt, 'ultimate_fallback')
        else:
            # Fall back to simple generation
            return generate_simple_game(prompt, 'ultimate_no_revolutionary')
            
    except Exception as e:
        print(f"❌ Ultimate generation error: {e}")
        return jsonify({
            'error': 'Ultimate generation failed',
            'details': str(e),
            'traceback': traceback.format_exc()
        }), 500

@app.route('/generate-game', methods=['POST'])
def generate_game():
    """Enhanced game generation endpoint"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        prompt = data.get('prompt', '').strip()
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        print(f"🎯 Enhanced generation request: {prompt}")
        
        # Try revolutionary system first, then fall back
        if REVOLUTIONARY_AVAILABLE:
            try:
                return ultimate_generate_game()
            except:
                pass
        
        # Fall back to simple generation
        return generate_simple_game(prompt, 'enhanced')
        
    except Exception as e:
        print(f"❌ Enhanced generation error: {e}")
        return jsonify({
            'error': 'Enhanced generation failed',
            'details': str(e)
        }), 500

@app.route('/ai-generate-game', methods=['POST'])
def ai_generate_game():
    """FREE AI game generation endpoint"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        prompt = data.get('prompt', '').strip()
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        print(f"🤖 FREE AI generation request: {prompt}")
        
        if FREE_AI_AVAILABLE:
            try:
                # Use FREE AI system
                game_concept = free_ai_engine.generate_concept(prompt)
                game_html = free_ai_generator.generate_game(game_concept)
                
                log_generation(prompt, game_concept.get('type', 'ai'), 'free_ai', True)
                
                return jsonify({
                    'success': True,
                    'game': {
                        'title': game_concept.get('title', 'AI Generated Game'),
                        'type': game_concept.get('type', 'AI Adventure'),
                        'html': game_html,
                        'features': game_concept.get('features', []),
                        'theme': game_concept.get('theme', 'ai_generated')
                    },
                    'generation_method': 'free_ai',
                    'timestamp': datetime.now().isoformat()
                })
            except Exception as e:
                print(f"❌ FREE AI generation failed: {e}")
                # Fall back to revolutionary system
                if REVOLUTIONARY_AVAILABLE:
                    return ultimate_generate_game()
                else:
                    return generate_simple_game(prompt, 'free_ai_fallback')
        else:
            # Fall back to revolutionary system
            if REVOLUTIONARY_AVAILABLE:
                return ultimate_generate_game()
            else:
                return generate_simple_game(prompt, 'free_ai_no_ai')
                
    except Exception as e:
        print(f"❌ FREE AI generation error: {e}")
        return jsonify({
            'error': 'FREE AI generation failed',
            'details': str(e)
        }), 500

def generate_simple_game(prompt, method):
    """Simple fallback game generation"""
    try:
        # Simple keyword detection
        prompt_lower = prompt.lower()
        
        if 'dart' in prompt_lower:
            game_type = 'Darts'
            title = 'Dart Master'
            character = 'Dart Player'
        elif 'basketball' in prompt_lower:
            game_type = 'Basketball'
            title = 'Hoop Dreams'
            character = 'Basketball Player'
        elif 'underwater' in prompt_lower or 'mermaid' in prompt_lower:
            game_type = 'Underwater Adventure'
            title = 'Deep Sea Explorer'
            character = 'Mermaid'
        elif 'medieval' in prompt_lower or 'knight' in prompt_lower:
            game_type = 'Medieval Adventure'
            title = 'Castle Defense'
            character = 'Knight'
        elif 'racing' in prompt_lower or 'car' in prompt_lower:
            game_type = 'Racing'
            title = 'Speed Racer'
            character = 'Race Driver'
        else:
            game_type = 'Adventure'
            title = 'Epic Quest'
            character = 'Hero'
        
        # Simple HTML game template
        game_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{title}</title>
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; background: #1a1a2e; color: white; }}
                .game-container {{ max-width: 800px; margin: 0 auto; padding: 20px; }}
                .character {{ font-size: 50px; margin: 20px; }}
                .controls {{ margin: 20px; }}
                button {{ padding: 10px 20px; font-size: 16px; margin: 5px; }}
            </style>
        </head>
        <body>
            <div class="game-container">
                <h1>{title}</h1>
                <p>A {game_type.lower()} game generated from: "{prompt}"</p>
                <div class="character">🎮</div>
                <div class="controls">
                    <button onclick="alert('Game started!')">Start Game</button>
                    <button onclick="alert('Score: ' + Math.floor(Math.random() * 1000))">Check Score</button>
                </div>
                <p>Character: {character}</p>
                <p>Generated using: {method}</p>
            </div>
        </body>
        </html>
        """
        
        log_generation(prompt, game_type.lower(), method, True)
        
        return jsonify({
            'success': True,
            'game': {
                'title': title,
                'type': game_type,
                'character': character,
                'html': game_html,
                'theme': game_type.lower().replace(' ', '_')
            },
            'generation_method': method,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Simple generation failed',
            'details': str(e)
        }), 500

@app.route('/generation-stats')
def generation_stats():
    """Get generation statistics"""
    try:
        return jsonify({
            'stats': stats,
            'total_requests': stats['total_games_generated'],
            'revolutionary_available': REVOLUTIONARY_AVAILABLE,
            'free_ai_available': FREE_AI_AVAILABLE,
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
            'components': {
                'prompt_processor': REVOLUTIONARY_AVAILABLE,
                'randomization_engine': REVOLUTIONARY_AVAILABLE,
                'template_library': REVOLUTIONARY_AVAILABLE,
                'free_ai_engine': FREE_AI_AVAILABLE,
                'free_ai_generator': FREE_AI_AVAILABLE
            },
            'status': 'operational' if (REVOLUTIONARY_AVAILABLE or FREE_AI_AVAILABLE) else 'limited',
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'error': 'AI status check failed',
            'details': str(e)
        }), 500

if __name__ == '__main__':
    print("🔥 Starting Fixed Revolutionary Ultimate Game Maker Backend...")
    print(f"🧠 Revolutionary System: {'✅ AVAILABLE' if REVOLUTIONARY_AVAILABLE else '❌ NOT AVAILABLE'}")
    print(f"🤖 FREE AI System: {'✅ AVAILABLE' if FREE_AI_AVAILABLE else '❌ NOT AVAILABLE'}")
    print("🌐 Server starting on port 8080")
    print("🎯 Ready to generate revolutionary games!")
    
    app.run(host='0.0.0.0', port=8080, debug=False)
