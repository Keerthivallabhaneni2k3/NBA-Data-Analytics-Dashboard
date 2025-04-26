# 🏀 NBA Player Analytics Dashboard

This project is an interactive web dashboard for exploring NBA player statistics using the [Preswald](https://preswald.com) framework and `plotly` for visualization. It loads player data, allows dynamic filtering based on points per game (PPG), and visualizes key statistics like points vs rebounds.

## 📁 Features

- Load and display NBA player stats from `all_seasons.csv`
- Robust fallback to sample data if CSV is unavailable
- Interactive slider to filter players by minimum points per game
- Dynamic scatter plot: Points vs Rebounds
- Summary table showing key player statistics

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Required packages:
  - `pandas`
  - `plotly`
  - `preswald` (for Preswald-native app interactivity)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/nba-player-dashboard.git
   cd nba-player-dashboard
