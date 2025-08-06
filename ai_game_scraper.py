"""
🎮 AI GAME SCRAPER - INTELLIGENT GAME COLLECTION SYSTEM
Scrapes and analyzes real games from the web to build a massive template library
"""

import requests
from bs4 import BeautifulSoup
import json
import re
import time
import random
from urllib.parse import urljoin, urlparse
import os
from datetime import datetime

class AIGameScraper:
    def __init__(self):
        self.game_library = {}
        self.scraped_games = []
        self.game_categories = {
            'underwater': ['underwater', 'ocean', 'sea', 'mermaid', 'submarine', 'diving', 'aquatic'],
            'space': ['space', 'alien', 'rocket', 'galaxy', 'planet', 'asteroid', 'spaceship'],
            'platformer': ['platform', 'jump', 'mario', 'sonic', 'side-scroll', 'runner'],
            'puzzle': ['puzzle', 'match', 'tetris', 'brain', 'logic', 'strategy'],
            'racing': ['racing', 'car', 'speed', 'track', 'formula', 'motorcycle'],
            'adventure': ['adventure', 'quest', 'rpg', 'exploration', 'treasure'],
            'action': ['action', 'fight', 'combat', 'battle', 'shooter'],
            'arcade': ['arcade', 'retro', 'classic', 'pacman', 'breakout'],
            'sports': ['sports', 'football', 'basketball', 'tennis', 'soccer'],
            'fantasy': ['fantasy', 'magic', 'wizard', 'dragon', 'medieval']
        }
        
        # Game sources to scrape from
        self.game_sources = [
            'https://www.crazygames.com',
            'https://poki.com',
            'https://www.addictinggames.com',
            'https://www.miniclip.com',
            'https://html5games.com',
            'https://www.kongregate.com',
            'https://itch.io/games/html5',
            'https://www.newgrounds.com/games',
            'https://www.y8.com',
            'https://www.friv.com'
        ]
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def scrape_game_links(self, source_url, category=None):
        """Scrape game links from a source website"""
        try:
            print(f"🔍 Scraping games from: {source_url}")
            response = requests.get(source_url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find game links (common patterns)
            game_links = []
            
            # Look for common game link patterns
            link_selectors = [
                'a[href*="/game/"]',
                'a[href*="/games/"]',
                'a[href*="/play/"]',
                '.game-link',
                '.game-item a',
                '.game-card a',
                '.game-thumbnail a'
            ]
            
            for selector in link_selectors:
                links = soup.select(selector)
                for link in links:
                    href = link.get('href')
                    if href:
                        full_url = urljoin(source_url, href)
                        title = link.get('title') or link.text.strip()
                        
                        if category:
                            # Check if game matches category keywords
                            if any(keyword in title.lower() for keyword in self.game_categories.get(category, [])):
                                game_links.append({
                                    'url': full_url,
                                    'title': title,
                                    'category': category,
                                    'source': source_url
                                })
                        else:
                            game_links.append({
                                'url': full_url,
                                'title': title,
                                'category': self.detect_category(title),
                                'source': source_url
                            })
            
            print(f"✅ Found {len(game_links)} games from {source_url}")
            return game_links
            
        except Exception as e:
            print(f"❌ Error scraping {source_url}: {e}")
            return []

    def detect_category(self, title):
        """Detect game category based on title"""
        title_lower = title.lower()
        
        for category, keywords in self.game_categories.items():
            if any(keyword in title_lower for keyword in keywords):
                return category
        
        return 'general'

    def scrape_game_code(self, game_url):
        """Scrape the actual game code from a game URL"""
        try:
            print(f"🎮 Scraping game code from: {game_url}")
            response = requests.get(game_url, headers=self.headers, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Look for embedded game content
            game_data = {
                'url': game_url,
                'html': str(soup),
                'scripts': [],
                'styles': [],
                'canvas_elements': [],
                'iframe_sources': []
            }
            
            # Extract JavaScript
            scripts = soup.find_all('script')
            for script in scripts:
                if script.string:
                    game_data['scripts'].append(script.string)
                elif script.get('src'):
                    # Try to fetch external scripts
                    try:
                        script_url = urljoin(game_url, script.get('src'))
                        script_response = requests.get(script_url, headers=self.headers, timeout=5)
                        game_data['scripts'].append(script_response.text)
                    except:
                        pass
            
            # Extract CSS
            styles = soup.find_all('style')
            for style in styles:
                if style.string:
                    game_data['styles'].append(style.string)
            
            # Look for canvas elements (HTML5 games)
            canvases = soup.find_all('canvas')
            for canvas in canvases:
                game_data['canvas_elements'].append(str(canvas))
            
            # Look for iframes (embedded games)
            iframes = soup.find_all('iframe')
            for iframe in iframes:
                src = iframe.get('src')
                if src:
                    game_data['iframe_sources'].append(urljoin(game_url, src))
            
            return game_data
            
        except Exception as e:
            print(f"❌ Error scraping game code from {game_url}: {e}")
            return None

    def analyze_game_mechanics(self, game_data):
        """Analyze game code to extract mechanics and features"""
        try:
            mechanics = {
                'movement': False,
                'shooting': False,
                'collision': False,
                'scoring': False,
                'levels': False,
                'powerups': False,
                'enemies': False,
                'physics': False,
                'sound': False,
                'graphics_type': 'unknown'
            }
            
            # Combine all code for analysis
            all_code = ' '.join(game_data.get('scripts', []))
            html_content = game_data.get('html', '')
            
            # Check for movement mechanics
            movement_patterns = [
                r'keydown|keyup|keypress',
                r'addEventListener.*key',
                r'arrow|wasd|movement',
                r'player\.x|player\.y',
                r'velocity|speed'
            ]
            
            for pattern in movement_patterns:
                if re.search(pattern, all_code, re.IGNORECASE):
                    mechanics['movement'] = True
                    break
            
            # Check for shooting mechanics
            shooting_patterns = [
                r'bullet|projectile|shoot|fire',
                r'ammunition|ammo',
                r'weapon|gun|laser'
            ]
            
            for pattern in shooting_patterns:
                if re.search(pattern, all_code, re.IGNORECASE):
                    mechanics['shooting'] = True
                    break
            
            # Check for collision detection
            collision_patterns = [
                r'collision|intersect|overlap',
                r'hitTest|hit.*detection',
                r'getBounds|getRect'
            ]
            
            for pattern in collision_patterns:
                if re.search(pattern, all_code, re.IGNORECASE):
                    mechanics['collision'] = True
                    break
            
            # Check for scoring system
            scoring_patterns = [
                r'score|points|highscore',
                r'scoreText|scoreDisplay',
                r'addScore|updateScore'
            ]
            
            for pattern in scoring_patterns:
                if re.search(pattern, all_code, re.IGNORECASE):
                    mechanics['scoring'] = True
                    break
            
            # Check for levels
            level_patterns = [
                r'level|stage|round',
                r'nextLevel|levelUp',
                r'currentLevel'
            ]
            
            for pattern in level_patterns:
                if re.search(pattern, all_code, re.IGNORECASE):
                    mechanics['levels'] = True
                    break
            
            # Check for enemies
            enemy_patterns = [
                r'enemy|enemies|monster|alien',
                r'opponent|adversary',
                r'enemyArray|enemies\[\]'
            ]
            
            for pattern in enemy_patterns:
                if re.search(pattern, all_code, re.IGNORECASE):
                    mechanics['enemies'] = True
                    break
            
            # Check for powerups
            powerup_patterns = [
                r'powerup|power.*up|bonus',
                r'upgrade|enhancement',
                r'collectible|pickup'
            ]
            
            for pattern in powerup_patterns:
                if re.search(pattern, all_code, re.IGNORECASE):
                    mechanics['powerups'] = True
                    break
            
            # Check for physics
            physics_patterns = [
                r'gravity|physics|matter\.js',
                r'box2d|p2\.js|cannon\.js',
                r'velocity|acceleration|force'
            ]
            
            for pattern in physics_patterns:
                if re.search(pattern, all_code, re.IGNORECASE):
                    mechanics['physics'] = True
                    break
            
            # Check for sound
            sound_patterns = [
                r'audio|sound|music',
                r'play\(\)|pause\(\)',
                r'AudioContext|Web Audio'
            ]
            
            for pattern in sound_patterns:
                if re.search(pattern, all_code, re.IGNORECASE):
                    mechanics['sound'] = True
                    break
            
            # Determine graphics type
            if 'canvas' in html_content.lower():
                if 'webgl' in all_code.lower() or 'three.js' in all_code.lower():
                    mechanics['graphics_type'] = '3d'
                else:
                    mechanics['graphics_type'] = '2d_canvas'
            elif 'svg' in html_content.lower():
                mechanics['graphics_type'] = 'svg'
            else:
                mechanics['graphics_type'] = 'dom'
            
            return mechanics
            
        except Exception as e:
            print(f"❌ Error analyzing game mechanics: {e}")
            return {}

    def create_game_template(self, game_data, mechanics, category):
        """Create a reusable game template from scraped data"""
        try:
            template = {
                'id': f"scraped_{int(time.time())}_{random.randint(1000, 9999)}",
                'name': f"Scraped {category.title()} Game",
                'category': category,
                'mechanics': mechanics,
                'quality_score': self.calculate_quality_score(mechanics),
                'source_url': game_data.get('url', ''),
                'scraped_at': datetime.now().isoformat(),
                'template_code': self.extract_template_code(game_data, mechanics),
                'customizable_elements': self.identify_customizable_elements(game_data, mechanics)
            }
            
            return template
            
        except Exception as e:
            print(f"❌ Error creating game template: {e}")
            return None

    def calculate_quality_score(self, mechanics):
        """Calculate quality score based on game mechanics"""
        score = 5  # Base score
        
        if mechanics.get('movement'): score += 1
        if mechanics.get('shooting'): score += 1
        if mechanics.get('collision'): score += 1
        if mechanics.get('scoring'): score += 0.5
        if mechanics.get('levels'): score += 0.5
        if mechanics.get('powerups'): score += 0.5
        if mechanics.get('enemies'): score += 1
        if mechanics.get('physics'): score += 1
        if mechanics.get('sound'): score += 0.5
        
        graphics_bonus = {
            '3d': 1,
            '2d_canvas': 0.5,
            'svg': 0.3,
            'dom': 0
        }
        score += graphics_bonus.get(mechanics.get('graphics_type', 'unknown'), 0)
        
        return min(10, score)

    def extract_template_code(self, game_data, mechanics):
        """Extract and clean template code for reuse"""
        try:
            # Start with basic HTML structure
            template_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{GAME_TITLE}}</title>
    <style>
        body { margin: 0; padding: 0; background: {{BACKGROUND_COLOR}}; font-family: Arial, sans-serif; }
        canvas { display: block; margin: 0 auto; background: {{CANVAS_BACKGROUND}}; }
        .ui { position: absolute; top: 10px; left: 10px; color: {{UI_COLOR}}; font-size: 18px; }
        .game-over { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); 
                     color: white; text-align: center; font-size: 24px; display: none; }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="{{CANVAS_WIDTH}}" height="{{CANVAS_HEIGHT}}"></canvas>
    <div class="ui">
        <div>Score: <span id="score">0</span></div>
        {{#if LIVES}}<div>Lives: <span id="lives">3</span></div>{{/if}}
        {{#if LEVELS}}<div>Level: <span id="level">1</span></div>{{/if}}
    </div>
    <div id="gameOver" class="game-over">
        <h2>Game Over!</h2>
        <p>Final Score: <span id="finalScore">0</span></p>
        <button onclick="restartGame()">Play Again</button>
    </div>

    <script>
        // Game initialization
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        
        // Responsive canvas
        function resizeCanvas() {
            canvas.width = window.innerWidth * 0.8;
            canvas.height = window.innerHeight * 0.8;
        }
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);

        // Game state
        let gameState = {
            score: 0,
            {{#if LIVES}}lives: 3,{{/if}}
            {{#if LEVELS}}level: 1,{{/if}}
            gameOver: false,
            paused: false
        };

        {{GAME_OBJECTS}}

        {{GAME_MECHANICS}}

        {{GAME_LOOP}}

        // Start game
        gameLoop();
    </script>
</body>
</html>'''
            
            return template_html
            
        except Exception as e:
            print(f"❌ Error extracting template code: {e}")
            return ""

    def identify_customizable_elements(self, game_data, mechanics):
        """Identify elements that can be customized based on user prompts"""
        customizable = {
            'theme': {
                'background_color': '#000000',
                'canvas_background': '#001122',
                'ui_color': '#ffffff',
                'player_color': '#00ff00',
                'enemy_color': '#ff0000'
            },
            'mechanics': {
                'movement_speed': 5,
                'shooting_enabled': mechanics.get('shooting', False),
                'enemy_spawn_rate': 0.02,
                'powerup_spawn_rate': 0.005
            },
            'content': {
                'game_title': 'Custom Game',
                'canvas_width': 800,
                'canvas_height': 600,
                'max_lives': 3,
                'starting_level': 1
            }
        }
        
        return customizable

    def scrape_games_by_category(self, category, max_games=10):
        """Scrape games for a specific category"""
        print(f"🎯 Scraping {category} games...")
        scraped_games = []
        
        for source in self.game_sources[:3]:  # Limit sources for demo
            try:
                # Add category-specific search terms to URL if possible
                search_url = f"{source}/games/{category}" if category != 'general' else source
                
                game_links = self.scrape_game_links(search_url, category)
                
                for game_link in game_links[:max_games//len(self.game_sources)]:
                    game_data = self.scrape_game_code(game_link['url'])
                    if game_data:
                        mechanics = self.analyze_game_mechanics(game_data)
                        template = self.create_game_template(game_data, mechanics, category)
                        if template:
                            scraped_games.append(template)
                    
                    # Rate limiting
                    time.sleep(random.uniform(1, 3))
                    
            except Exception as e:
                print(f"❌ Error scraping from {source}: {e}")
                continue
        
        return scraped_games

    def build_game_library(self):
        """Build a comprehensive game library by scraping multiple categories"""
        print("🚀 Building comprehensive game library...")
        
        for category in self.game_categories.keys():
            print(f"\n📂 Processing {category} games...")
            games = self.scrape_games_by_category(category, max_games=5)
            self.game_library[category] = games
            print(f"✅ Added {len(games)} {category} games to library")
        
        # Save library to file
        self.save_library()
        
        return self.game_library

    def save_library(self):
        """Save the game library to a JSON file"""
        try:
            with open('/home/ubuntu/scraped_game_library.json', 'w') as f:
                json.dump(self.game_library, f, indent=2)
            print("💾 Game library saved to scraped_game_library.json")
        except Exception as e:
            print(f"❌ Error saving library: {e}")

    def load_library(self):
        """Load existing game library from file"""
        try:
            with open('/home/ubuntu/scraped_game_library.json', 'r') as f:
                self.game_library = json.load(f)
            print("📚 Game library loaded from file")
            return True
        except FileNotFoundError:
            print("📚 No existing library found, will create new one")
            return False
        except Exception as e:
            print(f"❌ Error loading library: {e}")
            return False

    def find_matching_template(self, prompt):
        """Find the best matching game template for a user prompt"""
        prompt_lower = prompt.lower()
        best_match = None
        best_score = 0
        
        for category, games in self.game_library.items():
            # Check if prompt matches category keywords
            category_score = 0
            for keyword in self.game_categories.get(category, []):
                if keyword in prompt_lower:
                    category_score += 1
            
            if category_score > 0:
                # Find best game in this category
                for game in games:
                    total_score = category_score + game.get('quality_score', 0)
                    if total_score > best_score:
                        best_score = total_score
                        best_match = game
        
        return best_match

    def customize_template(self, template, prompt):
        """Customize a template based on user prompt"""
        if not template:
            return None
        
        customized = template.copy()
        prompt_lower = prompt.lower()
        
        # Customize theme based on prompt
        theme_mappings = {
            'underwater': {
                'background_color': '#001133',
                'canvas_background': '#003366',
                'ui_color': '#00ccff',
                'player_color': '#00ff88',
                'enemy_color': '#ff6600'
            },
            'space': {
                'background_color': '#000011',
                'canvas_background': '#000033',
                'ui_color': '#ffffff',
                'player_color': '#00ff00',
                'enemy_color': '#ff0000'
            },
            'forest': {
                'background_color': '#1a4a1a',
                'canvas_background': '#2d5a2d',
                'ui_color': '#ffff88',
                'player_color': '#88ff88',
                'enemy_color': '#ff4444'
            }
        }
        
        for theme, colors in theme_mappings.items():
            if theme in prompt_lower:
                customized['customizable_elements']['theme'].update(colors)
                break
        
        # Extract title from prompt
        if 'create' in prompt_lower:
            title_start = prompt_lower.find('create') + 6
            title_words = prompt[title_start:].split()[:4]
            customized['customizable_elements']['content']['game_title'] = ' '.join(title_words).title()
        
        return customized

# Example usage and testing
if __name__ == "__main__":
    scraper = AIGameScraper()
    
    # Try to load existing library first
    if not scraper.load_library():
        # Build new library if none exists
        print("🎮 Building new game library...")
        scraper.build_game_library()
    
    # Test finding templates
    test_prompts = [
        "Create a magical underwater adventure game with mermaids",
        "Make a space shooter with aliens and lasers",
        "Build a platformer game like Mario",
        "Create a puzzle game with matching colors"
    ]
    
    for prompt in test_prompts:
        print(f"\n🔍 Testing prompt: {prompt}")
        template = scraper.find_matching_template(prompt)
        if template:
            customized = scraper.customize_template(template, prompt)
            print(f"✅ Found template: {template['name']} (Quality: {template['quality_score']}/10)")
            print(f"🎨 Customized for: {customized['customizable_elements']['content']['game_title']}")
        else:
            print("❌ No matching template found")
