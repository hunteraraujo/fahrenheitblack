# Fahrenheit Black Quantitative Trading System

## Project Overview

This document provides a comprehensive architecture and design layout for a Quantitative Trading System aimed at executing multiple trading strategies simultaneously. The system will initially focus on trading stocks and options but is designed for easy extensibility to other asset types.

## Objective

To build a modular, scalable, and efficient trading system that can:

- Fetch and manage trading data in real-time
- Execute multiple trading strategies concurrently
- Evaluate and manage risks at both strategy and portfolio levels
- Backtest strategies using historical data
- Execute orders in real-time
- Monitor performance and adapt dynamically

## System Architecture

The system is divided into seven main modules:

### 1. Data Management Module

**Objective**: To fetch, store, and prepare trading data for strategy execution.

#### Classes and Functions

- `DataRetrieval`
  - `.fetch_realtime_data()`: Fetch real-time data from Interactive Brokers.
  - `.fetch_historical_data()`: Fetch historical data from Interactive Brokers.

- `DataStorage`
  - `.save_to_csv()`: Save data frames to CSV files.
  - `.load_from_csv()`: Load data frames from CSV files.

- `DataProcessing`
  - `.clean_data()`: Clean and preprocess data.
  - `.transform_data()`: Apply necessary transformations or calculations.

### 2. Trading Strategies Module

**Objective**: To execute trading strategies and generate trading signals.

#### Classes and Functions

- `StrategyInterface`
  - `.analyze()`: Analyze data and generate trading signals.
  - `.execute()`: Execute trading signals and generate orders.

- `StrategyExecutor`
  - `.run_strategy()`: Run a specific strategy.
  - `.scale_strategy()`: Scale a strategy based on performance.

### 3. Risk Management Module

**Objective**: To evaluate and manage risks associated with trading.

#### Classes and Functions

- `StrategyLevelRisk`
  - `.apply_stop_loss()`: Apply stop-loss levels to a strategy.
  - `.apply_take_profit()`: Apply take-profit levels to a strategy.

- `PortfolioLevelRisk`
  - `.calculate_max_drawdown()`: Calculate the maximum drawdown for the portfolio.
  - `.halt_trading()`: Halt trading activities if risk thresholds are breached.

### 4. Backtesting Module

**Objective**: To backtest strategies using historical data.

#### Classes and Functions

- `CustomBacktester`
  - `.run_backtest()`: Run backtest for a specific strategy.
  - `.calculate_performance_metrics()`: Calculate performance metrics after backtesting.

- `PerformanceAnalysis`
  - `.visualize_results()`: Generate visualizations for backtesting results.

### 5. Order Execution Module

**Objective**: To execute and manage orders.

#### Classes and Functions

- `BrokerIntegration`
  - `.execute_order()`: Send orders to Interactive Brokers for execution.
  - `.query_open_orders()`: Query the list of open orders from Interactive Brokers.
  - `.query_positions()`: Query the list of current positions from Interactive Brokers.
  - `.query_account_details()`: Query account-related details like available cash, margin, etc., from Interactive Brokers.

- `OrderManagement`
  - `.create_order()`: Create a new order based on trading signals.
  - `.monitor_order()`: Monitor the status of an open order.
  - `.cancel_order()`: Cancel an open order.
  - `.modify_order()`: Modify an existing order, e.g., change order size, type, or price.
 
- `OrderQueue`
  - `.enqueue_order()`: Add new orders to a queue for batch processing.
  - `.dequeue_order()`: Remove orders from the queue for execution.

### 6. Performance Metrics and Evaluation Module

**Objective**: To calculate and log performance metrics.

#### Classes and Functions

- `MetricsCalculation`
  - `.calculate_real_time_metrics()`: Calculate real-time performance metrics.
  - `.calculate_post_trade_metrics()`: Calculate post-trade metrics.

- `Optimization`
  - `.apply_half_kelly()`: Apply the Half Kelly Criterion for portfolio rebalancing.

### 7. Maintenance and Monitoring Module

**Objective**: To manage system updates and real-time monitoring.

#### Classes and Functions

- `UpdatesManagement`
  - `.apply_update()`: Apply system updates or bug fixes.

- `Diagnostics`
  - `.send_alert()`: Send real-time alerts via SMS or email.
  - `.log_activity()`: Log system activities and performance.

## Data Flow

1. **Data Retrieval**: Real-time and historical data are fetched from Interactive Brokers through the `DataRetrieval` class.
2. **Data Storage**: The fetched data are stored in CSV files and loaded into pandas DataFrames via the `DataStorage` class.
3. **Data Processing**: Data are cleaned and transformed using the `DataProcessing` class.
4. **Strategy Execution**: The `StrategyExecutor` class consumes the processed data to execute trading strategies, generating trading signals.
5. **Risk Management**: The `StrategyLevelRisk` and `PortfolioLevelRisk` classes evaluate these signals and apply risk parameters.
6. **Order Creation**: New orders are created based on valid signals by the `OrderManagement` class.
7. **Order Execution and Query**: Orders are sent to Interactive Brokers for execution through the `BrokerIntegration` class. Open orders, positions, and account details can be queried.
8. **Performance Metrics**: Performance metrics are calculated and logged by the `MetricsCalculation` class.
9. **Monitoring and Alerts**: System activities and performance anomalies are logged and alerts are sent by the `Diagnostics` class.
