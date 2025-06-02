# Keyword Research Platform

[English](#english) | [Português](#português)

## English

### Overview
Advanced keyword research platform built with Python and Flask. Features comprehensive keyword analysis, search volume data, competition metrics, and SEO insights for effective content strategy and search engine optimization.

### Features
- **Keyword Discovery**: Find relevant keywords and search terms
- **Search Volume Analysis**: Historical and current search volume data
- **Competition Metrics**: Keyword difficulty and competition analysis
- **SERP Analysis**: Search engine results page analysis
- **Trend Analysis**: Keyword popularity trends over time
- **Long-tail Keywords**: Discover long-tail keyword opportunities
- **Export Functionality**: CSV and Excel export capabilities
- **API Integration**: Connect with external keyword data sources

### Technologies Used
- **Python 3.8+**
- **Flask**: Web framework and API development
- **Pandas**: Data manipulation and analysis
- **Requests**: HTTP requests for data collection
- **Matplotlib**: Data visualization and charts
- **SQLite**: Keyword data storage

### Installation

1. Clone the repository:
```bash
git clone https://github.com/galafis/Keyword-Research-Platform.git
cd Keyword-Research-Platform
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python keyword_research.py
```

4. Open your browser to `http://localhost:5000`

### Usage

#### Web Interface
1. **Keyword Input**: Enter seed keywords for research
2. **Analysis Options**: Select analysis depth and data sources
3. **Generate Report**: Create comprehensive keyword analysis
4. **View Results**: Browse keyword metrics and opportunities
5. **Export Data**: Download results in various formats

#### API Endpoints

**Research Keywords**
```bash
curl -X POST http://localhost:5000/api/research \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["digital marketing", "SEO tools"], "country": "US", "language": "en"}'
```

**Get Keyword Metrics**
```bash
curl -X GET http://localhost:5000/api/keywords/metrics \
  -G -d "keyword=digital marketing" -d "country=US"
```

**Analyze Competition**
```bash
curl -X POST http://localhost:5000/api/competition \
  -H "Content-Type: application/json" \
  -d '{"keyword": "SEO tools", "depth": 10}'
```

#### Python API
```python
from keyword_research import KeywordResearcher

# Initialize researcher
researcher = KeywordResearcher()

# Research keywords
results = researcher.research_keywords(
    seed_keywords=["digital marketing", "content strategy"],
    country="US",
    language="en"
)

# Analyze keyword metrics
for keyword in results:
    metrics = researcher.get_keyword_metrics(keyword['term'])
    print(f"Keyword: {keyword['term']}")
    print(f"Search Volume: {metrics['search_volume']}")
    print(f"Competition: {metrics['competition']}")
    print(f"CPC: ${metrics['cpc']}")
```

### Keyword Analysis Features

#### Search Volume Data
- **Monthly Search Volume**: Average monthly searches
- **Seasonal Trends**: Search volume variations throughout the year
- **Historical Data**: Long-term search volume trends
- **Geographic Distribution**: Search volume by country/region

#### Competition Analysis
- **Keyword Difficulty**: SEO difficulty score (0-100)
- **Competition Level**: Low, medium, high competition classification
- **Top Competitors**: Websites ranking for target keywords
- **SERP Features**: Featured snippets, ads, local results analysis

#### Keyword Suggestions
- **Related Keywords**: Semantically related terms
- **Long-tail Variations**: Extended keyword phrases
- **Question Keywords**: Question-based search queries
- **LSI Keywords**: Latent semantic indexing terms

#### Content Opportunities
- **Content Gaps**: Underserved keyword opportunities
- **Topic Clusters**: Related keyword groupings
- **Intent Analysis**: Search intent classification (informational, commercial, transactional)
- **Content Ideas**: Content suggestions based on keywords

### Data Sources

#### Search Engines
- **Google**: Primary search volume and trends data
- **Bing**: Alternative search engine data
- **YouTube**: Video search keyword data
- **Amazon**: E-commerce keyword research

#### Third-Party APIs
- **Google Keyword Planner**: Official Google keyword data
- **SEMrush API**: Professional SEO data (requires API key)
- **Ahrefs API**: Backlink and keyword data (requires API key)
- **Ubersuggest API**: Keyword suggestions and metrics

### Analytics Dashboard

#### Keyword Overview
- **Total Keywords**: Number of researched keywords
- **Average Search Volume**: Mean monthly search volume
- **Competition Distribution**: Breakdown by competition level
- **Opportunity Score**: Overall keyword opportunity rating

#### Trend Analysis
- **Search Volume Trends**: Historical search volume charts
- **Seasonal Patterns**: Monthly and quarterly trends
- **Growth Opportunities**: Rising keyword trends
- **Declining Keywords**: Keywords losing search volume

#### Export Options
- **CSV Export**: Spreadsheet-compatible data export
- **Excel Reports**: Formatted Excel workbooks
- **PDF Reports**: Professional keyword research reports
- **JSON API**: Programmatic data access

### Advanced Features

#### Competitor Analysis
- **Competitor Keywords**: Keywords competitors rank for
- **Keyword Gaps**: Keywords competitors rank for but you don't
- **Content Analysis**: Competitor content strategy analysis
- **Ranking Opportunities**: Easy-to-rank keyword identification

#### Local SEO Research
- **Local Keywords**: Location-based keyword research
- **Local Competition**: Local business competition analysis
- **Google My Business**: Local listing optimization keywords
- **Local Search Trends**: Geographic search patterns

#### E-commerce Keywords
- **Product Keywords**: Product-specific keyword research
- **Commercial Intent**: Purchase-intent keyword identification
- **Price Comparison**: Price-related keyword analysis
- **Brand Keywords**: Brand-specific keyword opportunities

### Configuration
Configure keyword research settings in `config.json`:
```json
{
  "api_settings": {
    "google_api_key": "your_google_api_key",
    "semrush_api_key": "your_semrush_api_key",
    "rate_limit": 100
  },
  "research_settings": {
    "default_country": "US",
    "default_language": "en",
    "max_keywords": 1000,
    "min_search_volume": 10
  },
  "export_settings": {
    "include_metrics": true,
    "include_trends": true,
    "file_format": "xlsx"
  }
}
```

### Keyword Metrics Explained

#### Search Volume
- **Exact Match**: Searches for exact keyword phrase
- **Broad Match**: Searches including keyword variations
- **Monthly Average**: 12-month average search volume
- **Peak Volume**: Highest monthly search volume

#### Competition Metrics
- **Keyword Difficulty (KD)**: SEO difficulty score (0-100)
- **Competition Index**: Relative competition level
- **Top Page Authority**: Average authority of ranking pages
- **Backlink Requirements**: Estimated backlinks needed to rank

#### Commercial Metrics
- **Cost Per Click (CPC)**: Average paid advertising cost
- **Commercial Intent**: Likelihood of purchase intent
- **Ad Competition**: Number of advertisers bidding
- **SERP Features**: Special search result features

### Integration
- **Google Analytics**: Connect with website analytics data
- **Google Search Console**: Import search performance data
- **Content Management**: Integration with CMS platforms
- **SEO Tools**: Connect with other SEO software

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Português

### Visão Geral
Plataforma avançada de pesquisa de palavras-chave construída com Python e Flask. Apresenta análise abrangente de palavras-chave, dados de volume de busca, métricas de competição e insights de SEO para estratégia de conteúdo eficaz e otimização para mecanismos de busca.

### Funcionalidades
- **Descoberta de Palavras-chave**: Encontrar palavras-chave e termos de busca relevantes
- **Análise de Volume de Busca**: Dados históricos e atuais de volume de busca
- **Métricas de Competição**: Análise de dificuldade e competição de palavras-chave
- **Análise SERP**: Análise de páginas de resultados de mecanismos de busca
- **Análise de Tendências**: Tendências de popularidade de palavras-chave ao longo do tempo
- **Palavras-chave Long-tail**: Descobrir oportunidades de palavras-chave long-tail
- **Funcionalidade de Exportação**: Capacidades de exportação CSV e Excel
- **Integração API**: Conectar com fontes externas de dados de palavras-chave

### Tecnologias Utilizadas
- **Python 3.8+**
- **Flask**: Framework web e desenvolvimento de API
- **Pandas**: Manipulação e análise de dados
- **Requests**: Requisições HTTP para coleta de dados
- **Matplotlib**: Visualização de dados e gráficos
- **SQLite**: Armazenamento de dados de palavras-chave

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/galafis/Keyword-Research-Platform.git
cd Keyword-Research-Platform
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
python keyword_research.py
```

4. Abra seu navegador em `http://localhost:5000`

### Uso

#### Interface Web
1. **Entrada de Palavras-chave**: Digite palavras-chave semente para pesquisa
2. **Opções de Análise**: Selecione profundidade de análise e fontes de dados
3. **Gerar Relatório**: Criar análise abrangente de palavras-chave
4. **Ver Resultados**: Navegar métricas e oportunidades de palavras-chave
5. **Exportar Dados**: Download de resultados em vários formatos

#### Endpoints da API

**Pesquisar Palavras-chave**
```bash
curl -X POST http://localhost:5000/api/research \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["marketing digital", "ferramentas SEO"], "country": "BR", "language": "pt"}'
```

**Obter Métricas de Palavras-chave**
```bash
curl -X GET http://localhost:5000/api/keywords/metrics \
  -G -d "keyword=marketing digital" -d "country=BR"
```

**Analisar Competição**
```bash
curl -X POST http://localhost:5000/api/competition \
  -H "Content-Type: application/json" \
  -d '{"keyword": "ferramentas SEO", "depth": 10}'
```

#### API Python
```python
from keyword_research import KeywordResearcher

# Inicializar pesquisador
researcher = KeywordResearcher()

# Pesquisar palavras-chave
results = researcher.research_keywords(
    seed_keywords=["marketing digital", "estratégia de conteúdo"],
    country="BR",
    language="pt"
)

# Analisar métricas de palavras-chave
for keyword in results:
    metrics = researcher.get_keyword_metrics(keyword['term'])
    print(f"Palavra-chave: {keyword['term']}")
    print(f"Volume de Busca: {metrics['search_volume']}")
    print(f"Competição: {metrics['competition']}")
    print(f"CPC: R${metrics['cpc']}")
```

### Funcionalidades de Análise de Palavras-chave

#### Dados de Volume de Busca
- **Volume Mensal de Busca**: Média de buscas mensais
- **Tendências Sazonais**: Variações de volume de busca ao longo do ano
- **Dados Históricos**: Tendências de volume de busca de longo prazo
- **Distribuição Geográfica**: Volume de busca por país/região

#### Análise de Competição
- **Dificuldade de Palavra-chave**: Score de dificuldade SEO (0-100)
- **Nível de Competição**: Classificação de competição baixa, média, alta
- **Principais Competidores**: Sites que rankeiam para palavras-chave alvo
- **Recursos SERP**: Análise de snippets em destaque, anúncios, resultados locais

#### Sugestões de Palavras-chave
- **Palavras-chave Relacionadas**: Termos semanticamente relacionados
- **Variações Long-tail**: Frases de palavras-chave estendidas
- **Palavras-chave de Pergunta**: Consultas de busca baseadas em perguntas
- **Palavras-chave LSI**: Termos de indexação semântica latente

#### Oportunidades de Conteúdo
- **Lacunas de Conteúdo**: Oportunidades de palavras-chave mal atendidas
- **Clusters de Tópicos**: Agrupamentos de palavras-chave relacionadas
- **Análise de Intenção**: Classificação de intenção de busca (informacional, comercial, transacional)
- **Ideias de Conteúdo**: Sugestões de conteúdo baseadas em palavras-chave

### Contribuindo
1. Faça um fork do repositório
2. Crie uma branch de feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adicionar nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um Pull Request

### Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

