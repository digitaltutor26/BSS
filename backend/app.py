from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import os
from models import db, User, Product, ConsumptionRecord
from routes import api_bp, auth_bp
from services.consumption_service import ConsumptionService
from services.mbti_service import MBTIService

app = Flask(__name__)

# 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bss.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

# 데이터베이스 초기화
db.init_app(app)

# Blueprint 등록
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/auth')

# 서비스 초기화
consumption_service = ConsumptionService()
mbti_service = MBTIService()

@app.route('/')
def index():
    """홈 페이지"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """대시보드 페이지"""
    return render_template('dashboard.html')

@app.route('/analysis')
def analysis():
    """분석 페이지"""
    return render_template('analysis.html')

@app.route('/api/dashboard/summary')
def get_dashboard_summary():
    """대시보드 요약 정보"""
    try:
        # 전체 제품 수
        total_products = Product.query.count()
        
        # 이번 달 소비액
        current_month_spending = consumption_service.get_monthly_spending()
        
        # 다가올 알림
        upcoming_alerts = consumption_service.get_upcoming_alerts(days=7)
        
        return jsonify({
            'status': 'success',
            'data': {
                'total_products': total_products,
                'current_month_spending': current_month_spending,
                'upcoming_alerts_count': len(upcoming_alerts)
            }
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'status': 'error', 'message': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'status': 'error', 'message': 'Internal server error'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
