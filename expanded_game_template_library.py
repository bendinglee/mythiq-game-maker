"""
🎮 EXPANDED GAME TEMPLATE LIBRARY
Comprehensive library of game templates for adventure, fantasy, underwater, and all game types
Each template generates complete, playable HTML5 games with unique mechanics
"""

from typing import Dict, List, Any
import random

class ExpandedGameTemplateLibrary:
    """
    Comprehensive game template library with detailed templates for all game types
    """
    
    def __init__(self):
        self.templates = {
            'underwater': self._create_underwater_templates(),
            'medieval': self._create_medieval_templates(),
            'space': self._create_space_templates(),
            'darts': self._create_darts_templates(),
            'basketball': self._create_basketball_templates(),
            'racing': self._create_racing_templates(),
            'puzzle': self._create_puzzle_templates(),
            'adventure': self._create_adventure_templates(),
            'fantasy': self._create_fantasy_templates()
        }

    def _create_underwater_templates(self) -> List[Dict]:
        """Create underwater adventure game templates"""
        return [
            {
                'name': 'Deep Sea Explorer',
                'description': 'Explore the ocean depths, collect treasures, and avoid sea creatures',
                'html_template': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(to bottom, #006994, #003d5c);
            font-family: Arial, sans-serif;
            overflow: hidden;
        }}
        #gameContainer {{
            width: 100vw;
            height: 100vh;
            position: relative;
            background: linear-gradient(to bottom, #4682B4, #191970);
        }}
        #player {{
            position: absolute;
            width: 40px;
            height: 40px;
            background: #FF69B4;
            border-radius: 50%;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            transition: all 0.1s;
        }}
        .treasure {{
            position: absolute;
            width: 20px;
            height: 20px;
            background: #FFD700;
            border-radius: 3px;
        }}
        .enemy {{
            position: absolute;
            width: 30px;
            height: 30px;
            background: #8B0000;
            border-radius: 50%;
        }}
        #ui {{
            position: absolute;
            top: 10px;
            left: 10px;
            color: white;
            font-size: 18px;
            z-index: 100;
        }}
        .bubble {{
            position: absolute;
            background: rgba(255,255,255,0.3);
            border-radius: 50%;
            animation: float 3s infinite;
        }}
        @keyframes float {{
            0%, 100% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-20px); }}
        }}
    </style>
</head>
<body>
    <div id="gameContainer">
        <div id="ui">
            <div>{ui_element1}: <span id="treasures">0</span></div>
            <div>{ui_element2}: <span id="lives">3</span></div>
            <div>{ui_element3}: <span id="depth">0</span></div>
        </div>
        <div id="player"></div>
    </div>
    
    <script>
        const player = document.getElementById('player');
        const gameContainer = document.getElementById('gameContainer');
        let playerX = window.innerWidth / 2;
        let playerY = window.innerHeight / 2;
        let treasures = 0;
        let lives = 3;
        let depth = 0;
        let gameObjects = [];
        
        // Player movement
        document.addEventListener('keydown', (e) => {{
            switch(e.key) {{
                case 'ArrowLeft':
                case 'a':
                case 'A':
                    playerX = Math.max(20, playerX - 20);
                    break;
                case 'ArrowRight':
                case 'd':
                case 'D':
                    playerX = Math.min(window.innerWidth - 20, playerX + 20);
                    break;
                case 'ArrowUp':
                case 'w':
                case 'W':
                    playerY = Math.max(20, playerY - 20);
                    depth = Math.max(0, depth - 1);
                    break;
                case 'ArrowDown':
                case 's':
                case 'S':
                    playerY = Math.min(window.innerHeight - 20, playerY + 20);
                    depth += 1;
                    break;
            }}
            player.style.left = playerX + 'px';
            player.style.top = playerY + 'px';
            document.getElementById('depth').textContent = depth;
        }});
        
        // Touch controls for mobile
        let touchStartX, touchStartY;
        gameContainer.addEventListener('touchstart', (e) => {{
            touchStartX = e.touches[0].clientX;
            touchStartY = e.touches[0].clientY;
        }});
        
        gameContainer.addEventListener('touchend', (e) => {{
            const touchEndX = e.changedTouches[0].clientX;
            const touchEndY = e.changedTouches[0].clientY;
            const deltaX = touchEndX - touchStartX;
            const deltaY = touchEndY - touchStartY;
            
            if (Math.abs(deltaX) > Math.abs(deltaY)) {{
                if (deltaX > 30) {{
                    playerX = Math.min(window.innerWidth - 20, playerX + 30);
                }} else if (deltaX < -30) {{
                    playerX = Math.max(20, playerX - 30);
                }}
            }} else {{
                if (deltaY > 30) {{
                    playerY = Math.min(window.innerHeight - 20, playerY + 30);
                    depth += 1;
                }} else if (deltaY < -30) {{
                    playerY = Math.max(20, playerY - 30);
                    depth = Math.max(0, depth - 1);
                }}
            }}
            
            player.style.left = playerX + 'px';
            player.style.top = playerY + 'px';
            document.getElementById('depth').textContent = depth;
        }});
        
        // Create treasures
        function createTreasure() {{
            const treasure = document.createElement('div');
            treasure.className = 'treasure';
            treasure.style.left = Math.random() * (window.innerWidth - 20) + 'px';
            treasure.style.top = Math.random() * (window.innerHeight - 20) + 'px';
            gameContainer.appendChild(treasure);
            gameObjects.push({{element: treasure, type: 'treasure'}});
        }}
        
        // Create enemies
        function createEnemy() {{
            const enemy = document.createElement('div');
            enemy.className = 'enemy';
            enemy.style.left = Math.random() * (window.innerWidth - 30) + 'px';
            enemy.style.top = Math.random() * (window.innerHeight - 30) + 'px';
            gameContainer.appendChild(enemy);
            gameObjects.push({{element: enemy, type: 'enemy'}});
        }}
        
        // Create bubbles for atmosphere
        function createBubble() {{
            const bubble = document.createElement('div');
            bubble.className = 'bubble';
            const size = Math.random() * 20 + 10;
            bubble.style.width = size + 'px';
            bubble.style.height = size + 'px';
            bubble.style.left = Math.random() * window.innerWidth + 'px';
            bubble.style.top = window.innerHeight + 'px';
            gameContainer.appendChild(bubble);
            
            // Animate bubble floating up
            let bubbleY = window.innerHeight;
            const bubbleInterval = setInterval(() => {{
                bubbleY -= 2;
                bubble.style.top = bubbleY + 'px';
                if (bubbleY < -50) {{
                    clearInterval(bubbleInterval);
                    if (bubble.parentNode) {{
                        bubble.parentNode.removeChild(bubble);
                    }}
                }}
            }}, 50);
        }}
        
        // Collision detection
        function checkCollisions() {{
            const playerRect = player.getBoundingClientRect();
            
            gameObjects.forEach((obj, index) => {{
                const objRect = obj.element.getBoundingClientRect();
                
                if (playerRect.left < objRect.right &&
                    playerRect.right > objRect.left &&
                    playerRect.top < objRect.bottom &&
                    playerRect.bottom > objRect.top) {{
                    
                    if (obj.type === 'treasure') {{
                        treasures++;
                        document.getElementById('treasures').textContent = treasures;
                        obj.element.remove();
                        gameObjects.splice(index, 1);
                    }} else if (obj.type === 'enemy') {{
                        lives--;
                        document.getElementById('lives').textContent = lives;
                        obj.element.remove();
                        gameObjects.splice(index, 1);
                        
                        if (lives <= 0) {{
                            alert('Game Over! You collected ' + treasures + ' treasures!');
                            location.reload();
                        }}
                    }}
                }}
            }});
        }}
        
        // Game loop
        setInterval(() => {{
            checkCollisions();
            
            // Spawn new objects
            if (Math.random() < 0.02) createTreasure();
            if (Math.random() < 0.01) createEnemy();
            if (Math.random() < 0.05) createBubble();
        }}, 100);
        
        // Initial objects
        for (let i = 0; i < 5; i++) {{
            createTreasure();
            createEnemy();
        }}
        
        // Instructions
        setTimeout(() => {{
            alert('🧜‍♀️ Welcome to {title}!\\n\\nControls:\\n• Arrow keys or WASD to move\\n• Touch/swipe on mobile\\n• Collect treasures, avoid sea creatures!\\n\\nCharacter: {character}');
        }}, 500);
    </script>
</body>
</html>
                ''',
                'mechanics': ['Swimming movement', 'Treasure collection', 'Enemy avoidance', 'Depth tracking'],
                'features': ['Underwater atmosphere', 'Bubble effects', 'Mobile touch controls', 'Progressive difficulty']
            },
            
            {
                'name': 'Mermaid Kingdom',
                'description': 'Rule an underwater kingdom, manage resources, and protect your realm',
                'html_template': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(to bottom, #006994, #003d5c);
            font-family: Arial, sans-serif;
        }}
        #gameContainer {{
            width: 100vw;
            height: 100vh;
            position: relative;
            background: radial-gradient(circle, #4682B4, #191970);
        }}
        #kingdom {{
            position: absolute;
            bottom: 50px;
            left: 50%;
            transform: translateX(-50%);
            width: 200px;
            height: 150px;
            background: linear-gradient(45deg, #8A2BE2, #4B0082);
            border-radius: 20px;
            border: 3px solid #FFD700;
        }}
        #player {{
            position: absolute;
            width: 50px;
            height: 50px;
            background: #FF69B4;
            border-radius: 50%;
            left: 50%;
            top: 60%;
            transform: translate(-50%, -50%);
        }}
        .resource {{
            position: absolute;
            width: 25px;
            height: 25px;
            border-radius: 50%;
            cursor: pointer;
        }}
        .pearl {{ background: #F0F8FF; }}
        .coral {{ background: #FF7F50; }}
        .seaweed {{ background: #228B22; }}
        #ui {{
            position: absolute;
            top: 10px;
            left: 10px;
            color: white;
            font-size: 16px;
            background: rgba(0,0,0,0.5);
            padding: 10px;
            border-radius: 10px;
        }}
        .building {{
            position: absolute;
            width: 40px;
            height: 40px;
            background: #4169E1;
            border-radius: 5px;
            cursor: pointer;
        }}
    </style>
</head>
<body>
    <div id="gameContainer">
        <div id="ui">
            <div>{ui_element1}: <span id="pearls">10</span></div>
            <div>{ui_element2}: <span id="population">5</span></div>
            <div>{ui_element3}: <span id="happiness">100</span></div>
            <div>Buildings: <span id="buildings">1</span></div>
        </div>
        <div id="kingdom"></div>
        <div id="player"></div>
    </div>
    
    <script>
        let pearls = 10;
        let population = 5;
        let happiness = 100;
        let buildings = 1;
        let resources = [];
        
        function updateUI() {{
            document.getElementById('pearls').textContent = pearls;
            document.getElementById('population').textContent = population;
            document.getElementById('happiness').textContent = happiness;
            document.getElementById('buildings').textContent = buildings;
        }}
        
        function createResource(type) {{
            const resource = document.createElement('div');
            resource.className = 'resource ' + type;
            resource.style.left = Math.random() * (window.innerWidth - 25) + 'px';
            resource.style.top = Math.random() * (window.innerHeight - 100) + 50 + 'px';
            
            resource.addEventListener('click', () => {{
                if (type === 'pearl') pearls += 2;
                else if (type === 'coral') happiness += 5;
                else if (type === 'seaweed') population += 1;
                
                resource.remove();
                updateUI();
            }});
            
            document.getElementById('gameContainer').appendChild(resource);
            resources.push(resource);
        }}
        
        function createBuilding() {{
            if (pearls >= 20) {{
                pearls -= 20;
                buildings += 1;
                population += 3;
                
                const building = document.createElement('div');
                building.className = 'building';
                building.style.left = Math.random() * (window.innerWidth - 40) + 'px';
                building.style.bottom = Math.random() * 200 + 100 + 'px';
                document.getElementById('gameContainer').appendChild(building);
                
                updateUI();
                alert('New building constructed! +3 population');
            }} else {{
                alert('Need 20 pearls to build!');
            }}
        }}
        
        // Click to build
        document.getElementById('kingdom').addEventListener('click', createBuilding);
        
        // Game loop
        setInterval(() => {{
            // Spawn resources
            if (Math.random() < 0.03) {{
                const types = ['pearl', 'coral', 'seaweed'];
                createResource(types[Math.floor(Math.random() * types.length)]);
            }}
            
            // Passive income
            if (Math.random() < 0.1) {{
                pearls += buildings;
                updateUI();
            }}
            
            // Happiness decay
            if (Math.random() < 0.05) {{
                happiness = Math.max(0, happiness - 1);
                updateUI();
            }}
        }}, 1000);
        
        // Initial resources
        for (let i = 0; i < 8; i++) {{
            const types = ['pearl', 'coral', 'seaweed'];
            createResource(types[Math.floor(Math.random() * types.length)]);
        }}
        
        setTimeout(() => {{
            alert('🧜‍♀️ Welcome to {title}!\\n\\nYou are the ruler of an underwater kingdom!\\n\\n• Click resources to collect them\\n• Click your kingdom to build (costs 20 pearls)\\n• Manage your population and happiness\\n\\nCharacter: {character}');
        }}, 500);
    </script>
</body>
</html>
                ''',
                'mechanics': ['Resource management', 'Kingdom building', 'Population growth', 'Happiness system'],
                'features': ['Strategic gameplay', 'Economic simulation', 'Progressive expansion', 'Royal theme']
            }
        ]

    def _create_medieval_templates(self) -> List[Dict]:
        """Create medieval fantasy game templates"""
        return [
            {
                'name': 'Castle Defense',
                'description': 'Defend your castle from waves of enemies using medieval weapons',
                'html_template': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(to bottom, #8B4513, #654321);
            font-family: 'Times New Roman', serif;
            overflow: hidden;
        }}
        #gameContainer {{
            width: 100vw;
            height: 100vh;
            position: relative;
            background: linear-gradient(to bottom, #87CEEB, #228B22);
        }}
        #castle {{
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 200px;
            height: 150px;
            background: #696969;
            border-radius: 10px 10px 0 0;
        }}
        #player {{
            position: absolute;
            width: 40px;
            height: 40px;
            background: #4169E1;
            border-radius: 5px;
            left: 50%;
            bottom: 150px;
            transform: translateX(-50%);
        }}
        .enemy {{
            position: absolute;
            width: 30px;
            height: 30px;
            background: #8B0000;
            border-radius: 5px;
        }}
        .projectile {{
            position: absolute;
            width: 8px;
            height: 8px;
            background: #FFD700;
            border-radius: 50%;
        }}
        #ui {{
            position: absolute;
            top: 10px;
            left: 10px;
            color: white;
            font-size: 18px;
            text-shadow: 2px 2px 4px #000;
            background: rgba(0,0,0,0.7);
            padding: 10px;
            border-radius: 10px;
        }}
    </style>
</head>
<body>
    <div id="gameContainer">
        <div id="ui">
            <div>{ui_element1}: <span id="gold">100</span></div>
            <div>{ui_element2}: <span id="health">100</span></div>
            <div>{ui_element3}: <span id="wave">1</span></div>
            <div>Enemies: <span id="enemies">0</span></div>
        </div>
        <div id="castle"></div>
        <div id="player"></div>
    </div>
    
    <script>
        let gold = 100;
        let health = 100;
        let wave = 1;
        let enemies = [];
        let projectiles = [];
        let gameRunning = true;
        
        function updateUI() {{
            document.getElementById('gold').textContent = gold;
            document.getElementById('health').textContent = health;
            document.getElementById('wave').textContent = wave;
            document.getElementById('enemies').textContent = enemies.length;
        }}
        
        function createEnemy() {{
            const enemy = document.createElement('div');
            enemy.className = 'enemy';
            enemy.style.left = Math.random() * (window.innerWidth - 30) + 'px';
            enemy.style.top = '0px';
            document.getElementById('gameContainer').appendChild(enemy);
            
            enemies.push({{
                element: enemy,
                x: parseFloat(enemy.style.left),
                y: 0,
                health: 3
            }});
        }}
        
        function createProjectile(targetX, targetY) {{
            const projectile = document.createElement('div');
            projectile.className = 'projectile';
            projectile.style.left = window.innerWidth / 2 + 'px';
            projectile.style.bottom = '150px';
            document.getElementById('gameContainer').appendChild(projectile);
            
            const startX = window.innerWidth / 2;
            const startY = window.innerHeight - 150;
            const dx = targetX - startX;
            const dy = targetY - startY;
            const distance = Math.sqrt(dx * dx + dy * dy);
            const speed = 10;
            
            projectiles.push({{
                element: projectile,
                x: startX,
                y: startY,
                vx: (dx / distance) * speed,
                vy: (dy / distance) * speed
            }});
        }}
        
        // Click to shoot
        document.getElementById('gameContainer').addEventListener('click', (e) => {{
            if (gameRunning) {{
                createProjectile(e.clientX, e.clientY);
            }}
        }});
        
        // Game loop
        const gameLoop = setInterval(() => {{
            if (!gameRunning) return;
            
            // Move enemies
            enemies.forEach((enemy, index) => {{
                enemy.y += 2;
                enemy.element.style.top = enemy.y + 'px';
                
                // Check if enemy reached castle
                if (enemy.y > window.innerHeight - 180) {{
                    health -= 10;
                    enemy.element.remove();
                    enemies.splice(index, 1);
                    
                    if (health <= 0) {{
                        gameRunning = false;
                        alert('Castle destroyed! You survived ' + wave + ' waves!');
                        location.reload();
                    }}
                }}
            }});
            
            // Move projectiles
            projectiles.forEach((projectile, pIndex) => {{
                projectile.x += projectile.vx;
                projectile.y += projectile.vy;
                projectile.element.style.left = projectile.x + 'px';
                projectile.element.style.top = projectile.y + 'px';
                
                // Remove if off screen
                if (projectile.x < 0 || projectile.x > window.innerWidth || 
                    projectile.y < 0 || projectile.y > window.innerHeight) {{
                    projectile.element.remove();
                    projectiles.splice(pIndex, 1);
                    return;
                }}
                
                // Check collision with enemies
                enemies.forEach((enemy, eIndex) => {{
                    const dx = projectile.x - enemy.x;
                    const dy = projectile.y - enemy.y;
                    const distance = Math.sqrt(dx * dx + dy * dy);
                    
                    if (distance < 20) {{
                        enemy.health--;
                        projectile.element.remove();
                        projectiles.splice(pIndex, 1);
                        
                        if (enemy.health <= 0) {{
                            gold += 10;
                            enemy.element.remove();
                            enemies.splice(eIndex, 1);
                        }}
                    }}
                }});
            }});
            
            // Spawn enemies
            if (Math.random() < 0.02 + (wave * 0.005)) {{
                createEnemy();
            }}
            
            // Next wave
            if (enemies.length === 0 && Math.random() < 0.1) {{
                wave++;
                for (let i = 0; i < wave + 2; i++) {{
                    setTimeout(() => createEnemy(), i * 500);
                }}
            }}
            
            updateUI();
        }}, 50);
        
        setTimeout(() => {{
            alert('⚔️ Welcome to {title}!\\n\\nDefend your castle from enemy invaders!\\n\\n• Click anywhere to shoot arrows\\n• Earn gold by defeating enemies\\n• Survive as many waves as possible\\n\\nCharacter: {character}');
        }}, 500);
    </script>
</body>
</html>
                ''',
                'mechanics': ['Tower defense', 'Wave survival', 'Resource management', 'Projectile combat'],
                'features': ['Medieval atmosphere', 'Progressive difficulty', 'Strategic positioning', 'Castle theme']
            }
        ]

    def _create_space_templates(self) -> List[Dict]:
        """Create space adventure game templates"""
        return [
            {
                'name': 'Galactic Warrior',
                'description': 'Battle aliens across the galaxy in epic space combat',
                'html_template': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: #000;
            font-family: 'Courier New', monospace;
            overflow: hidden;
        }}
        #gameContainer {{
            width: 100vw;
            height: 100vh;
            position: relative;
            background: radial-gradient(circle, #191970, #000);
        }}
        #player {{
            position: absolute;
            width: 40px;
            height: 40px;
            background: #00BFFF;
            clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
            left: 50%;
            bottom: 50px;
            transform: translateX(-50%);
        }}
        .alien {{
            position: absolute;
            width: 30px;
            height: 30px;
            background: #FF4500;
            border-radius: 50%;
        }}
        .laser {{
            position: absolute;
            width: 4px;
            height: 15px;
            background: #00FF00;
        }}
        .star {{
            position: absolute;
            width: 2px;
            height: 2px;
            background: white;
            border-radius: 50%;
        }}
        #ui {{
            position: absolute;
            top: 10px;
            left: 10px;
            color: #00FF00;
            font-size: 16px;
            text-shadow: 0 0 10px #00FF00;
        }}
    </style>
</head>
<body>
    <div id="gameContainer">
        <div id="ui">
            <div>{ui_element1}: <span id="energy">100</span></div>
            <div>{ui_element2}: <span id="shields">100</span></div>
            <div>{ui_element3}: <span id="sector">1</span></div>
            <div>Score: <span id="score">0</span></div>
        </div>
        <div id="player"></div>
    </div>
    
    <script>
        const player = document.getElementById('player');
        let playerX = window.innerWidth / 2;
        let energy = 100;
        let shields = 100;
        let sector = 1;
        let score = 0;
        let aliens = [];
        let lasers = [];
        let stars = [];
        
        // Create stars background
        for (let i = 0; i < 100; i++) {{
            const star = document.createElement('div');
            star.className = 'star';
            star.style.left = Math.random() * window.innerWidth + 'px';
            star.style.top = Math.random() * window.innerHeight + 'px';
            document.getElementById('gameContainer').appendChild(star);
            stars.push(star);
        }}
        
        // Player movement
        document.addEventListener('keydown', (e) => {{
            switch(e.key) {{
                case 'ArrowLeft':
                case 'a':
                case 'A':
                    playerX = Math.max(20, playerX - 25);
                    break;
                case 'ArrowRight':
                case 'd':
                case 'D':
                    playerX = Math.min(window.innerWidth - 20, playerX + 25);
                    break;
                case ' ':
                case 'ArrowUp':
                case 'w':
                case 'W':
                    fireLaser();
                    break;
            }}
            player.style.left = playerX + 'px';
        }});
        
        // Touch controls
        let touchStartX;
        document.addEventListener('touchstart', (e) => {{
            touchStartX = e.touches[0].clientX;
        }});
        
        document.addEventListener('touchend', (e) => {{
            const touchEndX = e.changedTouches[0].clientX;
            const deltaX = touchEndX - touchStartX;
            
            if (Math.abs(deltaX) > 30) {{
                if (deltaX > 0) {{
                    playerX = Math.min(window.innerWidth - 20, playerX + 40);
                }} else {{
                    playerX = Math.max(20, playerX - 40);
                }}
                player.style.left = playerX + 'px';
            }} else {{
                fireLaser();
            }}
        }});
        
        function fireLaser() {{
            if (energy >= 5) {{
                energy -= 5;
                const laser = document.createElement('div');
                laser.className = 'laser';
                laser.style.left = playerX + 'px';
                laser.style.bottom = '90px';
                document.getElementById('gameContainer').appendChild(laser);
                
                lasers.push({{
                    element: laser,
                    x: playerX,
                    y: window.innerHeight - 90
                }});
                
                updateUI();
            }}
        }}
        
        function createAlien() {{
            const alien = document.createElement('div');
            alien.className = 'alien';
            alien.style.left = Math.random() * (window.innerWidth - 30) + 'px';
            alien.style.top = '0px';
            document.getElementById('gameContainer').appendChild(alien);
            
            aliens.push({{
                element: alien,
                x: parseFloat(alien.style.left),
                y: 0
            }});
        }}
        
        function updateUI() {{
            document.getElementById('energy').textContent = energy;
            document.getElementById('shields').textContent = shields;
            document.getElementById('sector').textContent = sector;
            document.getElementById('score').textContent = score;
        }}
        
        // Game loop
        setInterval(() => {{
            // Move stars
            stars.forEach(star => {{
                let y = parseFloat(star.style.top) || 0;
                y += 2;
                if (y > window.innerHeight) {{
                    y = -2;
                    star.style.left = Math.random() * window.innerWidth + 'px';
                }}
                star.style.top = y + 'px';
            }});
            
            // Move aliens
            aliens.forEach((alien, index) => {{
                alien.y += 3;
                alien.element.style.top = alien.y + 'px';
                
                if (alien.y > window.innerHeight) {{
                    alien.element.remove();
                    aliens.splice(index, 1);
                }}
                
                // Check collision with player
                const dx = alien.x - playerX;
                const dy = alien.y - (window.innerHeight - 50);
                if (Math.sqrt(dx*dx + dy*dy) < 35) {{
                    shields -= 20;
                    alien.element.remove();
                    aliens.splice(index, 1);
                    
                    if (shields <= 0) {{
                        alert('Ship destroyed! Final score: ' + score);
                        location.reload();
                    }}
                }}
            }});
            
            // Move lasers
            lasers.forEach((laser, lIndex) => {{
                laser.y -= 8;
                laser.element.style.bottom = (window.innerHeight - laser.y) + 'px';
                
                if (laser.y < 0) {{
                    laser.element.remove();
                    lasers.splice(lIndex, 1);
                    return;
                }}
                
                // Check collision with aliens
                aliens.forEach((alien, aIndex) => {{
                    const dx = laser.x - alien.x;
                    const dy = laser.y - alien.y;
                    if (Math.sqrt(dx*dx + dy*dy) < 25) {{
                        score += 100;
                        laser.element.remove();
                        alien.element.remove();
                        lasers.splice(lIndex, 1);
                        aliens.splice(aIndex, 1);
                    }}
                }});
            }});
            
            // Spawn aliens
            if (Math.random() < 0.02 + (sector * 0.005)) {{
                createAlien();
            }}
            
            // Regenerate energy
            if (energy < 100 && Math.random() < 0.1) {{
                energy = Math.min(100, energy + 1);
            }}
            
            // Next sector
            if (score > 0 && score % 1000 === 0) {{
                sector++;
            }}
            
            updateUI();
        }}, 50);
        
        setTimeout(() => {{
            alert('🚀 Welcome to {title}!\\n\\nDefend the galaxy from alien invaders!\\n\\n• Arrow keys or A/D to move\\n• Spacebar or W to shoot\\n• Touch: swipe to move, tap to shoot\\n\\nCharacter: {character}');
        }}, 500);
    </script>
</body>
</html>
                ''',
                'mechanics': ['Space combat', 'Alien shooting', 'Energy management', 'Progressive sectors'],
                'features': ['Starfield background', 'Sci-fi atmosphere', 'Touch controls', 'Score system']
            }
        ]

    def _create_darts_templates(self) -> List[Dict]:
        """Create darts game templates"""
        return [
            {
                'name': 'Bulls Eye Challenge',
                'description': 'Test your precision in this classic darts game',
                'html_template': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(45deg, #8B4513, #A0522D);
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }}
        #gameContainer {{
            text-align: center;
            background: rgba(0,0,0,0.8);
            padding: 20px;
            border-radius: 15px;
            color: white;
        }}
        #dartboard {{
            width: 300px;
            height: 300px;
            border-radius: 50%;
            background: radial-gradient(circle, #FFD700 0%, #FFD700 5%, #8B0000 5%, #8B0000 15%, #228B22 15%, #228B22 25%, #8B0000 25%, #8B0000 35%, #228B22 35%, #228B22 45%, #000 45%, #000 50%, #FFD700 50%, #FFD700 55%, #8B0000 55%);
            margin: 20px auto;
            position: relative;
            cursor: crosshair;
            border: 5px solid #000;
        }}
        #ui {{
            margin: 20px 0;
            font-size: 18px;
        }}
        .dart {{
            position: absolute;
            width: 8px;
            height: 8px;
            background: #FF4500;
            border-radius: 50%;
            border: 2px solid #000;
        }}
        #instructions {{
            margin-top: 20px;
            font-size: 14px;
            color: #CCC;
        }}
    </style>
</head>
<body>
    <div id="gameContainer">
        <h2>{title}</h2>
        <div id="ui">
            <div>{ui_element1}: <span id="score">0</span></div>
            <div>{ui_element2}: <span id="darts">10</span></div>
            <div>{ui_element3}: <span id="round">1</span></div>
        </div>
        <div id="dartboard"></div>
        <div id="instructions">
            Click on the dartboard to throw darts!<br>
            Bullseye (center) = 50 points<br>
            Inner ring = 25 points<br>
            Outer rings = 10-5 points
        </div>
    </div>
    
    <script>
        let score = 0;
        let darts = 10;
        let round = 1;
        
        function updateUI() {{
            document.getElementById('score').textContent = score;
            document.getElementById('darts').textContent = darts;
            document.getElementById('round').textContent = round;
        }}
        
        function calculateScore(x, y) {{
            const centerX = 150;
            const centerY = 150;
            const distance = Math.sqrt((x - centerX) ** 2 + (y - centerY) ** 2);
            
            if (distance <= 15) return 50; // Bullseye
            if (distance <= 30) return 25; // Inner ring
            if (distance <= 60) return 15; // Good ring
            if (distance <= 90) return 10; // Decent ring
            if (distance <= 120) return 5; // Outer ring
            return 0; // Miss
        }}
        
        document.getElementById('dartboard').addEventListener('click', (e) => {{
            if (darts <= 0) return;
            
            const rect = e.target.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            // Create dart visual
            const dart = document.createElement('div');
            dart.className = 'dart';
            dart.style.left = (x - 4) + 'px';
            dart.style.top = (y - 4) + 'px';
            document.getElementById('dartboard').appendChild(dart);
            
            // Calculate and add score
            const points = calculateScore(x, y);
            score += points;
            darts--;
            
            // Show points
            if (points > 0) {{
                const pointsDisplay = document.createElement('div');
                pointsDisplay.textContent = '+' + points;
                pointsDisplay.style.position = 'absolute';
                pointsDisplay.style.left = x + 'px';
                pointsDisplay.style.top = (y - 20) + 'px';
                pointsDisplay.style.color = '#FFD700';
                pointsDisplay.style.fontWeight = 'bold';
                pointsDisplay.style.pointerEvents = 'none';
                document.getElementById('dartboard').appendChild(pointsDisplay);
                
                setTimeout(() => {{
                    if (pointsDisplay.parentNode) {{
                        pointsDisplay.parentNode.removeChild(pointsDisplay);
                    }}
                }}, 1000);
            }}
            
            updateUI();
            
            // Check if round is over
            if (darts <= 0) {{
                setTimeout(() => {{
                    alert('Round ' + round + ' complete!\\nScore: ' + score + ' points\\n\\nStarting next round...');
                    round++;
                    darts = 10;
                    
                    // Clear darts
                    const dartElements = document.querySelectorAll('.dart');
                    dartElements.forEach(dart => dart.remove());
                    
                    updateUI();
                }}, 500);
            }}
        }});
        
        setTimeout(() => {{
            alert('🎯 Welcome to {title}!\\n\\nTest your precision and aim!\\n\\n• Click on the dartboard to throw darts\\n• Aim for the center for maximum points\\n• Complete rounds to improve your score\\n\\nCharacter: {character}');
        }}, 500);
    </script>
</body>
</html>
                ''',
                'mechanics': ['Precision aiming', 'Score calculation', 'Round progression', 'Visual feedback'],
                'features': ['Realistic dartboard', 'Point system', 'Round tracking', 'Dart visualization']
            }
        ]

    def _create_basketball_templates(self) -> List[Dict]:
        """Create basketball game templates"""
        return [
            {
                'name': 'Court Master',
                'description': 'Shoot hoops and score baskets in this basketball challenge',
                'html_template': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(to bottom, #8B4513, #D2691E);
            font-family: Arial, sans-serif;
            overflow: hidden;
        }}
        #gameContainer {{
            width: 100vw;
            height: 100vh;
            position: relative;
            background: linear-gradient(to bottom, #87CEEB, #8B4513);
        }}
        #court {{
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 200px;
            background: #D2691E;
            border-top: 5px solid #8B4513;
        }}
        #hoop {{
            position: absolute;
            top: 100px;
            right: 50px;
            width: 80px;
            height: 10px;
            background: #FF4500;
            border-radius: 50px;
        }}
        #backboard {{
            position: absolute;
            top: 80px;
            right: 40px;
            width: 10px;
            height: 60px;
            background: #FFF;
        }}
        #player {{
            position: absolute;
            width: 40px;
            height: 40px;
            background: #4169E1;
            border-radius: 50%;
            bottom: 200px;
            left: 100px;
        }}
        #ball {{
            position: absolute;
            width: 20px;
            height: 20px;
            background: #FF8C00;
            border-radius: 50%;
            bottom: 240px;
            left: 110px;
            cursor: pointer;
        }}
        #ui {{
            position: absolute;
            top: 10px;
            left: 10px;
            color: white;
            font-size: 18px;
            text-shadow: 2px 2px 4px #000;
        }}
        .trajectory {{
            position: absolute;
            width: 4px;
            height: 4px;
            background: rgba(255,140,0,0.5);
            border-radius: 50%;
        }}
    </style>
</head>
<body>
    <div id="gameContainer">
        <div id="ui">
            <div>{ui_element1}: <span id="score">0</span></div>
            <div>{ui_element2}: <span id="time">60</span></div>
            <div>{ui_element3}: <span id="shots">0</span></div>
        </div>
        <div id="court"></div>
        <div id="backboard"></div>
        <div id="hoop"></div>
        <div id="player"></div>
        <div id="ball"></div>
    </div>
    
    <script>
        let score = 0;
        let time = 60;
        let shots = 0;
        let ballInMotion = false;
        const ball = document.getElementById('ball');
        const hoop = document.getElementById('hoop');
        
        function updateUI() {{
            document.getElementById('score').textContent = score;
            document.getElementById('time').textContent = time;
            document.getElementById('shots').textContent = shots;
        }}
        
        function resetBall() {{
            ball.style.left = '110px';
            ball.style.bottom = '240px';
            ballInMotion = false;
        }}
        
        function shootBall(targetX, targetY) {{
            if (ballInMotion) return;
            
            ballInMotion = true;
            shots++;
            
            const startX = 110;
            const startY = 240;
            const endX = targetX;
            const endY = window.innerHeight - targetY;
            
            let progress = 0;
            const shootInterval = setInterval(() => {{
                progress += 0.05;
                
                if (progress >= 1) {{
                    clearInterval(shootInterval);
                    
                    // Check if ball went through hoop
                    const hoopRect = hoop.getBoundingClientRect();
                    const ballRect = ball.getBoundingClientRect();
                    
                    if (ballRect.left > hoopRect.left - 10 && 
                        ballRect.right < hoopRect.right + 10 &&
                        ballRect.top < hoopRect.bottom + 20 &&
                        ballRect.bottom > hoopRect.top - 20) {{
                        score += 2;
                        
                        // Show score animation
                        const scoreDisplay = document.createElement('div');
                        scoreDisplay.textContent = '+2';
                        scoreDisplay.style.position = 'absolute';
                        scoreDisplay.style.left = hoopRect.left + 'px';
                        scoreDisplay.style.top = hoopRect.top - 30 + 'px';
                        scoreDisplay.style.color = '#FFD700';
                        scoreDisplay.style.fontSize = '24px';
                        scoreDisplay.style.fontWeight = 'bold';
                        scoreDisplay.style.pointerEvents = 'none';
                        document.body.appendChild(scoreDisplay);
                        
                        setTimeout(() => {{
                            if (scoreDisplay.parentNode) {{
                                scoreDisplay.parentNode.removeChild(scoreDisplay);
                            }}
                        }}, 1000);
                    }}
                    
                    setTimeout(resetBall, 500);
                    updateUI();
                    return;
                }}
                
                // Parabolic trajectory
                const x = startX + (endX - startX) * progress;
                const baseY = startY + (endY - startY) * progress;
                const arc = Math.sin(progress * Math.PI) * 100;
                const y = baseY + arc;
                
                ball.style.left = x + 'px';
                ball.style.bottom = y + 'px';
            }}, 20);
        }}
        
        // Click to shoot
        document.getElementById('gameContainer').addEventListener('click', (e) => {{
            if (!ballInMotion && time > 0) {{
                shootBall(e.clientX, e.clientY);
            }}
        }});
        
        // Game timer
        const gameTimer = setInterval(() => {{
            time--;
            updateUI();
            
            if (time <= 0) {{
                clearInterval(gameTimer);
                alert('Time\'s up!\\n\\nFinal Score: ' + score + ' points\\nShots Made: ' + Math.floor(score/2) + '/' + shots + '\\nAccuracy: ' + Math.round((score/2)/shots*100) + '%');
            }}
        }}, 1000);
        
        setTimeout(() => {{
            alert('🏀 Welcome to {title}!\\n\\nShoot hoops and score points!\\n\\n• Click anywhere to shoot the ball\\n• Aim for the orange hoop\\n• Score as many baskets as possible\\n• You have 60 seconds!\\n\\nCharacter: {character}');
        }}, 500);
    </script>
</body>
</html>
                ''',
                'mechanics': ['Trajectory shooting', 'Time pressure', 'Accuracy tracking', 'Score system'],
                'features': ['Realistic physics', 'Court environment', 'Timer challenge', 'Accuracy statistics']
            }
        ]

    def _create_racing_templates(self) -> List[Dict]:
        """Create racing game templates"""
        return [
            {
                'name': 'Speed Racer',
                'description': 'Race at high speeds and avoid obstacles on the track',
                'html_template': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: #000;
            font-family: Arial, sans-serif;
            overflow: hidden;
        }}
        #gameContainer {{
            width: 100vw;
            height: 100vh;
            position: relative;
            background: linear-gradient(to bottom, #87CEEB, #228B22);
        }}
        #track {{
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 300px;
            background: #696969;
            border-top: 10px solid #FFD700;
        }}
        #player {{
            position: absolute;
            width: 40px;
            height: 60px;
            background: #FF0000;
            border-radius: 5px;
            bottom: 50px;
            left: 50%;
            transform: translateX(-50%);
        }}
        .obstacle {{
            position: absolute;
            width: 35px;
            height: 55px;
            background: #4169E1;
            border-radius: 5px;
        }}
        .road-line {{
            position: absolute;
            width: 4px;
            height: 30px;
            background: #FFF;
            left: 50%;
            transform: translateX(-50%);
        }}
        #ui {{
            position: absolute;
            top: 10px;
            left: 10px;
            color: white;
            font-size: 18px;
            text-shadow: 2px 2px 4px #000;
        }}
    </style>
</head>
<body>
    <div id="gameContainer">
        <div id="ui">
            <div>{ui_element1}: <span id="speed">0</span> MPH</div>
            <div>{ui_element2}: <span id="distance">0</span>m</div>
            <div>{ui_element3}: <span id="position">1st</span></div>
        </div>
        <div id="track"></div>
        <div id="player"></div>
    </div>
    
    <script>
        const player = document.getElementById('player');
        let playerX = window.innerWidth / 2;
        let speed = 0;
        let distance = 0;
        let position = 1;
        let obstacles = [];
        let roadLines = [];
        let gameRunning = true;
        
        // Player movement
        document.addEventListener('keydown', (e) => {{
            if (!gameRunning) return;
            
            switch(e.key) {{
                case 'ArrowLeft':
                case 'a':
                case 'A':
                    playerX = Math.max(50, playerX - 30);
                    break;
                case 'ArrowRight':
                case 'd':
                case 'D':
                    playerX = Math.min(window.innerWidth - 50, playerX + 30);
                    break;
                case 'ArrowUp':
                case 'w':
                case 'W':
                    speed = Math.min(120, speed + 5);
                    break;
                case 'ArrowDown':
                case 's':
                case 'S':
                    speed = Math.max(0, speed - 5);
                    break;
            }}
            player.style.left = playerX + 'px';
        }});
        
        // Touch controls
        let touchStartX, touchStartY;
        document.addEventListener('touchstart', (e) => {{
            touchStartX = e.touches[0].clientX;
            touchStartY = e.touches[0].clientY;
        }});
        
        document.addEventListener('touchend', (e) => {{
            if (!gameRunning) return;
            
            const touchEndX = e.changedTouches[0].clientX;
            const touchEndY = e.changedTouches[0].clientY;
            const deltaX = touchEndX - touchStartX;
            const deltaY = touchEndY - touchStartY;
            
            if (Math.abs(deltaX) > Math.abs(deltaY)) {{
                if (deltaX > 30) {{
                    playerX = Math.min(window.innerWidth - 50, playerX + 40);
                }} else if (deltaX < -30) {{
                    playerX = Math.max(50, playerX - 40);
                }}
            }} else {{
                if (deltaY < -30) {{
                    speed = Math.min(120, speed + 10);
                }} else if (deltaY > 30) {{
                    speed = Math.max(0, speed - 10);
                }}
            }}
            
            player.style.left = playerX + 'px';
        }});
        
        function createObstacle() {{
            const obstacle = document.createElement('div');
            obstacle.className = 'obstacle';
            obstacle.style.left = Math.random() * (window.innerWidth - 35) + 'px';
            obstacle.style.bottom = window.innerHeight + 'px';
            document.getElementById('gameContainer').appendChild(obstacle);
            
            obstacles.push({{
                element: obstacle,
                x: parseFloat(obstacle.style.left),
                y: -60
            }});
        }}
        
        function createRoadLine() {{
            const line = document.createElement('div');
            line.className = 'road-line';
            line.style.bottom = window.innerHeight + 'px';
            document.getElementById('gameContainer').appendChild(line);
            
            roadLines.push({{
                element: line,
                y: -30
            }});
        }}
        
        function updateUI() {{
            document.getElementById('speed').textContent = speed;
            document.getElementById('distance').textContent = Math.floor(distance);
            document.getElementById('position').textContent = position + 'st';
        }}
        
        // Game loop
        const gameLoop = setInterval(() => {{
            if (!gameRunning) return;
            
            // Update distance and speed
            distance += speed / 10;
            
            // Move obstacles
            obstacles.forEach((obstacle, index) => {{
                obstacle.y += speed / 2 + 5;
                obstacle.element.style.bottom = obstacle.y + 'px';
                
                // Remove if off screen
                if (obstacle.y > window.innerHeight + 100) {{
                    obstacle.element.remove();
                    obstacles.splice(index, 1);
                }}
                
                // Check collision
                const dx = obstacle.x - playerX;
                const dy = obstacle.y - 50;
                if (Math.abs(dx) < 35 && Math.abs(dy) < 55) {{
                    gameRunning = false;
                    alert('Crash!\\n\\nDistance: ' + Math.floor(distance) + 'm\\nTop Speed: ' + speed + ' MPH');
                    location.reload();
                }}
            }});
            
            // Move road lines
            roadLines.forEach((line, index) => {{
                line.y += speed / 2 + 10;
                line.element.style.bottom = line.y + 'px';
                
                if (line.y > window.innerHeight + 50) {{
                    line.element.remove();
                    roadLines.splice(index, 1);
                }}
            }});
            
            // Spawn obstacles
            if (Math.random() < 0.02 + (speed / 1000)) {{
                createObstacle();
            }}
            
            // Spawn road lines
            if (Math.random() < 0.1) {{
                createRoadLine();
            }}
            
            // Auto-accelerate slightly
            if (speed < 60) {{
                speed += 0.5;
            }}
            
            updateUI();
        }}, 50);
        
        // Initial road lines
        for (let i = 0; i < 10; i++) {{
            setTimeout(() => createRoadLine(), i * 100);
        }}
        
        setTimeout(() => {{
            alert('🏎️ Welcome to {title}!\\n\\nRace at high speeds and avoid crashes!\\n\\n• Arrow keys or WASD to control\\n• Touch: swipe to steer, up/down for speed\\n• Avoid blue cars and obstacles\\n• Go as far as possible!\\n\\nCharacter: {character}');
        }}, 500);
    </script>
</body>
</html>
                ''',
                'mechanics': ['High-speed racing', 'Obstacle avoidance', 'Speed control', 'Distance tracking'],
                'features': ['Racing atmosphere', 'Progressive difficulty', 'Touch controls', 'Crash detection']
            }
        ]

    def _create_puzzle_templates(self) -> List[Dict]:
        """Create puzzle game templates"""
        return [
            {
                'name': 'Block Master',
                'description': 'Arrange falling blocks to clear lines in this puzzle challenge',
                'html_template': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(45deg, #2F2F2F, #4F4F4F);
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }}
        #gameContainer {{
            text-align: center;
            background: rgba(0,0,0,0.8);
            padding: 20px;
            border-radius: 15px;
            color: white;
        }}
        #gameBoard {{
            width: 300px;
            height: 400px;
            background: #000;
            border: 3px solid #FFF;
            margin: 20px auto;
            position: relative;
            overflow: hidden;
        }}
        .block {{
            position: absolute;
            width: 30px;
            height: 30px;
            border: 1px solid #FFF;
        }}
        .red {{ background: #FF0000; }}
        .blue {{ background: #0000FF; }}
        .green {{ background: #00FF00; }}
        .yellow {{ background: #FFFF00; }}
        .purple {{ background: #800080; }}
        .orange {{ background: #FFA500; }}
        .cyan {{ background: #00FFFF; }}
        #ui {{
            margin: 20px 0;
            font-size: 18px;
        }}
        #controls {{
            margin-top: 20px;
            font-size: 14px;
            color: #CCC;
        }}
    </style>
</head>
<body>
    <div id="gameContainer">
        <h2>{title}</h2>
        <div id="ui">
            <div>{ui_element1}: <span id="score">0</span></div>
            <div>{ui_element2}: <span id="lines">0</span></div>
            <div>{ui_element3}: <span id="level">1</span></div>
        </div>
        <div id="gameBoard"></div>
        <div id="controls">
            Arrow Keys: Move | Space: Rotate | Down: Drop
        </div>
    </div>
    
    <script>
        const board = document.getElementById('gameBoard');
        const BOARD_WIDTH = 10;
        const BOARD_HEIGHT = 20;
        const BLOCK_SIZE = 30;
        
        let score = 0;
        let lines = 0;
        let level = 1;
        let gameBoard = Array(BOARD_HEIGHT).fill().map(() => Array(BOARD_WIDTH).fill(0));
        let currentPiece = null;
        let gameRunning = true;
        
        const pieces = [
            [[1,1,1,1]], // I
            [[1,1],[1,1]], // O
            [[0,1,0],[1,1,1]], // T
            [[0,1,1],[1,1,0]], // S
            [[1,1,0],[0,1,1]], // Z
            [[1,0,0],[1,1,1]], // J
            [[0,0,1],[1,1,1]]  // L
        ];
        
        const colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'cyan'];
        
        function createPiece() {{
            const pieceIndex = Math.floor(Math.random() * pieces.length);
            return {{
                shape: pieces[pieceIndex],
                color: colors[pieceIndex],
                x: Math.floor(BOARD_WIDTH / 2) - 1,
                y: 0
            }};
        }}
        
        function drawBoard() {{
            board.innerHTML = '';
            
            // Draw placed blocks
            for (let y = 0; y < BOARD_HEIGHT; y++) {{
                for (let x = 0; x < BOARD_WIDTH; x++) {{
                    if (gameBoard[y][x]) {{
                        const block = document.createElement('div');
                        block.className = 'block ' + gameBoard[y][x];
                        block.style.left = (x * BLOCK_SIZE) + 'px';
                        block.style.top = (y * BLOCK_SIZE) + 'px';
                        board.appendChild(block);
                    }}
                }}
            }}
            
            // Draw current piece
            if (currentPiece) {{
                for (let y = 0; y < currentPiece.shape.length; y++) {{
                    for (let x = 0; x < currentPiece.shape[y].length; x++) {{
                        if (currentPiece.shape[y][x]) {{
                            const block = document.createElement('div');
                            block.className = 'block ' + currentPiece.color;
                            block.style.left = ((currentPiece.x + x) * BLOCK_SIZE) + 'px';
                            block.style.top = ((currentPiece.y + y) * BLOCK_SIZE) + 'px';
                            board.appendChild(block);
                        }}
                    }}
                }}
            }}
        }}
        
        function canMove(piece, dx, dy) {{
            for (let y = 0; y < piece.shape.length; y++) {{
                for (let x = 0; x < piece.shape[y].length; x++) {{
                    if (piece.shape[y][x]) {{
                        const newX = piece.x + x + dx;
                        const newY = piece.y + y + dy;
                        
                        if (newX < 0 || newX >= BOARD_WIDTH || 
                            newY >= BOARD_HEIGHT || 
                            (newY >= 0 && gameBoard[newY][newX])) {{
                            return false;
                        }}
                    }}
                }}
            }}
            return true;
        }}
        
        function placePiece() {{
            for (let y = 0; y < currentPiece.shape.length; y++) {{
                for (let x = 0; x < currentPiece.shape[y].length; x++) {{
                    if (currentPiece.shape[y][x]) {{
                        const boardY = currentPiece.y + y;
                        const boardX = currentPiece.x + x;
                        if (boardY >= 0) {{
                            gameBoard[boardY][boardX] = currentPiece.color;
                        }}
                    }}
                }}
            }}
            
            clearLines();
            currentPiece = createPiece();
            
            if (!canMove(currentPiece, 0, 0)) {{
                gameRunning = false;
                alert('Game Over!\\nScore: ' + score + '\\nLines: ' + lines);
            }}
        }}
        
        function clearLines() {{
            let linesCleared = 0;
            
            for (let y = BOARD_HEIGHT - 1; y >= 0; y--) {{
                if (gameBoard[y].every(cell => cell !== 0)) {{
                    gameBoard.splice(y, 1);
                    gameBoard.unshift(Array(BOARD_WIDTH).fill(0));
                    linesCleared++;
                    y++; // Check same line again
                }}
            }}
            
            if (linesCleared > 0) {{
                lines += linesCleared;
                score += linesCleared * 100 * level;
                level = Math.floor(lines / 10) + 1;
                updateUI();
            }}
        }}
        
        function rotatePiece() {{
            const rotated = currentPiece.shape[0].map((_, i) =>
                currentPiece.shape.map(row => row[i]).reverse()
            );
            
            const testPiece = {{...currentPiece, shape: rotated}};
            if (canMove(testPiece, 0, 0)) {{
                currentPiece.shape = rotated;
            }}
        }}
        
        function updateUI() {{
            document.getElementById('score').textContent = score;
            document.getElementById('lines').textContent = lines;
            document.getElementById('level').textContent = level;
        }}
        
        // Controls
        document.addEventListener('keydown', (e) => {{
            if (!gameRunning || !currentPiece) return;
            
            switch(e.key) {{
                case 'ArrowLeft':
                case 'a':
                case 'A':
                    if (canMove(currentPiece, -1, 0)) {{
                        currentPiece.x--;
                    }}
                    break;
                case 'ArrowRight':
                case 'd':
                case 'D':
                    if (canMove(currentPiece, 1, 0)) {{
                        currentPiece.x++;
                    }}
                    break;
                case 'ArrowDown':
                case 's':
                case 'S':
                    if (canMove(currentPiece, 0, 1)) {{
                        currentPiece.y++;
                        score++;
                    }}
                    break;
                case ' ':
                case 'ArrowUp':
                case 'w':
                case 'W':
                    rotatePiece();
                    break;
            }}
            drawBoard();
            updateUI();
        }});
        
        // Game loop
        const gameLoop = setInterval(() => {{
            if (!gameRunning) {{
                clearInterval(gameLoop);
                return;
            }}
            
            if (currentPiece) {{
                if (canMove(currentPiece, 0, 1)) {{
                    currentPiece.y++;
                }} else {{
                    placePiece();
                }}
            }}
            
            drawBoard();
        }}, Math.max(100, 1000 - (level * 50)));
        
        // Initialize
        currentPiece = createPiece();
        drawBoard();
        
        setTimeout(() => {{
            alert('🧩 Welcome to {title}!\\n\\nArrange falling blocks to clear lines!\\n\\n• Arrow keys to move\\n• Space or Up to rotate\\n• Down to drop faster\\n• Clear horizontal lines to score\\n\\nCharacter: {character}');
        }}, 500);
    </script>
</body>
</html>
                ''',
                'mechanics': ['Block arrangement', 'Line clearing', 'Piece rotation', 'Progressive speed'],
                'features': ['Classic puzzle gameplay', 'Level progression', 'Score system', 'Tetris-style mechanics']
            }
        ]

    def _create_adventure_templates(self) -> List[Dict]:
        """Create adventure game templates"""
        return [
            {
                'name': 'Epic Quest',
                'description': 'Embark on an epic adventure through mystical lands',
                'html_template': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(to bottom, #4682B4, #228B22);
            font-family: 'Times New Roman', serif;
            overflow: hidden;
        }}
        #gameContainer {{
            width: 100vw;
            height: 100vh;
            position: relative;
        }}
        #player {{
            position: absolute;
            width: 40px;
            height: 40px;
            background: #8B4513;
            border-radius: 50%;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            transition: all 0.2s;
        }}
        .treasure {{
            position: absolute;
            width: 25px;
            height: 25px;
            background: #FFD700;
            border-radius: 3px;
            animation: sparkle 2s infinite;
        }}
        .monster {{
            position: absolute;
            width: 35px;
            height: 35px;
            background: #8B0000;
            border-radius: 50%;
            animation: pulse 1s infinite;
        }}
        .tree {{
            position: absolute;
            width: 30px;
            height: 50px;
            background: #228B22;
            border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
        }}
        #ui {{
            position: absolute;
            top: 10px;
            left: 10px;
            color: white;
            font-size: 18px;
            text-shadow: 2px 2px 4px #000;
            background: rgba(0,0,0,0.7);
            padding: 10px;
            border-radius: 10px;
        }}
        @keyframes sparkle {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.2); }}
        }}
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.7; }}
        }}
    </style>
</head>
<body>
    <div id="gameContainer">
        <div id="ui">
            <div>{ui_element1}: <span id="gold">0</span></div>
            <div>{ui_element2}: <span id="health">100</span></div>
            <div>{ui_element3}: <span id="quest">1</span></div>
            <div>Monsters: <span id="monsters">0</span></div>
        </div>
        <div id="player"></div>
    </div>
    
    <script>
        const player = document.getElementById('player');
        let playerX = window.innerWidth / 2;
        let playerY = window.innerHeight / 2;
        let gold = 0;
        let health = 100;
        let quest = 1;
        let gameObjects = [];
        
        // Player movement
        document.addEventListener('keydown', (e) => {{
            const moveDistance = 25;
            
            switch(e.key) {{
                case 'ArrowLeft':
                case 'a':
                case 'A':
                    playerX = Math.max(20, playerX - moveDistance);
                    break;
                case 'ArrowRight':
                case 'd':
                case 'D':
                    playerX = Math.min(window.innerWidth - 20, playerX + moveDistance);
                    break;
                case 'ArrowUp':
                case 'w':
                case 'W':
                    playerY = Math.max(20, playerY - moveDistance);
                    break;
                case 'ArrowDown':
                case 's':
                case 'S':
                    playerY = Math.min(window.innerHeight - 20, playerY + moveDistance);
                    break;
            }}
            
            player.style.left = playerX + 'px';
            player.style.top = playerY + 'px';
        }});
        
        // Touch controls
        let touchStartX, touchStartY;
        document.addEventListener('touchstart', (e) => {{
            touchStartX = e.touches[0].clientX;
            touchStartY = e.touches[0].clientY;
        }});
        
        document.addEventListener('touchend', (e) => {{
            const touchEndX = e.changedTouches[0].clientX;
            const touchEndY = e.changedTouches[0].clientY;
            const deltaX = touchEndX - touchStartX;
            const deltaY = touchEndY - touchStartY;
            const moveDistance = 40;
            
            if (Math.abs(deltaX) > Math.abs(deltaY)) {{
                if (deltaX > 30) {{
                    playerX = Math.min(window.innerWidth - 20, playerX + moveDistance);
                }} else if (deltaX < -30) {{
                    playerX = Math.max(20, playerX - moveDistance);
                }}
            }} else {{
                if (deltaY > 30) {{
                    playerY = Math.min(window.innerHeight - 20, playerY + moveDistance);
                }} else if (deltaY < -30) {{
                    playerY = Math.max(20, playerY - moveDistance);
                }}
            }}
            
            player.style.left = playerX + 'px';
            player.style.top = playerY + 'px';
        }});
        
        function createTreasure() {{
            const treasure = document.createElement('div');
            treasure.className = 'treasure';
            treasure.style.left = Math.random() * (window.innerWidth - 25) + 'px';
            treasure.style.top = Math.random() * (window.innerHeight - 25) + 'px';
            document.getElementById('gameContainer').appendChild(treasure);
            gameObjects.push({{element: treasure, type: 'treasure'}});
        }}
        
        function createMonster() {{
            const monster = document.createElement('div');
            monster.className = 'monster';
            monster.style.left = Math.random() * (window.innerWidth - 35) + 'px';
            monster.style.top = Math.random() * (window.innerHeight - 35) + 'px';
            document.getElementById('gameContainer').appendChild(monster);
            gameObjects.push({{element: monster, type: 'monster'}});
        }}
        
        function createTree() {{
            const tree = document.createElement('div');
            tree.className = 'tree';
            tree.style.left = Math.random() * (window.innerWidth - 30) + 'px';
            tree.style.top = Math.random() * (window.innerHeight - 50) + 'px';
            document.getElementById('gameContainer').appendChild(tree);
            gameObjects.push({{element: tree, type: 'tree'}});
        }}
        
        function updateUI() {{
            document.getElementById('gold').textContent = gold;
            document.getElementById('health').textContent = health;
            document.getElementById('quest').textContent = quest;
            document.getElementById('monsters').textContent = 
                gameObjects.filter(obj => obj.type === 'monster').length;
        }}
        
        function checkCollisions() {{
            const playerRect = {{
                left: playerX - 20,
                right: playerX + 20,
                top: playerY - 20,
                bottom: playerY + 20
            }};
            
            gameObjects.forEach((obj, index) => {{
                const objRect = obj.element.getBoundingClientRect();
                const gameRect = document.getElementById('gameContainer').getBoundingClientRect();
                
                const objLeft = objRect.left - gameRect.left;
                const objRight = objRect.right - gameRect.left;
                const objTop = objRect.top - gameRect.top;
                const objBottom = objRect.bottom - gameRect.top;
                
                if (playerRect.left < objRight &&
                    playerRect.right > objLeft &&
                    playerRect.top < objBottom &&
                    playerRect.bottom > objTop) {{
                    
                    if (obj.type === 'treasure') {{
                        gold += 10;
                        obj.element.remove();
                        gameObjects.splice(index, 1);
                        
                        if (gold >= quest * 50) {{
                            quest++;
                            alert('Quest ' + (quest-1) + ' completed!\\nStarting Quest ' + quest);
                        }}
                    }} else if (obj.type === 'monster') {{
                        health -= 15;
                        obj.element.remove();
                        gameObjects.splice(index, 1);
                        
                        if (health <= 0) {{
                            alert('Adventure ended!\\nGold collected: ' + gold + '\\nQuests completed: ' + (quest-1));
                            location.reload();
                        }}
                    }}
                }}
            }});
        }}
        
        // Game loop
        setInterval(() => {{
            checkCollisions();
            
            // Spawn objects
            if (Math.random() < 0.02) createTreasure();
            if (Math.random() < 0.015) createMonster();
            if (Math.random() < 0.01) createTree();
            
            updateUI();
        }}, 100);
        
        // Initial objects
        for (let i = 0; i < 5; i++) {{
            createTreasure();
            createMonster();
            createTree();
        }}
        
        setTimeout(() => {{
            alert('⚔️ Welcome to {title}!\\n\\nEmbark on an epic adventure!\\n\\n• Arrow keys or WASD to move\\n• Touch/swipe on mobile\\n• Collect gold treasures\\n• Avoid dangerous monsters\\n• Complete quests to progress\\n\\nCharacter: {character}');
        }}, 500);
    </script>
</body>
</html>
                ''',
                'mechanics': ['Exploration', 'Treasure hunting', 'Monster encounters', 'Quest progression'],
                'features': ['Adventure atmosphere', 'Quest system', 'Environmental objects', 'Progressive difficulty']
            }
        ]

    def _create_fantasy_templates(self) -> List[Dict]:
        """Create fantasy game templates"""
        return [
            {
                'name': 'Magical Realm',
                'description': 'Cast spells and explore a magical fantasy world',
                'html_template': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(to bottom, #4B0082, #8A2BE2);
            font-family: 'Times New Roman', serif;
            overflow: hidden;
        }}
        #gameContainer {{
            width: 100vw;
            height: 100vh;
            position: relative;
        }}
        #player {{
            position: absolute;
            width: 40px;
            height: 40px;
            background: #9370DB;
            border-radius: 50%;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            box-shadow: 0 0 20px #9370DB;
        }}
        .spell {{
            position: absolute;
            width: 15px;
            height: 15px;
            background: #FFD700;
            border-radius: 50%;
            box-shadow: 0 0 10px #FFD700;
        }}
        .crystal {{
            position: absolute;
            width: 20px;
            height: 30px;
            background: linear-gradient(45deg, #00FFFF, #0000FF);
            clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
            animation: glow 2s infinite;
        }}
        .dragon {{
            position: absolute;
            width: 50px;
            height: 40px;
            background: #8B0000;
            border-radius: 50%;
            animation: fly 3s infinite;
        }}
        #ui {{
            position: absolute;
            top: 10px;
            left: 10px;
            color: white;
            font-size: 18px;
            text-shadow: 2px 2px 4px #000;
            background: rgba(0,0,0,0.7);
            padding: 10px;
            border-radius: 10px;
        }}
        .magic-particle {{
            position: absolute;
            width: 4px;
            height: 4px;
            background: #FFD700;
            border-radius: 50%;
            animation: float 2s infinite;
        }}
        @keyframes glow {{
            0%, 100% {{ box-shadow: 0 0 10px #00FFFF; }}
            50% {{ box-shadow: 0 0 20px #00FFFF; }}
        }}
        @keyframes fly {{
            0%, 100% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-10px); }}
        }}
        @keyframes float {{
            0%, 100% {{ transform: translateY(0px) scale(1); }}
            50% {{ transform: translateY(-15px) scale(1.2); }}
        }}
    </style>
</head>
<body>
    <div id="gameContainer">
        <div id="ui">
            <div>{ui_element1}: <span id="mana">100</span></div>
            <div>{ui_element2}: <span id="crystals">0</span></div>
            <div>{ui_element3}: <span id="level">1</span></div>
            <div>Spells Cast: <span id="spells">0</span></div>
        </div>
        <div id="player"></div>
    </div>
    
    <script>
        const player = document.getElementById('player');
        let playerX = window.innerWidth / 2;
        let playerY = window.innerHeight / 2;
        let mana = 100;
        let crystals = 0;
        let level = 1;
        let spellsCast = 0;
        let gameObjects = [];
        let spells = [];
        
        // Player movement
        document.addEventListener('keydown', (e) => {{
            const moveDistance = 20;
            
            switch(e.key) {{
                case 'ArrowLeft':
                case 'a':
                case 'A':
                    playerX = Math.max(20, playerX - moveDistance);
                    break;
                case 'ArrowRight':
                case 'd':
                case 'D':
                    playerX = Math.min(window.innerWidth - 20, playerX + moveDistance);
                    break;
                case 'ArrowUp':
                case 'w':
                case 'W':
                    playerY = Math.max(20, playerY - moveDistance);
                    break;
                case 'ArrowDown':
                case 's':
                case 'S':
                    playerY = Math.min(window.innerHeight - 20, playerY + moveDistance);
                    break;
                case ' ':
                    castSpell();
                    break;
            }}
            
            player.style.left = playerX + 'px';
            player.style.top = playerY + 'px';
        }});
        
        // Touch controls
        let touchStartX, touchStartY;
        document.addEventListener('touchstart', (e) => {{
            touchStartX = e.touches[0].clientX;
            touchStartY = e.touches[0].clientY;
        }});
        
        document.addEventListener('touchend', (e) => {{
            const touchEndX = e.changedTouches[0].clientX;
            const touchEndY = e.changedTouches[0].clientY;
            const deltaX = touchEndX - touchStartX;
            const deltaY = touchEndY - touchStartY;
            const moveDistance = 30;
            
            if (Math.abs(deltaX) > 20 || Math.abs(deltaY) > 20) {{
                if (Math.abs(deltaX) > Math.abs(deltaY)) {{
                    if (deltaX > 0) {{
                        playerX = Math.min(window.innerWidth - 20, playerX + moveDistance);
                    }} else {{
                        playerX = Math.max(20, playerX - moveDistance);
                    }}
                }} else {{
                    if (deltaY > 0) {{
                        playerY = Math.min(window.innerHeight - 20, playerY + moveDistance);
                    }} else {{
                        playerY = Math.max(20, playerY - moveDistance);
                    }}
                }}
                
                player.style.left = playerX + 'px';
                player.style.top = playerY + 'px';
            }} else {{
                castSpell();
            }}
        }});
        
        function castSpell() {{
            if (mana >= 10) {{
                mana -= 10;
                spellsCast++;
                
                const spell = document.createElement('div');
                spell.className = 'spell';
                spell.style.left = playerX + 'px';
                spell.style.top = playerY + 'px';
                document.getElementById('gameContainer').appendChild(spell);
                
                spells.push({{
                    element: spell,
                    x: playerX,
                    y: playerY,
                    vx: (Math.random() - 0.5) * 10,
                    vy: (Math.random() - 0.5) * 10
                }});
                
                updateUI();
            }}
        }}
        
        function createCrystal() {{
            const crystal = document.createElement('div');
            crystal.className = 'crystal';
            crystal.style.left = Math.random() * (window.innerWidth - 20) + 'px';
            crystal.style.top = Math.random() * (window.innerHeight - 30) + 'px';
            document.getElementById('gameContainer').appendChild(crystal);
            gameObjects.push({{element: crystal, type: 'crystal'}});
        }}
        
        function createDragon() {{
            const dragon = document.createElement('div');
            dragon.className = 'dragon';
            dragon.style.left = Math.random() * (window.innerWidth - 50) + 'px';
            dragon.style.top = Math.random() * (window.innerHeight - 40) + 'px';
            document.getElementById('gameContainer').appendChild(dragon);
            gameObjects.push({{element: dragon, type: 'dragon', health: 3}});
        }}
        
        function createMagicParticle() {{
            const particle = document.createElement('div');
            particle.className = 'magic-particle';
            particle.style.left = Math.random() * window.innerWidth + 'px';
            particle.style.top = Math.random() * window.innerHeight + 'px';
            document.getElementById('gameContainer').appendChild(particle);
            
            setTimeout(() => {{
                if (particle.parentNode) {{
                    particle.parentNode.removeChild(particle);
                }}
            }}, 2000);
        }}
        
        function updateUI() {{
            document.getElementById('mana').textContent = mana;
            document.getElementById('crystals').textContent = crystals;
            document.getElementById('level').textContent = level;
            document.getElementById('spells').textContent = spellsCast;
        }}
        
        function checkCollisions() {{
            const playerRect = {{
                left: playerX - 20,
                right: playerX + 20,
                top: playerY - 20,
                bottom: playerY + 20
            }};
            
            // Player collisions
            gameObjects.forEach((obj, index) => {{
                const objRect = obj.element.getBoundingClientRect();
                const gameRect = document.getElementById('gameContainer').getBoundingClientRect();
                
                const objLeft = objRect.left - gameRect.left;
                const objRight = objRect.right - gameRect.left;
                const objTop = objRect.top - gameRect.top;
                const objBottom = objRect.bottom - gameRect.top;
                
                if (playerRect.left < objRight &&
                    playerRect.right > objLeft &&
                    playerRect.top < objBottom &&
                    playerRect.bottom > objTop) {{
                    
                    if (obj.type === 'crystal') {{
                        crystals++;
                        mana = Math.min(100, mana + 20);
                        obj.element.remove();
                        gameObjects.splice(index, 1);
                        
                        if (crystals >= level * 5) {{
                            level++;
                            alert('Level up! You are now level ' + level);
                        }}
                    }}
                }}
            }});
            
            // Spell collisions
            spells.forEach((spell, sIndex) => {{
                gameObjects.forEach((obj, oIndex) => {{
                    if (obj.type === 'dragon') {{
                        const dx = spell.x - (obj.element.offsetLeft + 25);
                        const dy = spell.y - (obj.element.offsetTop + 20);
                        
                        if (Math.sqrt(dx*dx + dy*dy) < 30) {{
                            obj.health--;
                            spell.element.remove();
                            spells.splice(sIndex, 1);
                            
                            if (obj.health <= 0) {{
                                crystals += 3;
                                mana = Math.min(100, mana + 30);
                                obj.element.remove();
                                gameObjects.splice(oIndex, 1);
                                alert('Dragon defeated! +3 crystals, +30 mana');
                            }}
                        }}
                    }}
                }});
            }});
        }}
        
        // Game loop
        setInterval(() => {{
            // Move spells
            spells.forEach((spell, index) => {{
                spell.x += spell.vx;
                spell.y += spell.vy;
                spell.element.style.left = spell.x + 'px';
                spell.element.style.top = spell.y + 'px';
                
                // Remove if off screen
                if (spell.x < 0 || spell.x > window.innerWidth || 
                    spell.y < 0 || spell.y > window.innerHeight) {{
                    spell.element.remove();
                    spells.splice(index, 1);
                }}
            }});
            
            checkCollisions();
            
            // Spawn objects
            if (Math.random() < 0.02) createCrystal();
            if (Math.random() < 0.01) createDragon();
            if (Math.random() < 0.1) createMagicParticle();
            
            // Regenerate mana
            if (mana < 100 && Math.random() < 0.1) {{
                mana = Math.min(100, mana + 1);
            }}
            
            updateUI();
        }}, 100);
        
        // Initial objects
        for (let i = 0; i < 3; i++) {{
            createCrystal();
            createDragon();
        }}
        
        setTimeout(() => {{
            alert('🧙‍♂️ Welcome to {title}!\\n\\nExplore a magical fantasy realm!\\n\\n• Arrow keys or WASD to move\\n• Spacebar or tap to cast spells\\n• Collect crystals for mana\\n• Defeat dragons with spells\\n• Level up by collecting crystals\\n\\nCharacter: {character}');
        }}, 500);
    </script>
</body>
</html>
                ''',
                'mechanics': ['Spell casting', 'Mana management', 'Crystal collection', 'Dragon combat'],
                'features': ['Fantasy atmosphere', 'Magic effects', 'Level progression', 'Combat system']
            }
        ]

    def get_template(self, game_type: str, variation_index: int = 0) -> Dict:
        """Get a specific template for a game type"""
        if game_type not in self.templates:
            game_type = 'darts'  # Fallback
        
        templates = self.templates[game_type]
        if variation_index >= len(templates):
            variation_index = 0
        
        return templates[variation_index]

    def get_random_template(self, game_type: str) -> Dict:
        """Get a random template for a game type"""
        if game_type not in self.templates:
            game_type = 'darts'  # Fallback
        
        templates = self.templates[game_type]
        return random.choice(templates)

    def get_available_types(self) -> List[str]:
        """Get list of available game types"""
        return list(self.templates.keys())

    def get_template_count(self, game_type: str) -> int:
        """Get number of templates available for a game type"""
        return len(self.templates.get(game_type, []))

# Example usage
if __name__ == "__main__":
    library = ExpandedGameTemplateLibrary()
    
    print("🎮 EXPANDED GAME TEMPLATE LIBRARY")
    print("=" * 50)
    
    for game_type in library.get_available_types():
        count = library.get_template_count(game_type)
        print(f"{game_type.title()}: {count} templates")
        
        # Show first template
        template = library.get_template(game_type, 0)
        print(f"  - {template['name']}: {template['description']}")
        print(f"  - Mechanics: {', '.join(template['mechanics'])}")
        print(f"  - Features: {', '.join(template['features'])}")
        print()

