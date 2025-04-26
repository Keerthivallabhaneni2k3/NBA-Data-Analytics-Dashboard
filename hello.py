from preswald import text, plotly, connect, get_df, table, slider
import pandas as pd
import plotly.express as px
import os

# 1. INITIALIZE APP
text("# 🏀 NBA Player Analytics Dashboard")
text("Loading data...")

# 2. SHOW AVAILABLE FILES
files = os.listdir('data')
text(f"📁 Files found: {', '.join(files)}")

# 3. LOAD DATA - ROBUST METHOD
df = None
try:
    # Try direct pandas read first
    if 'all_seasons.csv' in files:
        df = pd.read_csv('data/all_seasons.csv')
        text("✅ Loaded data/all_seasons.csv using pandas")
    else:
        # Fallback to Preswald's get_df
        connect()
        df = get_df('all_seasons.csv')
        text("✅ Loaded using get_df()")
except Exception as e:
    text(f"❌ Error loading file: {str(e)}")
    # Create minimal sample data
    sample_data = {
        'player_name': ['LeBron James', 'Stephen Curry', 'Kevin Durant'],
        'team': ['LAL', 'GSW', 'PHX'],
        'pts': [28.9, 29.4, 29.1],
        'reb': [8.4, 6.1, 7.3],
        'ast': [6.8, 6.3, 5.7]
    }
    df = pd.DataFrame(sample_data)
    text("⚠️ Using sample data as fallback")

# 4. SHOW BASIC DATA INFO
text(f"## 📊 Loaded {len(df)} players")
text("First 3 rows:")
table(df.head(3))

# 5. ADD INTERACTIVE FILTER
if 'pts' in df.columns:
    min_pts = slider("Minimum Points", 
                    min_val=float(df['pts'].min()), 
                    max_val=float(df['pts'].max()), 
                    default=10.0)
    filtered_df = df[df['pts'] >= min_pts]
    text(f"Showing {len(filtered_df)} players with ≥ {min_pts} PPG")
else:
    filtered_df = df
    text("⚠️ Points data not available")

# 6. CREATE VISUALIZATION
if all(col in df.columns for col in ['pts', 'reb']):
    fig = px.scatter(
        filtered_df,
        x='pts',
        y='reb',
        hover_name='player_name' if 'player_name' in df.columns else None,
        title='Points vs Rebounds'
    )
    plotly(fig)
else:
    text("⚠️ Not enough data for visualization")

# 7. SHOW FINAL TABLE
text("## Player Statistics")
table_cols = [col for col in ['player_name', 'team', 'pts', 'reb', 'ast'] if col in filtered_df.columns]
table(filtered_df[table_cols].head(15))