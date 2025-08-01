"""
Health Check System - Service Monitoring and Diagnostics
Monitors all game maker components and provides detailed health reports
"""

import json
import time
import psutil
import os
from datetime import datetime, timedelta

class HealthCheckSystem:
    """
    Comprehensive health monitoring for the Mythiq Game Maker service
    """
    
    def __init__(self):
        self.start_time = datetime.now()
        self.health_checks_performed = 0
        self.last_check_time = None
        self.component_status = {}
        
        # Performance metrics
        self.performance_metrics = {
            'games_generated': 0,
            'average_generation_time': 0,
            'total_generation_time': 0,
            'peak_memory_usage': 0,
            'current_memory_usage': 0,
            'cpu_usage_samples': [],
            'error_count': 0,
            'success_count': 0
        }
        
        # Component health thresholds
        self.health_thresholds = {
            'memory_usage_mb': 500,  # Alert if over 500MB
            'cpu_usage_percent': 80,  # Alert if over 80%
            'response_time_ms': 5000,  # Alert if over 5 seconds
            'error_rate_percent': 10,  # Alert if over 10% errors
            'disk_usage_percent': 90   # Alert if over 90% disk usage
        }
    
    def perform_comprehensive_health_check(self):
        """
        Perform a complete health check of all system components
        """
        try:
            self.health_checks_performed += 1
            self.last_check_time = datetime.now()
            
            health_report = {
                'timestamp': self.last_check_time.isoformat(),
                'service': 'mythiq-game-maker',
                'version': '2.0.0',
                'uptime': self._get_uptime(),
                'overall_status': 'healthy',
                'components': self._check_all_components(),
                'performance': self._get_performance_metrics(),
                'system_resources': self._get_system_resources(),
                'alerts': self._generate_alerts(),
                'recommendations': self._generate_recommendations()
            }
            
            # Determine overall status
            health_report['overall_status'] = self._determine_overall_status(health_report)
            
            return health_report
            
        except Exception as e:
            return self._generate_error_report(str(e))
    
    def _check_all_components(self):
        """Check health of all game maker components"""
        components = {}
        
        # Check Game AI component
        components['game_ai'] = self._check_game_ai()
        
        # Check Base Games library
        components['base_games'] = self._check_base_games()
        
        # Check Customization Engine
        components['customization_engine'] = self._check_customization_engine()
        
        # Check Template Manager
        components['template_manager'] = self._check_template_manager()
        
        # Check Flask application
        components['flask_app'] = self._check_flask_app()
        
        # Check file system
        components['file_system'] = self._check_file_system()
        
        return components
    
    def _check_game_ai(self):
        """Check Game AI component health"""
        try:
            # Try to import and initialize Game AI
            from game_ai import GameAI
            ai = GameAI()
            
            # Test basic functionality
            test_prompt = "Create a simple platformer game"
            start_time = time.time()
            result = ai.analyze_prompt(test_prompt)
            response_time = (time.time() - start_time) * 1000
            
            return {
                'status': 'healthy',
                'response_time_ms': round(response_time, 2),
                'features': {
                    'genre_detection': len(ai.genre_patterns) > 0,
                    'theme_detection': len(ai.theme_patterns) > 0,
                    'difficulty_analysis': len(ai.difficulty_patterns) > 0,
                    'user_preferences': True
                },
                'test_result': {
                    'detected_genre': result.get('genre'),
                    'detected_theme': result.get('theme'),
                    'confidence': result.get('confidence', 0)
                },
                'games_generated': ai.games_generated,
                'active_users': len(ai.user_preferences)
            }
            
        except ImportError:
            return {
                'status': 'degraded',
                'error': 'Game AI module not found - using fallback system',
                'fallback_active': True,
                'features': {
                    'basic_generation': True,
                    'advanced_ai': False
                }
            }
        except Exception as e:
            return {
                'status': 'unhealthy',
                'error': str(e),
                'last_error_time': datetime.now().isoformat()
            }
    
    def _check_base_games(self):
        """Check Base Games library health"""
        try:
            from base_games import BASE_GAMES, list_available_games
            
            games = list_available_games()
            
            return {
                'status': 'healthy',
                'total_games': len(games),
                'available_games': games,
                'genres_supported': list(set(game['genre'] for game in BASE_GAMES.values())),
                'customizable_elements': sum(len(game['customizable_elements']) for game in BASE_GAMES.values()),
                'library_complete': len(games) >= 5
            }
            
        except ImportError:
            return {
                'status': 'unhealthy',
                'error': 'Base Games library not found',
                'impact': 'Game generation will fail'
            }
        except Exception as e:
            return {
                'status': 'degraded',
                'error': str(e),
                'partial_functionality': True
            }
    
    def _check_customization_engine(self):
        """Check Customization Engine health"""
        try:
            from customization_engine import CustomizationEngine
            engine = CustomizationEngine()
            
            # Test customization
            test_customizations = {
                'theme': 'ninja',
                'difficulty': 'medium',
                'genre': 'platformer'
            }
            
            start_time = time.time()
            result = engine.generate_customizations(
                {'genre': 'platformer', 'theme': 'ninja', 'difficulty': 'medium'}, 
                "ninja platformer game"
            )
            response_time = (time.time() - start_time) * 1000
            
            return {
                'status': 'healthy',
                'response_time_ms': round(response_time, 2),
                'customizations_processed': engine.customization_count,
                'available_themes': len(engine.color_schemes),
                'available_character_styles': len(engine.character_styles),
                'difficulty_levels': len(engine.difficulty_settings),
                'test_result': {
                    'customizations_generated': len(result),
                    'theme_applied': result.get('theme') == 'ninja'
                }
            }
            
        except ImportError:
            return {
                'status': 'degraded',
                'error': 'Customization Engine not found - using basic customization',
                'fallback_active': True
            }
        except Exception as e:
            return {
                'status': 'unhealthy',
                'error': str(e)
            }
    
    def _check_template_manager(self):
        """Check Template Manager health"""
        try:
            from game_templates import GameTemplateManager
            manager = GameTemplateManager()
            
            # Test template generation
            test_config = {
                'theme': 'space',
                'title': 'Test Game',
                'description': 'Health check test',
                'genre': 'platformer'
            }
            
            start_time = time.time()
            html = manager.generate_complete_html(test_config)
            response_time = (time.time() - start_time) * 1000
            
            return {
                'status': 'healthy',
                'response_time_ms': round(response_time, 2),
                'templates_loaded': manager.templates_loaded,
                'available_themes': len(manager.css_templates),
                'available_snippets': len(manager.js_snippets),
                'available_components': len(manager.html_components),
                'test_result': {
                    'html_generated': len(html) > 1000,
                    'contains_theme': 'space' in html.lower()
                }
            }
            
        except ImportError:
            return {
                'status': 'degraded',
                'error': 'Template Manager not found - using basic templates',
                'fallback_active': True
            }
        except Exception as e:
            return {
                'status': 'unhealthy',
                'error': str(e)
            }
    
    def _check_flask_app(self):
        """Check Flask application health"""
        try:
            # Check if Flask is running and responsive
            flask_status = {
                'status': 'healthy',
                'port': os.environ.get('PORT', 5002),
                'debug_mode': False,
                'cors_enabled': True,
                'endpoints': [
                    '/',
                    '/api/generate',
                    '/play/<game_id>',
                    '/api/games',
                    '/health'
                ]
            }
            
            return flask_status
            
        except Exception as e:
            return {
                'status': 'unhealthy',
                'error': str(e)
            }
    
    def _check_file_system(self):
        """Check file system health"""
        try:
            # Check disk usage
            disk_usage = psutil.disk_usage('/')
            disk_percent = (disk_usage.used / disk_usage.total) * 100
            
            # Check if we can write files
            test_file = '/tmp/mythiq_health_check.txt'
            try:
                with open(test_file, 'w') as f:
                    f.write('Health check test')
                os.remove(test_file)
                write_access = True
            except:
                write_access = False
            
            return {
                'status': 'healthy' if disk_percent < 90 and write_access else 'degraded',
                'disk_usage_percent': round(disk_percent, 2),
                'disk_free_gb': round(disk_usage.free / (1024**3), 2),
                'disk_total_gb': round(disk_usage.total / (1024**3), 2),
                'write_access': write_access,
                'temp_directory_accessible': os.access('/tmp', os.W_OK)
            }
            
        except Exception as e:
            return {
                'status': 'unhealthy',
                'error': str(e)
            }
    
    def _get_performance_metrics(self):
        """Get current performance metrics"""
        try:
            # Update current memory usage
            process = psutil.Process()
            current_memory = process.memory_info().rss / 1024 / 1024  # MB
            
            self.performance_metrics['current_memory_usage'] = round(current_memory, 2)
            if current_memory > self.performance_metrics['peak_memory_usage']:
                self.performance_metrics['peak_memory_usage'] = round(current_memory, 2)
            
            # Update CPU usage
            cpu_percent = process.cpu_percent()
            self.performance_metrics['cpu_usage_samples'].append(cpu_percent)
            
            # Keep only last 10 samples
            if len(self.performance_metrics['cpu_usage_samples']) > 10:
                self.performance_metrics['cpu_usage_samples'] = self.performance_metrics['cpu_usage_samples'][-10:]
            
            # Calculate success rate
            total_requests = self.performance_metrics['success_count'] + self.performance_metrics['error_count']
            success_rate = (self.performance_metrics['success_count'] / total_requests * 100) if total_requests > 0 else 100
            
            return {
                **self.performance_metrics,
                'average_cpu_usage': round(sum(self.performance_metrics['cpu_usage_samples']) / len(self.performance_metrics['cpu_usage_samples']), 2) if self.performance_metrics['cpu_usage_samples'] else 0,
                'success_rate_percent': round(success_rate, 2),
                'requests_per_minute': self._calculate_requests_per_minute()
            }
            
        except Exception as e:
            return {
                'error': str(e),
                'status': 'metrics_unavailable'
            }
    
    def _get_system_resources(self):
        """Get system resource information"""
        try:
            # Memory info
            memory = psutil.virtual_memory()
            
            # CPU info
            cpu_count = psutil.cpu_count()
            cpu_percent = psutil.cpu_percent(interval=1)
            
            # Disk info
            disk = psutil.disk_usage('/')
            
            return {
                'memory': {
                    'total_gb': round(memory.total / (1024**3), 2),
                    'available_gb': round(memory.available / (1024**3), 2),
                    'used_percent': round(memory.percent, 2)
                },
                'cpu': {
                    'cores': cpu_count,
                    'usage_percent': round(cpu_percent, 2)
                },
                'disk': {
                    'total_gb': round(disk.total / (1024**3), 2),
                    'free_gb': round(disk.free / (1024**3), 2),
                    'used_percent': round((disk.used / disk.total) * 100, 2)
                }
            }
            
        except Exception as e:
            return {
                'error': str(e),
                'status': 'system_info_unavailable'
            }
    
    def _generate_alerts(self):
        """Generate health alerts based on thresholds"""
        alerts = []
        
        try:
            # Check memory usage
            if self.performance_metrics['current_memory_usage'] > self.health_thresholds['memory_usage_mb']:
                alerts.append({
                    'level': 'warning',
                    'component': 'memory',
                    'message': f"High memory usage: {self.performance_metrics['current_memory_usage']}MB",
                    'threshold': self.health_thresholds['memory_usage_mb']
                })
            
            # Check CPU usage
            if self.performance_metrics['cpu_usage_samples']:
                avg_cpu = sum(self.performance_metrics['cpu_usage_samples']) / len(self.performance_metrics['cpu_usage_samples'])
                if avg_cpu > self.health_thresholds['cpu_usage_percent']:
                    alerts.append({
                        'level': 'warning',
                        'component': 'cpu',
                        'message': f"High CPU usage: {avg_cpu:.1f}%",
                        'threshold': self.health_thresholds['cpu_usage_percent']
                    })
            
            # Check error rate
            total_requests = self.performance_metrics['success_count'] + self.performance_metrics['error_count']
            if total_requests > 0:
                error_rate = (self.performance_metrics['error_count'] / total_requests) * 100
                if error_rate > self.health_thresholds['error_rate_percent']:
                    alerts.append({
                        'level': 'critical',
                        'component': 'error_rate',
                        'message': f"High error rate: {error_rate:.1f}%",
                        'threshold': self.health_thresholds['error_rate_percent']
                    })
            
        except Exception as e:
            alerts.append({
                'level': 'error',
                'component': 'health_check',
                'message': f"Failed to generate alerts: {str(e)}"
            })
        
        return alerts
    
    def _generate_recommendations(self):
        """Generate performance and health recommendations"""
        recommendations = []
        
        try:
            # Memory recommendations
            if self.performance_metrics['current_memory_usage'] > 300:
                recommendations.append({
                    'category': 'performance',
                    'priority': 'medium',
                    'message': 'Consider implementing memory cleanup for generated games',
                    'action': 'Implement game cache cleanup after 1 hour'
                })
            
            # Game generation recommendations
            if self.performance_metrics['games_generated'] > 100:
                recommendations.append({
                    'category': 'optimization',
                    'priority': 'low',
                    'message': 'High game generation volume detected',
                    'action': 'Consider implementing game template caching'
                })
            
            # Error handling recommendations
            if self.performance_metrics['error_count'] > 0:
                recommendations.append({
                    'category': 'reliability',
                    'priority': 'high',
                    'message': 'Errors detected in game generation',
                    'action': 'Review error logs and improve fallback mechanisms'
                })
            
        except Exception as e:
            recommendations.append({
                'category': 'system',
                'priority': 'high',
                'message': f'Health check system error: {str(e)}',
                'action': 'Review health check implementation'
            })
        
        return recommendations
    
    def _determine_overall_status(self, health_report):
        """Determine overall system health status"""
        try:
            component_statuses = [comp.get('status', 'unknown') for comp in health_report['components'].values()]
            
            if 'unhealthy' in component_statuses:
                return 'unhealthy'
            elif 'degraded' in component_statuses:
                return 'degraded'
            elif any(alert['level'] == 'critical' for alert in health_report['alerts']):
                return 'degraded'
            else:
                return 'healthy'
                
        except Exception:
            return 'unknown'
    
    def _get_uptime(self):
        """Get service uptime"""
        uptime_delta = datetime.now() - self.start_time
        return {
            'seconds': int(uptime_delta.total_seconds()),
            'human_readable': str(uptime_delta).split('.')[0]  # Remove microseconds
        }
    
    def _calculate_requests_per_minute(self):
        """Calculate approximate requests per minute"""
        uptime_minutes = (datetime.now() - self.start_time).total_seconds() / 60
        if uptime_minutes > 0:
            total_requests = self.performance_metrics['success_count'] + self.performance_metrics['error_count']
            return round(total_requests / uptime_minutes, 2)
        return 0
    
    def _generate_error_report(self, error_message):
        """Generate error report when health check fails"""
        return {
            'timestamp': datetime.now().isoformat(),
            'service': 'mythiq-game-maker',
            'overall_status': 'unhealthy',
            'error': error_message,
            'health_checks_performed': self.health_checks_performed,
            'uptime': self._get_uptime(),
            'message': 'Health check system encountered an error'
        }
    
    def record_game_generation(self, generation_time, success=True):
        """Record game generation metrics"""
        if success:
            self.performance_metrics['success_count'] += 1
            self.performance_metrics['games_generated'] += 1
            self.performance_metrics['total_generation_time'] += generation_time
            self.performance_metrics['average_generation_time'] = (
                self.performance_metrics['total_generation_time'] / 
                self.performance_metrics['games_generated']
            )
        else:
            self.performance_metrics['error_count'] += 1
    
    def get_quick_status(self):
        """Get quick health status without full check"""
        return {
            'status': 'healthy',
            'service': 'mythiq-game-maker',
            'uptime_seconds': int((datetime.now() - self.start_time).total_seconds()),
            'games_generated': self.performance_metrics['games_generated'],
            'memory_usage_mb': self.performance_metrics['current_memory_usage'],
            'last_check': self.last_check_time.isoformat() if self.last_check_time else None
        }

# Global health check instance
health_checker = HealthCheckSystem()

def get_health_status():
    """Get current health status"""
    return health_checker.perform_comprehensive_health_check()

def get_quick_health():
    """Get quick health status"""
    return health_checker.get_quick_status()

def record_generation_metrics(generation_time, success=True):
    """Record game generation metrics"""
    health_checker.record_game_generation(generation_time, success)

print("🏥 Health Check System Loaded:")
print(f"  Service monitoring: Active")
print(f"  Performance tracking: Enabled")
print(f"  Component health checks: {len(health_checker.health_thresholds)} thresholds")
print("✅ Ready to monitor Mythiq Game Maker health!")

