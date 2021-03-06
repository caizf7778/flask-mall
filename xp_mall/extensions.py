# -*- coding: utf-8 -*-

from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_whooshee import Whooshee
from flask_dropzone import Dropzone
from pay.alipay.create_pay import Alipay
from pay.wxpay.create_pay import Wxpay

db            = SQLAlchemy()
login_manager = LoginManager()
csrf     = CSRFProtect()
ckeditor = CKEditor()
moment = Moment()
toolbar = DebugToolbarExtension()
migrate = Migrate()
whooshee  = Whooshee()
dropzone = Dropzone()
# 支付对象
alipay = Alipay()
wxpay = Wxpay()

@login_manager.user_loader
def load_user(user_id):
    from xp_mall.models.member import Member
    user = Member.query.get(int(user_id))
    return user

login_manager.login_view = 'auth.login'
# login_manager.login_message = 'Your custom message'
login_manager.login_message_category = 'info'
