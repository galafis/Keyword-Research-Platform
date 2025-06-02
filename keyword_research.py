#!/usr/bin/env python3
"""
Keyword Research Platform
Advanced keyword research and analysis tool for SEO professionals.
"""

from flask import Flask, render_template_string, jsonify, request
import requests
import json
import random
from datetime import datetime
import pandas as pd

app = Flask(__name__)

class KeywordResearcher:
    """Keyword research and analysis functionality."""
    
    def __init__(self):
        # Mock keyword database for demonstration
        self.keyword_database = self._generate_mock_keywords()
    
    def _generate_mock_keywords(self):
        """Generate mock keyword data for demonstration."""
        base_keywords = [
            "digital marketing", "seo optimization", "content marketing", "social media",
            "web development", "python programming", "data science", "machine learning",
            "artificial intelligence", "cloud computing", "cybersecurity", "blockchain",
            "e-commerce", "online business", "startup", "entrepreneurship"
        ]
        
        keywords = []
        for base in base_keywords:
            # Generate variations
            variations = [
                f"{base} tools",
                f"{base} strategy",
                f"{base} tips",
                f"best {base}",
                f"{base} guide",
                f"{base} course",
                f"{base} services",
                f"{base} agency",
                f"how to {base}",
                f"{base} tutorial"
            ]
            
            for variation in variations:
                keywords.append({
                    'keyword': variation,
                    'search_volume': random.randint(100, 50000),
                    'difficulty': random.randint(1, 100),
                    'cpc': round(random.uniform(0.5, 15.0), 2),
                    'competition': random.choice(['Low', 'Medium', 'High']),
                    'trend': random.choice(['Rising', 'Stable', 'Declining']),
                    'category': base.replace(' ', '_')
                })
        
        return keywords
    
    def search_keywords(self, seed_keyword, limit=50):
        """Search for keywords based on seed keyword."""
        results = []
        
        for kw in self.keyword_database:
            if seed_keyword.lower() in kw['keyword'].lower():
                results.append(kw)
        
        # Sort by search volume
        results.sort(key=lambda x: x['search_volume'], reverse=True)
        
        return results[:limit]
    
    def analyze_keyword(self, keyword):
        """Detailed analysis of a specific keyword."""
        # Find keyword in database
        kw_data = None
        for kw in self.keyword_database:
            if kw['keyword'].lower() == keyword.lower():
                kw_data = kw
                break
        
        if not kw_data:
            # Generate data for new keyword
            kw_data = {
                'keyword': keyword,
                'search_volume': random.randint(100, 10000),
                'difficulty': random.randint(1, 100),
                'cpc': round(random.uniform(0.5, 10.0), 2),
                'competition': random.choice(['Low', 'Medium', 'High']),
                'trend': random.choice(['Rising', 'Stable', 'Declining']),
                'category': 'general'
            }
        
        # Add additional analysis
        analysis = {
            **kw_data,
            'opportunity_score': self._calculate_opportunity_score(kw_data),
            'related_keywords': self._get_related_keywords(keyword),
            'seasonal_trends': self._generate_seasonal_data(),
            'serp_features': self._get_serp_features(),
            'content_suggestions': self._get_content_suggestions(keyword)
        }
        
        return analysis
    
    def _calculate_opportunity_score(self, kw_data):
        """Calculate keyword opportunity score."""
        volume_score = min(kw_data['search_volume'] / 1000, 50)
        difficulty_score = 100 - kw_data['difficulty']
        cpc_score = min(kw_data['cpc'] * 5, 30)
        
        return round((volume_score + difficulty_score + cpc_score) / 3, 1)
    
    def _get_related_keywords(self, keyword):
        """Get related keywords."""
        related = []
        words = keyword.split()
        
        for kw in self.keyword_database:
            if any(word in kw['keyword'] for word in words) and kw['keyword'] != keyword:
                related.append(kw)
        
        return sorted(related, key=lambda x: x['search_volume'], reverse=True)[:10]
    
    def _generate_seasonal_data(self):
        """Generate seasonal trend data."""
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        return [{'month': month, 'volume': random.randint(70, 130)} for month in months]
    
    def _get_serp_features(self):
        """Get SERP features for keyword."""
        features = ['Featured Snippets', 'People Also Ask', 'Local Pack', 
                   'Images', 'Videos', 'Shopping', 'News']
        
        return random.sample(features, random.randint(2, 5))
    
    def _get_content_suggestions(self, keyword):
        """Get content suggestions for keyword."""
        suggestions = [
            f"Ultimate Guide to {keyword.title()}",
            f"Top 10 {keyword.title()} Strategies",
            f"How to Master {keyword.title()}",
            f"{keyword.title()}: Best Practices",
            f"Common {keyword.title()} Mistakes to Avoid"
        ]
        
        return suggestions

researcher = KeywordResearcher()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Keyword Research Platform</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .search-section {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .search-form {
            display: flex;
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .search-input {
            flex: 1;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 16px;
        }
        
        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 10px;
            cursor: pointer;
            font-weight: 600;
        }
        
        .results-grid {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 30px;
        }
        
        .keywords-table {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .analysis-panel {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #e0e0e0;
        }
        
        th {
            background: #f8f9fa;
            font-weight: 600;
        }
        
        .keyword-row {
            cursor: pointer;
            transition: background 0.3s ease;
        }
        
        .keyword-row:hover {
            background: #f8f9fa;
        }
        
        .metric-card {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            text-align: center;
        }
        
        .metric-value {
            font-size: 2rem;
            font-weight: bold;
            color: #667eea;
        }
        
        .metric-label {
            color: #666;
            margin-top: 5px;
        }
        
        .chart-container {
            margin: 20px 0;
            height: 300px;
        }
        
        .suggestions {
            margin-top: 20px;
        }
        
        .suggestion-item {
            background: #f8f9fa;
            padding: 10px;
            margin: 5px 0;
            border-radius: 5px;
            border-left: 4px solid #667eea;
        }
        
        .difficulty-low { color: #27ae60; }
        .difficulty-medium { color: #f39c12; }
        .difficulty-high { color: #e74c3c; }
        
        .competition-low { background: #d4edda; color: #155724; }
        .competition-medium { background: #fff3cd; color: #856404; }
        .competition-high { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔍 Keyword Research Platform</h1>
            <p>Advanced keyword research and analysis for SEO professionals</p>
        </div>
        
        <div class="search-section">
            <div class="search-form">
                <input type="text" id="seedKeyword" class="search-input" placeholder="Enter seed keyword (e.g., digital marketing)">
                <button onclick="searchKeywords()" class="btn">🚀 Research Keywords</button>
            </div>
        </div>
        
        <div class="results-grid">
            <div class="keywords-table">
                <h3>📊 Keyword Results</h3>
                <table id="keywordsTable">
                    <thead>
                        <tr>
                            <th>Keyword</th>
                            <th>Volume</th>
                            <th>Difficulty</th>
                            <th>CPC</th>
                            <th>Competition</th>
                        </tr>
                    </thead>
                    <tbody id="keywordsBody">
                        <!-- Keywords will be populated here -->
                    </tbody>
                </table>
            </div>
            
            <div class="analysis-panel">
                <h3>📈 Keyword Analysis</h3>
                <div id="analysisContent">
                    <p>Select a keyword from the table to see detailed analysis</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        let currentKeywords = [];
        
        async function searchKeywords() {
            const seedKeyword = document.getElementById('seedKeyword').value;
            if (!seedKeyword) return;
            
            try {
                const response = await fetch('/search', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ seed_keyword: seedKeyword })
                });
                
                const keywords = await response.json();
                currentKeywords = keywords;
                displayKeywords(keywords);
                
            } catch (error) {
                console.error('Error:', error);
            }
        }
        
        function displayKeywords(keywords) {
            const tbody = document.getElementById('keywordsBody');
            tbody.innerHTML = '';
            
            keywords.forEach((kw, index) => {
                const row = document.createElement('tr');
                row.className = 'keyword-row';
                row.onclick = () => analyzeKeyword(kw.keyword);
                
                const difficultyClass = kw.difficulty < 30 ? 'difficulty-low' : 
                                      kw.difficulty < 70 ? 'difficulty-medium' : 'difficulty-high';
                
                const competitionClass = `competition-${kw.competition.toLowerCase()}`;
                
                row.innerHTML = `
                    <td>${kw.keyword}</td>
                    <td>${kw.search_volume.toLocaleString()}</td>
                    <td class="${difficultyClass}">${kw.difficulty}</td>
                    <td>$${kw.cpc}</td>
                    <td><span class="${competitionClass}">${kw.competition}</span></td>
                `;
                
                tbody.appendChild(row);
            });
        }
        
        async function analyzeKeyword(keyword) {
            try {
                const response = await fetch('/analyze', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ keyword: keyword })
                });
                
                const analysis = await response.json();
                displayAnalysis(analysis);
                
            } catch (error) {
                console.error('Error:', error);
            }
        }
        
        function displayAnalysis(analysis) {
            const content = document.getElementById('analysisContent');
            
            content.innerHTML = `
                <div class="metric-card">
                    <div class="metric-value">${analysis.opportunity_score}</div>
                    <div class="metric-label">Opportunity Score</div>
                </div>
                
                <h4>📊 Keyword Metrics</h4>
                <p><strong>Search Volume:</strong> ${analysis.search_volume.toLocaleString()}</p>
                <p><strong>Difficulty:</strong> ${analysis.difficulty}/100</p>
                <p><strong>CPC:</strong> $${analysis.cpc}</p>
                <p><strong>Trend:</strong> ${analysis.trend}</p>
                
                <h4>📈 Seasonal Trends</h4>
                <div class="chart-container">
                    <canvas id="trendsChart"></canvas>
                </div>
                
                <h4>🎯 SERP Features</h4>
                <div>
                    ${analysis.serp_features.map(feature => `<span class="suggestion-item">${feature}</span>`).join('')}
                </div>
                
                <h4>💡 Content Suggestions</h4>
                <div class="suggestions">
                    ${analysis.content_suggestions.map(suggestion => `<div class="suggestion-item">${suggestion}</div>`).join('')}
                </div>
            `;
            
            // Create trends chart
            const ctx = document.getElementById('trendsChart').getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: analysis.seasonal_trends.map(d => d.month),
                    datasets: [{
                        label: 'Search Volume Trend',
                        data: analysis.seasonal_trends.map(d => d.volume),
                        borderColor: '#667eea',
                        backgroundColor: '#667eea20',
                        tension: 0.4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        }
        
        // Load sample data on page load
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('seedKeyword').value = 'digital marketing';
            searchKeywords();
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Main keyword research page."""
    return render_template_string(HTML_TEMPLATE)

@app.route('/search', methods=['POST'])
def search_keywords():
    """Search for keywords based on seed keyword."""
    data = request.get_json()
    seed_keyword = data.get('seed_keyword', '')
    
    keywords = researcher.search_keywords(seed_keyword)
    return jsonify(keywords)

@app.route('/analyze', methods=['POST'])
def analyze_keyword():
    """Analyze specific keyword."""
    data = request.get_json()
    keyword = data.get('keyword', '')
    
    analysis = researcher.analyze_keyword(keyword)
    return jsonify(analysis)

def main():
    """Main execution function."""
    print("Keyword Research Platform")
    print("=" * 30)
    
    print("Starting web server...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()

