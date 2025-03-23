erDiagram
    RAW_DAILY_GAINERS ||--o{ CONSOLIDATED_GAINERS : transforms_to
    RAW_DAILY_GAINERS {
        symbol string
        name string
        price float
        change float
        change_percent float
        volume float "nullable"
        avg_vol_3m float "nullable"
        market_cap string "nullable"
        pe_ratio float "nullable"
        wk52_change float "nullable"
        wk52_range string "nullable"
        source string
        timestamp datetime
        file_name string
    }
    
    CONSOLIDATED_GAINERS ||--o{ SYMBOL_FREQUENCY : aggregates_to
    CONSOLIDATED_GAINERS ||--o{ PRICE_DISTRIBUTION : aggregates_to
    CONSOLIDATED_GAINERS ||--o{ VOLUME_DISTRIBUTION : aggregates_to
    CONSOLIDATED_GAINERS ||--o{ DAY_OF_WEEK_STATS : aggregates_to
    CONSOLIDATED_GAINERS {
        symbol string
        name string
        price float
        change float
        change_percent float
        volume float "nullable"
        avg_vol_3m float "nullable"
        market_cap string "nullable"
        pe_ratio float "nullable"
        wk52_change float "nullable"
        wk52_range string "nullable"
        source string
        date date
        time time
        day_of_week string
    }
    
    SYMBOL_FREQUENCY {
        symbol string
        name string
        appearance_count int
        first_appearance date
        last_appearance date
        avg_price float
        avg_change_percent float
        max_streak_length int
        sources_count int
    }
    
    PRICE_DISTRIBUTION {
        price_range string
        symbol_count int
        unique_symbols int
        avg_change_percent float
        median_change_percent float
        avg_volume float "if available"
    }
    
    VOLUME_DISTRIBUTION {
        volume_range string
        symbol_count int
        unique_symbols int
        avg_change_percent float
        avg_price float
    }
    
    DAY_OF_WEEK_STATS {
        day_of_week string
        gainer_count int
        unique_symbols int
        avg_change_percent float
        avg_volume float "if available"
    }
    
    SYMBOL_FREQUENCY ||--o{ RECURRING_SYMBOLS_ANALYSIS : feeds_into
    RECURRING_SYMBOLS_ANALYSIS {
        symbol string
        name string
        appearance_count int
        sources array
        avg_days_between_appearances float
        avg_price_change_between_appearances float
        appearance_frequency float
        avg_volume float "if available"
        gainer_pattern string
        performance_category string
    }
    
    PRICE_DISTRIBUTION ||--o{ PRICE_RANGE_ANALYSIS : feeds_into
    PRICE_RANGE_ANALYSIS {
        price_range string
        symbol_count int
        recurring_symbols_count int
        recurring_symbol_percentage float
        avg_appearances float
        high_performers_percentage float
        avg_volume float "if available"
        weighted_success_score float
    }
    
    VOLUME_DISTRIBUTION ||--o{ VOLUME_PATTERN_ANALYSIS : feeds_into
    VOLUME_PATTERN_ANALYSIS {
        volume_range string
        avg_change_percent float
        price_correlation float
        liquidity_score float
        trading_recommendation string
    }
    
    DAY_OF_WEEK_STATS ||--o{ TRADING_PATTERN_ANALYSIS : feeds_into
    TRADING_PATTERN_ANALYSIS {
        day_of_week string
        avg_gainers_per_day float
        avg_change_percent float
        repeat_percentage float
        volume_trend string "if available"
        trading_strategy string
    }
