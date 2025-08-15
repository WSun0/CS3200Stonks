# CS 3200 Stonks Project

A comprehensive stock trading strategy platform built for CS 3200 Database Design course. This application demonstrates modern full-stack development practices with role-based access control, real-time data analysis, and comprehensive trading strategy management.

## 🚀 Project Overview

**Stonks** is a multi-user trading strategy platform that provides different interfaces and capabilities based on user roles. The application allows users to create, test, evaluate, and export trading strategies while providing comprehensive performance analytics and risk management tools.

## 👥 User Personas & Features

### **Alex - Professional Financial Advisor**
- **View Strategy Performance**: Comprehensive dashboard with KPIs and portfolio tracking
- **Evaluate Strategies**: Detailed backtest results with trade-by-trade analysis
- **Export Strategy Reports**: Generate downloadable reports in CSV format
- **Performance Analytics**: ROI, Sharpe ratio, drawdown, and win rate metrics

### **Mia - College Student & Amateur Investor**
- **Learn Trading Metrics**: Educational content on trading fundamentals
- **Run Backtests**: Test strategies on historical data
- **Share Strategies**: Collaborate with other users
- **Beginner-Friendly Interface**: Simplified tools for learning

### **Jamie - System Administrator**
- **Error Diagnostics**: Monitor system health and resolve issues
- **Data Backup & Restore**: Manage system backups and recovery
- **Deploy Updates**: Manage system patches and deployments
- **System Monitoring**: Real-time system status and performance tracking

### **Daniel - Retail Investor**
- **Run Backtests**: Quick strategy testing on selected stocks
- **Compare Strategies**: Side-by-side performance comparison
- **Import/Export Strategies**: Share and import strategy templates
- **Stock Analysis**: Compare live market data with backtest results

## 🏗️ Architecture

### **Frontend (Streamlit)**
- **Role-Based Access Control**: Different interfaces for different user types
- **Responsive Design**: Wide layout optimized for data visualization
- **Interactive Components**: Charts, tables, forms, and real-time updates
- **Navigation System**: Custom sidebar with role-specific page links

### **Backend (Flask REST API)**
- **RESTful Endpoints**: Clean API design for data access
- **Database Integration**: MySQL with comprehensive trading data
- **Error Handling**: Robust error logging and user feedback
- **Authentication**: Session-based user management

### **Database (MySQL)**
- **Users & Authentication**: User management and role assignment
- **Trading Strategies**: Strategy definitions, rules, and parameters
- **Asset Information**: Stock data, sectors, and asset classes
- **Performance Metrics**: ROI, drawdown, Sharpe ratio, win rates
- **Backtest Results**: Historical strategy performance data
- **Error Logging**: System diagnostics and user activity tracking

### **Containerization (Docker)**
- **Multi-Service Architecture**: Separate containers for app, API, and database
- **Development Environment**: Sandbox configuration for testing
- **Production Ready**: Scalable container orchestration
- **Easy Deployment**: One-command setup and teardown

## 🛠️ Technology Stack

- **Frontend**: Streamlit, Pandas, Plotly, Altair
- **Backend**: Flask, Python 3.11, RESTful APIs
- **Database**: MySQL 9 with comprehensive schema
- **Data Analysis**: NumPy, Pandas, Scikit-learn
- **Containerization**: Docker, Docker Compose
- **Development**: VSCode, Git, Conda environments

## 📊 Database Schema

The application includes comprehensive tables for:
- **Users**: Authentication, roles, and permissions
- **Strategies**: Trading strategy definitions and rules
- **Assets**: Stock information, sectors, and classifications
- **Price History**: Historical price data and volume
- **Backtests**: Strategy testing results and performance
- **Metrics**: ROI, drawdown, Sharpe ratio calculations
- **Error Logging**: System diagnostics and user activity
- **Backups**: System backup management and restoration

## 🚀 Getting Started

### **Prerequisites**
- Docker and Docker Compose
- Python 3.11+ with Conda
- Git for version control

### **Quick Start**
1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd CS3200Stonks
   ```

2. **Set up environment variables**
   ```bash
   cd api
   # Create .env file with your database credentials
   cp .env.template .env
   # Edit .env with your secure password
   ```

3. **Start the application**
   ```bash
   # For development/testing
   docker compose -f sandbox.yaml up -d
   
   # For production
   docker compose up -d
   ```

4. **Access the application**
   - **Frontend**: http://localhost:8502 (sandbox) or http://localhost:8501 (production)
   - **API**: http://localhost:4001 (sandbox) or http://localhost:4000 (production)
   - **Database**: localhost:3201 (sandbox) or localhost:3200 (production)

### **Development Setup**
1. **Create conda environment**
   ```bash
   conda create -n db-proj python=3.11
   conda activate db-proj
   ```

2. **Install dependencies**
   ```bash
   pip install -r api/requirements.txt
   pip install -r app/src/requirements.txt
   ```

## 🔧 Development Commands

### **Docker Management**
```bash
# Start all services
docker compose -f sandbox.yaml up -d

# Stop services
docker compose -f sandbox.yaml stop

# Remove containers and volumes
docker compose -f sandbox.yaml down -v

# View logs
docker compose -f sandbox.yaml logs -f
```

### **Database Management**
```bash
# Reset database (runs SQL files again)
docker compose -f sandbox.yaml down db -v
docker compose -f sandbox.yaml up db -d
```

## 📁 Project Structure

```
CS3200Stonks/
├── app/                          # Streamlit frontend
│   ├── src/
│   │   ├── pages/               # User-specific pages
│   │   ├── modules/             # Navigation and utilities
│   │   └── assets/              # Images and static files
│   └── Dockerfile
├── api/                          # Flask backend
│   ├── backend/                  # API routes and business logic
│   ├── requirements.txt          # Python dependencies
│   └── Dockerfile
├── database-files/               # SQL schema and sample data
├── datasets/                     # Data storage
├── docker-compose.yaml           # Production configuration
└── sandbox.yaml                  # Development configuration
```

## 🎯 Key Features

- **Multi-User System**: Role-based access control with personalized interfaces
- **Strategy Management**: Create, test, and evaluate trading strategies
- **Performance Analytics**: Comprehensive metrics and visualization
- **Real-Time Data**: Live market data integration
- **Export Capabilities**: Download reports and strategy templates
- **System Administration**: Monitoring, backup, and update management
- **Educational Content**: Learning resources for new traders
- **Collaboration Tools**: Share and import strategies between users

## 🔒 Security Features

- **Environment Variables**: Secure credential management
- **Session Management**: User authentication and role validation
- **Input Validation**: Sanitized user inputs and SQL injection prevention
- **Error Handling**: Secure error messages without information leakage

## 📈 Future Enhancements

- **Real-time Market Data**: Live stock price feeds
- **Advanced Analytics**: Machine learning model integration
- **Mobile Interface**: Responsive design for mobile devices
- **API Documentation**: Comprehensive API reference
- **User Management**: Advanced user roles and permissions
- **Performance Optimization**: Caching and database optimization

## 🤝 Contributing

This project is developed for CS 3200 Database Design course. For development:
1. Follow the established code structure
2. Maintain role-based access control patterns
3. Add comprehensive error handling
4. Include logging for debugging
5. Test with Docker containers

## 📝 License

This project is developed for educational purposes as part of CS 3200 coursework.

## 🆘 Support

For technical issues or questions:
- Check Docker container logs
- Verify environment variable configuration
- Review database connection settings
- Consult the project documentation

---

**Built with ❤️ for CS 3200 Database Design Course**