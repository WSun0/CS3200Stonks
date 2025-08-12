drop database if exists stonks;
Create database if not exists stonks;
use stonks;

drop table if exists Users;
create table if not exists Users
(
    user_id integer primary key auto_increment,
    name    varchar(50),
    email   varchar(50),
    role    varchar(50),
    hash    varchar(50)
);

drop table if exists Strategies;
create table if not exists Strategies
(
    strat_id    integer auto_increment primary key,
    user_id     integer,
    name        varchar(50),
    description text,
    is_public   boolean default false,
    foreign key (user_id) references Users (user_id)
);

drop table if exists Assets;
create table if not exists Assets
(
    asset_id    integer auto_increment primary key,
    ticker      varchar(10) unique,
    name        varchar(50),
    asset_class varchar(50),
    sector      varchar(50)
);

drop table if exists Price_History;
create table if not exists Price_History
(
    price_id    integer auto_increment primary key,
    asset_id    integer,
    date        date,
    open_price  float,
    close_price float,
    high_price  float,
    low_price   float,
    volume      bigint,
    foreign key (asset_id) references Assets (asset_id)
);

drop table if exists Backtests;
create table if not exists Backtests
(
    backtest_id    integer auto_increment primary key,
    strat_id       integer,
    user_id        integer,
    start_date     date,
    end_date       date,
    result_summary text,
    may_cause_error boolean,
    foreign key (user_id) references Users (user_id),
    foreign key (strat_id) references Strategies (strat_id)
);

drop table if exists Backtest_assets;
create table if not exists Backtest_assets
(
    backtest_id integer,
    asset_id    integer,
    primary key (backtest_id, asset_id),
    foreign key (backtest_id) references Backtests (backtest_id),
    foreign key (asset_id) references Assets (asset_id)
);

drop table if exists Metrics;
create table if not exists Metrics
(
    metric_id    integer primary key auto_increment,
    backtest_id  integer,
    roi          float,
    drawdown     float,
    sharpe_ratio float,
    volatility   float,
    win_rate     float,
    foreign key (backtest_id) references Backtests (backtest_id)
);

drop table if exists Errors;
create table if not exists Errors
(
    error_id  integer primary key auto_increment,
    timestamp timestamp default current_timestamp,
    message   varchar(200),
    severity  varchar(20),
    may_cause_error boolean,
    backtest_id integer,
    foreign key (backtest_id) references Backtests(backtest_id)
);

drop table if exists User_activity_log;
create table if not exists User_activity_log
(
    log_id    integer primary key auto_increment,
    user_id   integer,
    action    text,
    timestamp timestamp default current_timestamp,
    foreign key (user_id) references Users (user_id)
);

drop table if exists Backups;
create table if not exists Backups
(
    backup_id integer auto_increment primary key,
    timestamp timestamp default current_timestamp,
    status    varchar(50),
    log_id integer,
    foreign key (log_id) references User_activity_log(log_id)
);


drop table if exists strategy_rules;
create table if not exists strategy_rules(
    rule_id integer auto_increment primary key,
    strat_id integer,
    rule_type varchar(50),
    parameters JSON,
    foreign key (strat_id) references Strategies(strat_id)
);

drop table if exists Tutorials;
create table if not exists Tutorials
(
    tutorial_id integer auto_increment primary key,
    title       varchar(50),
    content     text,
    is_active   boolean default true,
    rule_id integer,
    foreign key (rule_id) references strategy_rules(rule_id)
);