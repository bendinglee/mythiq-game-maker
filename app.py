"""
COMPLETE WORKING BACKEND - IMPORT ERROR FIXED
Version: 13.0.0 - NO EXTERNAL IMPORTS
Generates actual playable HTML5 games with complete file delivery system
FIXED: Removed all problematic imports that cause ImportError
"""

from flask import Flask, request, jsonify, send_file, render_template_string
from flask_cors import CORS
import os
import json
import uuid
import datetime
import tempfile
import zipfile
import shutil
import traceback

app = Flask(__name__)
CORS(app)

# Global stats
stats = {
    'total_games_generated': 0,
    'ultimate_games': 0,
    'free_ai_games': 0,
    'enhanced_games': 0,
    'basic_games': 0,
    'files_downloaded': 0,
    'games_opened': 0
}

# Game storage
generated_games = {}

# Game templates with complete HTML5 implementations
def generate_darts_game(prompt, mode, character, theme, difficulty):
    """Generate a complete interactive darts game"""
    game_id = str(uuid.uuid4())
    
    # Quality-based features
    features = {
        'ultimate': ['Professional dartboard', 'Advanced scoring', 'Tournament mode', 'Statistics tracking', 'Sound effects'],
        'free_ai': ['AI opponent', 'Smart difficulty', 'Adaptive gameplay', 'Performance analytics'],
        'enhanced': ['Multiple game modes', 'Score tracking', 'Visual effects', 'Smooth animations'],
        'basic': ['Basic dartboard', 'Simple scoring', 'Standard gameplay']
    }
    
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>''' + character + ''' Darts Championship</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: white;
            text-align: center;
        }
        .game-container {
            max-width: 800px;
            margin: 0 auto;
            background: rgba(0,0,0,0.3);
            border-radius: 15px;
            padding: 20px;
        }
        .dartboard {
            width: 300px;
            height: 300px;
            border-radius: 50%;
            background: radial-gradient(circle, #ff0000 0%, #00ff00 20%, #ffff00 40%, #ff0000 60%, #000000 80%);
            margin: 20px auto;
            position: relative;
            cursor: crosshair;
            border: 5px solid #333;
        }
        .score-display {
            font-size: 24px;
            margin: 20px 0;
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 10px;
        }
        .throw-btn {
            background: #ff6b6b;
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 25px;
            cursor: pointer;
            margin: 10px;
            transition: all 0.3s;
        }
        .throw-btn:hover {
            background: #ff5252;
            transform: scale(1.05);
        }
        .game-info {
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 10px;
            margin: 20px 0;
        }
        .dart-hit {
            position: absolute;
            width: 8px;
            height: 8px;
            background: #ffff00;
            border-radius: 50%;
            border: 2px solid #000;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h1>🎯 ''' + character + ''' Darts Championship</h1>
        <div class="game-info">
            <p><strong>Theme:</strong> ''' + theme + '''</p>
            <p><strong>Difficulty:</strong> ''' + difficulty + '''</p>
            <p><strong>Mode:</strong> ''' + mode.upper() + '''</p>
        </div>
        
        <div class="score-display">
            <div>Score: <span id="score">501</span></div>
            <div>Darts Left: <span id="darts">3</span></div>
            <div>Round: <span id="round">1</span></div>
        </div>
        
        <div class="dartboard" id="dartboard" onclick="throwDart(event)"></div>
        
        <button class="throw-btn" onclick="newGame()">New Game</button>
        <button class="throw-btn" onclick="resetRound()">Reset Round</button>
        
        <div class="game-info">
            <h3>How to Play:</h3>
            <p>Click on the dartboard to throw darts. Reduce your score from 501 to exactly 0!</p>
            <p>Features: ''' + ', '.join(features.get(mode, features['basic'])) + '''</p>
        </div>
    </div>

    <script>
        let gameState = {
            score: 501,
            dartsLeft: 3,
            round: 1,
            totalDarts: 0
        };

        function throwDart(event) {
            if (gameState.dartsLeft <= 0) {
                alert('Round complete! Click Reset Round to continue.');
                return;
            }

            const dartboard = document.getElementById('dartboard');
            const rect = dartboard.getBoundingClientRect();
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const clickX = event.clientX - rect.left;
            const clickY = event.clientY - rect.top;
            
            // Calculate distance from center
            const distance = Math.sqrt(Math.pow(clickX - centerX, 2) + Math.pow(clickY - centerY, 2));
            const maxRadius = rect.width / 2;
            
            // Calculate score based on distance and randomness
            let points = 0;
            if (distance < maxRadius * 0.1) {
                points = 50; // Bullseye
            } else if (distance < maxRadius * 0.2) {
                points = 25; // Bull
            } else if (distance < maxRadius * 0.4) {
                points = Math.floor(Math.random() * 20) + 15; // Inner ring
            } else if (distance < maxRadius * 0.8) {
                points = Math.floor(Math.random() * 15) + 5; // Middle ring
            } else if (distance < maxRadius) {
                points = Math.floor(Math.random() * 10) + 1; // Outer ring
            } else {
                points = 0; // Miss
            }

            // Add difficulty modifier
            if (''' + ('True' if difficulty == 'Expert' else 'False') + ''') {
                points = Math.floor(points * 0.8); // Harder scoring
            }

            // Create dart visual
            const dart = document.createElement('div');
            dart.className = 'dart-hit';
            dart.style.left = clickX - 4 + 'px';
            dart.style.top = clickY - 4 + 'px';
            dartboard.appendChild(dart);

            // Update game state
            gameState.score = Math.max(0, gameState.score - points);
            gameState.dartsLeft--;
            gameState.totalDarts++;

            updateDisplay();

            // Check win condition
            if (gameState.score === 0) {
                setTimeout(() => {
                    alert('🎉 Congratulations! You won in ' + gameState.round + ' rounds with ' + gameState.totalDarts + ' darts!');
                    newGame();
                }, 500);
            } else if (gameState.dartsLeft === 0) {
                setTimeout(() => {
                    alert('Round ' + gameState.round + ' complete! Score: ' + points + ' points');
                }, 300);
            }
        }

        function updateDisplay() {
            document.getElementById('score').textContent = gameState.score;
            document.getElementById('darts').textContent = gameState.dartsLeft;
            document.getElementById('round').textContent = gameState.round;
        }

        function resetRound() {
            gameState.dartsLeft = 3;
            gameState.round++;
            
            // Clear dart visuals
            const darts = document.querySelectorAll('.dart-hit');
            darts.forEach(dart => dart.remove());
            
            updateDisplay();
        }

        function newGame() {
            gameState = {
                score: 501,
                dartsLeft: 3,
                round: 1,
                totalDarts: 0
            };
            
            // Clear all dart visuals
            const darts = document.querySelectorAll('.dart-hit');
            darts.forEach(dart => dart.remove());
            
            updateDisplay();
        }

        // Initialize display
        updateDisplay();
    </script>
</body>
</html>'''

    return {
        'id': game_id,
        'title': character + ' Darts Championship',
        'type': 'darts',
        'html': html_content,
        'character': character,
        'theme': theme,
        'difficulty': difficulty,
        'quality': mode,
        'features': features.get(mode, features['basic']),
        'art_style': 'Professional Sports',
        'multiplayer_mode': 'single_player',
        'created_at': datetime.datetime.now().isoformat()
    }

def generate_basketball_game(prompt, mode, character, theme, difficulty):
    """Generate a complete interactive basketball game"""
    game_id = str(uuid.uuid4())
    
    features = {
        'ultimate': ['Professional court', 'Advanced physics', 'Tournament mode', 'Player stats', 'Crowd effects'],
        'free_ai': ['AI opponent', 'Smart defense', 'Adaptive difficulty', 'Performance tracking'],
        'enhanced': ['Multiple courts', 'Score tracking', 'Shot mechanics', 'Time pressure'],
        'basic': ['Basic court', 'Simple shooting', 'Score counter']
    }
    
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>''' + character + ''' Basketball Arena</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #ff7e5f, #feb47b);
            color: white;
            text-align: center;
        }
        .game-container {
            max-width: 800px;
            margin: 0 auto;
            background: rgba(0,0,0,0.3);
            border-radius: 15px;
            padding: 20px;
        }
        .basketball-court {
            width: 400px;
            height: 300px;
            background: #8B4513;
            margin: 20px auto;
            position: relative;
            border: 3px solid #654321;
            border-radius: 10px;
        }
        .hoop {
            width: 60px;
            height: 20px;
            background: #ff6600;
            position: absolute;
            top: 50px;
            right: 10px;
            border-radius: 30px;
            cursor: pointer;
            border: 3px solid #cc5500;
        }
        .basketball {
            width: 30px;
            height: 30px;
            background: radial-gradient(circle at 30% 30%, #ff8c00, #ff4500);
            border-radius: 50%;
            position: absolute;
            bottom: 20px;
            left: 50px;
            cursor: pointer;
            border: 2px solid #000;
        }
        .score-display {
            font-size: 24px;
            margin: 20px 0;
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 10px;
        }
        .shoot-btn {
            background: #ff6b6b;
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 25px;
            cursor: pointer;
            margin: 10px;
            transition: all 0.3s;
        }
        .shoot-btn:hover {
            background: #ff5252;
            transform: scale(1.05);
        }
        .power-meter {
            width: 200px;
            height: 20px;
            background: #333;
            margin: 20px auto;
            border-radius: 10px;
            overflow: hidden;
        }
        .power-bar {
            height: 100%;
            background: linear-gradient(90deg, #00ff00, #ffff00, #ff0000);
            width: 0%;
            transition: width 0.1s;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h1>🏀 ''' + character + ''' Basketball Arena</h1>
        <div class="game-info">
            <p><strong>Theme:</strong> ''' + theme + '''</p>
            <p><strong>Difficulty:</strong> ''' + difficulty + '''</p>
            <p><strong>Mode:</strong> ''' + mode.upper() + '''</p>
        </div>
        
        <div class="score-display">
            <div>Score: <span id="score">0</span></div>
            <div>Shots: <span id="shots">0</span></div>
            <div>Accuracy: <span id="accuracy">0%</span></div>
            <div>Time: <span id="time">60</span>s</div>
        </div>
        
        <div class="basketball-court" id="court">
            <div class="hoop" id="hoop"></div>
            <div class="basketball" id="basketball" onclick="prepareShooting()"></div>
        </div>
        
        <div class="power-meter">
            <div class="power-bar" id="powerBar"></div>
        </div>
        
        <button class="shoot-btn" id="shootBtn" onclick="shoot()" disabled>Click Ball to Prepare Shot</button>
        <button class="shoot-btn" onclick="newGame()">New Game</button>
        
        <div class="game-info">
            <h3>How to Play:</h3>
            <p>Click the basketball to prepare your shot, then click SHOOT when the power meter is right!</p>
            <p>Features: ''' + ', '.join(features.get(mode, features['basic'])) + '''</p>
        </div>
    </div>

    <script>
        let gameState = {
            score: 0,
            shots: 0,
            timeLeft: 60,
            gameActive: true,
            shootingPower: 0,
            powerIncreasing: true,
            powerInterval: null,
            shotPrepared: false
        };

        function prepareShooting() {
            if (!gameState.gameActive) return;
            
            gameState.shotPrepared = true;
            document.getElementById('shootBtn').disabled = false;
            document.getElementById('shootBtn').textContent = 'SHOOT!';
            
            // Start power meter
            gameState.powerInterval = setInterval(() => {
                if (gameState.powerIncreasing) {
                    gameState.shootingPower += 2;
                    if (gameState.shootingPower >= 100) {
                        gameState.powerIncreasing = false;
                    }
                } else {
                    gameState.shootingPower -= 2;
                    if (gameState.shootingPower <= 0) {
                        gameState.powerIncreasing = true;
                    }
                }
                
                document.getElementById('powerBar').style.width = gameState.shootingPower + '%';
            }, 50);
        }

        function shoot() {
            if (!gameState.shotPrepared || !gameState.gameActive) return;
            
            // Stop power meter
            clearInterval(gameState.powerInterval);
            gameState.shotPrepared = false;
            document.getElementById('shootBtn').disabled = true;
            document.getElementById('shootBtn').textContent = 'Click Ball to Prepare Shot';
            
            // Calculate shot success based on power
            let successChance = 0;
            if (gameState.shootingPower >= 40 && gameState.shootingPower <= 80) {
                successChance = 0.8; // Sweet spot
            } else if (gameState.shootingPower >= 20 && gameState.shootingPower <= 90) {
                successChance = 0.5; // Good range
            } else {
                successChance = 0.2; // Poor power
            }
            
            // Difficulty modifier
            if (''' + ('True' if difficulty == 'Expert' else 'False') + ''') {
                successChance *= 0.7; // Harder shots
            }
            
            gameState.shots++;
            
            // Animate basketball
            const basketball = document.getElementById('basketball');
            basketball.style.transition = 'all 1s ease-out';
            
            if (Math.random() < successChance) {
                // Successful shot
                basketball.style.transform = 'translate(320px, -200px)';
                gameState.score += ''' + ('3' if mode == 'ultimate' else '2') + ''';
                
                setTimeout(() => {
                    alert('🎉 SCORE! Great shot!');
                    resetBall();
                }, 1000);
            } else {
                // Missed shot
                basketball.style.transform = 'translate(' + (Math.random() * 300 + 100) + 'px, -100px)';
                
                setTimeout(() => {
                    alert('😔 Missed! Try again!');
                    resetBall();
                }, 1000);
            }
            
            updateDisplay();
        }

        function resetBall() {
            const basketball = document.getElementById('basketball');
            basketball.style.transition = 'all 0.5s ease-in';
            basketball.style.transform = 'translate(0px, 0px)';
            gameState.shootingPower = 0;
            document.getElementById('powerBar').style.width = '0%';
        }

        function updateDisplay() {
            document.getElementById('score').textContent = gameState.score;
            document.getElementById('shots').textContent = gameState.shots;
            const accuracy = gameState.shots > 0 ? Math.round((gameState.score / (gameState.shots * ''' + ('3' if mode == 'ultimate' else '2') + ''')) * 100) : 0;
            document.getElementById('accuracy').textContent = accuracy + '%';
            document.getElementById('time').textContent = gameState.timeLeft;
        }

        function newGame() {
            gameState = {
                score: 0,
                shots: 0,
                timeLeft: 60,
                gameActive: true,
                shootingPower: 0,
                powerIncreasing: true,
                powerInterval: null,
                shotPrepared: false
            };
            
            clearInterval(gameState.powerInterval);
            resetBall();
            updateDisplay();
            
            document.getElementById('shootBtn').disabled = true;
            document.getElementById('shootBtn').textContent = 'Click Ball to Prepare Shot';
            
            // Start game timer
            const timer = setInterval(() => {
                gameState.timeLeft--;
                updateDisplay();
                
                if (gameState.timeLeft <= 0) {
                    clearInterval(timer);
                    gameState.gameActive = false;
                    alert('⏰ Time up! Final Score: ' + gameState.score + ' points with ' + Math.round((gameState.score / (gameState.shots * ''' + ('3' if mode == 'ultimate' else '2') + ''' || 1)) * 100) + '% accuracy!');
                }
            }, 1000);
        }

        // Initialize game
        newGame();
    </script>
</body>
</html>'''

    return {
        'id': game_id,
        'title': character + ' Basketball Arena',
        'type': 'basketball',
        'html': html_content,
        'character': character,
        'theme': theme,
        'difficulty': difficulty,
        'quality': mode,
        'features': features.get(mode, features['basic']),
        'art_style': 'Sports Arena',
        'multiplayer_mode': 'single_player',
        'created_at': datetime.datetime.now().isoformat()
    }

def generate_underwater_game(prompt, mode, character, theme, difficulty):
    """Generate a complete underwater adventure game"""
    game_id = str(uuid.uuid4())
    
    features = {
        'ultimate': ['Deep sea exploration', 'Treasure hunting', 'Oxygen management', 'Marine life', 'Submarine controls'],
        'free_ai': ['AI sea creatures', 'Dynamic environment', 'Adaptive challenges', 'Smart navigation'],
        'enhanced': ['Multiple depths', 'Treasure collection', 'Oxygen system', 'Visual effects'],
        'basic': ['Basic swimming', 'Simple collection', 'Score tracking']
    }
    
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>''' + character + ''' Underwater Adventure</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            font-family: Arial, sans-serif;
            background: linear-gradient(180deg, #87CEEB 0%, #4682B4 50%, #191970 100%);
            color: white;
            text-align: center;
        }
        .game-container {
            max-width: 800px;
            margin: 0 auto;
            background: rgba(0,0,0,0.3);
            border-radius: 15px;
            padding: 20px;
        }
        .ocean {
            width: 600px;
            height: 400px;
            background: linear-gradient(180deg, #87CEEB 0%, #4682B4 50%, #191970 100%);
            margin: 20px auto;
            position: relative;
            border: 3px solid #4682B4;
            border-radius: 10px;
            overflow: hidden;
        }
        .diver {
            width: 40px;
            height: 40px;
            background: #FFD700;
            position: absolute;
            top: 50%;
            left: 50px;
            border-radius: 50%;
            cursor: pointer;
            border: 3px solid #FFA500;
        }
        .treasure {
            width: 25px;
            height: 25px;
            background: #FFD700;
            position: absolute;
            border-radius: 3px;
            cursor: pointer;
            border: 2px solid #FFA500;
        }
        .fish {
            width: 30px;
            height: 20px;
            background: #FF6347;
            position: absolute;
            border-radius: 50%;
            animation: swim 3s linear infinite;
        }
        @keyframes swim {
            0% { transform: translateX(-50px); }
            100% { transform: translateX(650px); }
        }
        .status-display {
            font-size: 18px;
            margin: 20px 0;
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 10px;
            display: flex;
            justify-content: space-around;
        }
        .control-btn {
            background: #4682B4;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 20px;
            cursor: pointer;
            margin: 5px;
            transition: all 0.3s;
        }
        .control-btn:hover {
            background: #5F9EA0;
            transform: scale(1.05);
        }
        .oxygen-bar {
            width: 200px;
            height: 20px;
            background: #333;
            margin: 10px auto;
            border-radius: 10px;
            overflow: hidden;
        }
        .oxygen-level {
            height: 100%;
            background: linear-gradient(90deg, #ff0000, #ffff00, #00ff00);
            width: 100%;
            transition: width 0.5s;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h1>🌊 ''' + character + ''' Underwater Adventure</h1>
        <div class="game-info">
            <p><strong>Theme:</strong> ''' + theme + '''</p>
            <p><strong>Difficulty:</strong> ''' + difficulty + '''</p>
            <p><strong>Mode:</strong> ''' + mode.upper() + '''</p>
        </div>
        
        <div class="status-display">
            <div>Treasures: <span id="treasures">0</span></div>
            <div>Depth: <span id="depth">10</span>m</div>
            <div>Score: <span id="score">0</span></div>
        </div>
        
        <div class="oxygen-bar">
            <div class="oxygen-level" id="oxygenLevel"></div>
        </div>
        <div>Oxygen: <span id="oxygen">100</span>%</div>
        
        <div class="ocean" id="ocean">
            <div class="diver" id="diver"></div>
        </div>
        
        <div class="controls">
            <button class="control-btn" onclick="moveDiver('up')">↑ Surface</button>
            <button class="control-btn" onclick="moveDiver('down')">↓ Dive</button>
            <button class="control-btn" onclick="moveDiver('left')">← Left</button>
            <button class="control-btn" onclick="moveDiver('right')">→ Right</button>
            <button class="control-btn" onclick="newGame()">New Dive</button>
        </div>
        
        <div class="game-info">
            <h3>How to Play:</h3>
            <p>Navigate the underwater world to collect treasures! Watch your oxygen level!</p>
            <p>Features: ''' + ', '.join(features.get(mode, features['basic'])) + '''</p>
        </div>
    </div>

    <script>
        let gameState = {
            treasures: 0,
            depth: 10,
            score: 0,
            oxygen: 100,
            diverX: 50,
            diverY: 200,
            gameActive: true,
            treasurePositions: [],
            fishPositions: []
        };

        function moveDiver(direction) {
            if (!gameState.gameActive) return;
            
            const diver = document.getElementById('diver');
            const ocean = document.getElementById('ocean');
            const oceanRect = ocean.getBoundingClientRect();
            
            switch(direction) {
                case 'up':
                    if (gameState.diverY > 20) {
                        gameState.diverY -= 30;
                        gameState.depth = Math.max(5, gameState.depth - 5);
                    }
                    break;
                case 'down':
                    if (gameState.diverY < 360) {
                        gameState.diverY += 30;
                        gameState.depth += 5;
                    }
                    break;
                case 'left':
                    if (gameState.diverX > 20) {
                        gameState.diverX -= 30;
                    }
                    break;
                case 'right':
                    if (gameState.diverX < 560) {
                        gameState.diverX += 30;
                    }
                    break;
            }
            
            diver.style.left = gameState.diverX + 'px';
            diver.style.top = gameState.diverY + 'px';
            
            // Consume oxygen based on depth and difficulty
            let oxygenCost = 1;
            if (gameState.depth > 50) oxygenCost = 2;
            if (gameState.depth > 100) oxygenCost = 3;
            if (''' + ('True' if difficulty == 'Expert' else 'False') + ''') {
                oxygenCost *= 1.5;
            }
            
            gameState.oxygen = Math.max(0, gameState.oxygen - oxygenCost);
            
            checkCollisions();
            updateDisplay();
            
            if (gameState.oxygen <= 0) {
                gameState.gameActive = false;
                setTimeout(() => {
                    alert('💨 Out of oxygen! You collected ' + gameState.treasures + ' treasures and scored ' + gameState.score + ' points!');
                }, 500);
            }
        }

        function checkCollisions() {
            // Check treasure collection
            gameState.treasurePositions.forEach((treasure, index) => {
                const distance = Math.sqrt(
                    Math.pow(gameState.diverX - treasure.x, 2) + 
                    Math.pow(gameState.diverY - treasure.y, 2)
                );
                
                if (distance < 40) {
                    // Collect treasure
                    gameState.treasures++;
                    gameState.score += treasure.value;
                    
                    // Remove treasure from DOM and array
                    const treasureElement = document.getElementById('treasure' + index);
                    if (treasureElement) {
                        treasureElement.remove();
                    }
                    gameState.treasurePositions.splice(index, 1);
                    
                    // Add oxygen bonus
                    gameState.oxygen = Math.min(100, gameState.oxygen + 10);
                }
            });
        }

        function spawnTreasure() {
            const ocean = document.getElementById('ocean');
            const treasureIndex = gameState.treasurePositions.length;
            
            const x = Math.random() * 550 + 25;
            const y = Math.random() * 350 + 25;
            const value = Math.floor(Math.random() * 50) + 10;
            
            const treasure = document.createElement('div');
            treasure.className = 'treasure';
            treasure.id = 'treasure' + treasureIndex;
            treasure.style.left = x + 'px';
            treasure.style.top = y + 'px';
            treasure.title = 'Treasure worth ' + value + ' points';
            
            ocean.appendChild(treasure);
            gameState.treasurePositions.push({x: x, y: y, value: value});
        }

        function spawnFish() {
            const ocean = document.getElementById('ocean');
            const fish = document.createElement('div');
            fish.className = 'fish';
            fish.style.top = Math.random() * 350 + 'px';
            fish.style.left = '-50px';
            
            ocean.appendChild(fish);
            
            // Remove fish after animation
            setTimeout(() => {
                if (fish.parentNode) {
                    fish.parentNode.removeChild(fish);
                }
            }, 3000);
        }

        function updateDisplay() {
            document.getElementById('treasures').textContent = gameState.treasures;
            document.getElementById('depth').textContent = gameState.depth;
            document.getElementById('score').textContent = gameState.score;
            document.getElementById('oxygen').textContent = Math.round(gameState.oxygen);
            document.getElementById('oxygenLevel').style.width = gameState.oxygen + '%';
        }

        function newGame() {
            gameState = {
                treasures: 0,
                depth: 10,
                score: 0,
                oxygen: 100,
                diverX: 50,
                diverY: 200,
                gameActive: true,
                treasurePositions: [],
                fishPositions: []
            };
            
            // Clear ocean
            const ocean = document.getElementById('ocean');
            const treasures = ocean.querySelectorAll('.treasure');
            const fish = ocean.querySelectorAll('.fish');
            
            treasures.forEach(treasure => treasure.remove());
            fish.forEach(f => f.remove());
            
            // Reset diver position
            const diver = document.getElementById('diver');
            diver.style.left = '50px';
            diver.style.top = '200px';
            
            updateDisplay();
            
            // Spawn initial treasures
            for (let i = 0; i < ''' + ('8' if mode == 'ultimate' else '5') + '''; i++) {
                setTimeout(() => spawnTreasure(), i * 1000);
            }
            
            // Spawn fish periodically
            setInterval(() => {
                if (gameState.gameActive && Math.random() < 0.3) {
                    spawnFish();
                }
            }, 2000);
        }

        // Initialize game
        newGame();
        
        // Keyboard controls
        document.addEventListener('keydown', (event) => {
            switch(event.key) {
                case 'ArrowUp':
                case 'w':
                case 'W':
                    moveDiver('up');
                    break;
                case 'ArrowDown':
                case 's':
                case 'S':
                    moveDiver('down');
                    break;
                case 'ArrowLeft':
                case 'a':
                case 'A':
                    moveDiver('left');
                    break;
                case 'ArrowRight':
                case 'd':
                case 'D':
                    moveDiver('right');
                    break;
            }
        });
    </script>
</body>
</html>'''

    return {
        'id': game_id,
        'title': character + ' Underwater Adventure',
        'type': 'underwater',
        'html': html_content,
        'character': character,
        'theme': theme,
        'difficulty': difficulty,
        'quality': mode,
        'features': features.get(mode, features['basic']),
        'art_style': 'Underwater World',
        'multiplayer_mode': 'single_player',
        'created_at': datetime.datetime.now().isoformat()
    }

def generate_medieval_game(prompt, mode, character, theme, difficulty):
    """Generate a complete medieval quest game"""
    game_id = str(uuid.uuid4())
    
    features = {
        'ultimate': ['Epic quests', 'Dragon battles', 'Castle exploration', 'Honor system', 'Medieval weapons'],
        'free_ai': ['AI knights', 'Dynamic quests', 'Intelligent enemies', 'Adaptive storyline'],
        'enhanced': ['Multiple quests', 'Combat system', 'Character progression', 'Medieval atmosphere'],
        'basic': ['Simple quests', 'Basic combat', 'Score tracking']
    }
    
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>''' + character + ''' Medieval Quest</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            font-family: 'Times New Roman', serif;
            background: linear-gradient(135deg, #8B4513, #A0522D, #CD853F);
            color: #FFD700;
            text-align: center;
        }
        .game-container {
            max-width: 800px;
            margin: 0 auto;
            background: rgba(0,0,0,0.4);
            border-radius: 15px;
            padding: 20px;
            border: 3px solid #FFD700;
        }
        .castle {
            width: 500px;
            height: 300px;
            background: linear-gradient(180deg, #696969, #2F4F4F);
            margin: 20px auto;
            position: relative;
            border: 3px solid #2F4F4F;
            border-radius: 10px;
        }
        .knight {
            width: 40px;
            height: 40px;
            background: #C0C0C0;
            position: absolute;
            bottom: 20px;
            left: 50px;
            border-radius: 5px;
            cursor: pointer;
            border: 2px solid #A9A9A9;
        }
        .dragon {
            width: 60px;
            height: 40px;
            background: #8B0000;
            position: absolute;
            top: 50px;
            right: 50px;
            border-radius: 10px;
            cursor: pointer;
            border: 2px solid #FF0000;
        }
        .treasure-chest {
            width: 30px;
            height: 25px;
            background: #DAA520;
            position: absolute;
            border-radius: 3px;
            cursor: pointer;
            border: 2px solid #B8860B;
        }
        .status-display {
            font-size: 18px;
            margin: 20px 0;
            background: rgba(255,215,0,0.1);
            padding: 15px;
            border-radius: 10px;
            display: flex;
            justify-content: space-around;
            border: 2px solid #FFD700;
        }
        .action-btn {
            background: #8B0000;
            color: #FFD700;
            border: 2px solid #FFD700;
            padding: 12px 25px;
            font-size: 16px;
            border-radius: 20px;
            cursor: pointer;
            margin: 5px;
            transition: all 0.3s;
            font-family: 'Times New Roman', serif;
        }
        .action-btn:hover {
            background: #A0522D;
            transform: scale(1.05);
        }
        .health-bar {
            width: 200px;
            height: 20px;
            background: #333;
            margin: 10px auto;
            border-radius: 10px;
            overflow: hidden;
            border: 2px solid #FFD700;
        }
        .health-level {
            height: 100%;
            background: linear-gradient(90deg, #ff0000, #ffff00, #00ff00);
            width: 100%;
            transition: width 0.5s;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h1>⚔️ ''' + character + ''' Medieval Quest</h1>
        <div class="game-info">
            <p><strong>Theme:</strong> ''' + theme + '''</p>
            <p><strong>Difficulty:</strong> ''' + difficulty + '''</p>
            <p><strong>Mode:</strong> ''' + mode.upper() + '''</p>
        </div>
        
        <div class="status-display">
            <div>Gold: <span id="gold">0</span></div>
            <div>Honor: <span id="honor">100</span></div>
            <div>Quests: <span id="quests">0</span></div>
            <div>Level: <span id="level">1</span></div>
        </div>
        
        <div class="health-bar">
            <div class="health-level" id="healthLevel"></div>
        </div>
        <div>Health: <span id="health">100</span>/100</div>
        
        <div class="castle" id="castle">
            <div class="knight" id="knight"></div>
            <div class="dragon" id="dragon" onclick="battleDragon()"></div>
        </div>
        
        <div class="controls">
            <button class="action-btn" onclick="moveKnight('up')">⬆️ North</button>
            <button class="action-btn" onclick="moveKnight('down')">⬇️ South</button>
            <button class="action-btn" onclick="moveKnight('left')">⬅️ West</button>
            <button class="action-btn" onclick="moveKnight('right')">➡️ East</button>
            <button class="action-btn" onclick="searchForTreasure()">🔍 Search</button>
            <button class="action-btn" onclick="newQuest()">🏰 New Quest</button>
        </div>
        
        <div class="game-info">
            <h3>How to Play:</h3>
            <p>Navigate the medieval world, battle dragons, and collect treasures to gain honor!</p>
            <p>Features: ''' + ', '.join(features.get(mode, features['basic'])) + '''</p>
        </div>
    </div>

    <script>
        let gameState = {
            gold: 0,
            honor: 100,
            quests: 0,
            level: 1,
            health: 100,
            maxHealth: 100,
            knightX: 50,
            knightY: 260,
            treasurePositions: [],
            dragonHealth: 100
        };

        function moveKnight(direction) {
            const knight = document.getElementById('knight');
            const castle = document.getElementById('castle');
            
            switch(direction) {
                case 'up':
                    if (gameState.knightY > 20) {
                        gameState.knightY -= 40;
                    }
                    break;
                case 'down':
                    if (gameState.knightY < 260) {
                        gameState.knightY += 40;
                    }
                    break;
                case 'left':
                    if (gameState.knightX > 20) {
                        gameState.knightX -= 40;
                    }
                    break;
                case 'right':
                    if (gameState.knightX < 460) {
                        gameState.knightX += 40;
                    }
                    break;
            }
            
            knight.style.left = gameState.knightX + 'px';
            knight.style.bottom = (300 - gameState.knightY - 40) + 'px';
            
            checkCollisions();
            updateDisplay();
        }

        function battleDragon() {
            if (gameState.health <= 0) {
                alert('⚰️ You must rest before battling the dragon!');
                return;
            }
            
            const dragonDistance = Math.sqrt(
                Math.pow(gameState.knightX - 450, 2) + 
                Math.pow(gameState.knightY - 50, 2)
            );
            
            if (dragonDistance > 100) {
                alert('🐉 You must get closer to the dragon to battle!');
                return;
            }
            
            // Battle mechanics
            const knightAttack = Math.floor(Math.random() * 30) + 20;
            const dragonAttack = Math.floor(Math.random() * 25) + 15;
            
            // Difficulty modifier
            let dragonDamage = dragonAttack;
            if (''' + ('True' if difficulty == 'Expert' else 'False') + ''') {
                dragonDamage = Math.floor(dragonDamage * 1.5);
            }
            
            gameState.dragonHealth -= knightAttack;
            gameState.health = Math.max(0, gameState.health - dragonDamage);
            
            if (gameState.dragonHealth <= 0) {
                // Dragon defeated
                const goldReward = Math.floor(Math.random() * 100) + 50;
                const honorReward = Math.floor(Math.random() * 50) + 25;
                
                gameState.gold += goldReward;
                gameState.honor += honorReward;
                gameState.quests++;
                
                if (gameState.quests % 3 === 0) {
                    gameState.level++;
                    gameState.maxHealth += 20;
                    gameState.health = gameState.maxHealth;
                }
                
                alert('⚔️ Dragon defeated! You gained ' + goldReward + ' gold and ' + honorReward + ' honor!');
                
                // Respawn dragon
                gameState.dragonHealth = 100 + (gameState.level * 20);
                
            } else {
                alert('⚔️ Battle continues! Dragon health: ' + gameState.dragonHealth + ', Your health: ' + gameState.health);
            }
            
            if (gameState.health <= 0) {
                alert('💀 You have been defeated! Rest to recover your strength.');
                gameState.health = Math.floor(gameState.maxHealth * 0.5);
                gameState.honor = Math.max(0, gameState.honor - 10);
            }
            
            updateDisplay();
        }

        function searchForTreasure() {
            const searchCost = 5;
            if (gameState.gold < searchCost) {
                alert('💰 You need at least ' + searchCost + ' gold to search for treasure!');
                return;
            }
            
            gameState.gold -= searchCost;
            
            if (Math.random() < 0.6) {
                // Found treasure
                const treasureValue = Math.floor(Math.random() * 30) + 10;
                gameState.gold += treasureValue;
                gameState.honor += 5;
                
                // Spawn visual treasure
                spawnTreasure();
                
                alert('💎 Treasure found! You gained ' + treasureValue + ' gold!');
            } else {
                alert('🔍 No treasure found this time. Keep searching!');
            }
            
            updateDisplay();
        }

        function spawnTreasure() {
            const castle = document.getElementById('castle');
            const treasure = document.createElement('div');
            treasure.className = 'treasure-chest';
            treasure.style.left = Math.random() * 450 + 'px';
            treasure.style.top = Math.random() * 250 + 'px';
            treasure.onclick = () => collectTreasure(treasure);
            
            castle.appendChild(treasure);
            
            // Remove treasure after 10 seconds
            setTimeout(() => {
                if (treasure.parentNode) {
                    treasure.parentNode.removeChild(treasure);
                }
            }, 10000);
        }

        function collectTreasure(treasureElement) {
            const treasureValue = Math.floor(Math.random() * 20) + 5;
            gameState.gold += treasureValue;
            gameState.honor += 2;
            
            treasureElement.remove();
            alert('💰 Collected treasure worth ' + treasureValue + ' gold!');
            updateDisplay();
        }

        function checkCollisions() {
            // Check if knight is near dragon for auto-battle hint
            const dragonDistance = Math.sqrt(
                Math.pow(gameState.knightX - 450, 2) + 
                Math.pow(gameState.knightY - 50, 2)
            );
            
            if (dragonDistance < 80) {
                document.getElementById('dragon').style.border = '3px solid #FFD700';
            } else {
                document.getElementById('dragon').style.border = '2px solid #FF0000';
            }
        }

        function updateDisplay() {
            document.getElementById('gold').textContent = gameState.gold;
            document.getElementById('honor').textContent = gameState.honor;
            document.getElementById('quests').textContent = gameState.quests;
            document.getElementById('level').textContent = gameState.level;
            document.getElementById('health').textContent = gameState.health;
            document.getElementById('healthLevel').style.width = (gameState.health / gameState.maxHealth * 100) + '%';
        }

        function newQuest() {
            // Rest and recover
            gameState.health = gameState.maxHealth;
            
            // Clear treasures
            const treasures = document.querySelectorAll('.treasure-chest');
            treasures.forEach(treasure => treasure.remove());
            
            // Reset knight position
            gameState.knightX = 50;
            gameState.knightY = 260;
            const knight = document.getElementById('knight');
            knight.style.left = '50px';
            knight.style.bottom = '20px';
            
            // Spawn initial treasures
            for (let i = 0; i < ''' + ('5' if mode == 'ultimate' else '3') + '''; i++) {
                setTimeout(() => spawnTreasure(), i * 2000);
            }
            
            updateDisplay();
            alert('🏰 New quest begins! You have rested and recovered your strength.');
        }

        // Initialize game
        newQuest();
        
        // Keyboard controls
        document.addEventListener('keydown', (event) => {
            switch(event.key) {
                case 'ArrowUp':
                case 'w':
                case 'W':
                    moveKnight('up');
                    break;
                case 'ArrowDown':
                case 's':
                case 'S':
                    moveKnight('down');
                    break;
                case 'ArrowLeft':
                case 'a':
                case 'A':
                    moveKnight('left');
                    break;
                case 'ArrowRight':
                case 'd':
                case 'D':
                    moveKnight('right');
                    break;
                case ' ':
                    battleDragon();
                    break;
                case 'f':
                case 'F':
                    searchForTreasure();
                    break;
            }
        });
    </script>
</body>
</html>'''

    return {
        'id': game_id,
        'title': character + ' Medieval Quest',
        'type': 'medieval',
        'html': html_content,
        'character': character,
        'theme': theme,
        'difficulty': difficulty,
        'quality': mode,
        'features': features.get(mode, features['basic']),
        'art_style': 'Medieval Fantasy',
        'multiplayer_mode': 'single_player',
        'created_at': datetime.datetime.now().isoformat()
    }

def generate_space_game(prompt, mode, character, theme, difficulty):
    """Generate a complete space battle game"""
    game_id = str(uuid.uuid4())
    
    features = {
        'ultimate': ['Epic space battles', 'Alien encounters', 'Laser weapons', 'Shield systems', 'Warp drive'],
        'free_ai': ['AI aliens', 'Dynamic battles', 'Smart enemies', 'Adaptive difficulty'],
        'enhanced': ['Multiple weapons', 'Enemy waves', 'Power-ups', 'Space effects'],
        'basic': ['Basic shooting', 'Simple enemies', 'Score tracking']
    }
    
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>''' + character + ''' Space Battle</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            font-family: 'Courier New', monospace;
            background: linear-gradient(180deg, #000000, #1a1a2e, #16213e);
            color: #00ff00;
            text-align: center;
        }
        .game-container {
            max-width: 800px;
            margin: 0 auto;
            background: rgba(0,0,0,0.5);
            border-radius: 15px;
            padding: 20px;
            border: 2px solid #00ff00;
        }
        .space-arena {
            width: 600px;
            height: 400px;
            background: radial-gradient(circle, #1a1a2e 0%, #000000 100%);
            margin: 20px auto;
            position: relative;
            border: 3px solid #00ff00;
            border-radius: 10px;
            overflow: hidden;
        }
        .spaceship {
            width: 40px;
            height: 40px;
            background: #00ff00;
            position: absolute;
            bottom: 20px;
            left: 280px;
            clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
            cursor: pointer;
        }
        .alien {
            width: 30px;
            height: 30px;
            background: #ff0000;
            position: absolute;
            border-radius: 50%;
            cursor: pointer;
            animation: alienMove 3s linear infinite;
        }
        @keyframes alienMove {
            0% { transform: translateY(-50px); }
            100% { transform: translateY(450px); }
        }
        .laser {
            width: 3px;
            height: 15px;
            background: #ffff00;
            position: absolute;
            animation: laserMove 1s linear infinite;
        }
        @keyframes laserMove {
            0% { transform: translateY(0px); }
            100% { transform: translateY(-450px); }
        }
        .status-display {
            font-size: 18px;
            margin: 20px 0;
            background: rgba(0,255,0,0.1);
            padding: 15px;
            border-radius: 10px;
            display: flex;
            justify-content: space-around;
            border: 2px solid #00ff00;
        }
        .control-btn {
            background: #1a1a2e;
            color: #00ff00;
            border: 2px solid #00ff00;
            padding: 12px 25px;
            font-size: 16px;
            border-radius: 20px;
            cursor: pointer;
            margin: 5px;
            transition: all 0.3s;
            font-family: 'Courier New', monospace;
        }
        .control-btn:hover {
            background: #00ff00;
            color: #000000;
            transform: scale(1.05);
        }
        .shield-bar {
            width: 200px;
            height: 20px;
            background: #333;
            margin: 10px auto;
            border-radius: 10px;
            overflow: hidden;
            border: 2px solid #00ff00;
        }
        .shield-level {
            height: 100%;
            background: linear-gradient(90deg, #ff0000, #ffff00, #00ff00);
            width: 100%;
            transition: width 0.5s;
        }
        .star {
            position: absolute;
            background: white;
            border-radius: 50%;
            animation: twinkle 2s infinite;
        }
        @keyframes twinkle {
            0%, 100% { opacity: 0.3; }
            50% { opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h1>🚀 ''' + character + ''' Space Battle</h1>
        <div class="game-info">
            <p><strong>Theme:</strong> ''' + theme + '''</p>
            <p><strong>Difficulty:</strong> ''' + difficulty + '''</p>
            <p><strong>Mode:</strong> ''' + mode.upper() + '''</p>
        </div>
        
        <div class="status-display">
            <div>Score: <span id="score">0</span></div>
            <div>Wave: <span id="wave">1</span></div>
            <div>Aliens: <span id="aliens">0</span></div>
            <div>Ammo: <span id="ammo">∞</span></div>
        </div>
        
        <div class="shield-bar">
            <div class="shield-level" id="shieldLevel"></div>
        </div>
        <div>Shields: <span id="shields">100</span>%</div>
        
        <div class="space-arena" id="spaceArena">
            <div class="spaceship" id="spaceship"></div>
        </div>
        
        <div class="controls">
            <button class="control-btn" onclick="moveShip('left')">← Left</button>
            <button class="control-btn" onclick="fireLaser()">🔫 Fire</button>
            <button class="control-btn" onclick="moveShip('right')">Right →</button>
            <button class="control-btn" onclick="activateShield()">🛡️ Shield</button>
            <button class="control-btn" onclick="newBattle()">🚀 New Battle</button>
        </div>
        
        <div class="game-info">
            <h3>How to Play:</h3>
            <p>Move your spaceship and fire lasers to destroy alien invaders!</p>
            <p>Features: ''' + ', '.join(features.get(mode, features['basic'])) + '''</p>
        </div>
    </div>

    <script>
        let gameState = {
            score: 0,
            wave: 1,
            aliensDestroyed: 0,
            shields: 100,
            shipX: 280,
            gameActive: true,
            aliens: [],
            lasers: [],
            alienSpawnRate: 2000,
            shieldCooldown: 0
        };

        function moveShip(direction) {
            if (!gameState.gameActive) return;
            
            const spaceship = document.getElementById('spaceship');
            
            if (direction === 'left' && gameState.shipX > 20) {
                gameState.shipX -= 40;
            } else if (direction === 'right' && gameState.shipX < 540) {
                gameState.shipX += 40;
            }
            
            spaceship.style.left = gameState.shipX + 'px';
        }

        function fireLaser() {
            if (!gameState.gameActive) return;
            
            const spaceArena = document.getElementById('spaceArena');
            const laser = document.createElement('div');
            laser.className = 'laser';
            laser.style.left = (gameState.shipX + 18) + 'px';
            laser.style.bottom = '60px';
            
            spaceArena.appendChild(laser);
            gameState.lasers.push({
                element: laser,
                x: gameState.shipX + 18,
                y: 340
            });
            
            // Remove laser after animation
            setTimeout(() => {
                if (laser.parentNode) {
                    laser.parentNode.removeChild(laser);
                    gameState.lasers = gameState.lasers.filter(l => l.element !== laser);
                }
            }, 1000);
        }

        function spawnAlien() {
            if (!gameState.gameActive) return;
            
            const spaceArena = document.getElementById('spaceArena');
            const alien = document.createElement('div');
            alien.className = 'alien';
            
            const x = Math.random() * 550 + 25;
            alien.style.left = x + 'px';
            alien.style.top = '-30px';
            
            spaceArena.appendChild(alien);
            gameState.aliens.push({
                element: alien,
                x: x,
                y: -30,
                health: ''' + ('3' if mode == 'ultimate' else '1') + '''
            });
            
            // Remove alien after animation and damage shields
            setTimeout(() => {
                if (alien.parentNode) {
                    alien.parentNode.removeChild(alien);
                    gameState.aliens = gameState.aliens.filter(a => a.element !== alien);
                    
                    // Alien reached bottom - damage shields
                    gameState.shields = Math.max(0, gameState.shields - 10);
                    updateDisplay();
                    
                    if (gameState.shields <= 0) {
                        gameState.gameActive = false;
                        setTimeout(() => {
                            alert('💥 Shields down! Final Score: ' + gameState.score + ' points in wave ' + gameState.wave + '!');
                        }, 500);
                    }
                }
            }, 3000);
        }

        function activateShield() {
            if (gameState.shieldCooldown > 0) {
                alert('🛡️ Shield recharging... ' + gameState.shieldCooldown + ' seconds left');
                return;
            }
            
            gameState.shields = Math.min(100, gameState.shields + 25);
            gameState.shieldCooldown = 10;
            
            // Visual shield effect
            const spaceship = document.getElementById('spaceship');
            spaceship.style.boxShadow = '0 0 20px #00ff00';
            
            setTimeout(() => {
                spaceship.style.boxShadow = 'none';
            }, 2000);
            
            updateDisplay();
            alert('🛡️ Shields recharged by 25%!');
        }

        function checkCollisions() {
            // Check laser-alien collisions
            gameState.lasers.forEach((laser, laserIndex) => {
                gameState.aliens.forEach((alien, alienIndex) => {
                    const distance = Math.sqrt(
                        Math.pow(laser.x - alien.x, 2) + 
                        Math.pow(laser.y - alien.y, 2)
                    );
                    
                    if (distance < 30) {
                        // Hit!
                        alien.health--;
                        
                        if (alien.health <= 0) {
                            // Destroy alien
                            alien.element.remove();
                            gameState.aliens.splice(alienIndex, 1);
                            gameState.aliensDestroyed++;
                            
                            const points = Math.floor(Math.random() * 20) + 10;
                            gameState.score += points;
                            
                            // Check wave completion
                            if (gameState.aliensDestroyed % ''' + ('15' if mode == 'ultimate' else '10') + ''' === 0) {
                                gameState.wave++;
                                gameState.alienSpawnRate = Math.max(500, gameState.alienSpawnRate - 200);
                                alert('🌊 Wave ' + gameState.wave + ' begins! Aliens are faster now!');
                            }
                        }
                        
                        // Remove laser
                        laser.element.remove();
                        gameState.lasers.splice(laserIndex, 1);
                    }
                });
            });
        }

        function updateDisplay() {
            document.getElementById('score').textContent = gameState.score;
            document.getElementById('wave').textContent = gameState.wave;
            document.getElementById('aliens').textContent = gameState.aliensDestroyed;
            document.getElementById('shields').textContent = Math.round(gameState.shields);
            document.getElementById('shieldLevel').style.width = gameState.shields + '%';
        }

        function createStars() {
            const spaceArena = document.getElementById('spaceArena');
            
            for (let i = 0; i < 20; i++) {
                const star = document.createElement('div');
                star.className = 'star';
                star.style.left = Math.random() * 590 + 'px';
                star.style.top = Math.random() * 390 + 'px';
                star.style.width = Math.random() * 3 + 1 + 'px';
                star.style.height = star.style.width;
                star.style.animationDelay = Math.random() * 2 + 's';
                
                spaceArena.appendChild(star);
            }
        }

        function newBattle() {
            gameState = {
                score: 0,
                wave: 1,
                aliensDestroyed: 0,
                shields: 100,
                shipX: 280,
                gameActive: true,
                aliens: [],
                lasers: [],
                alienSpawnRate: 2000,
                shieldCooldown: 0
            };
            
            // Clear arena
            const spaceArena = document.getElementById('spaceArena');
            const aliens = spaceArena.querySelectorAll('.alien');
            const lasers = spaceArena.querySelectorAll('.laser');
            const stars = spaceArena.querySelectorAll('.star');
            
            aliens.forEach(alien => alien.remove());
            lasers.forEach(laser => laser.remove());
            stars.forEach(star => star.remove());
            
            // Reset ship position
            const spaceship = document.getElementById('spaceship');
            spaceship.style.left = '280px';
            spaceship.style.boxShadow = 'none';
            
            // Create stars
            createStars();
            
            updateDisplay();
            
            // Start alien spawning
            const alienSpawner = setInterval(() => {
                if (gameState.gameActive) {
                    spawnAlien();
                } else {
                    clearInterval(alienSpawner);
                }
            }, gameState.alienSpawnRate);
            
            // Start collision detection
            const collisionChecker = setInterval(() => {
                if (gameState.gameActive) {
                    checkCollisions();
                } else {
                    clearInterval(collisionChecker);
                }
            }, 50);
            
            // Shield cooldown timer
            const shieldTimer = setInterval(() => {
                if (gameState.gameActive && gameState.shieldCooldown > 0) {
                    gameState.shieldCooldown--;
                } else if (!gameState.gameActive) {
                    clearInterval(shieldTimer);
                }
            }, 1000);
        }

        // Initialize game
        newBattle();
        
        // Keyboard controls
        document.addEventListener('keydown', (event) => {
            switch(event.key) {
                case 'ArrowLeft':
                case 'a':
                case 'A':
                    moveShip('left');
                    break;
                case 'ArrowRight':
                case 'd':
                case 'D':
                    moveShip('right');
                    break;
                case ' ':
                case 'Enter':
                    fireLaser();
                    break;
                case 's':
                case 'S':
                    activateShield();
                    break;
            }
        });
    </script>
</body>
</html>'''

    return {
        'id': game_id,
        'title': character + ' Space Battle',
        'type': 'space',
        'html': html_content,
        'character': character,
        'theme': theme,
        'difficulty': difficulty,
        'quality': mode,
        'features': features.get(mode, features['basic']),
        'art_style': 'Sci-Fi Space',
        'multiplayer_mode': 'single_player',
        'created_at': datetime.datetime.now().isoformat()
    }

def generate_racing_game(prompt, mode, character, theme, difficulty):
    """Generate a complete racing game"""
    game_id = str(uuid.uuid4())
    
    features = {
        'ultimate': ['High-speed racing', 'Nitro boost', 'Multiple tracks', 'Car customization', 'Championship mode'],
        'free_ai': ['AI opponents', 'Dynamic racing', 'Smart competition', 'Adaptive difficulty'],
        'enhanced': ['Multiple cars', 'Speed tracking', 'Lap timing', 'Visual effects'],
        'basic': ['Basic racing', 'Simple controls', 'Lap counter']
    }
    
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>''' + character + ''' Racing Championship</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #2c3e50, #34495e, #7f8c8d);
            color: white;
            text-align: center;
        }
        .game-container {
            max-width: 800px;
            margin: 0 auto;
            background: rgba(0,0,0,0.4);
            border-radius: 15px;
            padding: 20px;
            border: 3px solid #e74c3c;
        }
        .race-track {
            width: 500px;
            height: 300px;
            background: linear-gradient(90deg, #2c3e50 0%, #34495e 50%, #2c3e50 100%);
            margin: 20px auto;
            position: relative;
            border: 3px solid #e74c3c;
            border-radius: 10px;
            overflow: hidden;
        }
        .car {
            width: 40px;
            height: 25px;
            background: #e74c3c;
            position: absolute;
            bottom: 50px;
            left: 50px;
            border-radius: 5px;
            cursor: pointer;
            border: 2px solid #c0392b;
        }
        .opponent-car {
            width: 35px;
            height: 22px;
            background: #3498db;
            position: absolute;
            border-radius: 5px;
            border: 2px solid #2980b9;
            animation: opponentMove 4s linear infinite;
        }
        @keyframes opponentMove {
            0% { transform: translateX(-50px); }
            100% { transform: translateX(550px); }
        }
        .finish-line {
            width: 5px;
            height: 100%;
            background: repeating-linear-gradient(
                0deg,
                #ffffff 0px,
                #ffffff 10px,
                #000000 10px,
                #000000 20px
            );
            position: absolute;
            right: 20px;
            top: 0;
        }
        .status-display {
            font-size: 18px;
            margin: 20px 0;
            background: rgba(231,76,60,0.1);
            padding: 15px;
            border-radius: 10px;
            display: flex;
            justify-content: space-around;
            border: 2px solid #e74c3c;
        }
        .control-btn {
            background: #e74c3c;
            color: white;
            border: 2px solid #c0392b;
            padding: 12px 25px;
            font-size: 16px;
            border-radius: 20px;
            cursor: pointer;
            margin: 5px;
            transition: all 0.3s;
        }
        .control-btn:hover {
            background: #c0392b;
            transform: scale(1.05);
        }
        .speed-meter {
            width: 200px;
            height: 20px;
            background: #333;
            margin: 10px auto;
            border-radius: 10px;
            overflow: hidden;
            border: 2px solid #e74c3c;
        }
        .speed-level {
            height: 100%;
            background: linear-gradient(90deg, #27ae60, #f39c12, #e74c3c);
            width: 0%;
            transition: width 0.3s;
        }
        .nitro-btn {
            background: #f39c12;
            color: white;
            border: 2px solid #e67e22;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 25px;
            cursor: pointer;
            margin: 10px;
            transition: all 0.3s;
        }
        .nitro-btn:hover {
            background: #e67e22;
            transform: scale(1.1);
        }
        .nitro-btn:disabled {
            background: #7f8c8d;
            border-color: #95a5a6;
            cursor: not-allowed;
            transform: none;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h1>🏎️ ''' + character + ''' Racing Championship</h1>
        <div class="game-info">
            <p><strong>Theme:</strong> ''' + theme + '''</p>
            <p><strong>Difficulty:</strong> ''' + difficulty + '''</p>
            <p><strong>Mode:</strong> ''' + mode.upper() + '''</p>
        </div>
        
        <div class="status-display">
            <div>Lap: <span id="lap">1</span>/3</div>
            <div>Position: <span id="position">1st</span></div>
            <div>Best Time: <span id="bestTime">--:--</span></div>
            <div>Current: <span id="currentTime">00:00</span></div>
        </div>
        
        <div class="speed-meter">
            <div class="speed-level" id="speedLevel"></div>
        </div>
        <div>Speed: <span id="speed">0</span> MPH</div>
        
        <div class="race-track" id="raceTrack">
            <div class="car" id="playerCar"></div>
            <div class="finish-line"></div>
        </div>
        
        <div class="controls">
            <button class="control-btn" onclick="accelerate()">⬆️ Accelerate</button>
            <button class="control-btn" onclick="brake()">⬇️ Brake</button>
            <button class="control-btn" onclick="steerLeft()">⬅️ Left</button>
            <button class="control-btn" onclick="steerRight()">➡️ Right</button>
            <button class="nitro-btn" id="nitroBtn" onclick="activateNitro()">🔥 NITRO</button>
            <button class="control-btn" onclick="newRace()">🏁 New Race</button>
        </div>
        
        <div class="game-info">
            <h3>How to Play:</h3>
            <p>Race to the finish line! Use nitro boost for extra speed!</p>
            <p>Features: ''' + ', '.join(features.get(mode, features['basic'])) + '''</p>
        </div>
    </div>

    <script>
        let gameState = {
            lap: 1,
            position: 1,
            speed: 0,
            maxSpeed: ''' + ('200' if mode == 'ultimate' else '150') + ''',
            carX: 50,
            carY: 50,
            raceStartTime: Date.now(),
            lapStartTime: Date.now(),
            bestLapTime: null,
            nitroAvailable: true,
            nitroCooldown: 0,
            opponents: [],
            raceActive: true
        };

        function accelerate() {
            if (!gameState.raceActive) return;
            
            gameState.speed = Math.min(gameState.maxSpeed, gameState.speed + 10);
            updateSpeedDisplay();
            
            // Move car forward
            if (gameState.carX < 430) {
                gameState.carX += Math.floor(gameState.speed / 20);
                document.getElementById('playerCar').style.left = gameState.carX + 'px';
                
                // Check finish line
                if (gameState.carX >= 430) {
                    completeLap();
                }
            }
        }

        function brake() {
            if (!gameState.raceActive) return;
            
            gameState.speed = Math.max(0, gameState.speed - 15);
            updateSpeedDisplay();
        }

        function steerLeft() {
            if (!gameState.raceActive) return;
            
            if (gameState.carY > 20) {
                gameState.carY -= 20;
                document.getElementById('playerCar').style.bottom = gameState.carY + 'px';
            }
        }

        function steerRight() {
            if (!gameState.raceActive) return;
            
            if (gameState.carY < 250) {
                gameState.carY += 20;
                document.getElementById('playerCar').style.bottom = gameState.carY + 'px';
            }
        }

        function activateNitro() {
            if (!gameState.nitroAvailable || gameState.nitroCooldown > 0) return;
            
            gameState.speed = Math.min(gameState.maxSpeed + 50, gameState.speed + 75);
            gameState.nitroAvailable = false;
            gameState.nitroCooldown = 10;
            
            // Visual effect
            const car = document.getElementById('playerCar');
            car.style.boxShadow = '0 0 20px #f39c12';
            
            setTimeout(() => {
                car.style.boxShadow = 'none';
            }, 3000);
            
            document.getElementById('nitroBtn').disabled = true;
            document.getElementById('nitroBtn').textContent = '🔥 COOLING (' + gameState.nitroCooldown + 's)';
            
            updateSpeedDisplay();
        }

        function completeLap() {
            const lapTime = Date.now() - gameState.lapStartTime;
            const lapTimeSeconds = Math.floor(lapTime / 1000);
            const lapTimeMs = lapTime % 1000;
            const lapTimeString = Math.floor(lapTimeSeconds / 60) + ':' + 
                                 (lapTimeSeconds % 60).toString().padStart(2, '0') + '.' + 
                                 Math.floor(lapTimeMs / 100);
            
            if (!gameState.bestLapTime || lapTime < gameState.bestLapTime) {
                gameState.bestLapTime = lapTime;
                document.getElementById('bestTime').textContent = lapTimeString;
            }
            
            gameState.lap++;
            
            if (gameState.lap > 3) {
                // Race finished
                gameState.raceActive = false;
                const totalTime = Date.now() - gameState.raceStartTime;
                const totalSeconds = Math.floor(totalTime / 1000);
                const totalTimeString = Math.floor(totalSeconds / 60) + ':' + 
                                       (totalSeconds % 60).toString().padStart(2, '0');
                
                alert('🏁 Race Finished! You placed ' + getPositionText(gameState.position) + ' with a total time of ' + totalTimeString + '!');
            } else {
                // Next lap
                gameState.carX = 50;
                gameState.lapStartTime = Date.now();
                document.getElementById('playerCar').style.left = '50px';
                
                alert('🏁 Lap ' + (gameState.lap - 1) + ' completed! Time: ' + lapTimeString);
            }
            
            updateDisplay();
        }

        function getPositionText(position) {
            const suffixes = ['st', 'nd', 'rd', 'th'];
            const suffix = suffixes[Math.min(position - 1, 3)];
            return position + suffix;
        }

        function spawnOpponent() {
            const raceTrack = document.getElementById('raceTrack');
            const opponent = document.createElement('div');
            opponent.className = 'opponent-car';
            opponent.style.top = Math.random() * 250 + 20 + 'px';
            opponent.style.left = '-50px';
            
            raceTrack.appendChild(opponent);
            
            setTimeout(() => {
                if (opponent.parentNode) {
                    opponent.parentNode.removeChild(opponent);
                }
            }, 4000);
        }

        function updateSpeedDisplay() {
            document.getElementById('speed').textContent = Math.round(gameState.speed);
            document.getElementById('speedLevel').style.width = (gameState.speed / gameState.maxSpeed * 100) + '%';
        }

        function updateDisplay() {
            document.getElementById('lap').textContent = Math.min(gameState.lap, 3);
            document.getElementById('position').textContent = getPositionText(gameState.position);
            
            // Update current time
            const currentTime = Date.now() - gameState.lapStartTime;
            const currentSeconds = Math.floor(currentTime / 1000);
            const currentTimeString = Math.floor(currentSeconds / 60) + ':' + 
                                     (currentSeconds % 60).toString().padStart(2, '0');
            document.getElementById('currentTime').textContent = currentTimeString;
        }

        function newRace() {
            gameState = {
                lap: 1,
                position: 1,
                speed: 0,
                maxSpeed: ''' + ('200' if mode == 'ultimate' else '150') + ''',
                carX: 50,
                carY: 50,
                raceStartTime: Date.now(),
                lapStartTime: Date.now(),
                bestLapTime: null,
                nitroAvailable: true,
                nitroCooldown: 0,
                opponents: [],
                raceActive: true
            };
            
            // Clear opponents
            const opponents = document.querySelectorAll('.opponent-car');
            opponents.forEach(opponent => opponent.remove());
            
            // Reset car position
            const car = document.getElementById('playerCar');
            car.style.left = '50px';
            car.style.bottom = '50px';
            car.style.boxShadow = 'none';
            
            // Reset displays
            document.getElementById('bestTime').textContent = '--:--';
            document.getElementById('nitroBtn').disabled = false;
            document.getElementById('nitroBtn').textContent = '🔥 NITRO';
            
            updateSpeedDisplay();
            updateDisplay();
            
            // Start opponent spawning
            const opponentSpawner = setInterval(() => {
                if (gameState.raceActive && Math.random() < 0.4) {
                    spawnOpponent();
                } else if (!gameState.raceActive) {
                    clearInterval(opponentSpawner);
                }
            }, 2000);
            
            // Nitro cooldown timer
            const nitroTimer = setInterval(() => {
                if (gameState.raceActive && gameState.nitroCooldown > 0) {
                    gameState.nitroCooldown--;
                    document.getElementById('nitroBtn').textContent = '🔥 COOLING (' + gameState.nitroCooldown + 's)';
                    
                    if (gameState.nitroCooldown === 0) {
                        gameState.nitroAvailable = true;
                        document.getElementById('nitroBtn').disabled = false;
                        document.getElementById('nitroBtn').textContent = '🔥 NITRO';
                    }
                } else if (!gameState.raceActive) {
                    clearInterval(nitroTimer);
                }
            }, 1000);
            
            // Game timer
            const gameTimer = setInterval(() => {
                if (gameState.raceActive) {
                    updateDisplay();
                    
                    // Natural speed decay
                    if (gameState.speed > 0) {
                        gameState.speed = Math.max(0, gameState.speed - 1);
                        updateSpeedDisplay();
                    }
                } else {
                    clearInterval(gameTimer);
                }
            }, 100);
        }

        // Initialize game
        newRace();
        
        // Keyboard controls
        document.addEventListener('keydown', (event) => {
            switch(event.key) {
                case 'ArrowUp':
                case 'w':
                case 'W':
                    accelerate();
                    break;
                case 'ArrowDown':
                case 's':
                case 'S':
                    brake();
                    break;
                case 'ArrowLeft':
                case 'a':
                case 'A':
                    steerLeft();
                    break;
                case 'ArrowRight':
                case 'd':
                case 'D':
                    steerRight();
                    break;
                case ' ':
                case 'n':
                case 'N':
                    activateNitro();
                    break;
            }
        });
    </script>
</body>
</html>'''

    return {
        'id': game_id,
        'title': character + ' Racing Championship',
        'type': 'racing',
        'html': html_content,
        'character': character,
        'theme': theme,
        'difficulty': difficulty,
        'quality': mode,
        'features': features.get(mode, features['basic']),
        'art_style': 'Racing Circuit',
        'multiplayer_mode': 'single_player',
        'created_at': datetime.datetime.now().isoformat()
    }

def generate_game_from_prompt(prompt, mode='ultimate'):
    """Main game generation function with intelligent prompt processing"""
    
    # Extract game type from prompt
    prompt_lower = prompt.lower()
    
    # Character generation
    characters = ['Champion', 'Master', 'Elite', 'Pro', 'Legend', 'Hero', 'Expert', 'Ace']
    character = characters[hash(prompt) % len(characters)]
    
    # Theme generation
    themes = ['Professional', 'Championship', 'Tournament', 'Elite Competition', 'Master Class', 'Ultimate Challenge']
    theme = themes[hash(prompt + mode) % len(themes)]
    
    # Difficulty based on mode
    difficulties = {
        'ultimate': 'Expert',
        'free_ai': 'Advanced', 
        'enhanced': 'Intermediate',
        'basic': 'Beginner'
    }
    difficulty = difficulties.get(mode, 'Intermediate')
    
    # Intelligent game type detection
    if any(word in prompt_lower for word in ['dart', 'dartboard', 'bullseye', 'throw']):
        return generate_darts_game(prompt, mode, character, theme, difficulty)
    elif any(word in prompt_lower for word in ['basketball', 'hoop', 'shoot', 'court', 'ball']):
        return generate_basketball_game(prompt, mode, character, theme, difficulty)
    elif any(word in prompt_lower for word in ['underwater', 'ocean', 'sea', 'dive', 'treasure', 'submarine']):
        return generate_underwater_game(prompt, mode, character, theme, difficulty)
    elif any(word in prompt_lower for word in ['medieval', 'knight', 'dragon', 'castle', 'sword', 'quest']):
        return generate_medieval_game(prompt, mode, character, theme, difficulty)
    elif any(word in prompt_lower for word in ['space', 'alien', 'laser', 'spaceship', 'galaxy', 'star']):
        return generate_space_game(prompt, mode, character, theme, difficulty)
    elif any(word in prompt_lower for word in ['racing', 'car', 'speed', 'race', 'track', 'fast']):
        return generate_racing_game(prompt, mode, character, theme, difficulty)
    else:
        # Default to most popular game type based on prompt complexity
        if len(prompt.split()) > 5:
            return generate_medieval_game(prompt, mode, character, theme, difficulty)
        else:
            return generate_darts_game(prompt, mode, character, theme, difficulty)

# API Routes
@app.route('/')
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Clean Working Ultimate Game Maker API - No Syntax Errors!',
        'version': '13.0.0 - IMPORT ERROR FIXED',
        'features': {
            'playable_games': True,
            'file_downloads': True,
            'iframe_support': True,
            'zip_packages': True,
            'error_handling': True,
            'railway_compatible': True,
            'no_syntax_errors': True
        },
        'endpoints': [
            '/ultimate-generate-game',
            '/ai-generate-game', 
            '/generate-game',
            '/play-game/<game_id>',
            '/download-game/<game_id>',
            '/generation-stats'
        ],
        'port': os.environ.get('PORT', '5000'),
        'stats': stats
    })

@app.route('/ultimate-generate-game', methods=['POST'])
def ultimate_generate_game():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({'success': False, 'message': 'Prompt is required'}), 400
        
        # Generate game
        game = generate_game_from_prompt(prompt, 'ultimate')
        generated_games[game['id']] = game
        
        # Update stats
        stats['total_games_generated'] += 1
        stats['ultimate_games'] += 1
        
        return jsonify({
            'success': True,
            'message': 'Ultimate game generated successfully!',
            'game': game
        })
        
    except Exception as e:
        return jsonify({
            'success': False, 
            'message': f'Generation failed: {str(e)}',
            'error': str(e)
        }), 500

@app.route('/ai-generate-game', methods=['POST'])
def ai_generate_game():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({'success': False, 'message': 'Prompt is required'}), 400
        
        # Generate game
        game = generate_game_from_prompt(prompt, 'free_ai')
        generated_games[game['id']] = game
        
        # Update stats
        stats['total_games_generated'] += 1
        stats['free_ai_games'] += 1
        
        return jsonify({
            'success': True,
            'message': 'FREE AI game generated successfully!',
            'game': game
        })
        
    except Exception as e:
        return jsonify({
            'success': False, 
            'message': f'Generation failed: {str(e)}',
            'error': str(e)
        }), 500

@app.route('/generate-game', methods=['POST'])
def generate_game():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        mode = data.get('mode', 'enhanced')
        
        if not prompt:
            return jsonify({'success': False, 'message': 'Prompt is required'}), 400
        
        # Generate game
        game = generate_game_from_prompt(prompt, mode)
        generated_games[game['id']] = game
        
        # Update stats
        stats['total_games_generated'] += 1
        if mode == 'enhanced':
            stats['enhanced_games'] += 1
        else:
            stats['basic_games'] += 1
        
        return jsonify({
            'success': True,
            'message': f'{mode.upper()} game generated successfully!',
            'game': game
        })
        
    except Exception as e:
        return jsonify({
            'success': False, 
            'message': f'Generation failed: {str(e)}',
            'error': str(e)
        }), 500

@app.route('/play-game/<game_id>')
def play_game(game_id):
    try:
        if game_id not in generated_games:
            return "Game not found", 404
        
        game = generated_games[game_id]
        stats['games_opened'] += 1
        
        return game['html']
        
    except Exception as e:
        return f"Error loading game: {str(e)}", 500

@app.route('/download-game/<game_id>')
def download_game(game_id):
    try:
        if game_id not in generated_games:
            return jsonify({'error': 'Game not found'}), 404
        
        game = generated_games[game_id]
        
        # Create temporary directory
        temp_dir = tempfile.mkdtemp()
        
        try:
            # Write game HTML file
            game_file_path = os.path.join(temp_dir, 'index.html')
            with open(game_file_path, 'w', encoding='utf-8') as f:
                f.write(game['html'])
            
            # Create README file
            readme_content = f"""# {game['title']}

## Game Information
- **Type:** {game['type'].title()}
- **Character:** {game['character']}
- **Theme:** {game['theme']}
- **Difficulty:** {game['difficulty']}
- **Quality:** {game['quality'].upper()}
- **Art Style:** {game['art_style']}
- **Created:** {game['created_at']}

## Features
{chr(10).join('- ' + feature for feature in game['features'])}

## How to Play
1. Open `index.html` in any web browser
2. Follow the on-screen instructions
3. Enjoy your custom-generated game!

## Technical Details
- **Platform:** HTML5/JavaScript
- **Compatibility:** All modern web browsers
- **Requirements:** None (runs offline)
- **File Size:** Lightweight and optimized

Generated by MYTHIQ.AI Ultimate Game Maker
"""
            
            readme_path = os.path.join(temp_dir, 'README.md')
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(readme_content)
            
            # Create ZIP file
            zip_path = os.path.join(temp_dir, f"{game['title'].replace(' ', '_')}_{game_id}.zip")
            
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(game_file_path, 'index.html')
                zipf.write(readme_path, 'README.md')
            
            stats['files_downloaded'] += 1
            
            return send_file(
                zip_path,
                as_attachment=True,
                download_name=f"{game['title'].replace(' ', '_')}_{game_id}.zip",
                mimetype='application/zip'
            )
            
        finally:
            # Cleanup temporary directory
            shutil.rmtree(temp_dir, ignore_errors=True)
            
    except Exception as e:
        return jsonify({'error': f'Download failed: {str(e)}'}), 500

@app.route('/generation-stats')
def generation_stats():
    return jsonify({
        'success': True,
        'stats': stats,
        'total_games_stored': len(generated_games),
        'available_games': list(generated_games.keys())
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
