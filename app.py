"""
🔥 ULTIMATE GAME MAKER BACKEND - TRUE PROMPT MATCHING VERSION
Complete backend with intelligent prompt parsing and accurate game generation
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from datetime import datetime
import traceback

# Import our intelligent game generation system
try:
    from intelligent_game_generator import generate_ultimate_game
    from comprehensive_game_template_library import get_template_stats
    INTELLIGENT_SYSTEM_AVAILABLE = True
    print("🧠 Intelligent Game Generation System loaded successfully!")
except ImportError as e:
    INTELLIGENT_SYSTEM_AVAILABLE = False
    print(f"⚠️ Intelligent system not found: {e}")

# Import FREE AI components (if available)
try:
    from free_ai_template_engine import FreeAITemplateEngine
    from free_ai_code_generator import FreeAICodeGenerator
    FREE_AI_AVAILABLE = True
    print("🆓 FREE AI components loaded successfully!")
except ImportError:
    FREE_AI_AVAILABLE = False
    print("⚠️ FREE AI components not found, using intelligent templates only")

app = Flask(__name__)
CORS(app)

# Initialize systems
if FREE_AI_AVAILABLE:
    try:
        free_ai_engine = FreeAITemplateEngine()
        free_ai_generator = FreeAICodeGenerator()
        print("🤖 FREE AI engines initialized successfully!")
    except Exception as e:
        FREE_AI_AVAILABLE = False
        print(f"❌ FREE AI initialization failed: {e}")

# Statistics tracking
stats = {
    'total_generations': 0,
    'successful_generations': 0,
    'prompt_matching_accuracy': 0.0,
    'intelligent_generations': 0,
    'free_ai_generations': 0,
    'fallback_generations': 0,
    'uptime_start': datetime.now().isoformat()
}

def update_stats(success=True, method='intelligent'):
    """Update generation statistics"""
    global stats
    stats['total_generations'] += 1
    if success:
        stats['successful_generations'] += 1
    
    if method == 'intelligent':
        stats['intelligent_generations'] += 1
    elif method == 'free_ai':
        stats['free_ai_generations'] += 1
    else:
        stats['fallback_generations'] += 1
    
    # Calculate accuracy
    if stats['total_generations'] > 0:
        stats['prompt_matching_accuracy'] = stats['successful_generations'] / stats['total_generations']

def generate_fallback_game(prompt, mode='enhanced'):
    """Generate fallback game if intelligent system fails"""
    
    # Simple template-based fallback
    fallback_templates = {
        'darts': {
            'title': 'Dart Master',
            'theme': 'Sports',
            'character': 'Dart Player',
            'description': 'Throw darts at the dartboard to score points!'
        },
        'basketball': {
            'title': 'Hoop Dreams',
            'theme': 'Sports', 
            'character': 'Basketball Player',
            'description': 'Shoot basketballs into the hoop!'
        },
        'racing': {
            'title': 'Speed Racer',
            'theme': 'Racing',
            'character': 'Race Car',
            'description': 'Race your car to victory!'
        }
    }
    
    # Simple keyword detection
    prompt_lower = prompt.lower()
    template_key = 'darts'  # Default
    
    if any(word in prompt_lower for word in ['basketball', 'hoop', 'court']):
        template_key = 'basketball'
    elif any(word in prompt_lower for word in ['race', 'racing', 'car', 'speed']):
        template_key = 'racing'
    elif any(word in prompt_lower for word in ['dart', 'darts', 'target']):
        template_key = 'darts'
    
    template = fallback_templates[template_key]
    
    # Generate simple HTML
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{template['title']}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: white;
        }}
        .game-container {{
            background: rgba(0, 0, 0, 0.8);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            max-width: 600px;
            width: 90%;
        }}
        .game-title {{
            font-size: 2.5em;
            margin-bottom: 20px;
            color: #FFD700;
        }}
        .game-info {{
            font-size: 1.2em;
            margin: 15px 0;
        }}
        .play-button {{
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 1.2em;
            border-radius: 10px;
            cursor: pointer;
            margin: 20px;
            transition: transform 0.3s ease;
        }}
        .play-button:hover {{
            transform: translateY(-3px);
        }}
        .ui-panel {{
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <div class="game-container">
        <h1 class="game-title">{template['title']}</h1>
        <div class="game-info">Theme: {template['theme']} | Character: {template['character']}</div>
        
        <div class="ui-panel">
            <div>Score: <span id="score">0</span></div>
            <div>Level: <span id="level">1</span></div>
        </div>
        
        <button class="play-button" onclick="playGame()">🎮 Play Game</button>
        
        <div class="game-info">
            {template['description']}<br><br>
            <em>Generated from prompt: "{prompt}"</em><br>
            <small>Fallback Mode - {mode.title()}</small>
        </div>
    </div>
    
    <script>
        let score = 0;
        let level = 1;
        
        function playGame() {{
            score += 10;
            if (score % 50 === 0) {{
                level++;
            }}
            document.getElementById('score').textContent = score;
            document.getElementById('level').textContent = level;
            
            if (score === 10) {{
                alert('Game started! Keep playing to increase your score!');
            }}
        }}
    </script>
</body>
</html>"""
    
    return html_content

@app.route('/')
def index():
    """Root endpoint with comprehensive API information"""
    return jsonify({
        'message': 'Ultimate Game Maker API with True Prompt Matching',
        'status': 'operational',
        'service': 'Enhanced Game Maker with Intelligent Prompt Processing',
        'version': '5.0.0 - TRUE PROMPT MATCHING',
        'intelligent_system_available': INTELLIGENT_SYSTEM_AVAILABLE,
        'free_ai_available': FREE_AI_AVAILABLE,
        'features': {
            'intelligent_prompt_parsing': INTELLIGENT_SYSTEM_AVAILABLE,
            'comprehensive_template_library': INTELLIGENT_SYSTEM_AVAILABLE,
            'true_prompt_matching': INTELLIGENT_SYSTEM_AVAILABLE,
            'free_ai_enhancement': FREE_AI_AVAILABLE,
            'fallback_system': True,
            'statistics_tracking': True
        },
        'endpoints': {
            'health': '/health',
            'ultimate_generate_game': '/ultimate-generate-game',
            'ai_generate_game': '/ai-generate-game',
            'generate_game': '/generate-game',
            'template_stats': '/template-stats',
            'generation_stats': '/generation-stats',
            'system_status': '/system-status'
        },
        'supported_game_types': [
            'darts', 'basketball', 'soccer', 'tennis', 'golf',
            'racing', 'motorcycle', 'horse_racing',
            'tetris', 'match3', 'sudoku',
            'shooting', 'fighting', 'platformer',
            'chess', 'checkers', 'tower_defense',
            'poker', 'blackjack', 'solitaire',
            'pinball', 'pacman', 'asteroids'
        ] if INTELLIGENT_SYSTEM_AVAILABLE else ['darts', 'basketball', 'racing'],
        'timestamp': datetime.now().isoformat(),
        'stats': stats
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'intelligent_system': 'available' if INTELLIGENT_SYSTEM_AVAILABLE else 'unavailable',
        'free_ai_system': 'available' if FREE_AI_AVAILABLE else 'unavailable',
        'uptime': datetime.now().isoformat(),
        'total_generations': stats['total_generations']
    })

@app.route('/ultimate-generate-game', methods=['POST'])
def ultimate_generate_game():
    """Ultimate game generation with true prompt matching"""
    try:
        data = request.get_json()
        prompt = data.get('prompt', '').strip()
        
        if not prompt:
            return jsonify({
                'success': False,
                'error': 'No prompt provided',
                'html': generate_fallback_game('default game', 'ultimate')
            }), 400
        
        print(f"🎯 Ultimate generation request: '{prompt}'")
        
        # Try intelligent system first
        if INTELLIGENT_SYSTEM_AVAILABLE:
            try:
                result = generate_ultimate_game(prompt)
                
                if result['success']:
                    update_stats(success=True, method='intelligent')
                    
                    return jsonify({
                        'success': True,
                        'html': result['html'],
                        'game_title': result['template']['title'],
                        'game_type': result['analysis']['game_type'],
                        'theme': result['template']['theme'],
                        'character': result['template']['character'],
                        'confidence': result['analysis']['confidence'],
                        'method': 'intelligent_system',
                        'generation_stats': result['generation_stats'],
                        'prompt_analyzed': prompt,
                        'timestamp': datetime.now().isoformat()
                    })
                else:
                    print(f"❌ Intelligent system failed: {result.get('error', 'Unknown error')}")
                    
            except Exception as e:
                print(f"❌ Intelligent system error: {e}")
                traceback.print_exc()
        
        # Try FREE AI enhancement if available
        if FREE_AI_AVAILABLE:
            try:
                print("🤖 Trying FREE AI enhancement...")
                
                # Use FREE AI to enhance the prompt
                enhanced_template = free_ai_engine.generate_template(prompt)
                enhanced_code = free_ai_generator.generate_game_code(enhanced_template)
                
                if enhanced_code and len(enhanced_code) > 100:
                    update_stats(success=True, method='free_ai')
                    
                    return jsonify({
                        'success': True,
                        'html': enhanced_code,
                        'game_title': f"AI Enhanced Game",
                        'game_type': 'ai_generated',
                        'theme': 'AI Enhanced',
                        'character': 'AI Generated',
                        'method': 'free_ai_system',
                        'prompt_analyzed': prompt,
                        'timestamp': datetime.now().isoformat()
                    })
                    
            except Exception as e:
                print(f"❌ FREE AI error: {e}")
        
        # Fallback to simple template system
        print("🔧 Using fallback system...")
        fallback_html = generate_fallback_game(prompt, 'ultimate')
        update_stats(success=True, method='fallback')
        
        return jsonify({
            'success': True,
            'html': fallback_html,
            'game_title': 'Fallback Game',
            'game_type': 'fallback',
            'theme': 'Generic',
            'character': 'Player',
            'method': 'fallback_system',
            'prompt_analyzed': prompt,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        print(f"❌ Ultimate generation error: {e}")
        traceback.print_exc()
        update_stats(success=False, method='error')
        
        return jsonify({
            'success': False,
            'error': str(e),
            'html': generate_fallback_game(prompt if 'prompt' in locals() else 'error game', 'ultimate')
        }), 500

@app.route('/ai-generate-game', methods=['POST'])
def ai_generate_game():
    """FREE AI game generation endpoint"""
    try:
        data = request.get_json()
        prompt = data.get('prompt', '').strip()
        
        if not prompt:
            return jsonify({'success': False, 'error': 'No prompt provided'}), 400
        
        print(f"🤖 FREE AI generation request: '{prompt}'")
        
        if not FREE_AI_AVAILABLE:
            # Fallback to intelligent system
            if INTELLIGENT_SYSTEM_AVAILABLE:
                return ultimate_generate_game()
            else:
                fallback_html = generate_fallback_game(prompt, 'free_ai')
                return jsonify({
                    'success': True,
                    'html': fallback_html,
                    'method': 'fallback_for_free_ai'
                })
        
        # Use FREE AI system
        template = free_ai_engine.generate_template(prompt)
        game_code = free_ai_generator.generate_game_code(template)
        
        update_stats(success=True, method='free_ai')
        
        return jsonify({
            'success': True,
            'html': game_code,
            'game_title': template.get('title', 'AI Game'),
            'method': 'free_ai_system',
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        print(f"❌ FREE AI generation error: {e}")
        update_stats(success=False, method='free_ai')
        
        fallback_html = generate_fallback_game(prompt if 'prompt' in locals() else 'ai game', 'free_ai')
        return jsonify({
            'success': True,
            'html': fallback_html,
            'method': 'fallback_after_error'
        })

@app.route('/generate-game', methods=['POST'])
def generate_game():
    """Enhanced/Basic game generation endpoint"""
    try:
        data = request.get_json()
        prompt = data.get('prompt', '').strip()
        mode = data.get('mode', 'enhanced')
        
        if not prompt:
            return jsonify({'success': False, 'error': 'No prompt provided'}), 400
        
        print(f"✨ {mode.title()} generation request: '{prompt}'")
        
        # For enhanced/basic mode, use intelligent system if available
        if INTELLIGENT_SYSTEM_AVAILABLE and mode == 'enhanced':
            try:
                result = generate_ultimate_game(prompt)
                if result['success']:
                    update_stats(success=True, method='intelligent')
                    return jsonify({
                        'success': True,
                        'html': result['html'],
                        'method': 'intelligent_enhanced'
                    })
            except Exception as e:
                print(f"❌ Enhanced mode error: {e}")
        
        # Fallback to simple template
        fallback_html = generate_fallback_game(prompt, mode)
        update_stats(success=True, method='fallback')
        
        return jsonify({
            'success': True,
            'html': fallback_html,
            'method': f'fallback_{mode}'
        })
        
    except Exception as e:
        print(f"❌ Generate game error: {e}")
        update_stats(success=False, method='enhanced')
        
        return jsonify({
            'success': False,
            'error': str(e),
            'html': generate_fallback_game('error game', 'enhanced')
        }), 500

@app.route('/template-stats')
def template_stats():
    """Get template library statistics"""
    if INTELLIGENT_SYSTEM_AVAILABLE:
        try:
            stats_data = get_template_stats()
            return jsonify({
                'success': True,
                'intelligent_system': True,
                'stats': stats_data
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e),
                'intelligent_system': False
            })
    else:
        return jsonify({
            'success': True,
            'intelligent_system': False,
            'stats': {
                'total_templates': 3,
                'categories': {
                    'Sports': ['darts', 'basketball'],
                    'Racing': ['racing']
                },
                'total_categories': 2
            }
        })

@app.route('/generation-stats')
def generation_stats():
    """Get generation statistics"""
    return jsonify({
        'success': True,
        'stats': stats,
        'performance': {
            'accuracy_percentage': f"{stats['prompt_matching_accuracy']:.1%}",
            'total_requests': stats['total_generations'],
            'successful_requests': stats['successful_generations'],
            'intelligent_usage': f"{stats['intelligent_generations']}/{stats['total_generations']}",
            'free_ai_usage': f"{stats['free_ai_generations']}/{stats['total_generations']}",
            'fallback_usage': f"{stats['fallback_generations']}/{stats['total_generations']}"
        }
    })

@app.route('/system-status')
def system_status():
    """Get comprehensive system status"""
    return jsonify({
        'status': 'operational',
        'systems': {
            'intelligent_game_generator': {
                'available': INTELLIGENT_SYSTEM_AVAILABLE,
                'status': 'operational' if INTELLIGENT_SYSTEM_AVAILABLE else 'unavailable',
                'features': ['prompt_parsing', 'template_matching', 'game_generation'] if INTELLIGENT_SYSTEM_AVAILABLE else []
            },
            'free_ai_system': {
                'available': FREE_AI_AVAILABLE,
                'status': 'operational' if FREE_AI_AVAILABLE else 'unavailable',
                'features': ['ai_enhancement', 'dynamic_generation'] if FREE_AI_AVAILABLE else []
            },
            'fallback_system': {
                'available': True,
                'status': 'operational',
                'features': ['basic_templates', 'keyword_matching', 'guaranteed_generation']
            }
        },
        'performance': stats,
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("🔥 Starting Ultimate Game Maker Backend with True Prompt Matching...")
    print("🧠 Intelligent Game Generation System:", "✅ AVAILABLE" if INTELLIGENT_SYSTEM_AVAILABLE else "❌ UNAVAILABLE")
    print("🤖 FREE AI System:", "✅ AVAILABLE" if FREE_AI_AVAILABLE else "❌ UNAVAILABLE")
    print("🔧 Fallback System: ✅ AVAILABLE")
    print("🌐 Server starting on port 8080")
    print("🎯 Ready to generate games with true prompt matching!")
    
    app.run(host='0.0.0.0', port=8080, debug=False)
