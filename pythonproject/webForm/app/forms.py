# import  flask_wtf
#
# import wtforms
# from wtforms import  StringField,SubmitField,IntegerField,BooleanField
#
# class contactForm(flask_wtf.FlaskForm):
#
#     name =  wtforms.StringField("name",[wtforms.validators.length(min=5 ,max=14)])
#     country = wtforms.StringField("country",[wtforms.validators.length])
#     amount = wtforms.IntegerField("amount",[wtforms.validators.number_range])
#     Area = wtforms.IntegerField("Area",[wtforms.validators.number_range])
#     submit = wtforms.SubmitField('submit validate')