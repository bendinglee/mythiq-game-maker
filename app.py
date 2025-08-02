import os
import json
import uuid
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Configuration
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
HUGGINGFACE_API_KEY = os.environ.get('HUGGINGFACE_API_KEY')

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "service": "Mythiq Game Maker",
        "status": "online",
        "version": "1.0.0",
        "endpoints": ["/generate-game", "/health"]
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "service": "mythiq-game-maker",
        "groq_configured": bool(GROQ_API_KEY),
        "huggingface_configured": bool(HUGGINGFACE_API_KEY)
    })

@app.route('/generate-game', methods=['POST'])
def generate_game():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        game_type = data.get('type', 'html5')
        
        if not prompt:
            return jsonify({"error": "Game prompt is required"}), 400
        
        # Generate game concept using AI
        game_concept = generate_game_concept(prompt)
        
        # Create simple HTML5 game
        game_html = create_html5_game(game_concept, prompt)
        
        # Generate unique game ID
        game_id = str(uuid.uuid4())[:8]
        
        return jsonify({
            "game_id": game_id,
            "concept": game_concept,
            "html_content": game_html,
            "type": game_type,
            "status": "generated",
            "play_url": f"/play/{game_id}"
        })
        
    except Exception as e:
        print(f"Game generation error: {e}")
        return jsonify({"error": "Failed to generate game"}), 500

def generate_game_concept(prompt):
    """Generate game concept using AI"""
    try:
        if GROQ_API_KEY:
            return call_groq_for_game(prompt)
        elif HUGGINGFACE_API_KEY:
            return call_huggingface_for_game(prompt)
    except Exception as e:
        print(f"AI generation error: {e}")
    
    # Fallback concept
    return {
        "title": "Adventure Game",
        "description": f"An exciting game based on: {prompt}",
        "mechanics": ["Movement", "Interaction", "Scoring"],
        "theme": "Adventure"
    }

def call_groq_for_game(prompt):
    """Use Groq to generate game concept"""
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    system_prompt = """You are a game designer. Create a simple game concept based on the user's prompt. 
    Respond with a JSON object containing: title, description, mechanics (array), and theme."""
    
    payload = {
        "model": "llama-3.1-70b-versatile",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Create a game concept for: {prompt}"}
        ],
        "max_tokens": 500,
        "temperature": 0.8
    }
    
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    
    result = response.json()
    content = result["choices"][0]["message"]["content"]
    
    try:
        return json.loads(content)
    except:
        return {
            "title": "AI Generated Game",
            "description": content[:200],
            "mechanics": ["Movement", "Action"],
            "theme": "Creative"
        }

def call_huggingface_for_game(prompt):
    """Use Hugging Face to generate game concept"""
    # Simplified concept generation
    return {
        "title": f"Game: {prompt[:30]}",
        "description": f"A creative game inspired by: {prompt}",
        "mechanics": ["Click to play", "Score points", "Have fun"],
        "theme": "Interactive"
    }

def create_html5_game(concept, original_prompt):
    """Create a simple HTML5 game"""
    title = concept.get("title", "Mythiq Game")
    description = concept.get("description", "A fun game!")
    
    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 20px;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
        }}
        .game-container {{
            max-width: 800px;
            margin: 0 auto;
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            padding: 30px;
            backdrop-filter: blur(10px);
        }}
        .game-canvas {{
            background: #2a2a2a;
            border-radius: 10px;
            margin: 20px 0;
            cursor: pointer;
        }}
        .score {{
            font-size: 24px;
            margin: 20px 0;
        }}
        .btn {{
            background: #4CAF50;
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 25px;
            cursor: pointer;
            margin: 10px;
        }}
        .btn:hover {{
            background: #45a049;
        }}
    </style>
</head>
<body>
    <div class="game-container">
        <h1>{title}</h1>
        <p>{description}</p>
        
        <canvas id="gameCanvas" class="game-canvas" width="600" height="400"></canvas>
        
        <div class="score">Score: <span id="score">0</span></div>
        
        <button class="btn" onclick="startGame()">Start Game</button>
        <button class="btn" onclick="resetGame()">Reset</button>
        
        <div style="margin-top: 30px;">
            <h3>How to Play:</h3>
            <p>Click on the canvas to play! Move around and collect points.</p>
            <p><strong>Original Prompt:</strong> {original_prompt}</p>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        let score = 0;
        let gameRunning = false;
        let player = {{x: 300, y: 200, size: 20}};
        let targets = [];

        function startGame() {{
            gameRunning = true;
            score = 0;
            updateScore();
            generateTargets();
            gameLoop();
        }}

        function resetGame() {{
            gameRunning = false;
            score = 0;
            targets = [];
            updateScore();
            clearCanvas();
        }}

        function generateTargets() {{
            targets = [];
            for(let i = 0; i < 5; i++) {{
                targets.push({{
                    x: Math.random() * (canvas.width - 20),
                    y: Math.random() * (canvas.height - 20),
                    size: 15,
                    color: `hsl(${{Math.random() * 360}}, 70%, 60%)`
                }});
            }}
        }}

        function gameLoop() {{
            if(!gameRunning) return;
            
            clearCanvas();
            drawPlayer();
            drawTargets();
            
            requestAnimationFrame(gameLoop);
        }}

        function clearCanvas() {{
            ctx.fillStyle = '#2a2a2a';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
        }}

        function drawPlayer() {{
            ctx.fillStyle = '#4CAF50';
            ctx.fillRect(player.x - player.size/2, player.y - player.size/2, player.size, player.size);
        }}

        function drawTargets() {{
            targets.forEach(target => {{
                ctx.fillStyle = target.color;
                ctx.beginPath();
                ctx.arc(target.x, target.y, target.size, 0, Math.PI * 2);
                ctx.fill();
            }});
        }}

        function updateScore() {{
            document.getElementById('score').textContent = score;
        }}

        canvas.addEventListener('click', (e) => {{
            if(!gameRunning) return;
            
            const rect = canvas.getBoundingClientRect();
            const clickX = e.clientX - rect.left;
            const clickY = e.clientY - rect.top;
            
            // Move player towards click
            player.x = clickX;
            player.y = clickY;
            
            // Check for target collisions
            targets = targets.filter(target => {{
                const distance = Math.sqrt(
                    Math.pow(player.x - target.x, 2) + 
                    Math.pow(player.y - target.y, 2)
                );
                
                if(distance < player.size + target.size) {{
                    score += 10;
                    updateScore();
                    return false; // Remove target
                }}
                return true;
            }});
            
            // Generate new targets if all collected
            if(targets.length === 0) {{
                generateTargets();
            }}
        }});

        // Initialize
        clearCanvas();
    </script>
</body>
</html>
    """
    
    return html_template

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)
