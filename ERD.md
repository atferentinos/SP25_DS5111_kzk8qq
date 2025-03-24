   erDiagram
    RAW_DAILY_GAINERS ||--o{ CONSOLIDATED_GAINERS : transforms_to
    RAW_DAILY_GAINERS {
        string symbol
        string name
        float price
        float change
        float change_percent
        float volume
        float avg_vol_3m
        string market_cap
        float pe_ratio
        float wk52_change
        string wk52_range
        string source
        datetime timestamp
        string file_name
    }
    
    CONSOLIDATED_GAINERS ||--o{ SYMBOL_FREQUENCY : aggregates_to
    CONSOLIDATED_GAINERS ||--o{ PRICE_DISTRIBUTION : aggregates_to
    CONSOLIDATED_GAINERS ||--o{ VOLUME_DISTRIBUTION : aggregates_to
    CONSOLIDATED_GAINERS ||--o{ DAY_OF_WEEK_STATS : aggregates_to
    CONSOLIDATED_GAINERS {
        string symbol
        string name
        float price
        float change
        float change_percent
        float volume
        float avg_vol_3m
        string market_cap
        float pe_ratio
        float wk52_change
        string wk52_range
        string source
        date date
        time time
        string day_of_week
    }
    
    SYMBOL_FREQUENCY {
        string symbol
        string name
        int appearance_count
        date first_appearance
        date last_appearance
        float avg_price
        float avg_change_percent
        int max_streak_length
        int sources_count
    }
    
    PRICE_DISTRIBUTION {
        string price_range
        int symbol_count
        int unique_symbols
        float avg_change_percent
        float median_change_percent
        float avg_volume
    }
    
    VOLUME_DISTRIBUTION {
        string volume_range
        int symbol_count
        int unique_symbols
        float avg_change_percent
        float avg_price
    }
    
    DAY_OF_WEEK_STATS {
        string day_of_week
        int gainer_count
        int unique_symbols
        float avg_change_percent
        float avg_volume
    }
    
    SYMBOL_FREQUENCY ||--o{ RECURRING_SYMBOLS_ANALYSIS : feeds_into
    RECURRING_SYMBOLS_ANALYSIS {
        string symbol
        string name
        int appearance_count
        string sources
        float avg_days_between_appearances
        float avg_price_change_between_appearances
        float appearance_frequency
        float avg_volume
        string gainer_pattern
        string performance_category
    }
    
    PRICE_DISTRIBUTION ||--o{ PRICE_RANGE_ANALYSIS : feeds_into
    PRICE_RANGE_ANALYSIS {
        string price_range
        int symbol_count
        int recurring_symbols_count
        float recurring_symbol_percentage
        float avg_appearances
        float high_performers_percentage
        float avg_volume
        float weighted_success_score
    }
    
    VOLUME_DISTRIBUTION ||--o{ VOLUME_PATTERN_ANALYSIS : feeds_into
    VOLUME_PATTERN_ANALYSIS {
        string volume_range
        float avg_change_percent
        float price_correlation
        float liquidity_score
        string trading_recommendation
    }
    
    DAY_OF_WEEK_STATS ||--o{ TRADING_PATTERN_ANALYSIS : feeds_into
    TRADING_PATTERN_ANALYSIS {
        string day_of_week
        float avg_gainers_per_day
        float avg_change_percent
        float repeat_percentage
        string volume_trend
        string trading_strategy
    }"
